message = raw_input("Message To Encrypt: ")
message = int(message.encode('hex'),16)
print hex(message)[2:].decode('hex')
