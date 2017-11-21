#!/usr/bin/python3
#coding=utf-8

'''
定义一个学生类。有下面的类属性：
    1 姓名
    2 年龄
    3 成绩（语文，数学，英语)[每课成绩的类型为整数]
    类方法：
    1 获取学生的姓名：get_name() 返回类型:str
    2 获取学生的年龄：get_age() 返回类型:int
    3 返回3门科目中最高的分数。get_course() 返回类型:int
    写好类以后，可以定义2个同学测试下:
    zm = Student('zhangming',20,[69,88,100])
    返回结果：
    zhangming
    20
    100
    """
'''
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_name(self):
        print('姓名是：%s'%(self.name))

    def get_age(self):
        print('年龄是：%d' % (self.age))

    def get_course(self):
        max_course = max(self.grade)
        if self.grade.index(max_course) == 0:
            print('该学员最好的成绩是语文成绩%d分' % max_course)
        elif self.grade.index(max_course) == 1:
            print('该学员最好的成绩是数学成绩%d分' % max_course)
        elif self.grade.index(max_course) == 2:
            print('该学员最好的成绩是英语成绩%d分' % max_course)

zm=Student('zhangming',20,[69,88,100])
zm.get_age()
zm.get_name()
zm.get_course()


