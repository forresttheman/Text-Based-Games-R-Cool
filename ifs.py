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


#ifs
def nameBlock1():
  resources.slowprint1(Fore.BLUE+"Hello, traveler. What is your name?")
  name = input(Fore.RED+"")

  
  if name == "Idk" or name == "idk" or name == "I don't know." or name == "I don't know" or name == "What was it again?":
    resources.slowprint1(Fore.BLUE+"Oh you poor thing. We will get that sorted out soon.")
    resources.slowprint1("For now, let's just call you Traveler.")
    name = "Traveler"

  elif len(name)<3 or len(name)>15:
    resources.slowprint1(Fore.BLUE+"Hm. It seems that my connection is weak. Oh! There is the problem....")#add some cool stuff here? hacker????
    resources.slowload()
    resources.slowprint1("TASK FINISHED")
    resources.slowprint1(Fore.BLUE+"That was easy. Can you hear me now, traveler?")
    resources.slowprint2("If so, could you tell me your name?")
    resources.indentPoint5x2()
    name = input(Fore.RED+"")

  elif name == characters.char1Name:
    resources.slowprint1(Fore.BLUE+"Oh wow! That's my name!")
    resources.slowprint1(Fore.BLUE+"So happy to make your acquintance, "+char1Name+".")
    characters.sameName = True
    
  else:
    resources.slowprint1(Fore.BLUE+"Hm. "+name+". What "+random.choice(modes.atts)+" name!")

    
  time.sleep(1)
  modes.nameTitles.append(name)





def op1():
  name = modes.nameTitles[0]
  
  time.sleep(1)
  resources.slowprint1(Fore.BLUE+"So, "+name+", why are you here?")
  time.sleep(1)
  print(Fore.YELLOW+"Pick a single option by entering its specified key.")
  resources.slowprint1(Fore.YELLOW+"""
  1. I don't know.
  2. Where am I?
  3. Who are you?
  4. I was sent to find something.""")

  choice1 = input(Fore.RED+"")
  resources.slowprint1(Fore.BLUE+"Well?")
  time.sleep(1.5)
  
  if choice1 == "1":
    resources.slowprint1(Fore.RED+"I honestly don't know. I was thinking I would figure out as I go.")
  
  elif choice1 == "2":
    resources.slowprint1(Fore.RED+"Where exactly are we? If you are even real, that is, and I'm not just talking to myself.")
    resources.indentPoint5x2()
    resources.slowprint1(Fore.BLUE+"I'll have you know I am very real. I even have a name, a wonderful name, better than yours, "+name+".")
    resources.slowprint1("Just in case you were wondering, my name is "+characters.char1Name+".")
    #I AM REALLLLL. ++annoyance, buffered by a threshold (friendly)

  elif choice1 == "3":
    if characters.sameName == False:
      resources.slowprint1(Fore.RED+"Before I tell you anything else, I would like to know who I'm talking to.")
      resources.indentPoint5x2()
      resources.slowprint1(Fore.BLUE+"My name is "+characters.char1Name+". Thank you for asking!")
    else:
      resources.slowprint1(Fore.BLUE+"I'm a GDS program, or Gate Defense System, installed in this local node. My job is to keep foreign or unknown programs from infiltrating the vulnerable core systems of my base matrices.")
  
  elif choice1 == "4":
    resources.slowprint1(Fore.RED+"I remember that I was sent here to find something, wherever here is.")

  else:
    resources.slowprint1(Fore.RED+"I was hoping you could help me out a little here. I don't really have an idea why I'm here, wherever here is.")
    #well, since you asked so nicely, of course i will. ++charisma