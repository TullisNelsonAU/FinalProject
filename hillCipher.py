import numpy as np
# curently not working


def get_key_matrix(key):
    """Converts a key string into a square matrix for Hill Cipher."""

    key = key.upper().replace(" ", "")  # Prepare the key
    key_size = int(np.sqrt(len(key)))

    det = int(np.linalg.det(key_matrix))
    if math.gcd(det, 26) != 1:
        raise ValueError("Invalid key. Key matrix is not invertible.")

    # Check for valid key size (must be perfect square)
    if key_size * key_size != len(key):
        raise ValueError(
            "Invalid key. Key length must be a perfect square (e.g., 4, 9, 16).")

    # Create the key matrix and fill with characters
    key_matrix = np.zeros((key_size, key_size), dtype=int)
    for i, char in enumerate(key):
        key_matrix[i // key_size, i %
                   key_size] = ord(char) - 65  # Convert to 0-25 index

    return key_matrix


def mod_inverse(det, mod):
    """Calculates the modular multiplicative inverse."""

    det_inv = pow(det, -1, mod)  # Using efficient pow for modular inverse
    return det_inv


def encrypt(plaintext, key_matrix):
    """Encrypts plaintext using the Hill Cipher."""

    plaintext = plaintext.upper().replace(" ", "")

    # Add padding if necessary
    if len(plaintext) % key_matrix.shape[0] != 0:
        plaintext += 'X' * \
            (key_matrix.shape[0] - len(plaintext) % key_matrix.shape[0])

    ciphertext = ''
    for i in range(0, len(plaintext), key_matrix.shape[0]):
        # Extract a block of text the same size as the key matrix
        text_block = plaintext[i:i + key_matrix.shape[0]]

        # Convert characters to a numeric vector
        vector = np.array([ord(c) - 65 for c in text_block])

        # Multiply by the key matrix and take modulo 26
        cipher_vector = (key_matrix @ vector) % 26

        # Convert back to characters and append to the ciphertext
        ciphertext += ''.join(chr(c + 65) for c in cipher_vector)

    return ciphertext


def decrypt(ciphertext, key_matrix):
    """Decrypts ciphertext using the Hill Cipher."""

    # Calculate the determinant of the key matrix
    det = int(round(np.linalg.det(key_matrix)))

    # Find its inverse modulo 26
    det_inv = mod_inverse(det, 26)
    if det_inv == None:
        raise ValueError(
            "Key matrix is not invertible. Decryption not possible.")

    # Calculate the inverse of the key matrix (with modular arithmetic)
    key_matrix_inv = det_inv * \
        np.round(np.linalg.inv(key_matrix) * det).astype(int) % 26

    return encrypt(ciphertext, key_matrix_inv)  # Reuse the encrypt function

# ----------------------- Main Program ------------------------------


if __name__ == '__main__':
    while True:
        choice = input("Encrypt or Decrypt? (e/d/q to quit): ").lower()

        if choice == 'q':
            break

        elif choice == 'e':
            plaintext = input("Enter plaintext: ")
            key = input("Enter key: ")
            key_matrix = get_key_matrix(key)
            ciphertext = encrypt(plaintext, key_matrix)
            print("Ciphertext:", ciphertext)

        elif choice == 'd':
            ciphertext = input("Enter ciphertext: ")
            key = input("Enter key: ")
            key_matrix = get_key_matrix(key)
            plaintext = decrypt(ciphertext, key_matrix)
            print("Plaintext:", plaintext)

        else:
            print("Invalid choice.")
