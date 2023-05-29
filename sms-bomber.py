import os
import time

# take inputs
number = input("Phone number: ")
i = int(input("SMS Frequency: "))
msg = input("Message: ")

# send sms
while i > 0:
	os.system("termux-sms-send -n " + number + " " + msg)
	time.sleep(3)
	i -= 1
