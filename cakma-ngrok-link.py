import os
import time
import colorama
from colorama import Fore, Back, Style

os.system('clear')
os.system('pkg install figlet')
os.system('clear')
os.system('figlet Cakma Link')


print ('Dosya yolunu( pwd )yazarak öğrenin...')

dosya = input("Dosya yolu: ")
bos = " "
cd = "cd"
print (cd+ bos + dosya)
os.system ('cd')
os.system (cd+ bos + dosya)
os.system ('clear')
print(Fore.YELLOW + Back.BLUE)
print("Yeni sayfa açıp.")
print(Back.GREEN)
print("ngrok http 8081")
print(Fore.YELLOW + Back.BLUE)
print("Yazınız...")
print(Fore.YELLOW + Back.RED)
os.system ('npx http-server ./ -p 8081')