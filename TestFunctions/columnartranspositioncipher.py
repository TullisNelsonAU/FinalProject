def encrypt(plaintext, key):
    """Encrypts plaintext using a columnar transposition cipher with a given key."""
    plaintext = plaintext.replace(" ", "")  # Remove spaces
    ciphertext = [''] * key

    col = 0
    for char in plaintext:
        ciphertext[col] += char
        col = (col + 1) % key
        print(f"Column distribution: {ciphertext}")  # Added

    return ''.join(ciphertext)

def decrypt(ciphertext, key):
    """Decrypts a columnar transposition cipher using a specific key."""
    numRows = (len(ciphertext) + key - 1) // key  # Handle extra characters
    numExtra = len(ciphertext) % key
    transposed = [[] for _ in range(key)]

    col, row = 0, 0  
    for char in ciphertext:
        transposed[col].append(char)
        row += 1
        if row == numRows:
            col += 1         # Update column first
            row = 0 
        print(f"Transposed: {transposed}")  # Added

    result = ''.join(''.join(row) for row in transposed)  
    return result 


def main():
    while True:
        choice = input("Do you want to encrypt or decrypt? (e/d): ").lower()
        if choice not in ('e', 'd'):
            print("Invalid choice. Please enter 'e' for encrypt or 'd' for decrypt.")
            continue

        if choice == 'e':
            plaintext = input("Enter plaintext: ")
            key = int(input("Enter key (a number): "))
            ciphertext = encrypt(plaintext, key)
            print("Ciphertext:", ciphertext)
        else:  # choice == 'd' 
            ciphertext = input("Enter ciphertext: ")
            key = int(input("Enter key (a number): "))
            plaintext = decrypt(ciphertext, key)
            print("Plaintext:", plaintext)

        if input("Continue? (y/n): ").lower() != 'y':
            break

if __name__ == "__main__":
    main()