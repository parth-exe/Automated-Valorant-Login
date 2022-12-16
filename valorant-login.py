import pyautogui as pg
import os
import time

username = ""
password = ""
def menu():
    option = int(input("Enter which account to log in to: "))
    global username
    global password
    if option == 1:
        username = "<account username>"
        password = "<account password>"
    elif option == 2:
        username = "<account username>"
        password = "<account password>"
    elif option == 3:
        username = "<account username>"
        password = "<account password>"
    elif option == 4:
        username = "<account username>"
        password = "<account password>"
    #Copy elif code to add more accounts, replace with unique key and display in the prints below from code 31
        
    else:
        print(f"No account exists with the associated key: {option}")
        exit()
  

print("Accounts available:")
print("1. Account name")
print("2. Account name")
print("3. Account name")
# Print as many accounts as you want to display in terminal
menu()
os.startfile("C:\Riot Games\VALORANT\Riot Client\RiotClientServices.exe")
time.sleep(6)
pg.moveTo(349, 368)
pg.leftClick()
pg.typewrite(username)
time.sleep(1)
pg.moveTo(315, 423)
pg.leftClick()
pg.typewrite(password)
time.sleep(1)
pg.moveTo(402, 795)
pg.leftClick()



