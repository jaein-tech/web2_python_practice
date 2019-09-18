user_id = input('id?')
user_pwd = input('password?')

'''
if user_input == '123456':
    print('Hi Jaein')
else:
    print('who are you?')
'''

'''
if user_id == 'dvpin':
    if user_pwd == '123456':
        print('Hi Jaein')
    else:
        print('who are you?')
else:
    print('who are you?')
'''

if user_id == 'dvpin' and user_pwd == '123456':
    print('Hi Jaein')
elif user_id == '0102' and user_pwd == '123':
    print('Hi Jaein')
else:
    print('who are you?')
