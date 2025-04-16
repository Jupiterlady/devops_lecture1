def main():
    print("Hello from Hangman")
    secret_word = input("Bitte gib ein Wort ein: ").lower()
    print(f"Das geheime Wort hat {len(secret_word)} Buchstaben.")

    guessed_letters = set()
    errors = 0
    max_errors = 8

    while True:
        guess = input("Rate einen Buchstaben: ").lower()

        if guess in guessed_letters:
            print("Diesen Buchstaben hast du schon geraten.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("Treffer! Der Buchstabe ist im Wort.")
        else:
            print("Leider falsch.")
            errors += 1
            print(f"Fehler: {errors} von {max_errors}")

        display_game_state(secret_word, guessed_letters)


def display_game_state(secret_word, guessed_letters):
    display = [letter if letter in guessed_letters else "_" for letter in secret_word]
    print("\nAktueller Stand:")
    print(" ".join(display))
    print("Geratene Buchstaben:", " ".join(sorted(guessed_letters)))


if __name__ == "__main__":
    main()