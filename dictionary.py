import json
from difflib import get_close_matches                           # well already a meaningful name

# Loading Words from json file
dataFile = open("./data.json", "r")                             # open json file which contains a meaning for words
rawData = dataFile.read()                                       # getting file content to a variable
Data = json.loads(rawData)                                      # converting json into python dictionary
dataFile.close()
##############################################

# WELCOME MESSAGE AT STARTUP :)😁
line = "-----------------------------"
print(line*2)
print("| WELCOME TO THE DICTIONARY |")
print(line*2)
print("Enter quit(), q() or 000 to exit anytime")
print(line*2)
##############################################

# print all available or found answers
def printAnswer(answers):
    if "matches" in answers:                                    # logic for if matches are found
        length = len(answers[1])
        clearMatches(answers[1])
    else:                                                       # if meaning is found
        iterater = 0
        for answer in answers:
            iterater += 1
            print(f"[{iterater}] {answer}")
##############################################

# get the meaning from the data for asked word
def getmeaning(askWord):
    answer = []
    if askWord.lower() in Data:                                 # find by word in lower case in Data

        return Data[askWord]
    elif askWord.capitalize() in Data:                          # find by word in capital case in Data

        return Data[askWord.capitalize()]
    elif askWord.upper() in Data:                               # find by word in upper case in Data

        return Data[askWord.upper()]
    elif " " in askWord:                                        # find by word if word contains blank spaces
        askWord = askWord.replace(" ", "")

                                                                #looping through data to find the word that contains blank spaces
        for dash in Data:
            d = dash.replace(" ","")
            if d.lower() == askWord.lower():

                return Data[dash]
                break
        return "404"                                            # if not found return 404
    elif len(get_close_matches(askWord , Data.keys())) > 0:     # find only one possible match if word ( may be ) is miss spelled
        
        if get_close_matches(askWord, Data.keys())[0]:
            k = get_close_matches(askWord, Data.keys())[0]
            return ["matches",k]
        else:
            return "404"
    else:
        return "404" 
##############################################

# if word is not found but matches for that word are found
def clearMatches(match):
    nl = input(f"Did you mean \"{match.upper()}\" [y/n]").lower()            # user's input if he wants to know the meaning of suggested word

    if nl == "y" or nl == "yes" or nl == "yeah" or nl == "yeap" or nl == "": # looking for possible positive messages from a human user
        meaning = getmeaning(match)

        printAnswer(meaning)
##############################################

# the iterator of program's main loop
def Iterate():
    userInput = str(input(">> ")).lower()   # getting user input
                                            # return word
    if(userInput == "quit()" or userInput == "q()" or userInput == "000"):
        userInput = "exit"
        return userInput
    else:
        return userInput
##############################################

# if word was not found
def wordNotFound(word):
    if word == "":
        print("Empty Input!")
    else:
        print(f"Sorry the word \"{word}\" was not found in the dictionary")
##############################################

#main function for flow of program
def main():
    while True:
        wordToFind = Iterate()              # calling the iterate which will return a string
        
        if wordToFind == "exit":            #checking string if the user wants to quit if not then continue
            print("Exiting...")
            quit()
        
        answer = getmeaning(wordToFind)     # find the meaning for user entered word!
        if answer == "404":                 #if word was not found then call the wordNotFound function
            wordNotFound(wordToFind)
        elif answer != "404":
            printAnswer(answer)
        else:
            print("Internal Error :(")

#starting up
main()