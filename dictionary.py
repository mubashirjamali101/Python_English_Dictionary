import json
from difflib import get_close_matches # well already a meaningful name

# Loading Words from json file
dataFile = open("./data.json", "r") # open json file which contains a meaning for words
rawData = dataFile.read() # getting file content to a variable
Data = json.loads(rawData) # converting json into python dictionary
dataFile.close()

# welcome message
line = "-----------------------------"
print(line)
print("| WELCOME TO THE DICTIONARY |")
print(line)

# print all available or found answers
def printAnswer(answers):
    if "matches" in answers: # logic for if matches are found
        length = len(answers[1])
        # printAnswer(answers[1])
        clearMatches(answers[1])
    else: # if meaning is found
        iterater = 0
        for answer in answers:
            iterater += 1
            print(f"[{iterater}] {answer}")

# get the meaning from the data for asked word
def getmeaning(askWord):
    answer = []
    if askWord.lower() in Data:

        return Data[askWord]
    elif askWord.capitalize() in Data:

        return Data[askWord.capitalize()]
    elif askWord.upper() in Data:

        return Data[askWord.upper()]
    elif " " in askWord:
        askWord = askWord.replace(" ", "")
        myIterator = 0
        for dash in Data:
            d = dash.replace(" ","")
            if d.lower() == askWord.lower():

                return Data[dash]
                break
            myIterator += 1
        return "404"
    elif len(get_close_matches(askWord , Data.keys())) > 0:
        
        if get_close_matches(askWord, Data.keys())[0]:
            k = get_close_matches(askWord, Data.keys())[0]
            print(k)
            return ["matches",k]
        else:
            return "404"
    else:
        return "404" 

# if word is not found but matches for that word are found
def clearMatches(match):
    nl = input(f"Did you mean {match} [y/n]").lower()
    if nl == "y" or nl == "yes" or nl == "yeah" or nl == "yeap":
        meaning = getmeaning(match)
        printAnswer(meaning)

# ask the word to find
def askWord():
    word = input("ENTER THE WORD: ").lower()
    return word

# if word not found
def wordNotFound(word):
    if word == "":
        print("Empty Input!")
    else:
        print(f"Sorry the word \"{word}\" was not found in the dictionary")

# Ask to repeat or not
def askForRepeat():
    tempIn = input("ASK WORD? [y/n]: ").lower() # asking to reapet again or not
    print(line)
    if(tempIn == "n" or tempIn == "no" or tempIn == "na"): # checking if user wants to exit
        return "n"
        print("Exiting . . .")
    else:   # else continue rolling dice...
        return "y"

def main():
    repeat = "y" # initialy setting to y to get start the loop
    while repeat == "y":
        wordToFind = askWord()
        answers = [] # initialized an empty array as a tray for answer
        answers = getmeaning(wordToFind)
        if answers == "404":
            wordNotFound(wordToFind)
        elif answers != "404":
            printAnswer(answers)
        else:
            print("Internal Error :(")
        repeat = askForRepeat()

#starting up
main()