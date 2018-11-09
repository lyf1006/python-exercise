class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user = User('Qingqian', 'Fucha')
user.increment_login_attempts()
print(user.login_attempts)
user.increment_login_attempts()
print(user.login_attempts)
user.increment_login_attempts()
print(user.login_attempts)
user.increment_login_attempts()
print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)