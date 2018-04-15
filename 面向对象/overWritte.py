

class Parent:
    def myMethod(self):
        print('调用父类的方法')



class Child(Parent):
    def myMethod(self):
        print('调用子类方法')



c=Child()
c.myMethod()
super(Child,c).myMethod()