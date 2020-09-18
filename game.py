import random

def get_random_word():
    small_file = open("small.txt", "r")
    words = small_file.readlines()
    random_word = random.choice(words)
    print(random_word)
    return random_word


def start_game():
    print('''
You'll get 3 tries to guess the word. Lets START...''')
    random_word = get_random_word()
    length = len(random_word) - 1
    #print(length)
    for i in range(length):
        dash = "_ "
        print(dash, end = '')

    user_input = input("\n" + "Enter a letter: ")

    if user_input in random_word:
        index = random_word.index(user_input)
        print(index)
        print()



def menu():
    print('''Welcome to Hangman! 
Please choose one of the following: 
1.Start Game
2.Exit ''')
    choice = int(input("Please enter 1 or 2: "))
    if choice == 1:
        start_game()
    else:
        exit()

get_random_word()

menu()