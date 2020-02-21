import sys
import random

def getFiles(fileNames):
    """Creates a list of beatboxers by concatenating
       all of the file names in the passed-in list.
    """
    listBeatboxers = list()
    for fileName in fileNames:
        with open(fileName) as f:
            listBeatboxers.extend(f.readlines())
    return listBeatboxers

fileNames = list()

choices = [
    "warmup",
    "normal",
    "advanced",
    "veteran",
    "sudden death",
    "classic",
    "weird"
]

easy = 'beatboxers/easyMode.txt'
hard = 'beatboxers/hardMode.txt'
unfair = 'beatboxers/whatTheHeck.txt'
constants = 'beatboxers/constants.txt'

prompt = """Alright team, here's how it works.

warmup       = easy only
normal       = easy + hard
advanced     = hard only
veteran      = hard + unfair
sudden death = unfair only
classic      = easy + hard + unfair
weird        = easy + unfair

What mode would you like to play?
"""

# Get the game mode from the player
choice = input(prompt)
while choice not in choices:
	choice = input("Try again.  Possible choices are: %s\n" % choices)

# Determine the list of file names from the choice
if choice == 'warmup':
    fileNames.append(easy)
elif choice == 'normal':
    fileNames.append(easy)
    fileNames.append(hard)
elif choice == 'advanced':
    fileNames.append(hard)
elif choice == 'veteran':
    fileNames.append(hard)
    fileNames.append(unfair)
elif choice == 'sudden death':
    fileNames.append(unfair)
elif choice == 'classic':
    fileNames.append(easy)
    fileNames.append(hard)
    fileNames.append(unfair)
elif choice == 'weird':
    fileNames.append(easy)
    fileNames.append(unfair)

# Include the contents of the "constants" file no matter what
fileNames.append('beatboxers/constants.txt')

# Scrape the list of beatboxers from the files
listBeatboxers = getFiles(fileNames)

# Play the game until we run out of beatboxers
while len(listBeatboxers) > 0:
	meaningless = input("")
	if (meaningless == "new game"):
		listBeatboxers = getFiles(fileNames)
	elif (meaningless == "quit"):
		break
	else:
		beatboxer = random.choice(listBeatboxers)
		listBeatboxers.remove(beatboxer)
		print(beatboxer)