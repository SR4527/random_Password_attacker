from random import *
import pyautogui
import time


us_pass="123456789"
passord=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
guess =""
while (guess != us_pass):
    guess = ""
    for letter in range(len(us_pass)):
        guess_letter=passord[randint(0,51)]
        guess=str(guess_letter)+str(guess)
        print(guess)
        # while True:
        #     pyautogui.write(guess)
        #     pyautogui.press('Enter')
        #     guess=
        # for us_pass in guess:
        pyautogui.typewrite(guess)
        pyautogui.press('Enter')
