import smtplib
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart 

recipients = ["jesshua722@gmail.com"]

def send_email():
    from_adr = "jesshua722@gmail.com"
    server = SMTP('smtp.gmail.com', 587) # Defining SMTP server and port
    subject= "Control your light"
    
    # Format text and content in email 
    msg = MIMEMultipart()
    msg["From"] = from_adr
    msg["To"] = recipients[0]
    msg["Subject"] = subject
    message = "If you want to manually control the light, go to this website: http://192.168.50.199/index.php" 
    msg.attach(MIMEText(message))

    server.ehlo() # # Can be omitted
    server.starttls() # Create an unsecured SMTP connection and encrypt it
    server.ehlo() # Can be omitted
    server.login("jesshua722@gmail.com", "KIKI&&KICHI4ever")
    server.sendmail(from_adr, recipients, msg.as_string()) # Send email here
    server.quit()


