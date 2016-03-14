import urllib2
import hashlib
import itertools

opener = urllib2.build_opener()
opener.addheaders.append(('Cookie', 'PHPSESSID=rmh6mq2qu5ej09id02ojorove6'))
f = opener.open("https://ringzer0team.com/challenges/57")
GOTHASH=False
GOTSALT=False
HASH=""
SALT=""


def bruteforce(charset, maxlength):
    return (''.join(candidate)
        for candidate in itertools.chain.from_iterable(itertools.product(charset, repeat=i)
        for i in range(1, maxlength + 1)))

for line in f.readlines():
    if GOTHASH:
        HASH = line[2:-8]
        print "HASH: -{}-".format(line[2:-8])
        GOTHASH=False
    if GOTSALT:
        SALT = line[2:-8]
        print "SALT: -{}-".format(line[2:-8])
        GOTSALT=False
    if 'BEGIN HASH' in line:
        GOTHASH=True
    if 'BEGIN SALT' in line:
        GOTSALT=True

#abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
for i in bruteforce('0123456789', 4):
    print i
    hash_object = hashlib.sha256(SALT + str(i))
    print hash_object.hexdigest()
    if hash_object.hexdigest() == HASH:
        print "Done"
        result = opener.open("https://ringzer0team.com/challenges/57/" + hash_object.hexdigest())
        print result.read()
        break
