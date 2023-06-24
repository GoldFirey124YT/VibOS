import tkinter as tk
import os

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

label = tk.Label(root, text='Welcome to the VibOS installer!')
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

if __name__ == '__main__':
  setup()
  copy_osdata()
