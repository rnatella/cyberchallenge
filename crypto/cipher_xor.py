def xor(a, b):
  return bytes([x^y for x,y in zip(a,b)])

plaintext = "ciao"

key = "p" * len(plaintext)

plaintext_bytes = plaintext.encode()
key_bytes = key.encode()

ciphertext_bytes = xor(plaintext_bytes, key_bytes)

print("plaintext (bytes) is " + str(plaintext_bytes))
print("key (bytes) is " + str(key_bytes))
print("ciphertext (bytes) is " + str(ciphertext_bytes) + " (unprintable)")

newplaintext_bytes = xor(ciphertext_bytes, key_bytes)

newplaintext = newplaintext_bytes.decode()

print("decrypted cyphertext is '%s'" % newplaintext)

"""
key_recovered_bytes = xor(plaintext_bytes, ciphertext_bytes)

print('Hacking key is %s' % key)
"""