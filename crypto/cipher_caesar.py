def encrypt_text(plaintext, k):

  ciphertext = ""

  for i in range(len(plaintext)):

    c = plaintext[i]

    if c == " ":
      ciphertext += " "

    elif c.islower():
      x = ord(c) - 97                  # from lowercase ASCII char to 0..25
      enc = (x + k) % 26
      ciphertext += chr( enc + 97 )    # from 0..25 to lowercase ASCII char

  return ciphertext


def decrypt_text(ciphertext, k):

  plaintext = ""

  for i in range(len(ciphertext)):

    p = ciphertext[i]

    if p == " ":
      plaintext += " "

    elif p.islower():
      x = ord(p) - 97                  # from lowercase ASCII char to 0..25
      enc = (x - k) % 26
      plaintext += chr( enc + 97 )    # from 0..25 to lowercase ASCII char

  return plaintext





print("Cipher Text: " + encrypt_text("hello world", 3))




message = "udz wklv vlgh"

for key in range(0,26):
  translated = decrypt_text(message, key)
  print('Hacking key is %s: %s' % (key, translated))
