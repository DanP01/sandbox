
MIN_LENGTH = 1
MAX_LENGTH = 6

password = input('Enter password(max of 6 items): ')
while len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
       print('Not valid number of items')
       password = input('Enter password(max of 6 items): ')
print('*' * len(password))
