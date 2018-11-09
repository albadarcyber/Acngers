import os, sys, time, subprocess, socket, select, threading
from platform import python_version
pv = python_version()

try:
    import platform
except Exception as err:
    os.system('pip install --upgrade pip')
    os.system('pkg install php')
    os.system('pip install requests')
    os.system('pip install -r requirements.txt')
    os.system('python dar.py')()
except KeyboardInterrupt:
	  print (m+"[" + p + "Fail To Import" + m + "]")
	  sys.exit()

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
slowprint ('='*45)
slowprint ('Welcome To Albadar Cyber')
slowprint ('='*45)
slowprint("1. Bruteforce")
slowprint("="*45)
albadar = str(input("albadarcyber==> "))
if (albadar=='1') :
  os.system('cd Bruteforce;albadar.py')
