username = input('Username: ')
password = input('Password: ')
password_length = len(password)
print(f'{username}, your password {'*' * password_length} is {password_length} letters long')