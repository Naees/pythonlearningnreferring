import smtplib

sender = "sender@gmail.com"
receiver = "receiver@gmail.com"
password = "!@#$%^&*()"
subject = "Python email test"
body = "This is a test email please delete"

msg = f"""FROM: {sender}
To: {receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:
    server.login(sender, password)
    print("You have signed into the account..")
    server.sendmail(sender, receiver, msg)
    print("Your email has been sent!")
    
except smtplib.SMTPAuthenticationError:
    print("You have failed to sign in")