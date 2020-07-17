class User:
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd

    def login(self, name, pwd):
        if (self.name == name and self.pwd == pwd):
            print('登录成功')
        else:
            print('用户名密码不正确')
    def show(self):
        print('用户名：{}，密码：{}'.format(self.name, self.pwd))


# p170