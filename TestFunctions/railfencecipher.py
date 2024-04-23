
import random
import string
import nltk  
nltk.download('words') 

from nltk.corpus import words
ENGLISH_WORDS = set(words.words()) 

class RailFence:
    def __init__(self):
        pass  # No need for initialization in the Python version

    def encrypt(self, plain_text, key):
        encrypted_text = ""
        col = len(plain_text)
        row = key
        check = False
        j = 0
        rail = [['*' for _ in range(col)] for _ in range(row)]  

        for i in range(col):
            if j == 0 or j == key - 1:
                check = not check
            rail[j][i] = plain_text[i] 
            j += 1 if check else -1 

        print("Rail of encryption:")
        for i in range(row):
            for k in range(col):
                ch = rail[i][k]
                if ch != '*':
                    encrypted_text += ch
                print(ch, end=" ")
            print() 

        return encrypted_text

    def decrypt(self, encrypted_text, key):
        decrypted_text = ""
        col = len(encrypted_text)
        row = key
        check = False
        j = 0
        rail = [['*' for _ in range(col)] for _ in range(row)] 

        for i in range(col):
            if j == 0 or j == key - 1:
                check = not check
            rail[j][i] = '#' 
            j += 1 if check else -1 
            
        index = 0
        for i in range(row):
            for k in range(col):
                if rail[i][k] == '#' and index < col: 
                    rail[i][k] = encrypted_text[index]
                    index += 1
                
        j = 0
        check = False
        for i in range(col):
            if j == 0 or j == key - 1:
                check = not check
            decrypted_text += rail[j][i] 
            j += 1 if check else -1
        return decrypted_text


def calculate_score(text):
    """Calculates a score reflecting how likely 'text' is English.

    Args:
        text: The text to evaluate.

    Returns:
        A score representing how "English-like" the text seems.
    """
    score = 0
    for word in text.split():
        if word.lower() in ENGLISH_WORDS:
            score += len(word)  # Longer words get higher weight
    return score

def choose_best_decryption(encrypted_text, max_key_level):
    """Performs brute-force decryption and selects the most likely result.

    Args:
        encrypted_text: The text to decrypt.
        max_key_level: The maximum key level to attempt.

    Returns:
        The most probable plaintext decryption.
    """
    cipher = RailFence()  # Create a cipher object
    best_decryption = None
    best_decryption_score = 0

    print("\nTrying different key levels and offsets...\n")
    for key in range(2, max_key_level + 1):
        decryption = cipher.decrypt(encrypted_text, key)
        score = calculate_score(decryption)

        if not best_decryption or score > best_decryption_score:
            best_decryption = decryption
            best_decryption_score = score

        print(f"Key: {key} -> {decryption} (Score: {score})")

    return best_decryption

if __name__ == "__main__":
    cipher = RailFence()

    while True:
        print("\nRail Fence Cipher")
        print("-----------------")
        choice = input("(1) Encrypt\n(2) Decrypt\n(3) Brute-Force Decrypt\n(4) Exit\n\nEnter your choice: ")

        if choice == '1':
            plain_text = input("Enter the plain text: ")
            key = int(input("Enter the key: "))
            encrypted_text = cipher.encrypt(plain_text, key)
            print("Encrypted text is:", encrypted_text)

        elif choice == '2':
            encrypted_text = input("Enter the encrypted text: ")
            key = int(input("Enter the key: "))
            decrypted_text = cipher.decrypt(encrypted_text, key)
            print("Decrypted text is:", decrypted_text)

        elif choice == '3':
            encrypted_text = input("Enter the encrypted text: ")
            max_key_level = 15

            best_decryption = choose_best_decryption(encrypted_text, max_key_level)
            print("\nMost likely decryption:")
            print(best_decryption)

        else:
            break

