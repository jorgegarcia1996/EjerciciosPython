# Write a Python program to display the current date and time.
from datetime import datetime
now = datetime.now()
print(now.strftime("%Y/%m/%d %H:%M:%S"))