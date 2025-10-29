'''
Author: Olivia Donnelly
Program title: Flashcard Review
Description: A Program that reads through a file where each line 
consists of a term and its definition. It allows the user attach 
a file to play, log their username, and long their score in another 
file and print the file.

WWW: I was able to create a working program that allows the user to 
load a file with terms and definitions to be quizzed on. I was able 
to make it so the user could log their score and username in a .txt 
file that could be printed to show all player score history.

EBI: I had a hard time figuring out how to quiz the user on more than 
one term/definition without printing the whole list. Eventually, I 
figured it out and learned how to fix this problem in the future. If 
I had more time, I would have created a masterful program, by giving 
the user the ability to create their own file and load their own 
terms/definitions into it and then quiz them based on that file.
'''

import time

last_score = 0
last_total = 0
score_save = "scores.txt"

def play_quiz(filename):
    f = open(filename, "r")
    lines = f.readlines()
    f.close()

    term_def = []
    for line in lines[1:]:
        line = line.strip()
        if line == "":
            continue

        if "," in line:
            parts = line.split(",")
        elif ":" in line:
            parts = line.split(":")
        elif " - " in line:
            parts = line.split(" - ")
        else:
            continue

        if len(parts) >= 2:
            term = parts[0].strip()
            definition = parts[1].strip()
            term_def.append((term, definition))

    if len(term_def) == 0:
        print("No valid questions found in file.")
        return 0

    score = 0
    total = len(term_def)
    
    for term, definition in term_def:
        print("Definition:\n", definition)
        answer = input("\nWhat is the term? ").strip().lower()
    if answer == term.lower():
        print("Correct\n")
        score = score + 1
    else:
        print("Incorrect. The answer was", term, "\n")
    
    print("Your score:", score, "/", total)
    return score


def show_scores():
    f = open("scores.txt")
    for line in f:
        print(line)
        time.sleep(0.2)
    f.close()

    

def add_scores(new_score):
    username = input("what is your username?: ")
    newline = f"{username}: {new_score}\n"
    f = open("scores.txt", "a")
    f.write(newline)
    f.close()




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
                user_score = play_quiz(file_url) #int score from game
                add_scores(user_score)
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