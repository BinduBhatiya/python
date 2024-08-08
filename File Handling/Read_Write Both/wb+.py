# Open the file in wb+ mode and write initial binary data
with open('example_wb+.bin', 'wb+') as file:
    # Write some binary data
    file.write(b'\x00\x01\x02\x03\x04\x05')
    
    # Move the file pointer to the beginning to read the content
    file.seek(0)
    
    # Read and print the initial content
    initial_content = file.read()
    print('Initial content after write:')
    print(initial_content)

    # Modify the binary content at a specific position
    file.seek(2)  # Move to the 3rd byte (0-indexed)
    file.write(b'\xFF\xFF')  # Overwrite 2 bytes

    # Move the file pointer to the beginning to read the updated content
    file.seek(0)
    updated_content = file.read()
    print('Updated content after modification:')
    print(updated_content)



# output :
'''
Initial content after write:
b'\x00\x01\x02\x03\x04\x05'
Updated content after modification:
b'\x00\x01\xff\xff\x04\x05'
'''