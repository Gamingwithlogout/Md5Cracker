import hashlib
import os
import sys
import time as t
from colorama import Fore,Style
os.system('clear')

###LOGOS&ALL
print(Fore.RED + "\t\t\t\t MD5 CRACKER BY LOGOUT!")
print("\n\t\tCrack MD5 hashes in less time with 100% Guaranteed!!" + Style.RESET_ALL)

print("\n  ")

counter = 1
pass_in = input("Please Enter MD5 Hash : ")
t.sleep(1)
print(Fore.YELLOW + "\n\t\t\t\t ANALYZING MD5 HASHES" + Style.RESET_ALL)
t.sleep(2)
pwfile = input("\n\nPlease Enter File Path : ")
t.sleep(1)
print(Fore.YELLOW + "\n\t\t\t INITIALIZE & DETONATE MD5 ATTACK" + Style.RESET_ALL)
t.sleep(3)

try:
    pwfile = open(pwfile, "r")

except:
    print(" \n File not Found.")
    quit()

for password in pwfile:
    filemd5 = hashlib.md5(password.strip().encode('utf8')).hexdigest()
    print(Fore.MAGENTA + "\n\t\tTRYING PASSWORD NUMBER [ %d ] : %s " %(counter , password) + Style.RESET_ALL)

    counter += 1

    if pass_in == filemd5:
        print(Fore.RED + "\n\t\t\t\t Match Found. \n\t\t\t The password is : %s " % password + Style.RESET_ALL)
        break;

    else:
        print("")
