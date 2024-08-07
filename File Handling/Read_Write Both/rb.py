# Create a binary file with initial content
with open('example.bin', 'wb') as file:
    # Write some binary data to the file
    file.write(b'\x00\x01\x02\x03\x04\x05')


# Open the binary file in rb mode
with open('example.bin', 'rb') as file:
    # Read the binary content
    content = file.read()
    print('Binary content:', content)
    
    # Read individual bytes
    file.seek(0)
    for i in range(6):
        byte = file.read(1)
        print(f'Byte {i}:', byte)


# output :
'''
inary content: b'\x00\x01\x02\x03\x04\x05'
Byte 0: b'\x00'
Byte 1: b'\x01'
Byte 2: b'\x02'
Byte 3: b'\x03'
Byte 4: b'\x04'
Byte 5: b'\x05'
'''