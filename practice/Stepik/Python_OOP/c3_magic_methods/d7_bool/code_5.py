import sys
from typing import List


class MailItem:
    mail_from: str
    title: str
    content: str
    is_read = False

    def __init__(self, mail_from: str, title: str, content: str):
        self.mail_from = mail_from
        self.title = title
        self.content = content

    def __bool__(self):
        return self.is_read

    def set_read(self, fl_read: bool):
        self.is_read = fl_read


class MailBox:
    inbox_list: List[MailItem]

    def __init__(self):
        self.inbox_list = []

    def receive(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))
        self.inbox_list += [MailItem(*mail.split('; ')) for mail in lst_in]


if __name__ == '__main__':
    mail = MailBox()
    mail.receive()
    mail.inbox_list[0].set_read(True)
    mail.inbox_list[-1].set_read(True)

    inbox_list_filtered = list(filter(bool, mail.inbox_list))



