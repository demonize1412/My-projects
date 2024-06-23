class user():

    def __init__(self, name, age, password):
        self.name = name
        self.age = age
        self.password = password

    def print_user(self):
        print('я', self.name, '  мне', self.age, '  пароль', self.password)


user1 = user('max', 25, '123')
print(user1)
user1.print_user()
