import string, random


def create_translation_tables(key):
    N = len(key)
    s = string.ascii_lowercase
    trantab_enc = [None] * N
    trantab_dec = [None] * N

    for i, k in enumerate(key):
        mapping = list(s)
        random.Random(k).shuffle(mapping)  # Use key character to seed the shuffling
        trantab_enc[i] = ''.maketrans(s, ''.join(mapping))
        trantab_dec[i] = ''.maketrans(''.join(mapping), s)

    return trantab_enc, trantab_dec


def encrypt(text, trantab_enc, key):
    ciphertext = [None] * len(text)
    N = len(key)
    for i in range(len(text)):
        if text[i] in string.ascii_lowercase:  # Only translate lowercase letters
            ciphertext[i] = text[i].translate(trantab_enc[i % N])
        else:
            ciphertext[i] = text[i]
    return "".join(ciphertext)


def decrypt(text, trantab_dec, key):
    newtext = [None] * len(text)
    N = len(key)
    for i in range(len(text)):
        if text[i] in string.ascii_lowercase:  # Only translate lowercase letters
            newtext[i] = text[i].translate(trantab_dec[i % N])
        else:
            newtext[i] = text[i]
    return "".join(newtext)


# User-provided key
key = "b"

# Create translation tables
trantab_enc, trantab_dec = create_translation_tables(key)

# Read the text from file
with open("example.txt", "r") as myfile:
    txt = myfile.read()
print("Original text:", txt)

# Encrypt the text
enctext = encrypt(txt, trantab_enc, key)
print("Encrypted text:", enctext)

# Decrypt the text
dectext = decrypt(enctext, trantab_dec, key)
print("Decrypted text:", dectext)

# Another language
text = "merhaba dünya"
enctext2 = encrypt(text, trantab_enc, key)
print(enctext2)

dectext2 = decrypt(enctext2, trantab_dec, key)
print(dectext2)

# Brute force to find the key and decrypt
for key in string.ascii_lowercase:
    trantab_enc, trantab_dec = create_translation_tables(key)
    decrypted_text = decrypt(enctext, trantab_dec, key)
    print(f"Trying key '{key}': {decrypted_text}")


