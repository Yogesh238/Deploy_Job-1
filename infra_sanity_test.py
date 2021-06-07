#!/bin/python3

from smtplib import SMTP
import requests
from sys import argv

url = argv[1]

def send_email(email, msg):
    connection = SMTP("smtp.gmail.com", 587)
    connection.starttls()
    user_email = "eddygrantpython@gmail.com"
    user_pass = "pythonuser321"
    connection.login(user_email, user_pass)
    connection.sendmail(user_email, email, msg)
    print("Notification sent successfully")   
    

# url = 'http://18.212.67.28:8200/'

request_response = requests.head(url)
status_code = request_response.status_code
emails = ['yogesh.p@cloverbaytechnologies.com', 'sachin.saini@cloverbaytechnologies.com']

if status_code == 200:
    for email in emails:
        send_email(email, 'Website is Up')
else:
    for email in emails:
        send_email(email, 'Web App is Down')
