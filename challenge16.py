import base64

KEY = "LXPr5nhghMusNUn3CbdXK0RfVVZL9k3N4hGwiKjl"
HASH = "PCV2OgoAAQkFESI4NBA/WDMlMygkI3weNkl0VF0wHTo="

def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
        return "".join(["%s" % (ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join(["%s" % (ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

def decode(string):
    return base64.b64decode(string)

if __name__ == '__main__':
    print decode(strxor(KEY,HASH))
