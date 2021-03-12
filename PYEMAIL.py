import smtplib
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders

fromaddr = "Sender's Mail ID"
toaddr = "Receiver's Mail ID"

msg = MIMEMultipart() 
msg['From'] = fromaddr 
msg['To'] = toaddr 
msg['Subject'] ="Hiiii"
body = "THIS IS PDF"

msg.attach(MIMEText(body, 'plain'))

filename = "c7.pdf"
attachment = open("C:\\Users\\dell\\Downloads\\"+filename, "rb") 
p = MIMEBase('application', 'octet-stream') 
p.set_payload((attachment).read()) 
encoders.encode_base64(p)

p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
msg.attach(p) 
s = smtplib.SMTP('smtp.gmail.com', 587) 
s.starttls()

s.login(fromaddr, "sender's password") 
text = msg.as_string()
s.sendmail(fromaddr, toaddr, text)

print("sent")

s.quit()
