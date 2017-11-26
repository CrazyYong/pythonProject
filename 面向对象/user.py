#3.用户：创建一个名为User的类，其中包含属性first_name和last_name,
# 还有用户简介通常会存储的其他几个属性。在类User中定义一个名为describe_user()的方法，
# 它打印用户信息摘要；再定义一个名为greet_user()的方法，它向用户发出个性化的问候。
# 创建多个表示不同用户的实例，并对每个实例都调用上述两个方法.

# 5.尝试登录次数：在为完成练习3而编写的User类中，添加一个名为login_attempts的属性。
# 编写一个名为increment_login_attempts()的方法,它将属性 login_attempts的值加1。再
# 编写一个名为reset_login_attempts()方法,它将属性login_attempts的值重置为0。
#     根据User类创建一个实例,再调用方法increment_login_attempts()多次。
# 打印属性login_attempts的值,确认它被正确地递增；然后，调用方法reset_login_attempts(),
# 并再次打印属性login_attempts的值，确认它被重置为0。
class User:
    def __init__(self,first_name,last_name,tall,tele,login_attempts=0):
        self.first_name=first_name
        self.last_name=last_name
        self.tall=tall
        self.tele=tele
        self.login_attempts=login_attempts
    def describe_user(self):
        print('%s%s是中国人,身高有%s,电话号码有%s'%(self.first_name,self.last_name,self.tall,self.tele))
    def greet_user(self):
        print('您最近好吗?%s%s'%(self.first_name,self.last_name))
    def increment_login_attempts(self):
        self.login_attempts+=1
        # print('当前的login_attempts次数是%d次'%self.login_attempts)
    def reset_login_attempts(self):
        self.login_attempts=0
        # print('当前的login_attempts重置后是%d次' % self.login_attempts)
if __name__=='__main__':
    user1=User('李','小龙',178,13337894561)
    # user1.describe_user()
    # user1.greet_user()
    nn=int(input('请输入你的循环次数:'))
    for i in  range(0,nn):
        user1.increment_login_attempts()
    print('当前的login_attempts的次数是',user1.login_attempts)
    user1.reset_login_attempts()
    print('当前的login_attempts的重置后的次数是', user1.login_attempts)
    