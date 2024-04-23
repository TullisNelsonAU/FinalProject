from nltk.corpus import words
import string
import nltk

nltk.download('words')
ENGLISH_WORDS = set(words.words())


def vigenere_cipher(plain_text, keyword, mode):
    """Encrypts or decrypts text using the Vigenere cipher."""
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result_text = ''

    # Ensure keyword is within length limits and lowercase
    keyword = keyword.lower()
    if len(keyword) > 4:
        print("Error: Keyword length exceeds maximum (4). Truncating...")
        keyword = keyword[:4]
    elif len(keyword) < 1:
        print("Error: Keyword length is less than 1. Using 'a' as the key...")
        keyword = 'a'

    # Adjust keyword length to match plaintext
    keyword = (keyword * (len(plain_text) //
               len(keyword) + 1))[:len(plain_text)]

    for i in range(len(plain_text)):
        plain_char = plain_text[i]
        keyword_char = keyword[i % len(keyword)]

        if plain_char.isalpha():
            shift = alphabet.index(keyword_char) - alphabet.index('a')
            if mode == 'encrypt':
                result_char = alphabet[(
                    alphabet.index(plain_char) + shift) % 26]
            elif mode == 'decrypt':
                result_char = alphabet[(
                    alphabet.index(plain_char) - shift) % 26]
            else:
                print("Error: Invalid mode. Choose 'encrypt' or 'decrypt'.")
                return None
        else:
            result_char = plain_char

        result_text += result_char

    return result_text


def calculate_score(text):
    """Calculates a score based on the number of English words in the text."""
    word_count = len(text.split())  # Get the total number of words
    english_word_count = sum(1 for word in text.split()
                             if word.lower() in ENGLISH_WORDS)
    # Calculate the proportion of English words
    return english_word_count / word_count


def generate_keys(length):
    """Generates all possible keys of a given length (up to 4)."""
    if length == 1:
        return string.ascii_lowercase
    elif length > 4:
        print("Error: Maximum key length is 4. Generating keys up to length 4.")
        return generate_keys(4)
    else:
        return [char + subkey for char in string.ascii_lowercase for subkey in generate_keys(length - 1)]


def brute_force(ciphertext):
    """Attempts to crack a Vigenère cipher using brute force."""
    best_decryption = None
    best_decryption_score = 0
    for key_length in range(1, 5):
        for possible_key in generate_keys(key_length):
            if possible_key == 'keyx':
                print(vigenere_cipher(ciphertext, possible_key, 'decrypt'))
            decryption = vigenere_cipher(ciphertext, possible_key, 'decrypt')
            score = calculate_score(decryption)
            # Update if score is better (even for single words)
            if score > best_decryption_score:
                best_decryption = decryption
                best_decryption_score = score
                key_used = possible_key

    print("Key used: ", key_used)
    return best_decryption


# Get user input for mode
while True:
    mode = input(
        "Enter mode ('encrypt', 'decrypt', or 'decrypt_with_key'): ").lower()
    if mode in ['encrypt', 'decrypt', 'decrypt_with_key']:
        break
    else:
        print("Invalid mode. Please enter 'encrypt', 'decrypt', or 'decrypt_with_key'.")

# Get user input for text and keyword (if encrypting or decrypting with key)
text = input("Enter text: ").lower()
if mode == 'encrypt':
    keyword = input("Enter keyword (max length 4): ").lower()
    result = vigenere_cipher(text, keyword, mode)
    print("Ciphertext:", result)
elif mode == 'decrypt':
    result = brute_force(text)
    if result:
        print("Possible decryption:", result)
    else:
        print("Unable to decrypt with high confidence.")
else:  # decrypt_with_key mode
    keyword = input("Enter key to use for decryption: ").lower()
    result = vigenere_cipher(text, keyword, 'decrypt')  # Use decrypt mode
    print("Decryption:", result)
