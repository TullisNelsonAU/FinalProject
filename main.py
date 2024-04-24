
import time
import affineCipher  # Import your other cipher modules similarly
import shiftCipher
import railfenceCipher
import columnartranspositioncCipher
import playfairCipher
import affineCipher
import vigenereCipher
import threading
from nltk.corpus import words
import nltk
nltk.download('words')  # Download words list if not already downloaded

word_list = words.words()


def display_menu():
    """Displays the main menu to the user"""
    print("\n--- Jackson & Tullis' Cipher Program ---")
    print("0. Automatic Cipher Detection")
    print("1. Shift Cipher")
    print("2. Vigenère Cipher")
    print("3. Rail Fence Cipher")
    print("4. Hill Cipher")
    print("5. Affine Cipher")
    print("6. Playfair Cipher")
    print("7. Help")
    print("8. Exit")


def get_user_choice():
    """Gets the user's menu choice."""
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice in range(0, 9):  # Validate choice
                return choice
            else:
                print("Invalid choice. Please select a number between 1 and 8.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_operation_choice():
    """Gets the user's choice for encryption or decryption"""
    while True:
        operation = input(
            "Do you want to encrypt (E) or decrypt (D)? ").upper()
        if operation in ('E', 'D'):
            return operation
        else:
            print("Invalid choice. Please enter 'E' or 'D'.")


def main():
    """Main program loop."""
    while True:
        display_menu()
        choice = get_user_choice()
        if choice == 0:
            print("----- Cipher Detection -----")
            ciphertext = input("Enter your ciphertext: ")
            detected_cipher = detect_cipher(ciphertext)
            print("Detected cipher:", detected_cipher)

        elif choice == 1:
            shiftCipher.main()

        elif choice == 2:
            vigenereCipher.main()

        elif choice == 3:
            railfenceCipher.main()

        elif choice == 4:
            # columnartranspositioncCipher.main()
            print("Columnar Transposition Cipher is not yet implemented.")

        elif choice == 5:
            affineCipher.main()

        elif choice == 6:
            playfairCipher.main()

        elif choice == 7:
            print("\n--- Help ---")
            print("Enter your choice from the menu above. For example, if you want to encrypt or decrypt a message using the shift cipher, enter '1'")
            pass

        elif choice == 8:
            print("Exiting program...")
            break


def detect_and_score(ciphertext, cipher_name, cipher_module):
    """Decrypts using a specific cipher and calculates a score."""

    if cipher_name == "affine":
        # Affine Cipher Logic
        key, plaintext = affineCipher.crack_cipher(ciphertext)
        score = calculate_score(plaintext)
        return cipher_name, score, plaintext

    elif cipher_name == "vigenere":
        # Vigenere Cipher Logic
        best_plaintext = vigenereCipher.brute_force(ciphertext)
        score = vigenereCipher.calculate_score(best_plaintext)
        return cipher_name, score, best_plaintext

    elif cipher_name == "shift":
        # Shift Cipher Logic
        best_plaintext = shiftCipher.find_likely_decryption(
            ciphertext, word_list)
        if best_plaintext is not None:
            score = calculate_score(best_plaintext)
        else:
            score = 0
        return cipher_name, score, best_plaintext

    else:
        # Handle errors or add more ciphers here
        pass


def detect_cipher(ciphertext):
    threads = []

    for cipher_name, cipher_module in [("shift", shiftCipher),
                                       ("affine", affineCipher),
                                       ("vigenere", vigenereCipher)]:
        thread = threading.Thread(target=detect_and_score, args=(
            ciphertext, cipher_name, cipher_module))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    results = [thread.result for thread in threads]
    best_cipher, best_score, _ = max(results, key=lambda item: item[1])
    return best_cipher


def calculate_score(text):
    """Calculates a score based on the number of English words in the text."""
    word_count = len(text.split())  # Get the total number of words
    english_word_count = sum(1 for word in text.split()
                             if word.lower() in word_list)
    # Calculate the proportion of English words
    return english_word_count / word_count


if __name__ == "__main__":
    main()
