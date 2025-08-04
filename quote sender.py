import smtplib
import datetime as dt
import random

MY_EMAIL = "devansh.khandar@gmail.com"
MY_PASS = "dtbh bsxq fiwt cman"

now = dt.datetime.now()
weekday = now.weekday()

with open("quotes.txt") as quote_file:
    all_quotes = quote_file.readlines()
    quote = random.choice(all_quotes)

print(quote)
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASS)
    connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject: Everyday Motivation\n\n{quote}")

# import smtplib
#
# my_email = "devansh.khandar@gmail.com"
# password = "dtbh bsxq fiwt cman"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="devansh.khandar@yahoo.com", msg="Subject:I love Krishna\n\nI really love her")
#
# import datetime as dt
# now = dt.datetime.now()
# year = now.year
# print(year)