

class emailContext ():
    subject = None
    body = None
    senderEmail= None
    receiverEmail = None
    password = None

def arrayofEmailMaker ():
    arrayOfEmails=[]
    for i in range(0,numOfEmails,1):
        email=emailContext()
        email.subject=subject
        email.body=body
        email.senderEmail=yourEmail
        email.password=yourPassword
        promtMessage="enter the ",i+1,"Email"
        reEmail =input(promtMessage)
        email.receiverEmail=reEmail
        arrayOfEmails.append(email)

    return arrayOfEmails

numOfEmails = int (input("how many emails do you want to send :"))
yourEmail=input("what is your email :")
yourPassword= input("What is your Email's password :")
subject=input("What is your subject :")
body = input("what is the body :")

arrayOfEmails=[]
arrayOfEmails =arrayofEmailMaker()

