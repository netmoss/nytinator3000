import json
from urllib.request import urlopen
from datetime import date 

def wordle():
    url = "https://www.nytimes.com/svc/wordle/v2/" + str(date.today()) +".json"  
    response = urlopen(url)
    data = json.loads(response.read())

    print("The solution today is: "+ (data["solution"]).upper())
    return

def connections():
    url = "https://www.nytimes.com/svc/connections/v1/" + str(date.today()) + ".json"
    response = urlopen(url)
    data = json.loads(response.read())

    groups_list = list(data["groups"])
    items_list = list(data["groups"].values())

    difficulties = ["Straightforward","Intermediate","Hard","Tricky"]
    for i in range(0,4):
        print("Difficulty: " + str(difficulties[i]))
        print(groups_list[i] + ":\n" + ", ".join(items_list[i]["members"]) + "\n")
    return

def strands():
    url = "https://www.nytimes.com/games-assets/strands/" + str(date.today()) + ".json"
    response = urlopen(url)
    data = json.loads(response.read())

    spangram = data["spangram"]
    solutions_list = list(data["solutions"])
    answers_list = []

    print("Spangram: " + str(spangram))

    for i in range(0, solutions_list.index(str(spangram))):
        answers_list.append(solutions_list[i])

    print("Solutions: " + ", ".join(answers_list))
    return

def mini():
    url = "https://www.nytimes.com/svc/crosswords/v6/puzzle/mini.json"
    response = urlopen(url)
    data = json.loads(response.read())

    cells = data["body"][0]["cells"]
    answers_list = []
    row = 0

    for i in range(0, len(cells)):
        if not cells[i]:
            answers_list.append("_")
        elif cells[i]["clues"][0] > row: 
            row += 1
            answers_list.append("\n" + cells[i]["answer"])
        else:
            answers_list.append(cells[i]["answer"])

    print("Solutions across:\n" + "".join(answers_list))
    return

func_list = [wordle, connections, strands, mini]

def menu():
    print("Which NYT game would you like the answer(s) to?\n---------------")
    print("(1) Wordle\n(2) Connections\n(3) Strands\n(4) Mini Crossword\n")
    choice = int(input("Please enter a number: ").strip())
    func_list[choice-1]()
    return
menu()
