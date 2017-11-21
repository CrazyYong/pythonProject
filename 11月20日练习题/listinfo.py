'''
三.定义一个列表的操作类：Listinfo

包括的方法:

1 列表元素添加: add_key(keyname)  [keyname:字符串或者整数类型]
2 列表元素取值：get_key(num) [num:整数类型]
3 列表合并：update_list(list)      [list:列表类型]
4 删除并且返回最后一个元素：del_key()

'''

class Listinfo:
    def __init__(self,list_value):
        self.list_value=list_value

    def add_key(self,keyname):
        self.list_value.append(keyname)
        print(self.list_value)

    def get_key(self,num):
        print(self.list_value[num])

    def update_list(self,list):
        self.list_value.extend(list)
        print(self.list_value)

    def del_key(self):
        print(self.list_value.pop())

listob=Listinfo([1,2,3,4,5,6,7,8,9])
listob.add_key(10)
listob.get_key(3)
listob.update_list(['one','two','three','four'])
listob.del_key()


'''
四.一个整数，它加上100和加上268后都是一个完全平方数，请问该数是多少？
'''

import math
for i in range(-99,10000):
    x=int(math.sqrt(i+100))
    if x*x==i+100:
        y=int(math.sqrt(i+100+168))
        if y*y==i+100+168:
            print(i)

