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

#player stats/variables
morality = 100 #0 is completely murderous, uncaring, 200 is angelic and wonderful, 100 is neutral
antagonize = 0 #adds up, if passes threshold, character gets mad at you. Have diff aggression levels for repeated bad/good actions

#char lists
characterList = []

#antagonize thresholds for characters
veryFriendly = 50
friendly = 40
neutral = 30
unFriendly = 20
veryUnFriendly = 10
insane = 5

#functions
def charFrame(morality,savedMoralityIndex, antagonize, antThresh, charName):
  charlist = []
  charlist.append(morality)
  charlist.append(savedMoralityIndex)
  charlist.append(antagonize)
  charlist.append(antThresh)
  charlist.append(charName)
  
  return charlist

def createCharacter1():
  Marisa = charFrame(150, 0, veryFriendly, "Marisa", 0)
  print(Marisa) #check if char is actually created
  characterList.append(Marisa)
  print(moralitySaved)
  moralitySaved[0][0].append(150)
  time.sleep(3)
  print(moralitySaved)
  

def updateChars():
  #for x in range(len(characterList)):
    #MORALITY#
    #find vars in list of lists
    #characterMoralityCurrent = characterList[x][0]
    #print(characterMoralityCurrent)
    #find the saved morality list index of the char
    #characterSavedMoralityListIndex = characterList[x][1]
    
    #characterSavedMorality = moralitySaved[characterSavedMoralityListIndex]
    
    #if characterMorality != characterSavedMorality:
      #moralitySaved[x][0] = characterMoralityCurrent
        

#NOTE:
#char data is saved in list as:
#index 0 = morality
#1 = saved morality index
#2 = antagonize
#3 = antagonize threshold
#4 = character name