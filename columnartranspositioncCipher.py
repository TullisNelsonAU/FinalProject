#columnar transposition cipher
import detectEnglish

# def isEnglish(message):
#   """Checks if a string is likely to be English text using character frequency analysis."""
#   # Create a frequency table for common English letters
#   englishFreq = {'e': 12.51, 't': 9.09, 'a': 8.16, 'o': 7.57, 'i': 7.00, 'n': 6.24, 
#                  's': 6.02, 'r': 5.99, 'h': 5.28, 'd': 4.32, 'l': 3.98, 'u': 2.88, 
#                  'c': 2.71, 'm': 2.67, 'f': 2.20, 'y': 2.11, 'w': 1.78, 'g': 1.53,
#                  'p': 1.49, 'b': 1.49, 'v': 0.99, 'k': 0.77, 'x': 0.15, 'j': 0.15,
#                  'q': 0.10, 'z': 0.07}
#   # Remove spaces and punctuation
#   message = message.lower().replace(" ", "").replace(",","").replace(".","")
#   # Count character frequencies in the message
#   freqTable = {char: message.count(char) for char in message}
#   # Calculate the chi-square statistic for deviation from expected frequencies
#   chiSquare = sum([((freqTable[char] - englishFreq[char])**2) / englishFreq[char] for char in freqTable])
#   # Higher chi-square indicates less likely to be English
#   return chiSquare > 16
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
