#Playfair Cipher

import string
import nltk
import re 
from nltk.corpus import words

import itertools

nltk.download('words')
ENGLISH_WORDS = set(words.words())


import nltk
nltk.download('brown') 
from nltk.corpus import brown
from nltk import bigrams
from collections import Counter

def clean_text(text):
    """Cleans text for bigram analysis."""
    text = re.sub(r"[^\w\s]", "", text)  # Remove non-word, non-whitespace chars
    text = re.sub(r"\s+", " ", text)  # Normalize spaces 
    return text.lower()


def generate_key_square(key):
    """Generates the Playfair cipher key square."""
    key = key.upper().replace("J", "I")  
    alphabet = string.ascii_uppercase.replace("J", "")
    matrix = []

    for letter in key + alphabet:
        if letter not in matrix:
            matrix.append(letter)

    return [matrix[i:i+5] for i in range(0, len(matrix), 5)]


def prepare_plaintext(plaintext):
    """Prepares the plaintext for encryption (handles repeated letters and spaces)."""
    plaintext = plaintext.upper().replace("J", "I").replace(" ", "")
    result = []

    for i in range(0, len(plaintext), 2):
        result.append(plaintext[i])
        if i + 1 < len(plaintext):
            if plaintext[i] == plaintext[i + 1]:
                result.append("X" if plaintext[i] == "X" else plaintext[i])  
            else:
                result.append(plaintext[i + 1]) 
    
    # Special case when plaintext has an odd number of characters:
    if len(plaintext) % 2 == 1: 
        if result[-1] != 'X':  # Check if we already have an 'X' at the end.
            result.append('X')

    return "".join(result)




def locate_letter(matrix, letter):
    """Finds the row and column coordinates of a letter in the key square matrix."""
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == letter:
                return row, col

    # If the letter is not found:
    raise ValueError(f"Letter '{letter}' not found in the key square.")  



def playfair_encrypt(plaintext, key_square):
    """Encrypts a plaintext using the Playfair cipher."""
    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        letter1, letter2 = plaintext[i], plaintext[i + 1]
        row1, col1 = locate_letter(key_square, letter1)
        row2, col2 = locate_letter(key_square, letter2)

        if row1 == row2:
            ciphertext += key_square[row1][(col1 + 1) % 5] + key_square[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += key_square[(row1 + 1) % 5][col1] + key_square[(row2 + 1) % 5][col2]
        else:
            ciphertext += key_square[row1][col2] + key_square[row2][col1]

    return ciphertext


def playfair_decrypt(ciphertext, key_square):
    """Decrypts a ciphertext using the Playfair cipher."""
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        letter1, letter2 = ciphertext[i], ciphertext[i + 1]
        row1, col1 = locate_letter(key_square, letter1)
        row2, col2 = locate_letter(key_square, letter2)

        if row1 == row2:
            plaintext += key_square[row1][(col1 - 1) % 5] + key_square[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plaintext += key_square[(row1 - 1) % 5][col1] + key_square[(row2 - 1) % 5][col2]
        else: 
            plaintext += key_square[row1][col2] + key_square[row2][col1]

    return plaintext


def calculate_score(text):
    """Calculates a score for how likely 'text' is English."""
    score = 0
    for word in text.split():
        if word.lower() in ENGLISH_WORDS:
            score += len(word) 
    return score

def score_text_bigrams(text, bigram_counts):
    score = 0
    text_bigrams = bigrams(text.lower().split())  # Convert text to lowercase 
    for bigram in text_bigrams:
        if bigram.lower() in bigram_counts:  # Check lowercase bigrams
            score += bigram_counts[bigram.lower()] 
    return score



def choose_best_decryption(ciphertext, key):
    """Attempts decryption with different key rotations, chooses the best, and shows progress."""
    best_decryption = None
    best_decryption_score = -1  # Initialize with a negative score

    for i in range(len(key)):
        possible_key = key[i:] + key[:i]
        decryption = playfair_decrypt(ciphertext, generate_key_square(possible_key))
        score = score_text_bigrams(decryption.lower(), bigram_counts)  # Use bigram scoring

        print(f"Key Rotation: {i}, Key: {possible_key}, Decryption: {decryption} (Score: {score})")

        if score > best_decryption_score:
            best_decryption = decryption
            best_decryption_score = score

    print("\nMost likely decryption:")  # Display the best result at the end
    print(best_decryption)



def exhaustive_crack(ciphertext, max_key_length=15):
    """Attempts to crack the ciphertext by trying all keys and rotations up to a certain length."""
    best_decryption = None
    best_decryption_score = -1

    ciphertext = ciphertext.lower().replace("J", "I")
    ciphertext = ''.join(c for c in ciphertext if c.isalpha())

    for key_length in range(1, max_key_length + 1):
        possible_keys = generate_all_keys(key_length)  # We'll need to create this function

        for key in possible_keys:
            for i in range(len(key)):
                possible_key = key[i:] + key[:i]
                decryption = playfair_decrypt(ciphertext, generate_key_square(possible_key))
                score = score_text_bigrams(decryption.lower(), bigram_counts)  # Use the bigram scorer

                print(f"Key Length: {key_length}, Key: {possible_key}, Decryption: {decryption} (Score: {score})")

                if score > best_decryption_score:
                    best_decryption = decryption
                    best_decryption_score = score

    print("\nMost likely decryption:")
    print(best_decryption)



def generate_all_keys(key_length):
    """Generates all possible keys of a given length (using permutations)."""
    alphabet = string.ascii_uppercase.replace("J", "")
    keys = itertools.permutations(alphabet, key_length)
    return ["".join(key) for key in keys]  # Convert tuples of letters to strings 



def main():
    while True:
        print("\nPlayfair Cipher")
        print("-----------------")
        choice = input("(1) Encrypt\n(2) Decrypt\n(3) Crack\n(4) Exit\n\nEnter your choice: ")

        if choice == '1':
            plaintext = input("Enter the plaintext: ")
            key = input("Enter the key: ")
            prepared_text = prepare_plaintext(plaintext)
            key_square = generate_key_square(key)
            ciphertext = playfair_encrypt(prepared_text, key_square)
            print("Encrypted text:", ciphertext)

        elif choice == '2':
            ciphertext = input("Enter the ciphertext: ")
            ciphertext = ciphertext.lower()  # Convert to lowercase
            key = input("Enter the key: ")
            key_square = generate_key_square(key)
            plaintext = playfair_decrypt(ciphertext, key_square)
            print("Decrypted text:", plaintext)

        elif choice == '3':
            ciphertext = input("Enter the ciphertext: ")
            exhaustive_crack(ciphertext)

        
        elif choice == '4':
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    # Pre-process and calculate bigram counts (do this once at the beginning)
    all_words = [clean_text(word) for word in brown.words()]
    bigram_list = list(bigrams(all_words))
    bigram_counts = Counter(bigram_list)

    # Start the main program
    main() 