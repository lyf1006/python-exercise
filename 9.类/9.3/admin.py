import privileges 
class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        

    def describe_user(self):
        print('first_name :' + self.first_name)
        print('last_name :' + self.last_name)
        
    
    def greet_user(self):
        print('Hello, welcome to this new world!!!')

#继承User，增加新的属性
class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        """使用文件名使用Privileges类"""
        self.privilege = privileges.Privileges()

    """此方法移入Privileges类中，在init方法中创建一个Privileges实例，
    调用show_privileges方法"""
    # def show_privileges(self):
    #     print('Privileges are: ')
    #     for privilege in self.privileges:
    #         print(privilege)

admin = Admin('Qingqian', 'Murong')
admin.privilege.show_privileges()