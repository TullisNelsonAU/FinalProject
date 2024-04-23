import string

alphabet = string.ascii_lowercase


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def encrypt(text, a, b):
    result = ""
    for char in text.lower():
        if char in alphabet:
            x = alphabet.index(char)
            result += alphabet[(a * x + b) % 26]
        else:
            result += char
    return result


def mod_inverse(a, m):
    """Calculates the modular multiplicative inverse of 'a' modulo 'm'
       using the Extended Euclidean Algorithm.

       Returns the inverse if it exists, otherwise returns None.
    """
    if gcd(a, m) != 1:
        return None  # No inverse exists

    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m

    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (
            u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m


def decrypt(text, a, b):
    a_inverse = mod_inverse(a, 26)
    result = ""
    for char in text.lower():
        if char in alphabet:
            x = alphabet.index(char)
            result += alphabet[(a_inverse * (x - b)) % 26]
        else:
            result += char
    return result


def frequency_analysis(text):
    letter_counts = {letter: 0 for letter in alphabet}
    for char in text.lower():
        if char in alphabet:
            letter_counts[char] += 1

    total_letters = sum(letter_counts.values())
    letter_freqs = {letter: count / total_letters for letter,
                    count in letter_counts.items()}
    return letter_freqs


# https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html
expected_freqs = {
    'a': 0.082, 'b': 0.015, 'c': 0.028, 'd': 0.043, 'e': 0.127, 'f': 0.022, 'g': 0.020, 'h': 0.061, 'i': 0.070,
    'j': 0.002, 'k': 0.008, 'l': 0.040, 'm': 0.024, 'n': 0.067, 'o': 0.075, 'p': 0.019, 'q': 0.001, 'r': 0.060,
    's': 0.063, 't': 0.091, 'u': 0.028, 'v': 0.010, 'w': 0.020, 'x': 0.001, 'y': 0.019, 'z': 0.001
}


def score_text(text):
    observed_freqs = frequency_analysis(text)
    chi_squared = 0.0

    for letter in alphabet:
        expected = expected_freqs[letter] * len(text)
        observed = observed_freqs[letter] * len(text)
        chi_squared += ((observed - expected) ** 2) / expected

    return -chi_squared


def crack_cipher(ciphertext):
    best_score = -float('inf')
    best_key = None

    for a in range(1, 26):
        if gcd(a, 26) != 1:
            continue

        for b in range(26):
            decrypted = decrypt(ciphertext, a, b)
            score = score_text(decrypted)

            if score > best_score:
                best_score = score
                best_key = (a, b)

    return best_key, decrypt(ciphertext, *best_key)


def main():
    choice = input(
        "Do you want to encrypt (E), decrypt (D), or decrypt  with key (DK)? ").upper()

    if choice == 'E':
        plaintext = input("Enter plaintext: ")
        key1 = int(input("Enter Key 1: "))
        key2 = int(input("Enter Key 2: "))
        print(encrypt(plaintext, key1, key2))

    elif choice == 'D':
        ciphertext = input("Enter ciphertext: ")
        key, plaintext = crack_cipher(ciphertext)
        print("Cracked Key:", key)
        print("Decrypted Plaintext:", plaintext)

    elif choice == 'DK':
        ciphertext = input("Enter ciphertext: ")
        key1 = int(input("Enter key1: "))
        key2 = int(input("Enter key2: "))
        print("Decrypted Ciphertext:", decrypt(ciphertext, key1, key2))

    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
