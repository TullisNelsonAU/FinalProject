# # Python3 program to illustrate
# # Rail Fence Cipher Encryption
# # and Decryption
 
# # function to encrypt a message

# def encryptRailFence(text, key):
 

#     # create the matrix to cipher

#     # plain text key = rows ,

#     # length(text) = columns

#     # filling the rail matrix

#     # to distinguish filled

#     # spaces from blank ones

#     rail = [['\n' for i in range(len(text))]

#                 for j in range(key)]

     

#     # to find the direction

#     dir_down = False

#     row, col = 0, 0

     

#     for i in range(len(text)):

         

#         # check the direction of flow

#         # reverse the direction if we've just

#         # filled the top or bottom rail

#         if (row == 0) or (row == key - 1):

#             dir_down = not dir_down

         

#         # fill the corresponding alphabet

#         rail[row][col] = text[i]

#         col += 1

         

#         # find the next row using

#         # direction flag

#         if dir_down:

#             row += 1

#         else:

#             row -= 1

#     # now we can construct the cipher

#     # using the rail matrix

#     result = []

#     for i in range(key):

#         for j in range(len(text)):

#             if rail[i][j] != '\n':

#                 result.append(rail[i][j])

#     return("" . join(result))

     
# # This function receives cipher-text
# # and key and returns the original
# # text after decryption

# def decryptRailFence(cipher, key):
 

#     # create the matrix to cipher

#     # plain text key = rows ,

#     # length(text) = columns

#     # filling the rail matrix to

#     # distinguish filled spaces

#     # from blank ones

#     rail = [['\n' for i in range(len(cipher))]

#                 for j in range(key)]

     

#     # to find the direction

#     dir_down = None

#     row, col = 0, 0

     

#     # mark the places with '*'

#     for i in range(len(cipher)):

#         if row == 0:

#             dir_down = True

#         if row == key - 1:

#             dir_down = False

         

#         # place the marker

#         rail[row][col] = '*'

#         col += 1

         

#         # find the next row

#         # using direction flag

#         if dir_down:

#             row += 1

#         else:

#             row -= 1

             

#     # now we can construct the

#     # fill the rail matrix

#     index = 0

#     for i in range(key):

#         for j in range(len(cipher)):

#             if ((rail[i][j] == '*') and

#             (index < len(cipher))):

#                 rail[i][j] = cipher[index]

#                 index += 1

         

#     # now read the matrix in

#     # zig-zag manner to construct

#     # the resultant text

#     result = []

#     row, col = 0, 0

#     for i in range(len(cipher)):

         

#         # check the direction of flow

#         if row == 0:

#             dir_down = True

#         if row == key-1:

#             dir_down = False

             

#         # place the marker

#         if (rail[row][col] != '*'):

#             result.append(rail[row][col])

#             col += 1

             

#         # find the next row using

#         # direction flag

#         if dir_down:

#             row += 1

#         else:

#             row -= 1

#     return("".join(result))
 
# # Driver code

# if __name__ == "__main__":

#     print(encryptRailFence("attack at once", 2))

#     print(encryptRailFence("GeeksforGeeks ", 3))

#     print(encryptRailFence("defend the east wall", 3))

     

#     # Now decryption of the

#     # same cipher-text

#     print(decryptRailFence("GsGsekfrek eoe", 3))

#     print(decryptRailFence("atc toctaka ne", 2))

#     print(decryptRailFence("dnhaweedtees alf  tl", 3))
 
# # This code is contributed
# # by Pratik Somwanshi




import random  # We'll use this for a minor improvement

class RailFence:
    def __init__(self):
        pass  # No need for initialization in the Python version

    def encrypt(self, plain_text, key):
        encrypted_text = ""
        col = len(plain_text)
        row = key
        check = False
        j = 0
        rail = [['*' for _ in range(col)] for _ in range(row)]  

        for i in range(col):
            if j == 0 or j == key - 1:
                check = not check
            rail[j][i] = plain_text[i] 
            j += 1 if check else -1 

        print("Rail of encryption:")
        for i in range(row):
            for k in range(col):
                ch = rail[i][k]
                if ch != '*':
                    encrypted_text += ch
                print(ch, end=" ")
            print() 

        return encrypted_text

    def decrypt(self, encrypted_text, key):
        decrypted_text = ""
        col = len(encrypted_text)
        row = key
        check = False
        j = 0
        rail = [['*' for _ in range(col)] for _ in range(row)] 

        for i in range(col):
            if j == 0 or j == key - 1:
                check = not check
            rail[j][i] = '#' 
            j += 1 if check else -1 
            
        index = 0
        for i in range(row):
            for k in range(col):
                if rail[i][k] == '#' and index < col: 
                    rail[i][k] = encrypted_text[index]
                    index += 1
                
        j = 0
        check = False
        for i in range(col):
            if j == 0 or j == key - 1:
                check = not check
            decrypted_text += rail[j][i] 
            j += 1 if check else -1
        return decrypted_text



if __name__ == "__main__":
    cipher = RailFence()

    while True:
        print("\nRail Fence Cipher")
        print("-----------------")
        choice = input("(1) Encrypt\n(2) Decrypt\n(3) Brute-Force Decrypt\n(4) Exit\n\nEnter your choice: ")

        if choice == '1':
            plain_text = input("Enter the plain text: ")
            key = int(input("Enter the key: "))
            encrypted_text = cipher.encrypt(plain_text, key)
            print("Encrypted text is:", encrypted_text)

        elif choice == '2':
            encrypted_text = input("Enter the encrypted text: ")
            key = int(input("Enter the key: "))
            decrypted_text = cipher.decrypt(encrypted_text, key)
            print("Decrypted text is:", decrypted_text)

        elif choice == '3':
            encrypted_text = input("Enter the encrypted text: ")

            # Brute-force parameters
            max_key_level = 15

            print("\nTrying different key levels and offsets...\n")
            for key in range(2, max_key_level + 1):  # Start from key level 2 
                    possible_plaintext = cipher.decrypt(encrypted_text, key)

                    # Here you might want to add checks to see if the
                    #  decrypted text looks like English or some other recognizable format
                    print(f"Key: {key} -> {possible_plaintext}")

        else:
            break







