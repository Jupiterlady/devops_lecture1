def main():
    print("Hello from Hangman")
    secret_word = input("Bitte gib ein Wort ein: ").lower()
    print(f"Das geheime Wort hat {len(secret_word)} Buchstaben.")
    guess = input("Rate einen Buchstaben: ").lower()
    print(f"Du hast '{guess}' geraten.")

if __name__ == "__main__":
    main()