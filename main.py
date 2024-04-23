
import shiftCipher


def display_menu():
    """Displays the main menu to the user"""
    print("\n--- Jackson & Tullis' Cipher Program ---")
    print("1. Shift Cipher")
    print("2. Vigenère Cipher")
    print("3. Rail Fence Cipher")
    print("4. Hill Cipher")
    print("5. Affine Cipher")
    print("6. Affine Cipher")
    print("7. Help")
    print("8. Exit")


def get_user_choice():
    """Gets the user's menu choice."""
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice in range(1, 8):  # Validate choice
                return choice
            else:
                print("Invalid choice. Please select a number between 1 and 7.")
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
            operation = get_operation_choice()
            if operation == 'E':
                # *** Call your Vigenère Cipher encryption method here ***
                pass
            else:
                # *** Call your Vigenère Cipher decryption method here ***
                pass

        elif choice == 3:
            operation = get_operation_choice()
            if operation == 'E':
                # *** Call your Rail Fence Cipher encryption method here ***
                pass
            else:
                # *** Call your Rail Fence Cipher decryption method here ***
                pass

        elif choice == 4:
            operation = get_operation_choice()
            if operation == 'E':
                # *** Call your Hill Cipher encryption method here ***
                pass
            else:
                # *** Call your Hill Cipher decryption method here ***
                pass

        elif choice == 5:
            operation = get_operation_choice()
            if operation == 'E':
                # *** Call your Affine Cipher encryption method here ***
                pass
            else:
                # *** Call your Affine Cipher decryption method here ***
                pass

        elif choice == 6:
            operation = get_operation_choice()
            if operation == 'E':
                # *** Call your Playfair Cipher encryption method here ***
                pass
            else:
                # *** Call your Playfair Cipher decryption method here ***
                pass

        elif choice == 7:

            print("\n--- Help ---")
            print("Enter your choice from the menu above. For example, if you want to encrypt or decrypt a message using the shift cipher, enter '1'")
            pass

        elif choice == 8:
            print("Exiting program...")
            break


if __name__ == "__main__":
    main()
