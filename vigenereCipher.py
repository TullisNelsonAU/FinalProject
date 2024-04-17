def vigenere_cipher(plain_text, keyword, mode):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result_text = ''

    # If the keyword is longer than the plaintext, truncate it
    if len(keyword) > len(plain_text):
        keyword = keyword[:len(plain_text)]
    # If the keyword is shorter than the plaintext, repeat it
    elif len(keyword) < len(plain_text):
        keyword = (keyword * (len(plain_text) //
                   len(keyword) + 1))[:len(plain_text)]

    for i in range(len(plain_text)):
        plain_char = plain_text[i]
        # Use modulo to repeat keyword cyclically
        keyword_char = keyword[i % len(keyword)]

        if plain_char.isalpha():  # Check if the character is alphabetic
            shift = alphabet.index(keyword_char)
            if mode == 'encrypt':
                result_char = alphabet[(
                    alphabet.index(plain_char) + shift) % 26]
            elif mode == 'decrypt':
                result_char = alphabet[(
                    alphabet.index(plain_char) - shift) % 26]
        else:
            result_char = plain_char  # Leave non-alphabetic characters unchanged

        result_text += result_char

    return result_text


# Example usage
plaintext = input("Enter the message: ").lower()
keyword = input("Enter the keyword: ").lower()
mode = input("Enter 'encrypt' or 'decrypt': ").lower()

if mode == 'encrypt' or mode == 'decrypt':
    result = vigenere_cipher(plaintext, keyword, mode)
    print(f"{mode.capitalize()}ed message:", result)
else:
    print("Invalid mode. Please choose 'encrypt' or 'decrypt'.")
