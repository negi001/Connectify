########################################
# AUTHOR_NAME = AYUSH NEGI             #
# DEPARTMENT = CSE - AIML(1st Year)    #
# Modules need to be installed :-      #
# Python should be installed on System #
# 1) pip install selenium              #
# 2) pip install customtkinter         #
########################################

# importing modules

from selenium import webdriver
from tkinter.ttk import *
from time import sleep
from tkinter import *
import customtkinter
import selenium
import os

# package required modules
package = ["selenium", "customtkinter"]

# checking if package exists or not
# else importing the package
for i in package:
    try:
        __import__(i)
    except:
        os.system("pip install " + i)


# create CTK window
root = customtkinter.CTk()

# window title
root.title("Connectify")

# setting window width and height
root.geometry("400x150")

# set minimum window size value
root.minsize(400, 150)

# set maximum window size value
root.maxsize(400, 150)

# Username Label
label = customtkinter.CTkLabel(master=root, text="Username")
label.place(relx=0.1, rely=0.1)
# Username Field
entry = customtkinter.CTkEntry(
    master=root, placeholder_text="Enter Username...")
entry.pack(padx=5, pady=10, ipadx=30)

# Password Label
label1 = customtkinter.CTkLabel(master=root, text="Password")
label1.place(relx=0.1, rely=0.4)
# Password Field
entry1 = customtkinter.CTkEntry(
    master=root, placeholder_text="Enter Password...")
entry1.pack(padx=5, pady=10, ipadx=30)


def button_event():
    # chrome driver
    browser = webdriver.Chrome(executable_path="chromedriver.exe")

    browser.implicitly_wait(5)

    # Wifi Login Portal URL
    browser.get('https://192.168.1.254:8090')

    browser.implicitly_wait(3)

    # await the browser
    sleep(2)

    # Error handling
    try:
        # advanced button
        adv_button = browser.find_element(
            "xpath", "/html/body/div/div[2]/button[3]")
        adv_button.click()

        # proceed button
        proceed_button = browser.find_element(
            "xpath", "/html/body/div/div[3]/p[2]/a")
        proceed_button.click()

        # username field
        username = browser.find_element(
            "xpath", "/html/body/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]")
        username.send_keys(f"{entry.get()}")

        # password field
        pwd = browser.find_element(
            "xpath", "/html/body/div[1]/div[1]/div[2]/div[1]/div[1]/input[2]")
        pwd.send_keys(f"{entry1.get()}")

        # clicking the signin button
        btn = browser.find_element(
            "xpath", "/html/body/div[1]/div[1]/div[2]/div[3]/a/div")
        btn.click()

        # keep running browser
        sleep(9999999)

        # exit the browser
        browser.close()

    except Exception as e:
        print("Error is :", e)


# custom tkinter button
button = customtkinter.CTkButton(
    master=root, text="Connect", command=button_event)
button.pack(padx=20, pady=10)


# Running the App
root.mainloop()
