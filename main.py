import smtplib
import pandas
import random
import datetime as dt

today = dt.datetime.now()
month = today.month
day = today.day
bdayName = ""
bdayEmail = ""
randomLetter = "letter_templates/letter_" + str(random.randint(1,3)) + ".txt"
bdayMsg = ""

email = "[YOUR EMAIL HERE]"
password = "[YOUR EMAIL APP-PASSWORD HERE]"

data = pandas.read_csv('birthdays.csv')
birthdays = data.to_dict()

def write_birthday_email():
    global bdayMsg
    with open(randomLetter, 'r') as file:
        bdayMsg = file.read()
        bdayMsg = bdayMsg.replace('[NAME]', bdayName)
        print(bdayMsg)

index = 0
for x in data["month"]:
    if x == month and birthdays["day"][index] == day:
        bdayName = birthdays["name"][index]
        bdayEmail = birthdays["email"][index]
        write_birthday_email()
    index += 1

with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(email, password)
    connection.sendmail(from_addr=email, to_addrs=bdayEmail, msg=f"Subject:Happy Birthday!\n\n{bdayMsg}")
