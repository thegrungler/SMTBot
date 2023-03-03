import random
DemonList = {}
class demon:
    def __init__(demon, name: str, lvl: int, skills: list, learnset: list, stats: list, growths: list):
        demon.name = name
        demon.lvl = lvl
#        demon.location = location
#        demon.chance = chance
        demon.moves = skills
        demon.learnset = learnset
        demon.stats = stats
        demon.growths = growths
    
    def intro(self):
        message = "Hello! My name is "+ self.name
        return message
    
    def levelup(self):
        i = 0
        while i < 3:
            temp = random.randint(0, 100)
            chance0 = self.growths[0]
            chance1 = chance0+self.growths[1]
            chance2 = chance1+self.growths[2]
            chance3 = chance2+self.growths[3]
            chance4 = chance3+self.growths[4]
            if temp < chance0:
                self.stats[0]+=1
            elif temp > chance0 and temp < chance1:
                self.stats[1]+=1
            elif temp > chance1 and temp < chance2:
                self.stats[2]+=1
            elif temp > chance2 and temp < chance3:
                self.stats[3]+=1
            elif temp > chance3 and temp < chance4:
                self.stats[4]+=1
            i+=1
        

class player:
    def __init__(player, ID, lvl, storage):
        player.ID = ID
        player.lvl = lvl
        player.storage = {}

class skill:
    def __init__(skill, type, name, power, accuracy, crit):
        skill.type = type
        skill.name = name
        skill.power = power
        skill.accuracy = accuracy
        skill.crit = crit

def encountering(lvl):
    EncounterList = []
    i = 0
    maxEncounter = lvl + 3
    if maxEncounter > 99:
        maxEncounter = 99
    leastEncounter = lvl - 3
    if leastEncounter < 1:
        leastEncounter = 1
    for demon, lvl in DemonList.items():
        if lvl <= maxEncounter and lvl >= leastEncounter:
            EncounterList.append(demon)
    for demon in EncounterList:
        i += 1
    return EncounterList[random.randint(0,i)]
        


def negotiation(lvl):

    return

def fusion(type1, lvl1, type2, lvl2):

    return

def dmgCalc(atk, EnDef):
    print("damage!")
    return

#Checks if a given value is in a given dictionary
def checkKey(dict, key):
  if key in dict.keys():
    return True
  else:
    return False