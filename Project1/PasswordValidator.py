import re

pattern = re.compile(r"[A-Za-z0-9@#$%^&+=]{8,}")
password = input("Enter Password")
password = str(password)
password_check = pattern.fullmatch(password)

if password_check is None:
    print('Please try again')
else:
    print('Password created successfully')
