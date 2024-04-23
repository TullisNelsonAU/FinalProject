import detectEnglish
from itertools import permutations

def isEnglish(message):
    """Checks if a message is likely English text."""
    return detectEnglish.isEnglish(message) 

def encrypt(plaintext, key):
    """Encrypts plaintext using a columnar transposition cipher with a given key."""
    plaintext = plaintext.replace(" ", "")  # Remove spaces
    ciphertext = [''] * key

    col = 0
    for char in plaintext:
        ciphertext[col] += char
        col = (col + 1) % key
        print(col)

    return ''.join(ciphertext)

def decrypt(ciphertext, key):
    """Decrypts a columnar transposition cipher using a specific key."""
    numRows = (len(ciphertext) + key - 1) // key  # Handle extra characters
    numExtra = len(ciphertext) % key
    transposed = [[] for _ in range(key)]

    col, row = 0, 0
    for char in ciphertext:
        print(f"Before append - col: {col}, row: {row}") 
        transposed[col].append(char)       
        if col >= key - 1:  
            col = 0  # Reset column immediately after updating row 
            row += 1
        elif row == numRows and col < numExtra: 
            print(f"Resetting row - col: {col}, row: {row}") 
            row = 0 
        print(f"col before increment: {col}")
        if col < key - 1:  
            col += 1 
        print(f"col after increment: {col}") # Added for debugging 
    print(transposed)


    result = ''.join(''.join(row) for row in transposed)  
    return result 


def crack(ciphertext):
  """Attempts to crack the columnar transposition cipher using a brute-force approach."""
  potential_solutions = []
  for keyLength in range(1, len(ciphertext) + 1):
    # Try all possible key permutations
    if keyLength > 1:
        for key in permutations(range(keyLength)):
        # Decrypt with the current key
            print("Current key:", key)
            plaintext = decrypt(ciphertext, keyLength)

            if isEnglish(plaintext):
                return plaintext, keyLength 
    else:
        # Check if the decrypted text is likely English
        plaintext = decrypt(ciphertext, keyLength)
        if isEnglish(plaintext):
            potential_solutions.append((plaintext, keyLength)) 

  if potential_solutions:
    return min(potential_solutions, key=lambda x: isEnglish(x[0]))
  else:
    return None 
  # No key found
  return None, None

def main():
    while True:
        choice = input("Choose an option (e/d/c):\n"
                       "  e: Encrypt\n"
                       "  d: Decrypt\n"
                       "  c: Crack\n"
                       "  q: Quit\n"
                       "Enter your choice: ").lower()

        if choice == 'e':
            plaintext = input("Enter plaintext: ")
            key = int(input("Enter key (a number): "))
            ciphertext = encrypt(plaintext, key)
            print("Ciphertext:", ciphertext)

        elif choice == 'd':
            ciphertext = input("Enter ciphertext: ")
            key = int(input("Enter key (a number): "))
            plaintext = decrypt(ciphertext, key)
            print("Plaintext:", plaintext)

        elif choice == 'c':
            ciphertext = input("Enter ciphertext: ")
            result, key = crack(ciphertext)
            if result:
                print("Most likely decrypted text:", result)
                print("Key (Key Length):", key)
            else:
                print("Unable to crack the cipher.")

        elif choice == 'q':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
