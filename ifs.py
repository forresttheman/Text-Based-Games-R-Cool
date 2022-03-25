import colorama
import time
import random
import modes
import resources
import characters
from colorama import Fore
from resources import *
from modes import *
from characters import *

#lists
atts = ["a cool", "a lovely", "an epic", "a fabulous", "a nice", "a good"]
weakSignal = ["Hmm. This is odd. Let's try again. System Command: SIGDEBUG", "Maybe I tried the wrong thing. Hold on... System Command: SIGDEBUG", "What is wrong!?!? I swear that I had caught a wisp... Well, whatever. Let's give it another try. System Command: SIGDEBUG"]
nameTitles = []


#ifs
def nameBlock1():
  if True:
    if resources.tryAgain == False:
      resources.slowprint1(Fore.BLUE+"Hello, traveler. What is your name?")
      name = input(Fore.RED+"")
      
    elif resources.tryAgain == True:
      resources.slowprint2(random.choice(weakSignal))
      resources.slowload(1)
      resources.slowprint3(Fore.BLUE+"Could you tell me your name?")
      time.sleep(1)
      name = input(Fore.RED+"")
      resources.failCount += 1

  #you have a name. stop being dumb
  if name == "Idk" or name == "idk" or name == "I don't know." or name == "I don't know" or name == "What was it again?":
    resources.slowprint1(Fore.BLUE+"Oh you poor thing. We will get that sorted out soon.")
    resources.slowprint1("For now, let's just call you Traveler.")
    name = "Traveler"
    resources.subName = True
    resources.failCount += 1

  #stop the e spam guys pls
  if ('e' or 'E' in name) and (resources.failCount > 0):
    resources.slowprint3(Fore.RED+"Stop messing with me.")
    resources.slowprint2(Fore.BLUE+"Since you seem to be reluctant to give an identifier, I'll just call you Traveler.")
    resources.subName = True
    #this function makes sarah's antagonize go up to 1.
    characters.UpdateCharDict(characters.Char1Dict, 0, 1, 0)
    name = "Traveler"

  #don't threaten your friends...
  if name == 'kill' or name == 'Kill' or name == 'Murder' or name == 'murder' or name == 'erase' or name == 'Erase' or name == 'die' or name == 'Die' or name == 'Die!!!':
    resources.threatCount += 1
    characters.UpdateCharDict(characters.Char1Dict, 0, 1, 0)
    resources.slowprint2(Fore.BLUE+"You know, it isn't really nice to threaten someone less than a minute after you meet them.")

  if resources.threatCount > 0:
    resources.slowprint1(Fore.BLUE+"I'll give you another chance.")
    resources.slowprint2("What is your name?")
    name = input(Fore.RED+"")

    if name == 'kill' or name == 'Kill' or name == 'Murder' or name == 'murder' or name == 'erase' or name == 'Erase' or name == 'die' or name == 'Die' or name == 'Die!!!':
      resources.threatCount += 1
      characters.UpdateCharDict(characters.Char1Dict, 0, 1, 0)
      resources.slowprint2(Fore.BLUE+"Why do you insist on being unkind?")
      name = "Traveler"

  #you aren't markiplier... (probably)
  #and you definetly don't have a 1 character name
  if (len(name)<4 or len(name)>12 or name == 'Markiplier' or name == 'markiplier') and (resources.threatCount < 1):
    resources.slowprint1(Fore.BLUE+"Hm. It seems that my connection is weak. Oh! There is the problem...")
    resources.indentPoint5x2()
    resources.slowload(1)
    resources.slowprint1(Fore.BLUE+"That was easy. Can you hear me now, traveler?")
    time.sleep(1.2)
    resources.slowprint2("Oh! That's not right. One sec...")
    time.sleep(1)
    resources.indentPoint5x2()
    resources.tryAgain = True
    nameBlock1()

  #by some coincidence u have the same name! twinzies :)
  elif name == characters.char1Name:
    resources.slowprint1(Fore.BLUE+"Oh wow! That's my name!")
    resources.slowprint1(Fore.BLUE+"So happy to make your acquintance.")
    characters.sameName = True

  #good job. you didn't overtly threaten someone or stand out in any way!
  elif resources.subName == False and resources.threatCount < 1:
    resources.slowprint1(Fore.BLUE+"Hm. "+name+". What "+random.choice(atts)+" name!")
    
    
  time.sleep(1)
  modes.nameTitles.append(name)
  #print(modes.nameTitles)

###############################################
###############################################
###############################################

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
    resources.slowprint1(Fore.BLUE+"""I'll have you know I am very real. 
    I even have a name, a wonderful name, better than yours, """+name+".")
    resources.slowprint1("Just in case you were wondering, it is "+characters.char1Name+".")
    characters.UpdateCharDict(characters.Char1Dict, 0, 1, 0)

  elif choice1 == "3":
    if characters.sameName == False:
      resources.slowprint1(Fore.RED+"Before I tell you anything else, I would like to know who I'm talking to.")
      resources.indentPoint5x2()
      resources.slowprint1(Fore.BLUE+"My name is "+characters.char1Name+". Thank you for asking!")
      
    else:
      resources.slowprint1(Fore.BLUE+"I'm a GDS program, or Gate Defense System, installed in this local node. My job is to keep foreign or unknown programs from infiltrating the vulnerable core systems of my base matrices.")
  
  elif choice1 == "4":
    resources.slowprint1(Fore.RED+"I remember that I was sent here to find something, wherever here is.")

  elif 'kill' or 'Kill' or 'Murder' or 'murder' in choice1:
    resources.slowprint3(Fore.RED+"Your threats mean little to me.")
    resources.threatCount += 1

    if resources.threatCount > 1:
      resources.slowprint1(Fore.BLUE+"You are treading a thin line here. I've been trying to help you, but it seems you don't really care about that.")
  
  else:
    resources.slowprint1(Fore.RED+"I was hoping you could help me out a little here. I don't really have an idea why I'm here, wherever here is.")
    #well, since you asked so nicely, of course i will. ++charisma

###############################################
###############################################
###############################################