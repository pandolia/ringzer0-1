#key = "fselkladfklklakl"
#message = "KDERE2UNX1W1H96GYQNUSQT1KPGBKDERE2UNX1W1H96GYQNUSQT1KPGB"

#!/usr/bin/env python2

def genkey(length):
    return "01100110011100110110010101101100011010110110110001100001011001000110011001101011011011000110101101101100011000010110101101101100"

def xor_strings(s,t):
    """xor two strings together"""
    return "".join(chr(ord(a)^ord(b)) for a,b in zip(s,t))


message = 'KDERE2UNX1W1H96GYQNUSQT1KPGB'
print 'message:', message

key = genkey(len(message))
print 'key:', key

cipherText = xor_strings(message, key)
print 'cipherText:', cipherText
print 'decrypted:', xor_strings(cipherText, key)

# verify
if xor_strings(cipherText, key) == message:
    print 'Unit test passed'
else:
    print 'Unit test failed'
