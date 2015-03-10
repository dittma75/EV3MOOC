import webapp2
import appengine_config
from google.appengine.api import mail

t = "evanlavender13@gmail.com"
f = "registration@cs4hsrobots.appspotmail.com"
s = "HI"
b = "hello"

mail.send_mail(to=t, sender=f, subject=s, body=b)