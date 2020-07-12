import sys
import requests
from mail_sender import send_mail
from datetime import datetime
from formattxt import format_msg


def send(name, website=None, to_email=None, verbose=False):
    assert to_email != None
    if website != None:
        msg = format_msg(name=name, website=website)
    else:
        msg = format_msg(name=name)
    if verbose:
        print(name, website, to_email)
    try:
        send_mail(text=msg, to_emails=[to_email], html=None)
        sent = True
    except:
        sent = False
    return sent


if __name__ == "__main__":
    print(sys.argv)
    name = "Unknown"
    if len(sys.argv) > 1:
        name = sys.argv[1]
    email = None
    if len(sys.argv) > 2:
        email = sys.argv[2]
    response = send(name, to_email=email, verbose=True)
    print(response)
