import urllib2
import hashlib

opener = urllib2.build_opener()
opener.addheaders.append(('Cookie', 'PHPSESSID=8ic0a8ih38tqblg4ttrdvmliv2'))
f = opener.open("https://ringzer0team.com/challenges/56")
GOTIT=False

for line in f.readlines():
    if GOTIT:
        TOHASH = line[2:-8]
        print line[2:-8]
        GOTIT=False
    if 'BEGIN' in line:
        GOTIT=True

for i in range(9999):
    hash_object = hashlib.sha1(str(i))
    if hash_object.hexdigest() == TOHASH:
        print i
        result = opener.open("https://ringzer0team.com/challenges/56/" + str(i))
        print result.read()
