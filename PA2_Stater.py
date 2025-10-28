'''
Make a flashcard review game that reads through a file
where each line consists of a term and its definition.

An example text file and an example CSV file have been provided to you.

A masterful program includes the ability to create a new file
and load your own terms/definitions into it, before running the quiz on that file.

Save game records to a different file. Log username and high score.
Allow the user the option to view this file by printing it to the console.

You should at minimum edit the helper functions.
You may not necessarily have to edit the main function.
'''

import os
import csv

last_score = 0
last_total = 0
score_save = "scores.txt"

def play_quiz(filename):
    global last_score,last_total
    last_score = 0
    last_total = 0

    if not (filename.end(".txt") or filename.end(".csv")):
        print ("Please enter a .txt or .csv file")
        return
    
    if not os.path.exists(filename):
        print(f"{filename} not found. Please create it first and try again.")
        return


    cards = load_cards(filename)
    if len(cards) == 0:
        print ("No cards in file.")
        return
    
    print("\nStarting quiz! Type 'q' to stop.\n")
    correct = 0
    total = len(cards)

    for i, pair in list(cards, start=1):
        print ("Term:", term)
        answer = input("Your guess: ").strip()
        if answer.lower() == "q":
            total = i - 1
            break
        if answer.lower() == definition.lower():
            print ("Correct!\n")
            correct += 1
        else:
            print("Wrong. Correct answer was:", definition, "\n")

    if total == 0:
        total = 1
    print("You got", correct, "out of", total)
    last_score = correct
    last_total = total


def show_scores():
    if not os.path.exists(score_save):
        print("No scores saved yet.")
        return
    scores = {}
    with open(score_save, "r", newline="") as f:
        reader = csv.reader(f)
        header=next(reader, None)
        for row in reader:
            if len(row) >= 2:
                name = row[0].strip()
                val - row[1].strip()
                score = int(val) if val.isdigit() else 0
                scores[name] = max(scores.get(name, 0), scores)

    if len(scores) == 0:
        print("No scores found.")
    else:
        print('\n--- High Scores ---')
        for name, val in sorted(scores.items(), key= x[1], reverse=True):
            print(name, ":", val)
        print()


def add_scores():
    global last_score, last_total

    if last_total == 0:
        print("Play a quiz first.")
        return
    
    name = input("Enter your username: ").strip()
    if name == "":
        print("Username cannot be blank.")
        return
    
    scores = {}
    if os.path.exists(score_save):
        with open(score_save, "r", newline= "") as f:
            reader = csv.reader(f)
            _=next(reader, None)
            for row in reader:
                if len(row) >= 2:
                    n = row[0].strip()
                    v = row[1].strip()
                    scores[n] = int(v) if v.isdigit() else 0

    old_score = scores.get(name, 0)
    if last_score > old_score:
        scores[name] = last_score
        print("New high score for", name, ":", last_score)
    else:
        scores[name] = old_score
        print("High score unchanged:", old_score)
    

    with open(score_save, "w", newline="") as f:
        writer = txt.writer(f)
        writer.writerow (["username", "high_score"])
        for n, s in scores.items():
            writer.writerow([n, s])
    print ("Score saved.\n")

def create_file(filename):
    rows=[]
    print("\nEnter your flashcards. Leave a term empty to stop.\n")
    while True:
        term = input("Term: ").strip()
        if term == "":
            break
        definition = input("Definition: ").strip()
        if definition == "":
            print("Definition cannot be blank.")
            continue
        rows.append([term, definition])
    if len(rows) == 0:
        print("No cards added.")
        return

    if filename.ends(".csv"):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)
    else:
        with open(filename, "w") as file:
            for term, definition in rows:
                file.write(term + "," + definition + "\n")
    print("Saved", len(rows), "cards to", filename, "\n")

def load_cards(filename):
    cards=[]

    if filename.ends(".csv"):
        with open(filename, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) >=2:
                    term = row[0].strip()
                    definition = row[1].strip()
                    cards.append([term, definition])
    else:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if "," in line:
                    term, definition = line.split(",", 1)
                    term = term.strip()
                    definition = definition.strip()
                    if term != "" and definition !="" : 
                        cards.append([term, definition])
    return cards



def print_error():
    print("*"*50)
    print(" "*22+"error!"+" "*22)
    print(" "*12+"that is not a valid option"+" "*12)
    print(" "*17+"please try again"+" "*17)
    print("*"*50)

def main():
    #initialize variables
    initial_choices = ["play","see history","exit"]
    file_types = [".txt", ".csv", "txt", "csv"]
    p_options = ["play","p","play game"]
    h_options = ["see history", "history", "h", "see", "sh", "s"]
    e_options = ["exit","e","exit game"]
    first_choice = ""
    game_on = True

    while game_on: 
        print("welcome to the review game")
        
        while first_choice not in e_options: #first runs because first choice == "", then because they haven't said exit
            for item in initial_choices: #prints out play, see history, and exit
                print(f"- {item}")
            first_choice = input("what would you like to do?\n> ").lower().strip()
            if first_choice in p_options: #playing game
                quiz_fn = input("what is the name of your file?\n> ").lower().strip()
                quiz_ext = input("is it a .txt or .csv file?\n> ").lower().strip()
                while quiz_ext not in file_types: #error if they add something other than txt or csv
                    print_error()
                    print("your choices are:")
                    for item in file_types:
                        print(f"- {item}")
                    quiz_ext = input("is it a .txt or .csv file?\n> ").lower().strip()
                if quiz_ext in [".csv","csv"]: #comma separated value
                    file_url = quiz_fn+".csv"
                else: #text file
                    file_url = quiz_fn+".txt"
                play_quiz(file_url) #creating file name to pass into open function
                add_scores()
            elif first_choice in h_options: #looking at previous scores
                show_scores()
            elif first_choice in e_options: #exiting
                game_on = False
            else: #print error
                print_error()
        
        print("goodbye!")

main()