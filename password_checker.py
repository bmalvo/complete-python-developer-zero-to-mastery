user_name = (input('What is Your name?'))

user_password = (input('What is Your password?'))

pass_length = len(user_password)

hidden_pass = '*' * len(user_password)

message = f'Hi {user_name}! Your password: {hidden_pass} is {pass_length} letters long.'

print(message)