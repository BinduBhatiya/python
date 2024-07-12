# validate user input exercise
# username is no more then 12 character.
# username must not contain spaces.
# username must not contain digits.

username = input("enter the username: ")

if len(username) > 12:
    print("please enter less than 12 character.")   
elif not username.isalpha():
    print("not valid username.")
else:
    print("welcome",username)
