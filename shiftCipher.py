
def decrypt_shift_cipher(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        # check if alpha
        if char.isalpha():
            # shift by specified amount
            if char.islower():
                decrypted_text += chr((ord(char) -
                                      ord('a') - shift) % 26 + ord('a'))
            else:
                decrypted_text += chr((ord(char) -
                                      ord('A') - shift) % 26 + ord('A'))
        else:
            decrypted_text += char
    return decrypted_text


def brute_force_decrypt(ciphertext):
    for shift in range(26):
        decrypted_text = decrypt_shift_cipher(ciphertext, shift)
        print(f"Shift {shift}: {decrypted_text}")


# Example ciphertext
ciphertext = "BEEAKFYDJXUQYHYJIQRYHTYJIQFBQDUYJIIKFUHCQD"
brute_force_decrypt(ciphertext)
