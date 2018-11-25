import json

def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = r'C:\Users\huayu\Desktop\python-exercise\10.4\username.txt'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """提示用户输入用户名"""
    filename = r'C:\Users\huayu\Desktop\python-exercise\10.4\username.txt'
    username = input('What is your name? ')
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        isCurrent = input("Are you " + username + "? ")
        if isCurrent == 'yes':
            print('Welcome back, ' + username + '!')
        else:
            username = get_new_username()
            print("We'll remenber you when you come back, " + username + "!")

    else:
        username = get_new_username()
        print("We'll remenber you when you come back, " + username + "!")

greet_user()