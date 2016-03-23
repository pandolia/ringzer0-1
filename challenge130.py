import paramiko

if __name__ == '__main__':
    buff = ""
    minguess = 0
    maxguess = 10000
    currentguess = 5000

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("ringzer0team.com", username="number", password="Z7IwIMRC2dc764L", port=12643)
    ssh_term = ssh.invoke_shell()

    buff = ''
    while not buff.endswith('number>'):
        resp = ssh_term.recv(9999)
        buff += resp
    print buff

    while True:
        ssh_term.send(str(currentguess) + '\r\n')
        print "currentguess: {}".format(currentguess)
        buff = ''
        while not buff.endswith('number>'):
            resp = ssh_term.recv(9999)
            buff += resp
            if "big" in resp:
                print "big"
                maxguess = currentguess
                currentguess = currentguess - ((maxguess - minguess) / 2)
            if "small" in resp:
                print "small"
                minguess = currentguess
                currentguess = currentguess + ((maxguess - minguess) / 2)
            if "right" in resp:
                minguess = 0
                maxguess = 10000
                currentguess = 5000
            if "You beat the machine" in resp:
                break
            print buff
        if "FLAG" in resp:
            print buff
            break
