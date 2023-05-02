def xor(a, b):
  return bytes([x^y for x,y in zip(a,b)])

plaintext = "questo è un messaggio segreto"

# key is shared in advance, never repeats
key       = "ibkmsvagxlnwggrjoxtlkpdiqtejoodjssxlvhydkjymhhxvrgkljzwrisl"

plaintext_bytes = plaintext.encode()
key_bytes = key.encode()

ciphertext_bytes = xor(plaintext_bytes, key_bytes)


print("plaintext (bytes) is " + str(plaintext_bytes))
print("key (bytes) is " + str(key_bytes))
print("ciphertext (bytes) is " + str(ciphertext_bytes) + " (unprintable)")


key_recovered_bytes = xor(plaintext_bytes, ciphertext_bytes)

print('Hacking key is %s (but I do not know the rest...)' % key_recovered_bytes)
