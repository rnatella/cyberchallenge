from Crypto.Cipher import AES
from Crypto.Util import Padding

key_hex = '00112233445566778899AABBCCDDEEFF'    # 16 bytes (128 bits)
key_bytes = bytes.fromhex(key_hex)

plaintext = 'This message is not a multiple of 16 bytes'
plaintext_bytes = Padding.pad(plaintext.encode(), 16)

cipher = AES.new(key_bytes, AES.MODE_ECB)

ciphertext_bytes = cipher.encrypt(plaintext_bytes)

newplaintext_bytes = cipher.decrypt(ciphertext_bytes)

print(ciphertext_bytes.hex())
print(newplaintext_bytes.decode())
