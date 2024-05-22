from collections import Counter
import re
from tr import tr  # to import it, write and run on terminal: pip install python-tr

# Define constant key
CONSTANT_KEY = {'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v',
                'f': 'u', 'g': 't', 'h': 's', 'i': 'r', 'j': 'q',
                'k': 'p', 'l': 'o', 'm': 'n', 'n': 'm', 'o': 'l',
                'p': 'k', 'q': 'j', 'r': 'i', 's': 'h', 't': 'g',
                'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c', 'y': 'b', 'z': 'a'}


# Encryption
def encrypt(message, key):
    encrypted_message = ''
    for char in message.lower():
        if char.isalpha():
            encrypted_message += key[char]
        else:
            encrypted_message += char
    return encrypted_message


# Decryption
def decrypt(encrypted_message, key):
    decrypted_message = ''
    reversed_key = {v: k for k, v in key.items()}
    for char in encrypted_message.lower():
        if char.isalpha():
            decrypted_message += reversed_key[char]
        else:
            decrypted_message += char
    return decrypted_message


# Read and send the original text
alice = open("example.txt")
txt = alice.read()
alice.close()
print("Alice sends the text:")
print(txt)
print("")

# Encrypt the text
print("Encrypted text:")
encrypted_text = encrypt(txt, CONSTANT_KEY)
print(encrypted_text)
print("")

# Writing encrypted text to a file
with open("encrypted.txt", "w") as file:
    encrypted_text = encrypt(txt, CONSTANT_KEY)
    file.write(encrypted_text)

# Decrypt the text
print("Decrypted text:")
decrypted_text = decrypt(encrypted_text, CONSTANT_KEY)
print(decrypted_text)

# Frequency analysis
TOP_K = 20
N_GRAM = 3


def ngrams(n, text):
    for i in range(len(text) - n + 1):
        if not re.search(r'\s', text[i:i + n]):
            yield text[i:i + n]


with open('encrypted.txt') as f:
    text = f.read()

for N in range(N_GRAM):
    print("-------------------------")
    print("{}-gram (top {}):".format(N + 1, TOP_K))
    counts = Counter(ngrams(N + 1, text))
    sorted_counts = counts.most_common(TOP_K)
    for ngram, count in sorted_counts:
        print("{}: {}".format(ngram, count))

# Trying to hack with replacing the words
frequency_analysis_key = "virmtzwngshykofxblducepjaq"
change_key = "ERINGADMTHSBPLUCYOWFXVKQZJ"
hack = tr(frequency_analysis_key, change_key, encrypted_text)
print(hack)

# Alice will send a message in another language, such as "Select
# your mother language" or "German language," and repeat steps
# 2 and 3.


# Define a new constant key
CONSTANT_KEY_2 = {
    'a': 'q', 'b': 'w', 'c': 'e', 'd': 'r', 'e': 't',
    'f': 'y', 'g': 'u', 'h': 'i', 'i': 'o', 'j': 'p',
    'k': 'a', 'l': 's', 'm': 'd', 'n': 'f', 'o': 'g',
    'p': 'h', 'q': 'j', 'r': 'k', 's': 'l', 't': 'z',
    'u': 'x', 'v': 'c', 'w': 'v', 'x': 'b', 'y': 'n', 'z': 'm'
}

new_alice_text = open("turkish_example.txt")
txt2 = new_alice_text.read()
new_alice_text.close()
new_encrypted_text = encrypt(txt2, CONSTANT_KEY_2)
new_decrypted_text = decrypt(new_encrypted_text, CONSTANT_KEY_2)

frequency_analysis_key2 = "oqnewftxkrdlcusgamzih"
change_key2 = "IAYCBNEURDMSVGLOKZTHP"
new_hack = tr(frequency_analysis_key2, change_key2, new_encrypted_text)
print(new_encrypted_text)
print(new_decrypted_text)
print(new_hack)
