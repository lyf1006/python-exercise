users = ['Mary','Lily','admin','Jack','Tom']

for user in users:
    if user == 'admin':
        print("Hello admin,would you like to see a status report?")
    else:
        print("Hello "+user+", thank you for logging in again.")