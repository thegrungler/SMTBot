import random

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
        

class player:
    def __init__(player, ID, lvl, storage):
        player.ID = ID
        player.lvl = lvl
        player.storage = {}

def encountering(lvl):
    if lvl == 1:
        Pixie = demon("Pixie", 1, "Dia", "Zio", " ")
        return Pixie

    if (lvl > 1) and (lvl < 5):
        chance = random.randint(1,3)
        if (chance < 3):
            Slime = demon("Slime", 1, "Lunge", "Dustoma", "Poisma")
            return Slime
        else:
            PyroJack = demon("Pyro Jack", 3, "Agi", "Sukunda", "Rarukaja")
            return PyroJack

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