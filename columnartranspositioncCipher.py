#columnar transposition cipher
import detectEnglish


def isEnglish(message):
    detectEnglish.isEnglish(message)


def decrypt(ciphertext, key):
  """Decrypts a columnar transposition cipher using a specific key."""
  # Create empty list to store transposed rows
  transposed = [[] for _ in range(key)]
  # Fill the transposed rows with characters based on the key
  for i, char in enumerate(ciphertext):
    transposed[i % key].append(char)
  # Combine rows in order specified by the key
  plaintext = ''.join(''.join(row) for row in (zip(*transposed)))
  return plaintext

def crack(ciphertext):
  """Attempts to crack the columnar transposition cipher using a brute-force approach."""
  # Test key lengths from 1 to the length of the ciphertext
  potential_solutions = []
  for keyLength in range(1, len(ciphertext) + 1):
    # Try all possible key permutations
    if keyLength > 1:
        for key in permutations(range(keyLength)):
        # Decrypt with the current key
            print("Current key:", key)
            plaintext = decrypt(ciphertext, len(key))

            if detectEnglish.isEnglish(plaintext):
                return plaintext, key
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

# Import module for generating permutations (needs to be installed: pip install itertools)
from itertools import permutations

# Example usage
ciphertext = "IEHHETR"  # Example cipher text
plaintext, key = crack(ciphertext)

if plaintext:
  print("Decrypted Text:", plaintext)
  print("Key (Key Length):", len(key))
else:
  print("Unable to crack the cipher.")
