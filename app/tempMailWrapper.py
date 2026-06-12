import requests
import json
from mylogging import Logger
from markdownify import MarkdownConverter
import os
import time


MAIL_API_URL = "https://web2.temp-mail.org"
CACHE_FILENAME = "tempMailWrapper.cache"

logger = Logger(False)
s=requests.Session()
s.headers.update({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:134.0) Gecko/20100101 Firefox/134.0",})
logger.setLevel(Logger.DEBUG)


class Mailbox:
    def __init__(self, token=None, mailAdress=None):
        if token and mailAdress:
            self.__mailAdress = mailAdress
            self.__token = token
        elif token or mailAdress:
            logger.error("please also pass the mailAdress when passing a token", doRaise=True)
        else:
            valid, self.__mailAdress, self.__token = self.__getOldMailAdress()
            if not valid:
                self.__mailAdress, self.__token = self.__getNewMailAdress()

        s.headers.update({"Authorization": f"Bearer {self.__token}"})
        logger.debug(f"mailbox created")


    def getNewMail(self):
        self.__mailAdress, self.__token = self.__getNewMailAdress()
        s.headers.update({"Authorization": f"Bearer {self.__token}"})



    def getMailAdress(self):
        return self.__mailAdress
    
    def getToken(self):
        return self.__token

    def __getOldMailAdress(self):
        if not os.path.exists(CACHE_FILENAME):
            return False, None, None

        with open(CACHE_FILENAME, "r") as f:
            lines = f.readlines()

        if len(lines) < 3:
            logger.warning(f"cache: invalid number of line ({len(lines)})")
            return False, None, None
        
        key, value = lines[0].split(':')
        if key!="adress" or len(value)==0:
            logger.warning(f"cache: invalid key/value pair for the adress line (key: {key}, value: {value})")
            return False, None, None
        mailAdress = value

        key, value = lines[1].split(':')
        if key!="token" or len(value)==0:
            logger.warning(f"cache: invalid key/value pair for the token line (key: {key}, value: {value})")
            return False, None, None
        token = value

        key, value = lines[2].split(':')
        if key!="timestamp" or len(value)==0:
            logger.warning(f"cache: invalid key/value pair for the timestamp line (key: {key}, value: {value})")
            return False, None, None
        try:
            timestamp = int(value)       
        except:
            return False, None, None
        
        if time.time() - timestamp > 60*60: # si 1h de diff entre maintenant et quand l'adresse a été généré
            return False, None, None
        
        logger.debug(f"cached mail found and valid")
        logger.debug(f"mail: {mailAdress.strip()}")
        logger.debug(f"token: {token.strip()}")
        
        return True, mailAdress.strip(), token.strip()


    def __getNewMailAdress(self):
        res = s.post(f"{MAIL_API_URL}/mailbox")
        try:
            token = res.json()["token"]
            mail = res.json()["mailbox"]
        except:
            print(json.dumps(res.json(), indent=4))
            logger.critical("token or mail not found", doRaise=True)

        logger.debug("new email generated")
        logger.debug(f"mail: {self.__mailAdress}")
        logger.debug(f"token: {self.__token}")

        with open(CACHE_FILENAME, "w") as f:
            f.write(f"adress:{mail}\n")
            f.write(f"token:{token}\n")
            f.write(f"timestamp:{int(time.time())}\n")

        return mail, token
    

    def getNumberOfMails(self):
        res = s.get(f"{MAIL_API_URL}/messages")
        mails = res.json()["messages"]
        return len(mails)



    def getLastMailContent(self):
        res = s.get(f"{MAIL_API_URL}/messages")
        mails = res.json()["messages"]
        if len(mails)<=0:
            return ""
        
        id = mails[0]["_id"]
        res = s.get(f"{MAIL_API_URL}/messages/{id}")
        content = res.json()["bodyHtml"]

        return content


    def getMails(self) -> list[Mail]:
        res = s.get(f"{MAIL_API_URL}/messages")
        mails = res.json()["messages"]
        
        mailObjsList = []

        for mail in mails:
            mailObj = Mail()
            mailObj.id = mail["_id"]
            mailObj.receivedAt = mail["receivedAt"]
            mailObj.fromMail = mail["from"]
            mailObj.subject = mail["subject"]
            mailObj.bodyPreview = mail["bodyPreview"]
            mailObj.attachmentsCount = mail["attachmentsCount"]

            mailObjsList.append(mailObj)
        
        return mailObjsList



class Mail:
    def __init__(self):
        self.id = None
        self.receivedAt = None
        self.fromMail = None
        self.subject = None
        self.bodyPreview = None
        self.attachmentsCount = None
        self.__bodyContentHtml = None
        self.__bodyContentMarkdown = None

    def toFormatedStr(self):
        return f"id: {self.id}\nReceivedAt: {self.receivedAt}\nFrom: {self.fromMail}\nSubject: {self.subject}\nBody preview: {self.bodyPreview}\nAttachments Count: {self.attachmentsCount}"
    
    def __str__(self):
        return f"id: {self.id}, ReceivedAt: {self.receivedAt}, From: {self.fromMail}, Subject: {self.subject}, Body preview: {self.bodyPreview}, Attachments Count: {self.attachmentsCount}"

    def getBodyContentHtml(self):
        if self.__bodyContentHtml == None:
            self.__updateBodyContent()
        return self.__bodyContentHtml

    def getBodyContentMarkdown(self):
        if self.__bodyContentHtml == None:
            self.__updateBodyContent()
        return self.__bodyContentMarkdown

    def __updateBodyContent(self):
        res = s.get(f"{MAIL_API_URL}/messages/{self.id}")
        content = res.json()["bodyHtml"]
        self.__bodyContentHtml = content
        self.__bodyContentMarkdown = MdConverter().convert(self.__bodyContentHtml)


class MdConverter(MarkdownConverter):
    def convert_u(self, el, text, parent_tags):
        if not text.strip():
            return text
        return f"<u>{text}</u>"