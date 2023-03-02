import smtplib
import ssl
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# Set up the credentials
creds = None
token_path = 'token.json'
if os.path.exists(token_path):
    creds = Credentials.from_authorized_user_file(token_path, ['https://www.googleapis.com/auth/gmail.send'])

if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', ['https://www.googleapis.com/auth/gmail.send'])
        creds = flow.run_local_server(port=0)
    with open(token_path, 'w') as token:
        token.write(creds.to_json())

# Set up the email details
sender = "YOUR_EMAIL_ADDRESS"
receiver = "RECIPIENT_EMAIL_ADDRESS"
subject = "Python email test"
body = "This is a test email please delete"

message = MIMEMultipart()
message['From'] = sender
message['To'] = receiver
message['Subject'] = subject
message.attach(MIMEText(body, 'plain'))

# Set up the SMTP server
smtp_server = 'smtp.gmail.com'
smtp_port = 587

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls(context=context)
    server.login(sender, creds.token)
    server.sendmail(sender, receiver, message.as_string())
    print("Email sent successfully!")
