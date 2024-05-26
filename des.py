# Initial Permutation Table
IP = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

# Final Permutation Table
FP = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

# Expansion Table
E = [
    32, 1, 2, 3, 4, 5, 4, 5,
    6, 7, 8, 9, 8, 9, 10, 11,
    12, 13, 12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21, 20, 21,
    22, 23, 24, 25, 24, 25, 26, 27,
    28, 29, 28, 29, 30, 31, 32, 1
]

# S-Boxes
S_BOXES = [
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
    ],
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
    ],
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
    ],
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
    ],
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
    ],
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
    ],
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
    ],
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
    ],
]

# Permutation Table
P = [
    16, 7, 20, 21, 29, 12, 28, 17,
    1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9,
    19, 13, 30, 6, 22, 11, 4, 25
]

# Permuted Choice 1 Table
PC1 = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
]

# Permuted Choice 2 Table
PC2 = [
    14, 17, 11, 24, 1, 5, 3, 28,
    15, 6, 21, 10, 23, 19, 12, 4,
    26, 8, 16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55, 30, 40,
    51, 45, 33, 48, 44, 49, 39, 56,
    34, 53, 46, 42, 50, 36, 29, 32
]

# Left Shifts per Round
SHIFTS = [
    1, 1, 2, 2, 2, 2, 2, 2,
    1, 2, 2, 2, 2, 2, 2, 1
]


def permute(block, table):
    return [block[x - 1] for x in table]


def split_bits(bits, n):
    return bits[:n], bits[n:]


def left_shift(bits, n):
    return bits[n:] + bits[:n]


def xor(bits1, bits2):
    return [b1 ^ b2 for b1, b2 in zip(bits1, bits2)]


def sbox_substitution(block):
    output = []
    for i in range(8):
        chunk = block[i * 6:(i + 1) * 6]
        row = int(f"{chunk[0]}{chunk[5]}", 2)
        col = int(''.join(map(str, chunk[1:5])), 2)
        sbox_val = S_BOXES[i][row][col]
        output.extend([int(x) for x in f"{sbox_val:04b}"])
    return output


def initial_permutation(block):
    return permute(block, IP)


def final_permutation(block):
    return permute(block, FP)


def expand(block):
    return permute(block, E)


def key_schedule(key):
    key = permute(key, PC1)
    left, right = split_bits(key, 28)
    keys = []
    for shift in SHIFTS:
        left = left_shift(left, shift)
        right = left_shift(right, shift)
        combined = left + right
        round_key = permute(combined, PC2)
        keys.append(round_key)
    return keys


def str_to_bit_array(text):
    array = []
    byte_array = text.encode('utf-8')  # Encode text to bytes
    for byte in byte_array:
        binval = binvalue(byte, 8)
        array.extend([int(x) for x in list(binval)])
    return array


def bit_array_to_hex(array):
    hex_str = ''.join([f"{int(''.join(map(str, array[i:i + 4])), 2):x}" for i in range(0, len(array), 4)])
    return hex_str


def hex_to_bit_array(hex_str):
    bit_array = []
    for char in hex_str:
        binval = binvalue(int(char, 16), 4)
        bit_array.extend([int(x) for x in binval])
    return bit_array


def binvalue(val, bitsize):
    binval = bin(val)[2:] if isinstance(val, int) else bin(ord(val))[2:]
    if len(binval) > bitsize:
        raise ValueError("binary value larger than the expected size")
    while len(binval) < bitsize:
        binval = "0" + binval
    return binval


def pad_text(text):
    pad_len = 8 - (len(text.encode('utf-8')) % 8)
    return text + chr(pad_len) * pad_len


def unpad_text(text):
    pad_len = ord(text[-1])
    return text[:-pad_len]


def des_round(left, right, round_key):
    expanded_right = expand(right)
    xored = xor(expanded_right, round_key)
    substituted = sbox_substitution(xored)
    permuted = permute(substituted, P)
    new_right = xor(left, permuted)
    return right, new_right


def des_encrypt_block(block, keys):
    block = initial_permutation(block)
    left, right = split_bits(block, 32)
    for round_key in keys:
        left, right = des_round(left, right, round_key)
    combined = right + left
    return final_permutation(combined)


def des_decrypt_block(block, keys):
    block = initial_permutation(block)
    left, right = split_bits(block, 32)
    for round_key in reversed(keys):
        left, right = des_round(left, right, round_key)
    combined = right + left
    return final_permutation(combined)


def bit_array_to_str(array):
    byte_array = bytearray()
    for i in range(0, len(array), 8):
        byte = int(''.join([str(x) for x in array[i:i + 8]]), 2)
        byte_array.append(byte)
    return byte_array.decode('utf-8', errors='ignore')  # Decode bytes to text, ignore errors


def encrypt(text, key):
    key = str_to_bit_array(key)
    keys = key_schedule(key)
    text = pad_text(text)
    blocks = [text[i:i + 8] for i in range(0, len(text), 8)]
    encrypted_blocks = []
    for block in blocks:
        block = str_to_bit_array(block)
        if len(block) != 64:
            block.extend([0] * (64 - len(block)))  # Pad the block to 64 bits if necessary
        encrypted_block = des_encrypt_block(block, keys)
        encrypted_blocks.extend(encrypted_block)
    return bit_array_to_hex(encrypted_blocks)


def decrypt(ciphertext, key):
    key = str_to_bit_array(key)
    keys = key_schedule(key)
    bit_array = hex_to_bit_array(ciphertext)
    blocks = [bit_array[i:i + 64] for i in range(0, len(bit_array), 64)]
    decrypted_blocks = []
    for block in blocks:
        decrypted_block = des_decrypt_block(block, keys)
        decrypted_blocks.extend(decrypted_block)
    decrypted_text = bit_array_to_str(decrypted_blocks)
    return unpad_text(decrypted_text)


# Usage
plaintext = "I remember as a child, and as a young budding naturalist, spending all my time observing and testing the world around me moving pieces, altering the flow of things, and documenting ways the world responded to me. Now, as an adult and a professional naturalist, I’ve approached language in the same way, not from an academic point of view but as a curious child still building little mud dams in creeks and chasing after frogs. So this book is an odd thing: it is a naturalist’s walk through the language-making landscape of the English language, and following in the naturalist’s tradition it combines observation, experimentation, speculation, and documentation activities we don’t normally associate with language. This book is about testing, experimenting, and playing with language. It is a handbook of tools and techniques for taking words apart and putting them back together again in ways that I hope are meaningful and legitimate (or even illegitimate). This book is about peeling back layers in search of the language-making energy of the human spirit. It is about the gaps in meaning that we urgently need to notice and name the places where our dreams and ideals are no longer fulfilled by a society that has become fast-paced and hyper-commercialized. Language is meant to be a playful, ever-shifting creation but we have been taught, and most of us continue to believe, that language must obediently follow precisely prescribed rules that govern clear sentence structures, specific word orders, correct spellings, and proper pronunciations. If you make a mistake or step out of bounds there are countless, self-appointed language experts who will promptly push you back into safe terrain and scold you for your errors. And in case you need reminding, there are hundreds of dictionaries and grammar books to ensure that you remember the 'right' way to use English."
key = "berkinso"  # 8-byte key
ciphertext = encrypt(plaintext, key)
print("Encrypted:", ciphertext)
decrypted_text = decrypt(ciphertext, key)
print("Decrypted:", decrypted_text)


