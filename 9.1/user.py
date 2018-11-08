class User():
    def __init__(self, first_name, last_name, sex, location, birthdate):
        self.first_name = first_name
        self.last_name = last_name
        self.sex =sex
        self.location = location
        self.birthdate = birthdate

    def describe_user(self):
        print('first_name :' + self.first_name)
        print('last_name :' + self.last_name)
        print('sex :' + self.sex)
        print('location :' +self.location)
        print('birthdate :' + self.birthdate)
    
    def greet_user(self):
        print('Hello, welcome to this new world!!!')
        

userone = User('Xiaoming', 'Li', 'male', 'Nanjing', '1996-11-10')
usertwo = User('Feier', 'Tian', 'female', 'Chengdu', '1997-06-12')
userone.describe_user()
userone.greet_user()
print('\n')
usertwo.describe_user()
usertwo.greet_user()