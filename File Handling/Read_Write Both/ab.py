# Open the file in ab mode and write initial binary data
with open('example_ab.bin', 'ab') as file:
    file.write(b'\x00\x01\x02\x03\x04\x05')

# Open the file in ab mode and append additional binary data
with open('example_ab.bin', 'ab') as file:
    file.write(b'\x06\x07\x08\x09\x0A')

# Read the content to verify
with open('example_ab.bin', 'rb') as file:
    content = file.read()
    print('Binary content read from file:', content)

# output :
# Binary content read from file: b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n'
