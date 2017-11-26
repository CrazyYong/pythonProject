# 类属性和实例属性  people类
#类属性可以在类方法中去调用,需要类名.属性名去调用;实例属性通过构造方法__init__去初始化
class people:
    '''
    这个类是一个人类,实例属性包含name,age,sex
    '''
    eat='喜欢吃饭喜欢睡觉'
    __like='喜欢的类型'
    #self是类的实例
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
        print('这是一个初始化方法!')
    def getinfo(self):
        print('这个人叫%s,然后年纪是%d,最后呢性别竟然是%s'%(self.name,self.age,self.sex))
        print('%s%s'%(self.name,people.eat))
#person1是类的实例化对象
# if __name__=='__main__':
person1=people('成乔恩',34,'女')
# print(person1._people__like)
# 通过实例化属性名调用类的方法
# person1.getinfo()

#查看类的属性
print(person1.eat)
#查看类的实例属性
print(person1.name)
#通过函数的方式访问
#getattr()的用法
# print(getattr(person1,'name1','范冰冰'))
#hasattr()的用法
# print(hasattr(person1,'eat'))
#setattr()的用法 可以给类或者实例化对象添加属性,然后通过类名.属性名或者通过函数去查看
# setattr(people,'professional','明星')
# print(person1.professional)
# print(getattr(person1,'professional','范冰冰'))

# 内置内属性 __dict__
# print(person1.__dict__)
# 内置内属性 __doc__ 类似help()方法
# print(people.__doc__)
# print(person1.__doc__)
# 内置内属性 __name__ 类
# print(people.__name__)
# print(person1.__name__) 会报错
