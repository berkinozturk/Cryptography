from PIL import Image  # Import it
import numpy as np  # Import it

# Constants for DES
IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

FP = [40, 8, 48, 16, 56, 24, 64, 32,
      39, 7, 47, 15, 55, 23, 63, 31,
      38, 6, 46, 14, 54, 22, 62, 30,
      37, 5, 45, 13, 53, 21, 61, 29,
      36, 4, 44, 12, 52, 20, 60, 28,
      35, 3, 43, 11, 51, 19, 59, 27,
      34, 2, 42, 10, 50, 18, 58, 26,
      33, 1, 41, 9, 49, 17, 57, 25]

E = [32, 1, 2, 3, 4, 5, 4, 5,
     6, 7, 8, 9, 8, 9, 10, 11,
     12, 13, 12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21, 20, 21,
     22, 23, 24, 25, 24, 25, 26, 27,
     28, 29, 28, 29, 30, 31, 32, 1]

P = [16, 7, 20, 21,
     29, 12, 28, 17,
     1, 15, 23, 26,
     5, 18, 31, 10,
     2, 8, 24, 14,
     32, 27, 3, 9,
     19, 13, 30, 6,
     22, 11, 4, 25]

S_boxes = [
    # S1
    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
    # S2
    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
     [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
     [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
     [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],
    # S3
    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
     [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
     [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
     [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],
    # S4
    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
     [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
     [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
     [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],
    # S5
    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
     [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
     [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
     [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],
    # S6
    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
     [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
     [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
     [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],
    # S7
    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
     [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
     [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
     [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
    # S8
    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
     [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
]


def permute(block, table):
    return [block[i - 1] for i in table]


def xor(t1, t2):
    return [i ^ j for i, j in zip(t1, t2)]


# Function to implement the S-box substitution
def substitute(expanded_half_block):
    subblocks = [expanded_half_block[i:i + 6] for i in range(0, len(expanded_half_block), 6)]
    result = []
    for i in range(8):
        row = (subblocks[i][0] << 1) + subblocks[i][5]
        col = (subblocks[i][1] << 3) + (subblocks[i][2] << 2) + (subblocks[i][3] << 1) + subblocks[i][4]
        val = S_boxes[i][row][col]
        bin_val = [int(x) for x in format(val, '04b')]
        result += bin_val
    return result


# The round function
def des_round(left, right, round_key):
    expanded_right = permute(right, E)
    temp = xor(expanded_right, round_key)
    substituted = substitute(temp)
    permuted = permute(substituted, P)
    new_right = xor(left, permuted)
    return right, new_right


def generate_round_keys(key):
    return [key] * 16  # Simplified, normally keys would be different for each round



def des_encrypt(block, key):
    block = permute(block, IP)
    left, right = block[:32], block[32:]
    round_keys = generate_round_keys(key)
    for round_key in round_keys:
        left, right = des_round(left, right, round_key)
    combined = right + left
    ciphertext = permute(combined, FP)
    return ciphertext


def des_decrypt(block, key):
    block = permute(block, IP)
    left, right = block[:32], block[32:]
    round_keys = generate_round_keys(key)[::-1]  # Reverse the round keys for decryption
    for round_key in round_keys:
        left, right = des_round(left, right, round_key)
    combined = right + left
    plaintext = permute(combined, FP)
    return plaintext



def bytes_to_bits(byte_array):
    bits = []
    for byte in byte_array:
        bits.extend([int(bit) for bit in format(byte, '08b')])
    return bits


def bits_to_bytes(bit_array):
    byte_array = []
    for i in range(0, len(bit_array), 8):
        byte = bit_array[i:i + 8]
        byte_array.append(int(''.join(map(str, byte)), 2))
    return byte_array


# Step 1: Load the bitmap images
def load_image(image_path):
    image = Image.open("sample.bmp")
    if image.mode != 'RGB':
        image = image.convert('RGB')
    return image


def load_encrypted_image(image_path):
    image = Image.open("encrypted_image.bmp")
    if image.mode != 'RGB':
        image = image.convert('RGB')
    return image


def load_decrypted_image(image_path):
    image = Image.open("decrypted_image.bmp")
    if image.mode != 'RGB':
        image = image.convert('RGB')
    return image


# Step 2: Convert the image to a byte array
def image_to_byte_array(image):
    image_bytes = np.array(image).flatten().tolist()
    return image_bytes


# Step 3: Encrypt the byte array using DES
def encrypt_image(byte_array, key):
    padded_size = len(byte_array) + (8 - len(byte_array) % 8) if len(byte_array) % 8 != 0 else len(byte_array)
    byte_array += [0] * (padded_size - len(byte_array))  # Padding
    encrypted_bytes = []
    for i in range(0, len(byte_array), 8):
        block = byte_array[i:i + 8]
        block_bits = bytes_to_bits(block)
        key_bits = bytes_to_bits(key)
        encrypted_bits = des_encrypt(block_bits, key_bits)
        encrypted_block = bits_to_bytes(encrypted_bits)
        encrypted_bytes.extend(encrypted_block)
    return encrypted_bytes, padded_size


# Step 4: Save the encrypted byte array as an image
def save_encrypted_image(encrypted_bytes, image_size, output_path):
    encrypted_image_array = np.array(encrypted_bytes[:image_size[0] * image_size[1] * 3], dtype=np.uint8).reshape(
        image_size[1], image_size[0], 3)
    encrypted_image = Image.fromarray(encrypted_image_array)
    encrypted_image.save(output_path)


# Step 5: Decrypt the encrypted image
def decrypt_image(encrypted_bytes, key, original_size):
    decrypted_bytes = []
    for i in range(0, len(encrypted_bytes), 8):
        block = encrypted_bytes[i:i + 8]
        block_bits = bytes_to_bits(block)
        key_bits = bytes_to_bits(key)
        decrypted_bits = des_decrypt(block_bits, key_bits)
        decrypted_block = bits_to_bytes(decrypted_bits)
        decrypted_bytes.extend(decrypted_block)
    return decrypted_bytes[:original_size]


# Load original image
original_image_path = 'samplebmp'
original_image = load_image(original_image_path)
print(f"Original Image Size: {original_image.size}")
original_image.show()

# Convert image to byte array
image_bytes = image_to_byte_array(original_image)
print(f"Original Image Bytes Length: {len(image_bytes)}")

# Key for DES (must be 8 bytes long)
key_hex = "133457799BBCDFF1"
key = bytes.fromhex(key_hex)

# Encrypt the byte array
encrypted_bytes, padded_size = encrypt_image(image_bytes, key)
print(f"Encrypted Bytes Length: {len(encrypted_bytes)}")

# Save encrypted image
encrypted_image_path = 'encrypted_image.bmp'
save_encrypted_image(encrypted_bytes, original_image.size, encrypted_image_path)

# Load and show encrypted image
encrypted_image = load_encrypted_image(encrypted_image_path)
print(f"Encrypted Image Size: {encrypted_image.size}")
encrypted_image.show()

# Decrypt the byte array
decrypted_bytes = decrypt_image(encrypted_bytes, key, len(image_bytes))
print(f"Decrypted Bytes Length: {len(decrypted_bytes)}")

# Convert decrypted byte array to image and save
decrypted_image_array = np.array(decrypted_bytes, dtype=np.uint8).reshape(original_image.size[1],
                                                                          original_image.size[0], 3)
decrypted_image = Image.fromarray(decrypted_image_array)
decrypted_image_path = 'decrypted_image.bmp'
decrypted_image.save(decrypted_image_path)

# Load and show decrypted image
decrypted_image = load_decrypted_image(decrypted_image_path)
print(f"Decrypted Image Size: {decrypted_image.size}")
decrypted_image.show()
