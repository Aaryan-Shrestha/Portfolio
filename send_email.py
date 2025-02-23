import smtplib
import ssl
import os

def send_email(user_email, raw_message):
    host = "smtp.gmail.com"
    port = 465

    username = "programmingofficialacc@gmail.com"
    password = os.getenv("PASSWORD")

    receiver = "programmingofficialacc@gmail.com"
    context = ssl.create_default_context()

    message = f"""\
Subject: New email from {user_email}
\n
From: {user_email}
{raw_message}
"""


    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)