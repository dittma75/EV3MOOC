import logging, email
from google.appengine.ext import webapp 
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler 
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import mail
from google.appengine.ext import db
from models.models import PreRegisterEntity
from models.models import Student

class LogSenderHandler(InboundMailHandler):
    def receive(self, message):
        logging.info("Received email from %s" % message.sender)
        #q = db.Query(Student, namespace="ns_data")
        #for p in q:
            #mail.send_mail(sender="registration@cs4hsrobots.appspotmail.com", to=p.name, subject=message.subject, body=message.body)
            #logging.info("Sent mail to %s" % p.email)	
        #mail.send_mail(sender="registration@cs4hsrobots.appspotmail.com", to="kay@rowan.edu", subject=message.subject, body=message.body)
        #mail.send_mail(sender="registration@cs4hsrobots.appspotmail.com", to="evanlavender13@gmail.com", subject=message.subject, body=message.body)

app = webapp.WSGIApplication([LogSenderHandler.mapping()], debug=True)

def main():
    run_wsgi_app(app)
if __name__ == "__main__":
    main()