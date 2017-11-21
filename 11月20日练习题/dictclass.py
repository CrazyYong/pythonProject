#!/usr/bin/python3
#coding=utf-8

'''


二：定义一个字典类：dictclass。完成下面的功能：


dict = dictclass({你需要操作的字典对象})

1 删除某个key

del_dict(key)


2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"

get_dict(key)

3 返回键组成的列表：返回类型;(list)

get_key()

4 合并字典，并且返回合并后字典的values组成的列表。返回类型:(list)

update_dict({要合并的字典})
"""
'''

class Dictclass:
    def __init__(self,dict_value):
        self.dict_value=dict_value

    def del_dict(self,key):
        del self.dict_value[key]
        print('已删除')

    def get_dict(self,key):
        if key in self.dict_value:
            print(self.dict_value[key])
        else:
            print('not found')

    def get_key(self):
        return self.dict_value.keys()

    def update_dict(self):
        dict={'Sex':'Man','Colleage':'HH'}
        self.dict_value.update(dict)
        print(self.dict_value)


dict = Dictclass({'Name': 'Zara', 'Age': 7, 'Like': 'game'})
dict.del_dict('Name')
dict.get_dict('Age')
print(dict.get_key())
dict.update_dict()



