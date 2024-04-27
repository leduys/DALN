import os
import C_P
# Initial permutation (IP)
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

# Initial permutation (IP) inverse
IP_INV = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

# Expansion permutation (E)
E = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

# S-boxes
S_BOXES = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
		[0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
		[4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
		[15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

		[[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
		[3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
		[0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
		[13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

		[[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
		[13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
		[13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
		[1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

		[[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
		[13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
		[10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
		[3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

		[[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
		[14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
		[4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
		[11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

		[[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
		[10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
		[9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
		[4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

		[[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
		[13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
		[1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
		[6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

		[[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
		[1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
		[7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
		[2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]
# Permutation (P)
P = [
    16, 7, 20, 21,
    29, 12, 28, 17,
    1, 15, 23, 26,
    5, 18, 31, 10,
    2, 8, 24, 14,
    32, 27, 3, 9,
    19, 13, 30, 6,
    22, 11, 4, 25
]

# Permutation choice 1 (PC1)
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

# Permutation choice 2 (PC2)
PC2 = [
    14, 17, 11, 24, 1, 5,
    3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8,
    16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
]

# Left circular shift for key generation
SHIFT_SCHEDULE = [
    1, 1, 2, 2, 2, 2, 2, 2,
    1, 2, 2, 2, 2, 2, 2, 1
]

# Initial permutation for plaintext (before IP)
def initial_permutation(plain_text):
    return permute(plain_text, IP, 64)

# Final permutation for ciphertext (after IP_INV)
def final_permutation(cipher_text):
    return permute(cipher_text, IP_INV, 64)

# Permute the input according to the specified permutation table
def permute(input_block, table, block_size):
    output_block = [0] * block_size
    for i, bit_position in enumerate(table):
        output_block[i] = input_block[bit_position - 1]
    return output_block

# Expansion function (E) for the right half
def expansion(right_half):
    return permute(right_half, E, 48)

# XOR operation for two bit strings of the same length
def xor(left, right):
    return [l ^ r for l, r in zip(left, right)]

# S-box substitution
def s_box_substitution(expanded_half):
    output = []
    for i in range(8):
        s_box_input = expanded_half[i * 6:(i + 1) * 6]
        row = int(f"{s_box_input[0]}{s_box_input[5]}", 2)
        col = int("".join(map(str, s_box_input[1:5])), 2)
        s_box_output = S_BOXES[i][row][col]
        output.extend([int(b) for b in format(s_box_output, '04b')])
    return output

# P permutation (permutation after S-box substitution)
def p_permutation(s_box_output):
    return permute(s_box_output, P, 32)

# Perform the Feistel function for one round
def feistel_function(right_half, round_key):
    expanded_half = expansion(right_half)
    xor_result = xor(expanded_half, round_key)
    s_box_result = s_box_substitution(xor_result)
    p_result = p_permutation(s_box_result)
    return p_result

# Generate subkeys for all rounds
def generate_subkeys(key):
    key = permute(key, PC1, 64)
    subkeys = []
    left_half = key[:28]
    right_half = key[28:]
    for shift_bits in SHIFT_SCHEDULE:
        left_half = left_circular_shift(left_half, shift_bits)
        right_half = left_circular_shift(right_half, shift_bits)
        round_key = permute(left_half + right_half, PC2, 56)
        subkeys.append(round_key)
    return subkeys

# Perform a left circular shift on a bit string
def left_circular_shift(bits, shift_bits):
    return bits[shift_bits:] + bits[:shift_bits]

# Encrypt a 64-bit plaintext using DES
def des_encrypt(plain_text_string, key_string):
    # Initial permutation
    plain_text_hex = string_to_hex(plain_text_string)
    plain_text = hex_to_binary(plain_text_hex)
    plain_text = initial_permutation(plain_text)
    key_hex=string_to_hex(key_string)
    key=hex_to_binary(key_hex)
    # Generate subkeys
    subkeys = generate_subkeys(key)
    
    # Split the plaintext into left and right halves
    left_half = plain_text[:32]
    right_half = plain_text[32:]
    
    # Perform 16 rounds of Feistel network
    for i in range(16):
        next_left_half = right_half
        feistel_output = feistel_function(right_half, subkeys[i])
        right_half = xor(left_half, feistel_output)
        left_half = next_left_half
    
    # Swap left and right halves
    left_half, right_half = right_half, left_half
    
    # Combine left and right halves
    cipher_text = left_half + right_half
    
    # Final permutation
    cipher_text = final_permutation(cipher_text)
    
    return hex(int((''.join(str(i) for i in cipher_text)),2))[2:]

# Helper function to convert a hexadecimal string to a binary string
def hex_to_binary(hex_string):
    binary_string = bin(int(hex_string, 16))[2:].zfill(64)
    return [int(bit) for bit in binary_string]

# Helper function to convert a list of integers to a hexadecimal string
def binary_to_hex(binary_list):
    binary_string = ''.join(map(str, binary_list))
    return hex(int(binary_string, 2))[2:].zfill(16)



# Decryption function for DES
def des_decrypt(cipher_text_hex, key_string):
    # Initial permutation
    cipher_text = hex_to_binary(cipher_text_hex)
    cipher_text = initial_permutation(cipher_text)
    key_hex=string_to_hex(key_string)
    key=hex_to_binary(key_hex)
    # Generate subkeys in reverse order
    subkeys = generate_subkeys(key)[::-1]
    
    # Split the ciphertext into left and right halves
    left_half = cipher_text[:32]
    right_half = cipher_text[32:]
    
    # Perform 16 rounds of Feistel network in reverse
    x=""
    for i in range(16):
        next_left_half = right_half
        feistel_output = feistel_function(right_half, subkeys[i])
        right_half = xor(left_half, feistel_output)
        
            
        left_half = next_left_half

    
    # Swap left and right halves
    left_half, right_half = right_half, left_half
    
    # Combine left and right halves
    plain_text = left_half + right_half
    
    # Final permutation
    plain_text = final_permutation(plain_text)
    pt=''.join(str(i) for i in plain_text)
    pt_hex=hex(int(pt,2))[2:]
    return hex_to_string(pt_hex)

def string_to_hex(input_string):
    # Convert the string to its hexadecimal representation
    return input_string.encode("utf-8").hex()
def hex_to_string(inpt):
    try:
        return bytes.fromhex(inpt).decode("utf-8")
    except:
        pass
key_main = C_P.key()
def encrypt(filename):
    C_P.encrypt_file(filename,key_main)
    hidden_directory =  ".hidden"
    # Ghi chuỗi vào file
    filename = os.path.join(hidden_directory, "key2.bin")
    with open(filename, 'wb') as file:
        file.write(key_main)
def decrypt(filename):
    C_P.decrypt_file(filename,key_main)