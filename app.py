import json
import difflib
from difflib import get_close_matches
data = json.load(open("data.json"))


def response(value):
    value = value.lower()
    if value in data:
        for item in data[value]:
            print("\n"+item)
    elif len(get_close_matches(value, data.keys())) > 0:
        ans = input("\nDid you mean %s? Type Y for Yes and N for No: " %
                    get_close_matches(value, data.keys())[0])
        if ans.upper() == "Y":
            for item in data[get_close_matches(value, data.keys())[0]]:
                print("\n"+item)
        elif ans.upper() == "N":
            print("\nSorry we dont have this word in our database")
        else:
            print("\nSorry, We didnt understand Your query")

    elif len(get_close_matches(value, data.keys())) == 0:
        print("\nSorry this word doesnt exist in our database")


while True:
    ques = input("\nEnter your word: ")
    response(ques)
