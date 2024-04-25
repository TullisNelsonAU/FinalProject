import nltk
from itertools import permutations
import string

# Download NLTK word corpus if not already downloaded
nltk.download('words')


list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def is_english_word(word):
    return word.lower() in set(nltk.corpus.words.words())

# Function to convert the string to lowercase


def toLowerCase(text):
    return text.lower()

# Rest of the code remains the same...


# Function to remove all spaces in a string
def removeSpaces(text):
    return ''.join(text.split())

# Function to group 2 elements of a string as a list element


def Diagraph(text):
    Diagraph = []
    group = 0
    for i in range(2, len(text), 2):
        Diagraph.append(text[group:i])
        group = i
    Diagraph.append(text[group:])
    return Diagraph

# Function to fill a letter in a string element If 2 letters in the same string matches


def FillerLetter(text):
    k = len(text)
    if k % 2 == 0:
        for i in range(0, k, 2):
            if text[i] == text[i+1]:
                new_word = text[0:i+1] + str('x') + text[i+1:]
                new_word = FillerLetter(new_word)
                break
            else:
                new_word = text
    else:
        for i in range(0, k-1, 2):
            if text[i] == text[i+1]:
                new_word = text[0:i+1] + str('x') + text[i+1:]
                new_word = FillerLetter(new_word)
                break
            else:
                new_word = text
    return new_word


def generateKeyTable(key, list1):
    key_letters = []
    for i in key:
        if i not in key_letters:
            key_letters.append(i)

    compElements = []
    for i in key_letters:
        if i not in compElements:
            compElements.append(i)
    for i in list1:
        if i not in compElements:
            compElements.append(i)

    matrix = []
    while compElements != []:
        matrix.append(compElements[:5])
        compElements = compElements[5:]

    return matrix


def search(mat, element):
    for i in range(5):
        for j in range(5):
            if (mat[i][j] == element):
                return i, j


def encrypt_RowRule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    if e1c == 4:
        char1 = matr[e1r][0]
    else:
        char1 = matr[e1r][e1c+1]

    char2 = ''
    if e2c == 4:
        char2 = matr[e2r][0]
    else:
        char2 = matr[e2r][e2c+1]

    return char1, char2


def encrypt_ColumnRule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    if e1r == 4:
        char1 = matr[0][e1c]
    else:
        char1 = matr[e1r+1][e1c]

    char2 = ''
    if e2r == 4:
        char2 = matr[0][e2c]
    else:
        char2 = matr[e2r+1][e2c]

    return char1, char2


def encrypt_RectangleRule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    char1 = matr[e1r][e2c]

    char2 = ''
    char2 = matr[e2r][e1c]

    return char1, char2


def encryptByPlayfairCipher(Matrix, plainList):
    CipherText = []
    for i in range(0, len(plainList)):
        c1 = 0
        c2 = 0
        ele1_x, ele1_y = search(Matrix, plainList[i][0])
        ele2_x, ele2_y = search(Matrix, plainList[i][1])

        if ele1_x == ele2_x:
            c1, c2 = encrypt_RowRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
        elif ele1_y == ele2_y:
            c1, c2 = encrypt_ColumnRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
        else:
            c1, c2 = encrypt_RectangleRule(
                Matrix, ele1_x, ele1_y, ele2_x, ele2_y)

        cipher = c1 + c2
        CipherText.append(cipher)
    return CipherText


def decrypt(str, keyT):
    ps = len(str)
    i = 0
    while i < ps:
        a = search(keyT, str[i])
        b = search(keyT, str[i + 1])
        if a[0] == b[0]:
            str = str[:i] + keyT[a[0]
                                 ][mod5(a[1]-1)] + keyT[b[0]][mod5(b[1]-1)] + str[i+2:]
        elif a[1] == b[1]:
            str = str[:i] + keyT[mod5(a[0]-1)][a[1]] + \
                keyT[mod5(b[0]-1)][b[1]] + str[i+2:]
        else:
            str = str[:i] + keyT[a[0]][b[1]] + keyT[b[0]][a[1]] + str[i+2:]
        i += 2
    return str


def decryptByPlayfairCipher(str, key):
    ks = len(key)
    key = removeSpaces(toLowerCase(key))
    str = removeSpaces(toLowerCase(str))
    keyT = generateKeyTable(key, list1)
    decrypted_text = decrypt(str, keyT)
    decrypted_text = decrypted_text.replace(
        'x', '')  # Remove any 'x' characters
    return decrypted_text


def mod5(a):
    if a < 0:
        a += 5
    return a % 5


def bruteForceCrack(cipher_text):
    for key in list1:
        key = removeSpaces(toLowerCase(key))
        keyT = generateKeyTable(key, list1)
        decrypted_text = decrypt(cipher_text, keyT)
        decrypted_text = decrypted_text.replace(
            'x', '')  # Remove any 'x' characters
        words = decrypted_text.split()
        if all(is_english_word(word) for word in words):
            print(f"Key: {key}, Deciphered text: {decrypted_text}")
            break
    else:
        print("Failed to crack: No English words found in decrypted text")


def main():
    while True:
        print("\nMenu:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Crack")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            text = input("Enter the text to encrypt: ")
            key = input("Enter the key: ")
            text = removeSpaces(toLowerCase(text))
            PlainTextList = Diagraph(FillerLetter(text))
            if len(PlainTextList[-1]) != 2:
                PlainTextList[-1] = PlainTextList[-1]+'z'
            key = removeSpaces(toLowerCase(key))
            Matrix = generateKeyTable(key, list1)
            CipherList = encryptByPlayfairCipher(Matrix, PlainTextList)
            CipherText = "".join(CipherList)
            print("CipherText:", CipherText)
        elif choice == '2':
            text = input("Enter the text to decrypt: ")
            key = input("Enter the key: ")
            text = removeSpaces(toLowerCase(text))
            key = removeSpaces(toLowerCase(key))
            decrypted_text = decryptByPlayfairCipher(text, key)
            print("Deciphered text:", decrypted_text)
        elif choice == '3':
            cipher_text = input("Enter the cipher text to crack: ")
            bruteForceCrack(cipher_text)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
