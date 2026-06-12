from colors import Colors, cPrint
import datetime



def getCurrentDate() -> str:
    return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

LOG_FILE = "log_"+ datetime.datetime.now().strftime("%d-%m-%Y_%Hh%Mmin%Ssec") +  ".txt"
    

class Logger:

    DEBUG = 1     # GREY
    INFO = 2      # BLUE
    WARNING = 3   # YELLOW
    ERROR = 4     # RED
    CRITICAL = 5  # RED WITH BG

    fileLogging = False

    def __init__(self, logToFile: bool):
        if logToFile:
            self.file = open(LOG_FILE, 'x')
            self.fileLogging = True
        self.level = 1


    def setLevel(self, level):
        self.level = level


    def addToFile(self, data):
        if (not self.fileLogging):
            return
        self.file.write(data + "\n")
        self.file.flush()

    def debug(self, *args, **kwargs):
        if self.level <= Logger.DEBUG:
            cPrint(f"[ {getCurrentDate()} ]  [ DEBUG ]    ", *args, color=Colors.GREY, **kwargs)
            self.addToFile(f"[ {getCurrentDate()} ]  [ DEBUG ]    " + ' '.join(args))


    def info(self, *args, color,  **kwargs):
        if self.level <= Logger.INFO:
            cPrint(f"[ {getCurrentDate()} ]  [ INFO ]     ", *args, color=color, **kwargs)
            self.addToFile(f"[ {getCurrentDate()} ]  [ INFO ]     " + ' '.join(args))

    def info_small(self, *args, color=Colors.SILVER,  **kwargs):
        self.info(*args, color=color,  **kwargs)

    def info_mid(self, *args, color=Colors.BLUE,  **kwargs):
        self.info(*args, color=color,  **kwargs)

    def info_big(self, *args, color=Colors.LIGHT_BLUE,  **kwargs):
        self.info(*args, color=color,  **kwargs)



    def warning(self, *args, doRaise: bool = False, exception: BaseException|None = None, **kwargs):
        if self.level <= Logger.WARNING:
            cPrint(f"[ {getCurrentDate()} ]  [ WARNING ]  ", *args, color=Colors.YELLOW, **kwargs)
            self.addToFile(f"[ {getCurrentDate()} ]  [ WARNING ]  " + ' '.join(args))
        if doRaise:
            if exception and isinstance(exception, BaseException):
                raise exception
            raise Exception()

    def error(self, *args, doRaise: bool = False, exception: BaseException|None = None, **kwargs):
        if self.level <= Logger.ERROR:
            cPrint(f"[ {getCurrentDate()} ]  [ ERROR ]    ", *args, color=Colors.RED, **kwargs)
            self.addToFile(f"[ {getCurrentDate()} ]  [ ERROR ]    " + ' '.join(args.__str__()))
        if doRaise:
            if exception and isinstance(exception, BaseException):
                raise exception
            raise Exception()

    def critical(self, *args, doRaise: bool = False, exception = None, **kwargs):
        if self.level <= Logger.CRITICAL:
            cPrint(f"[ {getCurrentDate()} ]  [ CRITICAL ] ", *args, color=Colors.BG_RED, **kwargs)
            self.addToFile(f"[ {getCurrentDate()} ]  [ CRITICAL ] " + ' '.join(args))
        if doRaise:
            if exception and isinstance(exception, BaseException):
                raise exception
            raise Exception()