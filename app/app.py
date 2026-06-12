from tempMailWrapper import Mailbox, Mail
import mylogging
from imgui_bundle import imgui, imgui_md



DEFAULT_LAYOUT = """
[Window][selected mail]
DockId=0x00000002,0

[Window][mails]
DockId=0x00000004,0

[Window][mail info]
DockId=0x00000003,0

[Docking][Data]
DockSpace     ID=0x08BD597D Window=0x1BBC0F80 Pos=0,0 Size=1280,720 Split=X Selected=0x173DA63C
  DockNode    ID=0x00000001 Parent=0x08BD597D SizeRef=555,720 Split=Y Selected=0x4F4C8DBF
    DockNode  ID=0x00000003 Parent=0x00000001 SizeRef=555,100 HiddenTabBar=1 Selected=0xED09FA44
    DockNode  ID=0x00000004 Parent=0x00000001 SizeRef=555,602 HiddenTabBar=1 Selected=0x4F4C8DBF
  DockNode    ID=0x00000002 Parent=0x08BD597D SizeRef=723,720 CentralNode=1 HiddenTabBar=1 Selected=0x173DA63C
"""

mailbox: Mailbox | None = None
mails: list[Mail] | None = None
selectedMail: Mail | None = None

winClass_noTabBar = imgui.WindowClass()
winClass_noTabBar.dock_node_flags_override_set = 1<<12 # ImGuiDockNodeFlags_NoTabBar in imgui_internal.h




def renderMailInfo():
    global mails
    global selectedMail

    imgui.begin("mail info")
    if imgui.button("get new mail adress"):
        mailbox.getNewMail()
        mails = mailbox.getMails()
        selectedMail = None

    imgui.same_line()

    if imgui.button("reload"):
        mails = mailbox.getMails()

    imgui.dummy([0, 10])

    imgui.text(mailbox.getMailAdress())
    imgui.same_line()
    if imgui.button("copy"):
        imgui.set_clipboard_text(mailbox.getMailAdress())


    imgui.end()


def bigSeparator():
    imgui.dummy([0, 10])
    imgui.separator()
    imgui.dummy([0, 10])



def mailList():
    global selectedMail


    imgui.begin("mails")

    imgui.same_line()
    imgui.text_disabled(f"mail count: {len(mails)}")
    bigSeparator()

    for mail in mails:
        imgui.begin_group()
        imgui.text(f"{mail.fromMail}")
        imgui.spacing()
        imgui.text(f"{mail.subject}")
        imgui.spacing()
        imgui.text_disabled(f"{mail.bodyPreview}")
        imgui.end_group()
        if imgui.is_item_clicked():
            selectedMail = mail
        bigSeparator()

    imgui.end()


def mailBody():
    imgui.begin("selected mail")
    if not selectedMail:
        imgui.end()
        return
    imgui_md.render(selectedMail.getBodyContentMarkdown())
    imgui.end()




def init():
    imgui.load_ini_settings_from_memory(DEFAULT_LAYOUT)
    imgui.get_io().set_ini_filename(None)



def loop():
    global mailbox
    global mails
    if mailbox is None:
        print("hm1")
        mailbox = Mailbox()
        mails = mailbox.getMails()

    imgui.set_next_window_class(winClass_noTabBar)
    renderMailInfo()

    imgui.set_next_window_class(winClass_noTabBar)
    mailList()

    imgui.set_next_window_class(winClass_noTabBar)
    mailBody()
