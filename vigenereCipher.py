from nltk.corpus import words
import string
import nltk  # Import the NLTK library
nltk.download('words')  # Make sure to download the word list
ENGLISH_WORDS = set(words.words())  # Define ENGLISH_WORDS globally


def vigenere_cipher(plain_text, keyword, mode):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result_text = ''

    # If the keyword is longer than the plaintext, truncate it
    if len(keyword) > len(plain_text):
        keyword = keyword[:len(plain_text)]
    elif len(keyword) < len(plain_text):  # If the keyword is shorter, repeat it
        keyword = (keyword * (len(plain_text) //
                   len(keyword) + 1))[:len(plain_text)]

    for i in range(len(plain_text)):
        plain_char = plain_text[i]
        keyword_char = keyword[i % len(keyword)]

        if plain_char.isalpha():
            shift = alphabet.index(keyword_char)
            if mode == 'encrypt':
                result_char = alphabet[(
                    alphabet.index(plain_char) + shift) % 26]
            elif mode == 'decrypt':
                result_char = alphabet[(
                    alphabet.index(plain_char) - shift) % 26]
        else:
            result_char = plain_char

        result_text += result_char

    return result_text


def calculate_score(text):
    """Calculates a score reflecting how likely 'text' is English.
    This is a placeholder - we need a more robust implementation
    """
    ENGLISH_WORDS = set(words.words())  # Load the English word list
    score = 0
    for word in text.split():
        if word.lower() in ENGLISH_WORDS:
            score += len(word)
    return score


def generate_keys(length):
    """Generates all possible keys of a given length."""
    if length == 1:
        return string.ascii_lowercase
    else:
        return [char + subkey
                for char in string.ascii_lowercase
                for subkey in generate_keys(length - 1)]


def calculate_score(text):
    """Calculates a score reflecting how likely 'text' is English.
    This is a placeholder - you'll need a more robust implementation
    """
    score = 0
    for word in text.split():
        if word.lower() in ENGLISH_WORDS:  # Assuming you have a set called ENGLISH_WORDS
            score += len(word)
    return score


def brute_force(ciphertext, max_key_length):
    """Attempts to crack a Vigenère cipher using brute force."""
    best_decryption = None
    best_decryption_score = 0

    for key_length in range(1, max_key_length + 1):
        for possible_key in generate_keys(key_length):
            decryption = vigenere_cipher(ciphertext, possible_key, 'decrypt')
            score = calculate_score(decryption)

            if not best_decryption or score > best_decryption_score:
                best_decryption = decryption
                best_decryption_score = score

    return best_decryption

# ... Your existing example usage code ...


# Additional usage for cracking
ciphertext = input("Enter the ciphertext: ").lower()
max_key_length = int(input("Enter the maximum keyword length to try: "))
result = brute_force(ciphertext, max_key_length)

if result:
    print("Possible decryption:", result)
