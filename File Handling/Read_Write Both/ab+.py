# Open the file in ab+ mode and write initial binary data
with open('example_ab+.bin', 'ab+') as file:
    # Write initial binary data
    file.write(b'\x00\x01\x02\x03\x04\x05')

    # Move the file pointer to the beginning to read the content
    file.seek(0)
    content = file.read()
    print('Current content after initial write:', content)

# Open the file in ab+ mode and append additional binary data
with open('example_ab+.bin', 'ab+') as file:
    # Append additional binary data
    file.write(b'\x06\x07\x08\x09\x0A')

    # Move the file pointer to the beginning to read the updated content
    file.seek(0)
    updated_content = file.read()
    print('Updated content after additional append:', updated_content)


# output :
'''
Current content after initial write: b'\x00\x01\x02\x03\x04\x05'
Updated content after additional append: b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n'
'''