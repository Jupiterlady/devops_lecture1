def main():
    while True:
        play_game()
        replay = input("\nWillst du nochmal spielen? (j/n): ").lower()
        if replay != "j":
            print("Bis zum nächsten Mal!")
            break

def play_game():
    print("Hier ist das Galgenmännchen!", "\n")
    original_word = input("Bitte gib ein Wort ein: ")
    secret_word = original_word.lower()
    print(f"Das geheime Wort hat {len(secret_word)} Buchstaben.")
    print()

    guessed_letters = set()
    errors = 0
    max_errors = 8

    while True:
        print("---------------------------------")
        guess = input("Rate einen Buchstaben: ").lower()

        if len(guess) != 1:
            print("Bitte gib genau einen Buchstaben ein.")
            continue

        if not guess.isalpha():
            print("Bitte gib einen Buchstaben ein.")
            continue

        if guess in guessed_letters:
            print("Diesen Buchstaben hast du schon geraten.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("Treffer! Der Buchstabe ist im Wort.")
        else:
            print("Leider falsch.")
            errors += 1

        display_game_state(secret_word, guessed_letters)
        print_hangman(errors)
        print(f"Fehler: {errors} von {max_errors}")
        print()

        # win or loose
        if all(letter in guessed_letters for letter in secret_word):
            print("Glückwunsch! Du hast das Wort erraten!")
            break

        if errors >= max_errors:
            print("Leider verloren! Das Wort war:", original_word)
            break

def display_game_state(secret_word, guessed_letters):
    display = [letter if letter in guessed_letters else "_" for letter in secret_word]
    print("\nAktueller Stand:", " ".join(display))
    print("Geratene Buchstaben:", " ".join(sorted(guessed_letters)))

HANGMAN_PICS = [
    """
     +---+
         |
         |
         |
        ===""",
    """
     +---+
     O   |
         |
         |
        ===""",
    """
     +---+
     O   |
     |   |
         |
        ===""",
    """
     +---+
     O   |
    /|   |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ===""",
    """
     +---+
    [O   |
    /|\\  |
    / \\  |
        ===""",
    """
     +---+
    [O]  |
    /|\\  |
    / \\  |
        ==="""
]

def print_hangman(errors):
    print(HANGMAN_PICS[errors])

if __name__ == "__main__":
    main()