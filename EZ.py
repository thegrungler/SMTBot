#Homemade functions just to make the main much easier to read. 
#Also didn't want to clutter SMT.py with functions that aren't used
#as a game purpose.

#Checks if a given value is in a given dictionary
def checkKey(dict, key):
  if key in dict.keys():
    return True
  else:
    return False