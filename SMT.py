import random

class demon:
    def __init__(demon, name, lvl, move1, move2, move3):
        demon.name = name
        demon.lvl = lvl
#        demon.location = location
#        demon.chance = chance
        demon.move1 = move1
        demon.move2 = move2
        demon.move3 = move3
    
    def intro(self):
        message = "Hello! My name is "+ self.name
        return message

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