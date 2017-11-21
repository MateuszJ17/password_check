#!python3


# Password strength check and hashing (sha256)


import re, sys
from passlib.hash import pbkdf2_sha256


def strongpasswd():

    strenght = 0
    testpsswd = input('Give password to test (at least 8 characters): ')
    if len(testpsswd) >=8:
        psswdupperregex = re.compile(r'[QWERTYUIOPASDFGHJKLZXCVBNM]+')  # custom regex for uppercase letters
        mo1 = psswdupperregex.search(testpsswd)  # search for uppercase letters
        if mo1 is not None:
            strenght = strenght + 1
        psswdlowerregex = re.compile(r'[qwertyuiopasdfghjklzxcvbnm]+')  # custom regex for lowercase letters
        mo2 = psswdlowerregex.search(testpsswd)  # search for lowercase letters
        if mo2 is not None:
            strenght = strenght + 1
        psswddigitregex = re.compile(r'[1234567890]+')  # custom regex for digits
        mo3 = psswddigitregex.search(testpsswd)  # search for digits
        if mo3 is not None:
            strenght = strenght + 1
    else:
        print("Password is too short!")
        sys.exit()
    if strenght <= 1:
        print("Password is weak")
    elif strenght == 2:
        print("Password is moderate")
    elif strenght == 3:
        print("Password is strong")

    hash = pbkdf2_sha256.encrypt(testpsswd, rounds=20000, salt_size=16)  # hash password using sha256
    print(pbkdf2_sha256.verify(testpsswd, hash))  # for debugging


strongpasswd()
