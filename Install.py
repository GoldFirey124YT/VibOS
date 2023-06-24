import os
import time

print("Welcome To VibOS Beta :\\")
print("Install at your own risk; This isnt quite finish but please let me know :)")
input('Start installing VibOS? ')
print('Installing VibOS..')
print('Please wait for a little while, while we prepare.')
print('If you see anything about a APT lock, please reboot your computer.')

time.sleep(3)

os.system('sudo apt-get update') # Always run this first, can fix broken installs.

os.system('sudo apt -y install plymouth-themes')
os.system('sudo apt -y install python3-tk')
os.system('sudo apt -y install git')

print('\nFinishing up.')

os.system('python3 Start2.py')
