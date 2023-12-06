
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import Optional
from app.config import settings  # Import your app settings

def send_password_reset_email(to_email: str, reset_token: str):
    subject = "ARBAB Password Reset Request"
    body = f"Click the link below to reset your password for your ARBAB account:\n\n{settings.reset_password_url}?token={reset_token}"

    send_email(subject, to_email, body)

def send_email(subject: str, to_email: str, body: str):
    smtp_server = settings.smtp_server
    smtp_port = settings.smtp_port
    smtp_username = settings.smtp_username
    smtp_password = settings.smtp_password
    sender_email = settings.sender_email

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach body
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(sender_email, to_email, msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")
        
