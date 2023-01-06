import uuid

user = None

class User:
    def __init__(self, user_name, uuid, quest_log):
        self.user_name = user_name
        self.uuid = uuid
        self.quest_log = quest_log
    
def new_user():
    global user
    new_uuid = uuid.uuid4()
    user = User(input('What is your User Name? '), new_uuid, f'quest_log_{new_uuid}.txt' )
    print(f'\nWelcome {user.user_name}')


def start_program():
    global user
    if user == None:
        new_user()
        main_menu()
    else:
        main_menu()
    

def main_menu():
    global user
    print(f'What would you like to do today, {user.user_name}?\n1. Start a Quest\n2. [BLANK]\n3. Settings')
    while True:
        if input('Your Choice: ') == '1':
            try:
                stream = open(user.quest_log, 'a+')
                stream.write(input('Quest title: '))
                stream.write(input('Exp reward: '))
                stream.close()
            except Exception as e:
                print('Something went wrong', e)
            try:
                stream = open(user.quest_log)
                stream.read(1000)
                stream.close()
            except Exception as e:
                print('Something went wrong', e)
        break
        if input('Your Choice: ') == '3':
            settings_menu()
            break
        else:
            print('Sorry, I cannot help with that right now')


def settings_menu():
    global user
    while True:
        user_input = input('\nWhat would you like to do?\n1. Update User Name\n2. Check User ID\n3. Exit ')
        if user_input == '1':
            print(f'Current User Name: {user.user_name}')
            user.user_name = input('New User Name: ')
            print(f'\nYour User Name has been changed to {user.user_name}')
            
        elif user_input == '2':
            print(f'\nYour User ID is {user.uuid}')
            print(f'\nYour Quest Log file is {user.quest_log}')
        
        elif user_input == '3':
            main_menu()
            
        else:
            print('Invalid input')
    
    
start_program()
