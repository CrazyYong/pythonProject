#类方法(需要传入cls)和静态方法(不需要传参,直接通过类名.类属性名去调用)不能调用实例属性,只能针对类属性,
class people:
    '''
    这个类是一个人类,实例属性包含name,age,sex
    '''
    eat='喜欢吃饭喜欢睡觉'
    #self是类的实例
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
        print('这是一个初始化方法!')
    def getinfo(self):
        print('这个人叫%s,然后年纪是%d,最后呢性别竟然是%s'%(self.name,self.age,self.sex))
        print('%s%s'%(self.name,people.eat))
    #定义一个静态方法 用@staticmethod
    @staticmethod
    def static1():
        print('人们几乎都%s'%people.eat)
    #定义一个类方法 用@classmethod
    @classmethod
    def class1(cls):
        print('人们几乎都%s' % cls.eat)
#person1是类的实例化对象
if __name__=='__main__':
    person1=people('成乔恩',34,'女')
    # person1.static1()
    person1.class1()



    # person1.getinfo()
    # person1.__eat='不喜欢吃饭不喜欢睡觉'
    # print(person1._people__eat)
    # print(person1.__eat)