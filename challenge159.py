import urllib2
import hashlib
import itertools

opener = urllib2.build_opener()
opener.addheaders.append(('Cookie', 'PHPSESSID=rmh6mq2qu5ej09id02ojorove6'))
f = opener.open("https://ringzer0team.com/challenges/159")
TOHASH = ""
GOTIT = False

def bruteforce(charset, maxlength):
    return (''.join(candidate)
        for candidate in itertools.chain.from_iterable(itertools.product(charset, repeat=i)
        for i in range(1, maxlength + 1)))

for line in f.readlines():
    if GOTIT:
        TOHASH=line[2:-8]
        GOTIT = False
    if 'BEGIN' in line:
        GOTIT=True

TOHASH = "57fb0f689e4749dec1d3f40462a5ca21f9039e93"

#abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

for i in bruteforce('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 6):
    hash_object = hashlib.sha1(str(i))
    #print "{} - {}".format(alg,i)
    #print hash_object.hexdigest()
    if hash_object.hexdigest() == TOHASH:
        print "{} - ".format(i)
        print "Done"
        break
        #result = opener.open("https://ringzer0team.com/challenges/159/" + str(i))
        #print result.read()
