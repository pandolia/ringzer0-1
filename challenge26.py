import base64

code = "RU9CRC43aWdxNDsxaWtiNTFpYk9PMDs6NDFS"
secret_data = base64.b64decode(code)
print secret_data
# That looks kinda like a flag....
# OK I'm going mad,I've tried everything
# wait, ord('E') ^ ord('F') = 3...

key = 3

for i in secret_data:
    print chr(int(ord(i)) ^ key)

# FLAG-4jdr782jha62jaLL38972Q
