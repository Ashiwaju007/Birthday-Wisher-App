import smtplib
import datetime as dt
import pandas
import random

my_email = "Email Address Goes Here"
password = "Password Goes HEre"
now = dt.datetime.now()
today = (now.month, now.day)
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for (name, data_row) in data.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    PLACEHOLDER = "[NAME]"
    with open(file_path) as letter_file:
        content = letter_file.read()
        content = content.replace(PLACEHOLDER, birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="ik.umez@yahoo.com",
            msg=f"Subject:Happy Birthday\n\n {content}")
