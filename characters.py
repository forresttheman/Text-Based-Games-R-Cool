import time
import characters
import resources
from resources import *
from characters import *

#player stats/variables
playerMorality = 100 
playerAntagonize = 0 
#adds up, if passes threshold, character gets mad at you. 
#0 for morality is completely murderous, uncaring, the epitamy of evil. 200 is angelic and wonderful. 100 is neutral

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

#character names and related things
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


###########
#FUNCTIONS#
###########

#call this to change any values in the character's dictionary
def UpdateCharDict(dict, moralityD, antagonizeD, antThreshD):
  #print(dict)
  #time.sleep(3)

  #if the morality has been changed
  if moralityD != 0:
    #add the new morality to old morality and make that the new morality value in dictionary
    moralityDelta = dict["morality"] + moralityD
    dict["morality"] = moralityDelta

  #is the antagonize has changed
  if antagonizeD != 0:
    antagonizeDelta = dict["antagonize"] + antagonizeD
    dict["antagonize"] = antagonizeDelta

  if antThreshD != 0:
    #if the antagonize threshold is different, update it
    if dict["antThresh"] != antThreshD:
      dict["antThresh"] = antThreshD

  if dict["antagonize"] > dict["antThresh"]:
    resources.exAntThresh = True
    

#intialize char dicts in case values are broken somehow
def InitializeCharDicts():
  #char 1
  UpdateCharDict(SarahDict, 0, 0, 0)
