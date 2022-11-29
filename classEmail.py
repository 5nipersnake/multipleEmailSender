import smtplib
import ssl
from email.message import EmailMessage

class emailContext ():
    subject = None
    body = None
    senderEmail= None
    receiverEmail = None
    password = None

numOfEmails = int (input("how many emails do you want to send :"))
yourEmail=input("what is your email :")
yourPassword= input("What is your Email's password :")
subject=input("What is your subject :")
body = input("what is the body :")

arrayOfEmails=[]
for i in range(0,numOfEmails,1):
    email=emailContext()
    email.subject=subject
    email.body=body
    email.senderEmail=yourEmail
    email.password=yourPassword
    promtMessage= "enter the "+i+1+"Email "
    reEmail =input(promtMessage)
    email.receiverEmail=reEmail
    arrayOfEmails.append(email)

for i in range(0,numOfEmails):
    message = EmailMessage()
    message["From"]= arrayOfEmails[i].senderEmail
    message["To"]=arrayOfEmails[i].receiverEmail
    message["Subject"]=arrayOfEmails[i].subject
    bodyText=arrayOfEmails[i].body
    message.set_content(bodyText)

    contexts = ssl.create_default_context()

    print("sending Email :")
    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=contexts) as server :
        server.login(arrayOfEmails[i].senderEmail,arrayOfEmails[i].password)
        server.sendmail(arrayOfEmails[i].senderEmail,arrayOfEmails[i].receiverEmail,message.as_string())
    print("Success")


