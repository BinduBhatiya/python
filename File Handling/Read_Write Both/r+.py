with open('example_r+.txt', 'w') as file:
    file.write('Initial content\n')

# Open the file in r+ mode
with open('example_r+.txt', 'r+') as file:
    # Read the current content
    content = file.read()
    print('Current content:', content)

    # Move the file pointer to the end of the file
    file.seek(0,2)

    # Write new content
    file.write('Additional content\n')

    # Move the file pointer to the beginning of the file
    file.seek(0)

    # Read the updated content
    updated_content = file.read()
    print('Updated content:', updated_content)


# output :
'''
    Current content: Initial content

    Updated content: Initial content
    Additional content

'''
