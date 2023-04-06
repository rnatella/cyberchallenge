from Crypto.Util import number

p = number.getPrime(2048)
q = number.getPrime(2048)

n = p * q

e = 65537 # used by default

phi = (p - 1) * (q - 1)

if not number.GCD(e, phi) == 1:
    raise Exception("e and phi(n) are not relatively prime,"
                    "try again.")

d = number.inverse(e, phi)

M=123

C = pow(M, e, n)        # C = M^e mod n

print("Ciphertext: %d" % C)

M_new = pow(C, d, n)    # M = C^d mod n

print("Plaintext: %d" % M_new)