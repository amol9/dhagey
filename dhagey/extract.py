import re
from pdb import set_trace as pdbst

from .message import Message

filename = "thread.txt"

def extract_messages():
    thread_txt = None
    with open(filename, "r") as f:
        thread_txt = f.read()
        thread_txt += "\n----------"  # the last email does not have a dashed line separator after it, to make the regex ahead work, have to append one ourselves

    msg_re = re.compile("\*[a-zA-Z\s]*?\*<.*?@.*?>.*?----------", re.M | re.S)
    mails = msg_re.findall(thread_txt)

    msgs = []

    for mail in mails:
        msg = Message()

        sender_re = re.compile("\*([a-zA-Z\s]*?)\*")
        msg.sender = sender_re.findall(mail)[0].strip()
        #print(msg.sender)

        #pdbst()
        body_start = mail.rfind(">\n") + 2
        body = mail[body_start : ]
        msg.body = filter_body(body)
        #print(msg.body)
        #print("---")
        #input()

        msgs.append(msg)

    return msgs
    

    #pdbst()


def filter_body(body):
    lines = body.splitlines()

    c = 0
    for line in reversed(lines):
        if line.startswith("----------") or (len(line.split()) < 5):
            c += 1
        else:
            break

    return '\n'.join(lines[0 : -c])