#Write a Python program to print yesterday, today, tomorrow.
import datetime
today = datetime.datetime.now()

print("Yesterday: ", today - datetime.timedelta(days=1))
print("Today: ", today)
print("Tomorrow: ", today + datetime.timedelta(days=1))