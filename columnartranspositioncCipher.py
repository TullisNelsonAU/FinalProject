# import detectEnglish
# from itertools import permutations

# def isEnglish(message):
#     """Checks if a message is likely English text."""
#     return detectEnglish.isEnglish(message) 

# def encrypt(plaintext, key, keep_spaces=False):  # Added keep_spaces parameter
#     """Encrypts plaintext using a columnar transposition cipher with a given key."""
#     if not keep_spaces:
#         plaintext = plaintext.replace(" ", "")

#     # Handle both integer and string keys
#     if isinstance(key, int):
#         key = str(key)  # Convert integer key to a string
#     ciphertext = [''] * len(key)  

#     col = 0
#     for char in plaintext:
#         ciphertext[col] += char
#         col = (col + 1) % len(key)

#     return ''.join(ciphertext)


# def decrypt(ciphertext, key, keep_spaces=False):  # Added keep_spaces parameter
#     """Decrypts a columnar transposition cipher using a specific key."""
#     order = sorted(range(len(key)), key=lambda k: key[k])
#     numRows = (len(ciphertext) + len(key) - 1) // len(key)  
#     numCols = len(key)
#     numRowsPerCol = [numRows] * numCols 

#     # Distribute leftover characters into shorter columns first
#     extra = len(ciphertext) % numCols  
#     for i in range(extra): 
#         numRowsPerCol[i] += 1  

#     col = 0
#     decoded = [''] * len(ciphertext)  
#     for index in range(len(ciphertext)):  
#         row = index // numRowsPerCol[col]  
#         pos = order[col] * numRowsPerCol[col] + row  
#         decoded[pos] = ciphertext[index]  
#         col = (col + 1) % numCols  

#     return ''.join(decoded)



# def crack(ciphertext):
#   """Attempts to crack the columnar transposition cipher using a brute-force approach."""
#   potential_solutions = []
#   for keyLength in range(1, len(ciphertext) + 1):
#     # Try all possible key permutations
#     if keyLength > 1:
#         for key in permutations(range(keyLength)):
#         # Decrypt with the current key
#             print("Current key:", key)
#             plaintext = decrypt(ciphertext, keyLength)

#             if isEnglish(plaintext):
#                 return plaintext, keyLength 
#     else:
#         # Check if the decrypted text is likely English
#         plaintext = decrypt(ciphertext, keyLength)
#         if isEnglish(plaintext):
#             potential_solutions.append((plaintext, keyLength)) 

#   if potential_solutions:
#     return min(potential_solutions, key=lambda x: isEnglish(x[0]))
#   else:
#     return None 
#   # No key found
#   return None, None

# def main():
#     while True:
#         choice = input("Choose an option (e/d/c):\n"
#                        "  e: Encrypt\n"
#                        "  d: Decrypt\n"
#                        "  c: Crack\n"
#                        "  q: Quit\n"
#                        "Enter your choice: ").lower()

#         if choice == 'e':
#             plaintext = input("Enter plaintext: ")
#             key = int(input("Enter key (a number): "))
#             ciphertext = encrypt(plaintext, key)
#             print("Ciphertext:", ciphertext)

#         elif choice == 'd':
#             ciphertext = input("Enter ciphertext: ")
#             key = int(input("Enter key (a number): "))
#             plaintext = decrypt(ciphertext, key)
#             print("Plaintext:", plaintext)

#         elif choice == 'c':
#             ciphertext = input("Enter ciphertext: ")
#             result, key = crack(ciphertext)
#             if result:
#                 print("Most likely decrypted text:", result)
#                 print("Key (Key Length):", key)
#             else:
#                 print("Unable to crack the cipher.")

#         elif choice == 'q':
#             break
#         else:
#             print("Invalid choice.")

# if __name__ == "__main__":
#     main()




import nltk
from pycld2 import detect
from itertools import permutations

nltk.download('words') 
from nltk.corpus import words
ENGLISH_WORDS = set(words.words()) 

def isEnglish(message):
    """Checks if a message is likely English text."""
    # Use pycld2's detection (reliable=True improves accuracy)
    _, _, details = detect(message, bestEffort=True) 
    return details[0][1] == 'ENGLISH' 

def encrypt(plaintext, key, keep_spaces=False):
    """Encrypts plaintext using a columnar transposition cipher with a given key."""
    if not keep_spaces:
        plaintext = plaintext.replace(" ", "") 

    ciphertext = [''] * len(key)  
    col = 0
    for char in plaintext:
        ciphertext[col] += char
        col = (col + 1) % len(key) 

    return ''.join(ciphertext)

def decrypt(ciphertext, key, keep_spaces=False):
    """Decrypts a columnar transposition cipher using a specific key."""
    order = sorted(range(len(key)), key=lambda k: key[k])
    numRows = len(ciphertext) // len(key) # Integer division for base rows 
    numCols = len(key)
    numRowsPerCol = [numRows] * numCols  

    extra = len(ciphertext) % numCols  
    for i in range(extra): 
        numRowsPerCol[i] += 1  # Dis

    col = 0
    decoded = [''] * len(ciphertext)  # Create decoded list to match ciphertext length
    for index in range(len(ciphertext)):  
        row = index // numRowsPerCol[col]  
        pos = order[col] * numRowsPerCol[col] + row  
        print(f"index: {index}, col: {col}, row: {row}, pos: {pos}, len(decoded): {len(decoded)}") # Add this line
        decoded[pos] = ciphertext[index]  
        col = (col + 1) % numCols  

    return ''.join(decoded)

def calculate_score(text):
    """Calculates a score reflecting how likely 'text' is English using word frequencies."""
    score = 0
    for word in text.split():
        if word.lower() in ENGLISH_WORDS:
            score += len(word)  
    return score

def crack(ciphertext):
    """Tries to crack a columnar transposition cipher using brute force and English scoring."""
    potential_solutions = []
    for keyLength in range(1, len(ciphertext) + 1):
        if keyLength > 1:
            for key in permutations(range(keyLength)):
                    # Decrypt with the current key
                    plaintext = decrypt(ciphertext, keyLength)
                    score = calculate_score(plaintext) 
                    potential_solutions.append((plaintext, keyLength, score)) 
        else:
            plaintext = decrypt(ciphertext, keyLength)
            score = calculate_score(plaintext) 
            potential_solutions.append((plaintext, keyLength, score)) 

    if potential_solutions:
        return sorted(potential_solutions, key=lambda x: x[2], reverse = True)[0]
    else:
        return None 

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
            key = input("Enter key: ")  
            ciphertext = encrypt(plaintext, key)
            print("Ciphertext:", ciphertext)

        elif choice == 'd':
            ciphertext = input("Enter ciphertext: ")
            key = input("Enter key: ")  
            plaintext = decrypt(ciphertext, key)
            print("Plaintext:", plaintext)

        elif choice == 'c':
            ciphertext = input("Enter ciphertext: ")
            result, key, score = crack(ciphertext)
            if result:
                print("Most likely decrypted text:", result)
                print("Key (Key Length):", key)
                print("Score:", score)
            else:
                print("Unable to crack the cipher.")

        elif choice == 'q':
            break
        else:
            print("Invalid choice.")




if __name__ == '__main__':
    main()
