from random import *
import pyautogui
import t
import random


us_pass=">>>>>>>>>>>>>>>>>>>>"
passord=['0','1','2','3','4','5','6','7','8','9','*','-','+','/','=','@','#','$','!','^','&','9','0','~',',','|','[',']','}','{','(',')','q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
guess =""
while (guess != us_pass):
    guess = ""
    long="12345678"
    for letter in range(len(us_pass)):
        guess_letter=passord[randint(0,51)]
        guess=str(guess_letter)+str(guess)
        if len(guess) >= len(long):
            print(guess)
            pyautogui.typewrite(guess)
            pyautogui.press('Enter')

        # while True:
        #     pyautogui.write(guess)
        #     pyautogui.press('Enter')
        #     guess=
        # for us_pass in guess:

