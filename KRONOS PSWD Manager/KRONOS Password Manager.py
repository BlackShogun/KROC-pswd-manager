# imported Modules
import os
import sys
import socket

# Intro
print("==========!!!DO NOT TELL YOU'RE ASSIGNED PASSWORD TO ANYONE!!!==========")
print("----------------------YOU'RE DATA IS KEPT PRIVATE-----------------------")
print("---------------DONATE TO PAYPAL : blackshogun66@gmail.com-------------- ")
print("============We need YOUR Support to develop more amazing things=========")
print("========================================================================")

# Login to access you're Password Library
cpass = input("Enter Password :")

# Processing Request...
if cpass == 'test':
    ans = True
    while ans:
        # Input Password to save...
        pswdfile = input("Enter Password to Save to Library : ")
        with open (pswdfile, "w") as f:
            f.write (input())
            print("File saved to your directory...")
else:
    print("!!!WRONG PASSWORD!!!")
