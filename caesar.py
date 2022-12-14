
def encrypt(key,plaintext):
    ciphertext=""
    #YOUR CODE HERE
    key = key % 26
    for x in plaintext:
        code = ord(x)
        newCode = code + key
        if newCode > 90:
            newCode = 64 + newCode%90 #64 as 91 mod 90 is 1 and this would give us A (65)
        if newCode < 65:
            newCode = 91 - (65-newCode)
        ciphertext += chr(newCode)

    return ciphertext

def decrypt(key,ciphertext):
    plaintext=""
    #YOUR CODE HERE
    key = key % 26
    for x in ciphertext:
        code = ord(x)
        newCode = code - key
        if newCode < 65:
            newCode = 91 - (65-newCode)
        if newCode > 90:
            newCode = 64 + newCode%90 #64 as 91 mod 90 is 1 and this would give us A (65)
        plaintext += chr(newCode)

    return plaintext

