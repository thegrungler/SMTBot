#Only contains classes and functions. Not supposed to be ran by itself
import random

#Temp dictionary for testing, will be replaced by (possibly) a json file containing every demon we
#want to be encounterable
DemonList = {"Pixie":1, "Slime":2, "Preta":3, "Yoshitsune":4}

class demon:
    def __init__(demon, name: str, lvl: int, skills: list, learnset: list, stats: list, growths: list):
        demon.name = name
        demon.lvl = lvl
        demon.moves = skills
        demon.learnset = learnset
        demon.stats = stats
        demon.growths = growths
    
    #Will become more in depth, I want this to maybe somehow contain the personality of
    #each demon so they will have more unique introductions and personalities
    def intro(self):
        message = "Hello! My name is "+ self.name
        return message
    
    #This function is called whenever the demon levels up
    #This works by setting grabbing the chance each demon levels up and making a range with each
    #growth chance. Three random numbers are generated, and the range that each number is in
    #determines which stat will increase
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
        player.storage = storage
        storage = {}

    def checkparty(self):
        return self.storage

class skill:
    def __init__(skill, type, name, power, accuracy, crit):
        skill.type = type
        skill.name = name
        skill.power = power
        skill.accuracy = accuracy
        skill.crit = crit

#This function is only for finding out which demon will be encountered.
#This is determined by taking the player level, and creating a range around it by three. The entire demon
#list is then searched for demons that are within this range. Demons matching this criteria is added to a 
#new list. A random demon is then pulled from this list and returned as a dictionary value with their
#name and level.
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

    demon = EncounterList[random.randint(0,i-1)]
    for d, l in DemonList.items():
        if d == demon:
            Encountered = {demon:l}
    return Encountered

#Probably temporary. Checks if your level is higher, level, or higher. Gives you a percent chance to 
#return True or False, as in whether or not you obtain the demon or not
def negotiation(lvl, deflvl):
    if lvl < deflvl:
        if random.randint(0,2) == 2:
            return True
        else: 
            return False
    elif lvl == deflvl:
        if random.randint(0,1) == 1:
            return True
        else:
            return False
    else:
        return True


def fusion(type1, lvl1, type2, lvl2):

    return

#Heavily based of the pokemon damage formula, will be modified as demons are balanced
def dmgCalc(lvl, atkPower, atk, atkBoost, enDef, enDefBoost, crit, type):
    Damage = (((2*lvl)/5)+2)
    Damage = (Damage*atkPower)*((atk*atkBoost)/(enDef*enDefBoost))
    Damage = ((Damage/50)+2)
    Random = ((random.randint(100,110))/100)
    Damage = Damage*Random
    if crit == True:
        Damage = Damage*1.5
    if type == True:
        Damage = Damage*1.5
    return Damage

#Based off I believe SMT Nocturne's evasion check?
def evasion(atkrAgi, defAgi, atkrlvl, deflvl, skillAccuracy):
    atkrTemp = ((atkrlvl/5)+3)
    atkrTemp = ((atkrAgi/atkrTemp)*6.25)
    defTemp = ((deflvl/5)+3)
    defTemp = ((defAgi/defTemp)*6.25)
    Hit = (atkrTemp - defTemp) + skillAccuracy
    if random.randint(0,100) <= Hit:
        return True
    else:
        return False
    
