import time
import characters
from characters import *

#player stats/variables
morality = 100 #0 is completely murderous, uncaring, 200 is angelic and wonderful, 100 is neutral
antagonize = 0 
#adds up, if passes threshold, character gets mad at you. Have diff aggression levels for repeated bad/good actions

#antagonize thresholds for characters
veryFriendly = 50
friendly = 40
neutral = 30
unFriendly = 20
veryUnFriendly = 10
insane = 5

#char lists
characterList = []
char1MoralitySaved = []

#char specific lists
SarahList = []

#names and related things
char1Name = "Sarah"
sameName = False

#character dictionaries
#these hold working values and start out with base values
SarahDict = {
  "morality": 150,
  "antagonize": 0,
  "antThresh": veryFriendly,
  "charName": char1Name
}

#functions
#do i even need this function?
def charFrame(charDict, charList):
  morality = charDict["morality"]
  antagonize = charDict["antagonize"]
  antThresh = charDict["antThresh"]
  charName = charDict["charName"]

  charList.append(morality)
  charList.append(antagonize)
  charList.append(antThresh)
  charList.append(charName)

#call this to change any values in the character's dictionary
def UpdateCharDict(dict, moralityD, antagonizeD, antThreshD):
  #print(dict)
  #time.sleep(3)

  #if the morality has been changed
  #-1 bcs a character with a value of 0 is the evil extreme
  if moralityD != -1:
    #add the new morality to old morality and make that the new morality value in dictionary
    moralityDelta = dict["morality"] + moralityD
    dict["morality"] = moralityDelta

  #is the antagonize has changed
  if antagonizeD != 0:
    antagonizeDelta = dict["antagonize"] + antagonizeD
    dict["antagonize"] = antagonizeDelta

  if antThreshD != 0:
    #if the anntagonize threshold is different, update it
    if dict["antThresh"] != antThreshD:
      dict["antThresh"] = antThreshD
      
  #time.sleep(2)
  #print(dict)

#intialize char dicts in case values are broken somehow
def InitializeCharDicts():
  #char 1
  UpdateCharDict(SarahDict, -1, 1, 0)
