from email.message import EmailMessage
from multiprocessing import context
from app2 import password
import ssl
import smtplib
  
email_sender='codewithtomi@gmail.com'
email_password=password

email_receiver='ilker.eker@outlook.com.tr'

subject='Dont forget to subscribe'
body="""" 
When you watch a video, please hit subcribe
"""

em = EmailMessage()
em['From']=email_sender
em['To']=email_receiver
em['subject']=subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtpçgmail.com',465,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())