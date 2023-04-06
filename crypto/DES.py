from Crypto.Cipher import DES

key_hex = '0011223344556677'    # 8 bytes, 1 is discarded...
key = bytes.fromhex(key_hex)

plaintext = 'Hello World.....'  # 16 bytes

cipher = DES.new(key, DES.MODE_ECB)
ciphertext = cipher.encrypt(plaintext.encode())
print(ciphertext.hex())

newplaintext = cipher.decrypt(ciphertext)
print(newplaintext.decode())
