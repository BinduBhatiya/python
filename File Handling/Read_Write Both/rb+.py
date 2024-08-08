# Create a binary file with initial content
with open('example_rb+.bin', 'wb') as file:
    file.write(b'\x00\x01\x02\x03\x04\x05')
print("Initial binary data written to 'example_rb+.bin'")

# Open the file in rb+ mode to read and modify content
with open('example_rb+.bin', 'rb+') as file:
    # Read the initial binary content
    content = file.read()
    print('Initial content read from file:', content)

    # Modify the binary content at a specific position
    file.seek(2)  # Move to the 3rd byte (0-indexed)
    file.write(b'\xFF\xFF')  # Overwrite 2 bytes

    # Move the file pointer to the beginning to read the updated content
    file.seek(0)
    updated_content = file.read()
    print('Updated content after modification:', updated_content)


# output :
'''
Initial binary data written to 'example_rb+.bin'
Initial content read from file: b'\x00\x01\x02\x03\x04\x05'
Updated content after modification: b'\x00\x01\xff\xff\x04\x05'
'''