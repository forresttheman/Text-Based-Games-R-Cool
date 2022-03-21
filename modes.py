import sys
import colorama
from colorama import Fore
import time
import random
import os
import modes
import resources
from resources import *
from modes import *
import characters
from characters import *



#lists
atts = ["a cool", "a lovely", "an epic", "a fabulous", "a nice", "a good"]
nameTitles = []

def start():
  resources.clearConsole()
  resources.slowprint1(Fore.BLUE+"Hello, traveler. What is your name?")
  
  name = input(Fore.RED+"")
  
  if name == "Idk" or name == "idk" or name == "I don't know." or name == "I don't know" or name == "What was it again?":
    resources.slowprint1(Fore.BLUE+"Oh you poor thing. We will get that sorted out soon.")
    resources.slowprint1("For now, let's just call you Traveler.")
    name = "Traveler"

  else:
    resources.slowprint1(Fore.BLUE+"Hm. "+name+". What  "+random.choice(atts)+" name!")

  time.sleep(1)
  nameTitles.append(name)


def op1():
  name = nameTitles[0]

  resources.indentPoint5x2()
  resources.slowprint1(Fore.BLUE+"So, "+name+", why are you here?")
  time.sleep(1)
  print(Fore.WHITE+"Pick a single option by entering its specified key.")
  resources.slowprint1(Fore.YELLOW+"""
  1. I don't know.
  2. Where am I?
  3. Who are you?
  4. I was sent to find something.""")

  choice1 = input(Fore.RED+"")

  if choice == "1":
    resources.slowprint1("I honestly don't know. I was thinking I would figure out as I go.")
  
  elif choice == "2":
    resources.slowprint1("Where exactly are we? If you are even real, that is, and I'm not just talking to myself.")
    resources.indentPoint5x2()
    resources.slowprint1(Fore.BLUE+"I'll have you know I am very real I even have a name, a wonderful name, better than yours, "+name+".")
    resources.slowprint1("In case you were wondering, my name is Case.")
    morality -= 1
    
    #I AM REALLLLL. ++annoyance, buffered by a threshold (friendly)

  elif choice == "3":
    resources.slowprint1("Before I tell you anything else, I would like to know who I'm talking to.")
  
  elif choice == "4":
    resources.slowprint1("I remember that I was sent here to find something, wherever here is.")

  else:
    resources.slowprint1("I was hoping you could help me out a little here. Please?")
    #well, since you asked so nicely, of course i will. ++charisma

  