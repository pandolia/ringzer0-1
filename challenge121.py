import hashlib
import itertools
import requests
import subprocess

cookie = {'PHPSESSID':'6vtuto56shu0duifsongv7cia5'}
page   = requests.get('https://ringzer0team.com/challenges/121', cookies=cookie)

start = False
input = []

for line in page.iter_lines():
    if start:
        break
    if 'BEGIN' in line:
        start = True

shellcode=line.strip()
print "got shellcode :",shellcode

#res = subprocess.check_output('python run_shell.py "'+str(shellcode)+'"', stderr=subprocess.STDOUT)

proc = subprocess.Popen('python run_shell.py "'+str(shellcode)+'" 0>&1' ,stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
res = proc.communicate()[0]
print 'code output :',res

page = requests.get('https://ringzer0team.com/challenges/121/' + res , cookies=cookie)

for line in page.iter_lines():
    if 'FLAG-' in line:
        print line.replace('<',' ').replace('>',' ').split(' ')[4]
