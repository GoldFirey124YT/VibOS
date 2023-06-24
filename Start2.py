import os
from tkinter import *

def setup():
  os.system('sudo cp $PWD/Assets/NewLogo.png /usr/share/plymouth/themes/spinner/watermark.png')
  os.system('sudo cp $PWD/Assets/GoldOSMiniLogo.png /usr/share/plymouth/themes/spinner/bgrt-fallback.png')
  os.system('sudo cp $PWD/Assets/GoldOSMiniLogo.png /usr/share/pixmaps/ubuntu-logo-icon.png')
  os.system('sudo cp $PWD/OSData.txt /etc/os-release')
  os.system('gsettings set org.gnome.shell.extensions.dash-to-dock dock-position BOTTOM')
  os.system('sudo cp $PWD/Assets/NewLogo.png /usr/share/plymouth/themes/spinner/watermark.png')
  os.system('sudo cp $PWD/OSData.txt /usr/lib/os-release')
  os.system('sudo cp $PWD/Assets/NewLogo.png /usr/share/pixmaps/ubuntu-logo')
  os.system('sudo mkdir /usr/vibris-apps')

  window = Tk()
  window['bg'] = '#FFBF00'
  window.title('Choose BG')
  window.geometry("630x242+150+300")
  window.resizable(False, False)

  clean = PhotoImage(file = 'Assets/Small/CleanGold.png')
  cleanB = Button(window, image = clean, command = Clean).grid(column = 1, row = 1)

  cleanD = PhotoImage(file = 'Assets/Small/CleanGoldDark.png')
  cleanDB = Button(window, image = cleanD, command = DClean).grid(column = 1, row = 2)

  Gold = PhotoImage(file = 'Assets/Small/GoldFirey.png')
  GoldB = Button(window, image = Gold, command = Firey).grid(column = 2, row = 1)

  GoldD = PhotoImage(file = 'Assets/Small/GoldFireyDark.png')
  GoldDB = Button(window, image = GoldD, command = DFirey).grid(column = 2, row = 2)

  Horr = PhotoImage(file = 'Assets/Small/GoldHorizon.png')
  HorrB = Button(window, image = Horr, command = Horri).grid(column = 3, row = 1)

  HorrD = PhotoImage(file = 'Assets/Small/GoldHorizonDark.png')
  HorrDB = Button(window, image = HorrD, command = DHorri).grid(column = 3, row = 2)

  window.mainloop()

if __name__ == '__main__':
  setup()
