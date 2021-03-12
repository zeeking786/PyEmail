# PyEmail

Sending Attachment Mail's From Python

This is the unique way to send E-mail using Python technology with easy and simpliest way in just few lines of code.

Before starting our journey , we need to install some module :

```pip install secure-smtplib```

What is SMTP in Python ?

Simple Mail Transfer Protocol (SMTP) is a protocol, which handles sending e-mail and routing e-mail between mail servers.
Python provides smtplib module, which defines an SMTP client session object that can be used to send mail to any Internet
machine with an SMTP or ESMTP listener daemon.

So, After importing this module our coding journey will start !

Before writing code , import the module in file :

```
import smtplib
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders
```
These are some libraries which will make our work simple. These are the built-in libraries so you don't need to import any external library for this.

```
fromaddr = "SENDER's Mail ID"
toaddr = "RECEIVER's MAIL ID"
```
Here fromaddr variable is used to take sender's mail id to send the mail and toaddr variable for taking receiver's mail id to whom we have to send .

```
msg = MIMEMultipart()
```
Firstly, create an instance of MIMEMultipart, namely “msg” to begin with.(MIMEMultipart means it will encode 'From','To' and 'MSG')

```
msg['From'] = fromaddr 
msg['To'] = toaddr 
msg['Subject'] ="Hiiii"
body = "THIS IS PDF"
```

In this , Taken mail id of sender's will be invoke to msg['From'] and msg['To'] will invoke the receiver's mail id . And body variablewill contain the actual msg that will shown under mail .

```msg.attach(MIMEText(body, 'plain'))```

In this line , we see that msg variable is using method attach that takes the values first value as body variable and second value 'plain' that convert the encoded value to plain text .

```
filename = "c7.pdf"
attachment = open("C:\\Users\\dell\\Downloads\\"+filename, "rb") 
```
Attachment scenerio start by making variable named as filename and under that pass the filename you want to send .(for e.g: abc.pdf / xyz.docx) .
After this I have make an variable as attachment , this will have the method open in it . The method open has the path where my given file is stored .
And "rb" is used for Opening the file as read-only in binary format and starts reading from the beginning of the file. While binary format can be used 
for different purposes, it is usually used when dealing with things like images, videos, etc .

```
p = MIMEBase('application', 'octet-stream') 
p.set_payload((attachment).read()) 
encoders.encode_base64(p)
```
Here , I called MIMEBase instance in new variable p under that the value has passed as 'application', 'octet-stream' (A MIME attachment with the content type "application/octet-stream" is a binary file. Typically,
it will be an application or a document that must be opened in an application, such as a pdf or word.)

After this we have set the payload to variable p it is used to change the payload to encoded form. Encode it in encode_base64. And finally attach the file with the MIMEMultipart created instance msg.
the line encoders.encode_base64 used to encodes the payload into base64 form and sets the Content-Transfer-Encoding header to base64 .

```
p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
msg.attach(p) 
```

p.add_header is used to set the filename parameter under that 'Content-Disposition' is a response-type header field that gives information on how to process the response payload and additional information such as 
filename when user saves it locally. After this the attachment filename in %s that is string will be passed .

msg.attach is work for attaching the instance of 'p' to instance 'msg'

```
s = smtplib.SMTP('smtp.gmail.com', 587) 
s.starttls()
```
After this we need to create a session, we will be using its instance SMTP to encapsulate an SMTP connection.In this, you need to pass the first parameter of the server location and the second parameter of the 
port to use. For Gmail, we use port number 587.

Using s.starttls for security reasons, now put the SMTP connection in the TLS mode. TLS (Transport Layer Security) encrypts all the SMTP commands. After that, for security and authentication, you need to pass 
your Gmail account credentials in the login instance.The compiler will show an authentication error if you enter invalid email id or password.

```
s.login(fromaddr, "SENDER'S PASSWORD") 
text = msg.as_string()
s.sendmail(fromaddr, toaddr, text)
```

Now we need to do the authentication from sender's this will take two values first is the sender's email id and second value is sender's password
After that text variable converts the Multipart msg into a string 
And s.sendmail will send the message by using the value of fromaddr , toaddr and text .

```print("sent")```

This is just for checking purpose  it is send or not .

```s.quit()```

This line will terminate the session of SMTP .

Wait...Our work is not finished yet there is few setup steps we need to do in our google accounts .

1. Go to Google Account click on "Manage your Google Account" .

2. Now go to the left side you will see the "Security" click on it .

3. After SSecurity page open scroll down you will get "Less Secure App Access" click on it from OFF to ON .

This is needed so your Python script can access and your account and send emails from it.

At last we have finished our E-mail sending concept with attachment and basic setup's.
