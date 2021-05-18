import pickle, base64, sys, os, subprocess as sp
from time import sleep
from getpass import getpass
from random import randint

with open("etc/passwd", "rb") as pwf:
  pwd = pickle.load(pwf)
  print("\33[F\33[2K\33[F")
  while True:
    log = input("Username: ")
    try:
      realpass = base64.b64decode(pwd[base64.b64encode(log.encode())]).decode()
      if realpass == "~":
        print("this user cannot be logged in")
        continue
    except KeyError:
      print("you do not exist")
    else:
      fakepass = getpass()
      if realpass == fakepass:
        os.environ["RSSUSER"] = log
        sp.call(["python","bin/sh.py"])

      else:
        print(f"password incorrect")
        time.sleep(randint(6, 17))
