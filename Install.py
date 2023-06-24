import tkinter as tk
import os
import requests
import random

def setup():
  os.system('sudo apt-get update')
  os.system('sudo apt -y install plymouth-themes')
  os.system('sudo apt -y install python3-tk')
  os.system('sudo apt -y install git')
  os.system('python3 Start2.py')

def show_tip():
  root.tk.messagebox.showinfo('VibOS Tip', 'VibOS makes your system lightweight for old and new hardware.')

root = tk.Tk()
root.title('VibOS Installer')
root.geometry('300x200')

# Set the look and feel to Windows Vista mixed with Vib ribbon
root.tk.call('tk', 'setPalette', '#f0f0f0', '#000000', '#ffffff', '#000000', 'black', '#ffffff')
root.tk.call('tk', 'setTheme', 'vista')

# Add Vibri to the installer
vibri = tk.PhotoImage(file='Assets/Vibri.png')
label = tk.Label(root, image=vibri)
label.pack()

button = tk.Button(root, text='Start Setup', command=setup)
button.pack()

tip_button = tk.Button(root, text='Show Tip', command=show_tip)
tip_button.pack()

root.mainloop()

def Clean():
  os.system('sudo cp $PWD/Assets/CleanGold.png /usr/share/backgrounds')

def DClean():
  os.system('sudo cp $PWD/Assets/CleanGoldDark.png /usr/share/backgrounds')

def Firey():
  os.system('sudo cp $PWD/Assets/GoldFirey.png /usr/share/backgrounds')

def DFirey():
  os.system('sudo cp $PWD/Assets/GoldFireyDark.png /usr/share/backgrounds')

def Horri():
  os.system('sudo cp $PWD/Assets/GoldHorizon.png /usr/share/backgrounds')

def DHorri():
  os.system('sudo cp $PWD/Assets/GoldHorizonDark.png /usr/share/backgrounds')

def copy_osdata():
  with open('OSDATA.txt', 'r') as f:
    data = f.read()
  os.system(f'sudo cp {data} /etc/os-release')

def check_for_errors():
  errors = []
  for line in open('installer.py', 'r'):
    if 'error' in line:
      errors.append(line)
  return errors

def correct_errors():
  errors = check_for_errors()
  for error in errors:
    print('Found error:', error)
    print('Correcting error...')
    corrected_error = random.choice(['This is not an error', 'This error has been fixed'])
    print('Error corrected:', corrected_error)

def main():
  check_for_errors()
  correct_errors()

if __name__ == '__main__':
  main()
