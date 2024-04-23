from nltk.corpus import words
import nltk
nltk.download('words')  # Download words list if not already downloaded

word_list = words.words()


def encrypt_shift_cipher(plaintext, shift):
    """Encrypts plaintext using a Shift Cipher with the provided shift value."""
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            ciphertext += chr((ord(char) - base + shift) % 26 + base)
        else:
            ciphertext += char
    return ciphertext


def decrypt_shift_cipher(ciphertext, shift):
    """Decrypts ciphertext using a Shift Cipher with the provided shift value."""
    return encrypt_shift_cipher(ciphertext, -shift)  # Reuse encryption with negative shift


def find_likely_decryption(ciphertext, word_list):
    """Attempts to find the correct decryption of a Shift Cipher ciphertext."""
    best_shift = None
    max_word_match = 0

    for shift in range(26):
        decrypted_text = decrypt_shift_cipher(ciphertext, shift)
        words = decrypted_text.split()

        num_real_words = sum(word.lower() in word_list for word in words)
        if num_real_words > max_word_match:
            max_word_match = num_real_words
            best_shift = shift

    if best_shift is not None:
        print("Likely Decryption: ", decrypt_shift_cipher(ciphertext, best_shift))
        print("Likely key: ", best_shift)
    else:
        print("No likely decryption found.")


def main():
    choice = input("Do you want to encrypt (E) or decrypt (D)? ").upper()

    if choice == 'E':
        plaintext = input("Enter plaintext: ")
        shift = int(input("Enter shift (1-25): "))
        ciphertext = encrypt_shift_cipher(plaintext, shift)
        print("Ciphertext:", ciphertext)

    elif choice == 'D':
        ciphertext = input("Enter ciphertext: ")
        find_likely_decryption(ciphertext, word_list)

    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
