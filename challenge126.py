import hashlib
import itertools
import requests
import subprocess

cookie = {'PHPSESSID':'74g5nfvnri4pav0d2c7s1vlq97'}

def anagram(w):
    result = []
    word_letters = sorted(list(w))
    for word in dico:
        if sorted(word) == word_letters:
            return word


print 'loading en_gb_clean.txt'
dico=set(map(str.rstrip, open('en_gb_clean.txt')))
print 'loaded'
print

start = False
input = []

page   = requests.get('https://ringzer0team.com/challenges/126', cookies=cookie)

for line in page.iter_lines():
    if start:
        break
    if 'BEGIN' in line:
        start = True

words=line.strip().replace('<',' ').split()[0].split(',')

result=[]

for word in words:
    if word in dico:
        print 'found',word
        result.append(word)
    else:
        gram=anagram(word)
        if gram:
                print 'anagram found for',word,'=>',gram
                result.append(gram)
        else:
                print 'no anagram, try anyway =>',word
                result.append(word)

res=','.join(result)
page = requests.get('https://ringzer0team.com/challenges/126/' + res , cookies=cookie)

for line in page.iter_lines():
    if 'FLAG-' in line:
        print line.replace('<',' ').replace('>',' ').split(' ')[4]
