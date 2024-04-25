import nltk
from itertools import permutations
import string

def encrypt(plain_text, key):
    num_columns = len(key)
    num_rows = -(-len(plain_text) // num_columns)
    matrix = [[''] * num_columns for _ in range(num_rows)]
    for i, char in enumerate(plain_text):
        matrix[i // num_columns][i % num_columns] = char
    cipher_text = ''
    sorted_key = sorted(enumerate(key), key=lambda x: x[1])
    for index, _ in sorted_key:
        cipher_text += ''.join(row[index] for row in matrix if row[index] != '')
    return cipher_text

def decrypt(cipher_text, key):
    num_columns = len(key)
    num_rows = -(-len(cipher_text) // num_columns)
    sorted_key = sorted(range(num_columns), key=lambda x: key[x])
    
    # Calculate the number of characters in the last row
    last_row_length = len(cipher_text) % num_columns
    
    plain_text = ''
    for row in range(num_rows):
        for col in sorted_key:
            # Calculate the index of the character in the cipher text
            index = col * num_rows + row
            # Check if the index is within the length of the cipher text
            if index < len(cipher_text):
                plain_text += cipher_text[index]
            # If we are in the last row and there are empty spaces,
            # add them to the plain text
            elif row == num_rows - 1 and col >= num_columns - last_row_length:
                plain_text += ' '
    
    return plain_text

def is_english_word(word):
    return word.lower() in set(nltk.corpus.words.words())

def crack_cipher(cipher_text):
    for key_length in range(1, len(string.ascii_lowercase) + 1):
        possible_keys = permutations(string.ascii_lowercase, key_length)
        for key in possible_keys:
            key = ''.join(key)
            decrypted_text = decrypt(cipher_text, key)
            if all(word in nltk.corpus.words.words() for word in decrypted_text.split()):
                return key, decrypted_text
    return None, None

def main():
    while True:
        print("\nMenu:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Crack")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ").strip()
        
        if choice == '1':
            plain_text = input("Enter the plain text: ").strip()
            key = input("Enter the key: ").strip()
            cipher_text = encrypt(plain_text, key)
            print("Encrypted text:", cipher_text)
        elif choice == '2':
            cipher_text = input("Enter the cipher text: ").strip()
            key = input("Enter the key: ").strip()
            plain_text = decrypt(cipher_text, key)
            print("Decrypted text:", plain_text)
        elif choice == '3':
            cipher_text = input("Enter the cipher text: ").strip()
            cracked_key, cracked_text = crack_cipher(cipher_text)
            if cracked_key:
                print("Cracked key:", cracked_key)
                print("Cracked text:", cracked_text)
            else:
                print("Failed to crack the cipher.")
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
