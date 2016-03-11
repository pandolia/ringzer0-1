import hashlib
import itertools

chars = ['0','1','2','3','4','5','6','7','8','9','-','_',',',':','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

for pass_length in range (15):
    gen = itertools.combinations_with_replacement(chars,pass_length)
    for password in gen:
        print password
        hash_object = hashlib.sha1(password)
        print hash_object.hexdigest()

"""
mystring = input('Enter String to hash: ')
# Assumes the default UTF-8
hash_object = hashlib.md5(mystring.encode())
print(hash_object.hexdigest())


b89356ff6151527e89c4f3e3d30c8e6586c63962
"""
