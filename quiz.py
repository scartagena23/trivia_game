import json
import time
import pyfiglet
import random

# category names need to be same as the filenames that will contain the trivia questions
CATEGORY_LIST = ['music', 'movies', 'cars', 'politics', 'literature']


def generate_question(question):
    print("\n" + question)
    choice = input("Enter Your Answer [a/b/c/d]: ")
    while True:
        if choice.lower() in ['a', 'b', 'c', 'd']:
            return choice
        else:
            print("Invalid choice. Enter again")
            choice = input("Enter a valid choice. Options are [a/b/c/d]: ")


def score_response(key, response):
    actual = response["answer"]
    if response["user_response"].lower() == actual.lower():
        print("Q.{0} Absolutely Correct!\n".format(key))
        return 2
    else:
        print("Q.{0} Incorrect!".format(key))
        print("Your Answer was ({0})".format(response['user_response']))
        print("Right Answer is ({0})".format(actual))
        print("Learn more : " + response["more_info"] + "\n")
        return 0


def quiz(questions):
    score = 0
    print(
        "Instructions:\n1. Please enter only the letter choice corresponding to your answer."
        "\n2. Each correct question gets you 2 points\n3. Wrong answers are a big FAT 0 points"
        "\nQuiz will start momentarily. May the odds be in your favor!\n")
    time.sleep(5)
    for key, choice in questions.items():
        questions[key]["user_response"] = generate_question(choice["question"])
    print("\n***************** SCORE ********************\n")
    for key, choice in questions.items():
        score += score_response(key, choice)
    print("Your Score is:", score, "/", (2 * len(questions)))


# Reads/loads questions from JSON files and returns it
def read_question(filename):
    questions = None
    with open(filename, "r") as read_file:
        questions = json.load(read_file)
    return questions


# Start quiz
def start_quiz():
    flag = False
    try:
        choice = int(input(f"\nChoose your category of interest:\n(1). Music\n(2). "
                           f"Movies\n(3). Cars\n(4). Politics\n(5). Literature\nEnter Your Choice [1/2/3/4/5]: "))
        if choice > len(CATEGORY_LIST) or choice < 1:
            print("Invalid Choice. Please Try Again")
            flag = True  # raise flag
    except ValueError as e:
        print("Invalid Choice. Please Try Again")
        flag = True  # raise flag

    if not flag:
        questions = read_question('topics/' + CATEGORY_LIST[choice - 1] + '.json')
        quiz(questions)
    else:
        start_quiz()  # replay if flag was raised


# Starts quiz game prompt
def user_begin_prompt():
    intro = pyfiglet.figlet_format("Do you want to play a TRIVIA GAME?", width=200)
    print(intro)

    print("\nA. Yes\nB. No")
    play = input("What is your choice? : ")
    if play.lower() == 'a' or play.lower() == 'y':
        name = input("What is your name? : ")
        print(f"\nHi there {name}! Let's play a Trivia Game!")
        start_quiz()
    elif play.lower() == 'b':
        print("We are sad to see you go. Hope you come back soon!")
    else:
        print("Hmm. I didn't quite understand that.\nEnter A to play, or B to quit.")
        user_begin_prompt()


# Executes the game
def execute_quiz():
    user_begin_prompt()


if __name__ == '__main__':
    execute_quiz()