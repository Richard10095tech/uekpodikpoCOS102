import string

filename = 'users.txt'
with open(filename, 'a') as f:
    users = []
    def ask_user():
        while True:
            print('enter "q" at any time to stop loop')
            first_name = input('Enter firstname >> ').replace(' ', '')
            if first_name=='q':
                break
            last_name = input('Enter lastname >> ').replace(' ', '')
            if last_name=='q':
                break
            person = f'{first_name} {last_name}'.title().strip()
            users.append(person)
        for user in users:
            f.write(f'Dear {user}, your username is\n')
        print(users)    
         
    ask_user()
        