import pyautogui as pg
import subprocess as sp
import os
import time

os.startfile("C:\Riot Games\VALORANT\Riot Client\RiotClientServices.exe") # This is the default target location of Riot Client. If your target location is different then paste the target by going to the properties of the shortcut and pasting the location.
time.sleep(6)
pg.moveTo(349, 368)
pg.leftClick()
pg.typewrite(<your username>)
time.sleep(1)
pg.moveTo(315, 423)
pg.leftClick()
pg.typewrite(<your password>)
time.sleep(1)
pg.moveTo(402, 795)
pg.leftClick()

#To make this easier, in terminal type pip install pyinstaller.
#Once the installation of the package is done, in the terminal type the command
# pyinstaller valorant-login.py --onefile
# This will create .exe file of this program which can be run without opening a code editor.
