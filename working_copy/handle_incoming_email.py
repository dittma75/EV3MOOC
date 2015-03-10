import logging, email
from google.appengine.ext import webapp 
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler 
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import mail

class LogSenderHandler(InboundMailHandler):
    def receive(self, message):
        logging.info("Received email from %s" % message.sender)
        mail.send_mail(to=message.sender, sender=message.to, subject="Re: "+message.subject,
                       body="Thank you for your email. We are busy trying to get the course ready to go \
and unfortunately we are unable to respond \
to you personally at this time. If you have preregistered for our course, we will \
update you with new information as we have it.\n\n \
If you are a reporter or an editor looking for more information about the course, \
please send a request to robots@rowan.edu\n\n \
Thanks, \n -- The Educational Robotics for Absolute Beginners Team\n \
https://cs4hsrobots.appspot.com")
        mail.send_mail(to="cs4hsrobots@rowan.edu", sender=message.to, subject=message.subject+"   From: "+message.sender, body=message.body)

app = webapp.WSGIApplication([LogSenderHandler.mapping()], debug=True)

def main():
    run_wsgi_app(app)
if __name__ == "__main__":
    main()