### Login System by @qwilyy on github.

# Imports add others if you have any.
import os, sys, time
from os import system

def typewriter(text):
    for letter in text:
        print(end="")
        sys.stdout.flush()
        time.sleep(0.1) #you can adjust the speed of each letter being typed here.


valid_keys = [
  "key1",
  "key2",
  "key3"
] #add more if necessary.

os.system('title example | Login')
os.system('cls' if os.name 'nt' else 'clear')
print("[#] Get yourself a key at example.com")
login = input("[%] Key: ")
if login in valid_keys:
  typewriter("Login Successful.")
  time.sleep(0.5)
  os.system('cls' if os.name 'nt' else 'clear')
  os.system('title example')
  
  #rest of your code.
  #rest of your code.
  #rest of your code.

else:
  print("Wrong Key! Get a key at example.com")
  exit()
