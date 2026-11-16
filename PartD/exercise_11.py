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
# - Use an external Random Word API to generate a new secret word for each round.
# - Provide more advanced hints, such as revealing a correctly positioned letter.

import requests, random

best_score: int = -1
current_score: int = 0

rounds_completed: int = 0
rounds_won: int = 0
rounds_lost: int = 0

current_word: str = ""
remaining_guesses: int = 0
game_in_progress: bool = False

max_hints: int = 0
hints_used: int = 0
letters_indexes_given_as_hints: list = []


def start_game(new_game: bool = True):
    global current_word, max_hints, letters_indexes_given_as_hints, hints_used, remaining_guesses, current_score
    global rounds_completed, rounds_won, rounds_lost, game_in_progress

    if new_game or not game_in_progress:
        current_word = get_random_word()
        current_score = 0
        remaining_guesses = 10
        max_hints = len(current_word)
        hints_used = 0
        letters_indexes_given_as_hints = []
        game_in_progress = True

    if new_game == True:
        rounds_completed = 0
        rounds_won = 0
        rounds_lost = 0

    outcome: bool = False
    # Guessing loop
    print() # empty space to show differnet area
    while remaining_guesses > 0:
        print(f"The word is {len(current_word)} letters long and you have {remaining_guesses} guesses remaining")

        user_guess = input("Please enter your guess: ")
        if user_guess.strip() == "":
            print("Please enter a word")
            continue

        guess_result = guess_word(user_guess)
        remaining_guesses -= 1

        if guess_result == True:
            print("Correct!")
            outcome = True
            break

        else:
            print("Incorrect")

            if hints_used < max_hints:
                hint_letter, hint_position = get_hint()
                hints_used += 1

                if hint_position == 1:
                    position_follow_text = "st"
                elif hint_position == 2:
                    position_follow_text = "nd"
                elif hint_position == 3:
                    position_follow_text = "rd"
                else:
                    position_follow_text = "th"

                print(f"The {hint_position}{position_follow_text} letter is '{hint_letter}'")

    game_in_progress = False
    rounds_completed += 1
    end_screen(outcome)


def end_screen(outcome: bool):
    global remaining_guesses, current_word, rounds_won, rounds_lost

    # The victory or loss screen
    if outcome == True:
        rounds_won += 1
        input(
            "You win!"
            f"\nYou had {remaining_guesses} guesses left"
            "\nPress enter to return to the main menu"
        )
    else:
        rounds_lost += 1
        input(
            f"You lost! The word was '{current_word}'"
            "\nPress enter to return to the main menu\n"
        )


def guess_word(guess: str):
    global current_word, best_score, current_score
    current_score += 1

    if guess.lower() == current_word.lower():
        if (best_score == -1) or (current_score < best_score):
            best_score = current_score

        return True
    else:

        return False


def get_random_word() -> str:
    try:
        response = requests.get("https://random-word-api.herokuapp.com/word?number=1", timeout=5)
        response.raise_for_status()
        return response.json()[0]
    
    # incase website cannot be reached for whatever reason
    except (requests.RequestException, ValueError, IndexError):
        return random.choice(["python", "keyboard", "beans", "planet", "function", "variable"])


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
                "\n5. Quit"
                "\nEnter your choice: "
            ))
        except ValueError:
            error_message = "Please enter an integer in the range 1-5"
            continue

        if not (1 <= user_choice <= 5):
            error_message = "Choice out of range"
            continue

        elif user_choice == 1:
            start_game(new_game = True)

        elif user_choice == 2:
            start_game(new_game = False)

        elif user_choice == 3:
            show_rules()

        elif user_choice == 4:
            display_stats()

        elif user_choice == 5:
            break


def display_stats():
    global best_score, rounds_completed, rounds_lost, rounds_won
    print("\033[2J\033[H", end="") # 'Clear' console

    if rounds_completed != 0:
        input(
            "Here are your stats:"
            f"\n- Best Score: {best_score if best_score != -1 else "None"}"
            f"\n- Rounds Completed: {rounds_completed}"
            f"\n- Rounds Won: {rounds_won}"
            f"\n- Rounds Lost: {rounds_lost}"
            f"\n- Win Rate: {round((rounds_won / rounds_completed) * 100, 2)}%"
            "\nPress enter to return to the main menu...\n"
        )
    else:
        input("Please play a round to view your stats (enter to continue)\n")

def show_rules():
    print("\033[2J\033[H", end="") # 'Clear' console

    input(
        "\nHere are the rules:" 
        "\n1. You have 10 guesses" 
        "\n2. Guess the word and you win"
        "\n3. Your guesses are not case sensitive" 
        "\nNot many rules... press enter to continue\n" 
    )


def get_hint() -> tuple[str, int]:
    """
    Returns a letter and its position
    """
    global current_word, letters_indexes_given_as_hints
    word = list(current_word)

    while True:
        index = random.randint(0, len(word) - 1)
        if not (index in letters_indexes_given_as_hints):
            break

    letters_indexes_given_as_hints.append(index)
    
    letter = word[index]
    position = index + 1
    return letter, position



if __name__ == '__main__':
    main()