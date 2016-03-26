import base64
import urllib2
import re

"""
Assuming the key is in the xor string, and that it's sequential, and modulo is not needed.

The assuming that the only things we need to send bask are alphanumeric.

Just try them and send back the ones that match [a-zA-Z0-9.]
"""

KEYFLAG=False
CIPHERFLAG=False

def special_match(strg, search=re.compile(r'[^a-zA-Z0-9.]').search):
    return not bool(search(strg))

opener = urllib2.build_opener()
opener.addheaders.append(('Cookie', 'PHPSESSID=u9qs3oeocppo3he3i80umhpg77'))
f = opener.open("https://ringzer0team.com/challenges/16")

for line in f.readlines():
    if KEYFLAG:
        #print line[2:-8]
        completekey = line[2:-8]
        KEYFLAG=False
    if 'BEGIN XOR' in line:
        print "got keys"
        KEYFLAG=True
    if CIPHERFLAG:
        base64cipher = line[2:-8]
        #print line[2:-8]
        CIPHERFLAG=False
    if 'BEGIN CRYPTED' in line:
        CIPHERFLAG=True

cipher=base64.b64decode(base64cipher)

for number in range(len(completekey)-10):
    print number
    result = ""
    key = completekey[number:number+10]
    for num in range(len(cipher)):
        result += chr(ord(cipher[num]) ^ ord(key[num%len(key)]))

    if special_match(result):
        try:
            reqresult = opener.open("https://ringzer0team.com/challenges/16/"+str(result))
            for line in reqresult.readlines():
                if "FLAG" in line:
                    print line
        except Exception as e:
            print "bad one"
