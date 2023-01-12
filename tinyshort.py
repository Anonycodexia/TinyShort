#!/usr/bin/env python3
import os
os.system('pip install pyshorteners')
import pyshorteners as ninja
os.system('clear')
os.system('figlet -c -t TinyShort')
bgreen="\033[1;32m"
logo=f"""{bgreen}                 
                     Created by Anonycodexia{bgreen}"""
print(logo)
import pyshorteners as ninja
addr = input("Enter your Url: ")
sword = ninja.Shortener()
anony = (sword.tinyurl.short(addr))
print("Your TinyUrl Address=>  "  +anony)