import urllib2
import hashlib

opener = urllib2.build_opener()
opener.addheaders.append(('Cookie', 'PHPSESSID=j5d2rk5e9sb1crn5dqkv1fia21'))
f = opener.open("https://ringzer0team.com/challenges/119")
MESSAGE=""
CONTENT=False
REPLY=""

Char0 = "&nbsp;xxx&nbsp;<br />x&nbsp;&nbsp;&nbsp;x<br />x&nbsp;&nbsp;&nbsp;x<br />x&nbsp;&nbsp;&nbsp;x<br />&nbsp;xxx&nbsp;"
Char1 = "&nbsp;xx&nbsp;&nbsp;<br />x&nbsp;x&nbsp;&nbsp;<br />&nbsp;&nbsp;x&nbsp;&nbsp;<br />&nbsp;&nbsp;x&nbsp;&nbsp;<br />xxxxx"
Char2 = "&nbsp;xxx&nbsp;<br />x&nbsp;&nbsp;&nbsp;x&nbsp;<br />&nbsp;&nbsp;xx&nbsp;<br />&nbsp;x&nbsp;&nbsp;&nbsp;<br />xxxxx"
Char3 = "&nbsp;xxx&nbsp;<br />x&nbsp;&nbsp;&nbsp;x<br />&nbsp;&nbsp;xx&nbsp;<br />x&nbsp;&nbsp;&nbsp;x<br />&nbsp;xxx&nbsp;"
Char4 = "&nbsp;x&nbsp;&nbsp;&nbsp;x<br />x&nbsp;&nbsp;&nbsp;&nbsp;x<br />&nbsp;xxxxx<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x<br />&nbsp;&nbsp;&nbsp;&nbsp;x"
Char5 = "xxxxx<br />x&nbsp;&nbsp;&nbsp;&nbsp;<br />&nbsp;xxxx<br />&nbsp;&nbsp;&nbsp;&nbsp;x<br />xxxxx"


for line in f.readlines():
    if 'END' in line:
        CONTENT = False
    if CONTENT:
        MESSAGE+=line
    if 'BEGIN' in line:
        CONTENT = True


split_MESSAGE = MESSAGE.split("<br /><br />")

for num in split_MESSAGE:
    if Char0 in num:
        REPLY += "0"
        print "NUMBER: {} --END NUM--".format(num)
    if Char1 in num:
        REPLY += "1"
        print "NUMBER: {} --END NUM--".format(num)
    if Char2 in num:
        REPLY += "2"
        print "NUMBER: {} --END NUM--".format(num)
    if Char3 in num:
        REPLY += "3"
        print "NUMBER: {} --END NUM--".format(num)
    if Char4 in num:
        REPLY += "4"
        print "NUMBER: {} --END NUM--".format(num)
    if Char5 in num:
        REPLY += "5"
        print "NUMBER: {} --END NUM--".format(num)



print REPLY

f = opener.open("https://ringzer0team.com/challenges/119/"+REPLY)
print f.read()
