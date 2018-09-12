import pandas as pd
import smtplib

e = pd.read_excel("Email.xlsx")
emails = e['Emails'].values

server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login("your_email@gmail.com","your_mail_password")
msg = """
Your message over here
"""
subject = "Your subject over here"
body = "Subject: {}\n\n{}".format(subject,msg)

for email in emails:
    server.sendmail("your_email@gmail.com",email,body)
server.quit()