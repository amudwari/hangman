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

    for letters in random_word:
        user_input = input("\n" + "Enter a letter: ")

        for c in range(0, length):

            if random_word[c] == user_input:
                result = user_input
                print(user_input, end="")
            elif random_word[c] == " ":
                print(" ", end="")
            else:
                print(" _ ", end="")
                result = " _ "
        print(result)


#def step_one():



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