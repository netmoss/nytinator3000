import json
from urllib.request import urlopen
from datetime import date 

def wordle():
    url = "https://www.nytimes.com/svc/wordle/v2/" + str(date.today()) +".json"  
    response = urlopen(url)
    data = json.loads(response.read())
    print("The solution today is: "+ (data['solution']).upper())

def connections():
    url = "https://www.nytimes.com/svc/connections/v1/" + str(date.today()) + ".json"
    response = urlopen(url)
    data = json.loads(response.read())

    groups_list = list(data['groups'])
    items_list = list(data['groups'].values())

    difficulties = ['straightforward','intermediate','hard', 'tricky']

    for i in range(0,4):
        print('Difficulty: ' + str(difficulties[i]))
        print(groups_list[i] + ":\n" + ', '.join(items_list[i]['members']) + "\n")

def strands():
    url = "https://www.nytimes.com/games-assets/strands/" + str(date.today()) + ".json"
    response = urlopen(url)
    data = json.loads(response.read())

    spangram = data['spangram']
    solutions_list = list(data['solutions'])
    answers_list = []

    print('Spangram: ' + str(spangram))

    for i in range(0, solutions_list.index(str(spangram))):
        answers_list.append(solutions_list[i])

    print('Solutions: ' + ', '.join(answers_list))

func_list = [wordle, connections, strands]

def menu():
    print("Which NYT game would you like the answer(s) to?\n---------------")
    print("(1) Wordle\n(2) Connections\n(3) Strands")
    choice = int(input("").strip())
    func_list[choice-1]()

menu()
