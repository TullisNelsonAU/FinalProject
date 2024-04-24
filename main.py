
import shiftCipher
import railfenceCipher
import columnartranspositioncCipher
import playfairCipher
import affineCipher
import vigenereCipher


def display_menu():
    """Displays the main menu to the user"""
    print("\n--- Jackson & Tullis' Cipher Program ---")
    print("1. Shift Cipher")
    print("2. Vigenère Cipher")
    print("3. Rail Fence Cipher")
    print("4. Columnar Transposition Cipher")
    print("5. Affine Cipher")
    print("6. Playfair Cipher")
    print("7. Help")
    print("8. Exit")


def get_user_choice():
    """Gets the user's menu choice."""
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice in range(1, 9):  # Validate choice
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

        if choice == 1:
            shiftCipher.main()

        elif choice == 2:
            vigenereCipher.main()

        elif choice == 3:
            railfenceCipher.main()

        elif choice == 4:
            columnartranspositioncCipher.main()

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


if __name__ == "__main__":
    main()
