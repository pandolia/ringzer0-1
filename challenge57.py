import urllib2
import hashlib
import itertools

opener = urllib2.build_opener()
opener.addheaders.append(('Cookie', 'PHPSESSID=8ic0a8ih38tqblg4ttrdvmliv2'))
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


for i in bruteforce('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', 6):
    hash_object = hashlib.sha256(SALT + str(i))
    if hash_object.hexdigest() == HASH:
        print i
        result = opener.open("https://ringzer0team.com/challenges/57/" + str(i))
        print result.read()
