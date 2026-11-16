# Your program should include the following features:
# 1. Allow the user to start a new game.
# 2. Generate or assign a secret word.
# 3. Allow a maximum of 10 attempts to guess the word.
# 4. Provide hints after incorrect guesses.
# 5. Display the number of attempts used.
# 6. Display a success or failure message at the end of each round.
# 7. Allow the user to play another round.
# 8. Keep track of the user's best score (fewest attempts).
# Programming requirements:
# 9. Organise your program using functions, including a main() function.
# 10. Use appropriate lists or other data structures where needed.
# 11. Include input validation and error handling.
# 12. Test at least two of your functions using pytest.
# Optional extensions:
# • Use an external Random Word API to generate a new secret word for each round.
# • Provide more advanced hints, such as revealing a correctly positioned letter.

import requests, random

def get_random_word() -> str:
    response = requests.get("https://random-word-api.herokuapp.com/word?number=1")
    return response.json()[0]

BEST_SCORE: int = -1
ROUNDS_COMPLETED: int = 0
ROUNDS_WON: int = 0
ROUNDS_LOST: int = 0
CURRENT_WORD: str = get_random_word()
REMAINING_GUESSES: int = 0
LETTERS_INDEXES_GIVEN_AS_HINTS: list = []

def start_game(new_game: bool = True):
    global CURRENT_WORD, REMAINING_GUESSES, LETTERS_INDEXES_GIVEN_AS_HINTS

    CURRENT_WORD = get_random_word()
    REMAINING_GUESSES = 5
    LETTERS_INDEXES_GIVEN_AS_HINTS = []

    if new_game == True:
        global ROUNDS_COMPLETED, ROUNDS_WON, ROUNDS_LOST

        ROUNDS_COMPLETED: int = 0
        ROUNDS_WON: int = 0
        ROUNDS_LOST: int = 0


def main():
    print("\033[2J\033[H", end="") # 'Clear' console
    main_menu()
    print("\033[2J\033[H", end="")
    print("Closing...")


def main_menu():
    """
    - Clear console
    - Start new game
    - Next round
    - Show rules
    """
    # While loop so the game loop can be forever
    error_message: str = ""
    while True:
        print("\033[2J\033[H", end="") # 'Clear' console

        if error_message != "":
            print(error_message)
        # Reset error message so one error doesnt cause infinite messages
        error_message = ""

        try:
            user_choice = int(input(
                "Welcome to a random word guessing game!"
                
                "\nGame options:"
                "\n1. Start New Game"
                "\n2. Continue Game"
                "\n3. Show the Rules"
                "\n4. Display your stats"
                "\n4. Quit"
                "\nEnter your choice: "
            ))
        except ValueError:
            error_message = "Please enter an integer in the range 1-4"
            continue

        if not (1 <= user_choice <= 4):
            error_message = "Choice out of range"
            continue

        elif user_choice == 1:
            start_game(new_game = True)

        elif user_choice == 2:
            start_game(new_game = False)

        elif user_choice == 3:
            show_rules()

        elif user_choice == 4:
            break





def show_rules():
    print("\033[2J\033[H", end="") # 'Clear' console

    input(
        "\nHere are the rules:" 
        "\n1. You have 3 guesses" 
        "\n2. Guess the word and you win" 
        "\nNot many rules... press enter to continue\n" 
    )
    

def guess_word():
    pass


def get_hint() -> tuple[str, int]:
    """
    Returns a letter and its position
    """
    global CURRENT_WORD, LETTERS_INDEXES_GIVEN_AS_HINTS
    word = list(CURRENT_WORD)

    while index not in LETTERS_INDEXES_GIVEN_AS_HINTS:
        index = random.randint(0, len(word))
        
    letter = word[index]
    position = index + 1
    return letter, position



main()