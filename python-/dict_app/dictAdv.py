import json
import time
from difflib import get_close_matches
import filemerger

data = json.load(open("data.json"))

key = input("Enter a word: ")

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    else:
        match = get_close_matches(w, data.keys())
        if len(match) > 0:
            answer = input("Did you mean %s instead (Y or N): " %match[0])
            if answer=="Y":
                return data[match[0]]
            elif answer == "N":
                add = input("Your word was not found, would you like to add it (Y or N): ")
                if(add == "Y"):
                    definition = input("What is the definition: ")
                    file = open("data.txt", "a+")
					file.seek(1)
                    file.write('"' + w + '":["' + definition + '"],')
                elif answer == "N":
                    return "Ok Goodbye"
                else:
                    return 0
            else:
                return "I don't understand"
        else:
            return "Your word doesn't exist. Please check it!"

output = translate(key)
if (type(output) == list):
    for item in output:
        print(item)
else:
    print(output)

another = input("Would you like to enter another word (Y or N): ")
if another == "Y":
    while another == "Y":
        key = input("Enter a word: ")
        output = translate(key)
        if (type(output) == list):
            for item in output:
                print(item)
        else:
            print(output)
        another = input("Would you like to enter another word (Y or N): ")
elif another == "N":
    print("Ok. Goodbye!")
else:
    while(another != "Y" & another !=" N"):
        print("I don't understand")
        another = input("Would you like to enter another word (Y or N): ")
