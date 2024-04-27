from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

def pad(text):
    # Chèn bytes padding để đảm bảo độ dài của văn bản là bội số của kích thước khối
    block_size = DES.block_size
    return text + (block_size - len(text) % block_size) * chr(block_size - len(text) % block_size).encode()

def encrypt_des(key, plaintext):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plaintext)
    ciphertext = cipher.encrypt(padded_text)
    return ciphertext

def encrypt_file(input_file, key):
    with open(input_file, 'rb') as file:
        plaintext = file.read()
    
    ciphertext = encrypt_des(key, plaintext)

    with open(input_file, 'wb') as file:
        file.write(ciphertext)
def unpad(text):
    # Loại bỏ bytes padding khi giải mã
    return text[:-text[-1]]

def decrypt_des(key, ciphertext):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_text = cipher.decrypt(ciphertext)
    return unpad(decrypted_text)

def decrypt_file(input_file, key):
    with open(input_file, 'rb') as file:
        ciphertext = file.read()

    decrypted_text = decrypt_des(key, ciphertext)

    with open(input_file, 'wb') as file:
        file.write(decrypted_text)

def key():
    return b'\x8f\xa2\x1e\xe7\xf0\x90\x0b\xcd'