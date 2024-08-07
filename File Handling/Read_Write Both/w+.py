# Open the file in w+ mode
with open('example_w+.txt', 'w+') as file:
    # Write initial content
    file.write('Initial content\n')

    # Move the file pointer to the beginning of the file to read
    file.seek(0)

    # Read the current content
    content = file.read()
    print('Current content after initial write:')
    print(content)

    # Write new content
    file.write('Additional content\n')

    # Move the file pointer to the beginning of the file again to read all content
    file.seek(0)

    # Read the updated content
    updated_content = file.read()
    print('Updated content after additional write:')
    print(updated_content)


# output :
'''
    Current content after initial write:
    Initial content

    Updated content after additional write:
    Initial content
    Additional content
'''