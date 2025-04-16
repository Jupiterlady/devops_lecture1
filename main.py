def main():
    print("Hello from Hangman")
    secret_word = input("Bitte gib ein Wort ein: ").lower()
    print(f"Das geheime Wort hat {len(secret_word)} Buchstaben.")
    guess = input("Rate einen Buchstaben: ").lower()
    print(f"Du hast '{guess}' geraten.")

    while True:
        guess = input("Rate einen Buchstaben: ").lower()

        if guess in secret_word:
            print("Treffer! Der Buchstabe ist im Wort.")
        else:
            print("Leider falsch.")



if __name__ == "__main__":
    main()