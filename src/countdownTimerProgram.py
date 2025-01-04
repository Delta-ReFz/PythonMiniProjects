'''
for loops
'''

import time

myTime = int(input("Enter the time in seconds: "))

for x in range(myTime,0, -1):
    seconds = x % 60
    print(f"00:00:{seconds:02}")
    time.sleep(1)



print("TIME'S UP!")