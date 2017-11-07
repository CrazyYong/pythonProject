#直接赋值
#字符串
# str1='Python'
# str2=str1
# print(id(str1))
# print(id(str2))
# str2='123'
# print(id(str1))
# print(id(str2))
# print(str2)
#列表
list1=[1,2,3,['问','Python']]
list2=list1
# print(list2)
list2[0]='AI'
print(list1)
print(list2)

#深浅拷贝
#原始对象
import copy
list0=[1,2,3,['we','haha','Python']]
#浅拷贝
list1=list0[:]
list2=list(list0)
list3=list0.copy()
list4=copy.copy(list0)
#深拷贝
# list0=[1,2,3,['we','haha','Python']]
listd=copy.deepcopy(list0)
# print(id(list0))
# print(id(list1))
# print(id(list2))
# print(id(list3))
# print(id(list4))
# print(id(list0[0]))
# print(id(list1[0]))
# print(id(list2[0]))
# print(id(list3[0]))
# print(id(list4[0]))
# print(id(listd[0]))
# list1[0]='A1'
# list2[0]='A2'
# list3[0]='A3'
# list4[0]='A4'
# listd[0]='A5'
# print(list0)
# print(list1)
# print(list2)
# print(list3)
# print(list4)
# print(listd)
# print(id(list0[0]))
# print(id(list1[0]))
# print(id(list2[0]))
# print(id(list3[0]))
# print(id(list4[0]))
# print(id(listd[0]))
list0=[1,2,3,['we','haha','Python']]
list1[3][0]='11'
list2[3][0]='12'
list3[3][0]='13'
list4[3][0]='14'
listd[3][0]='15'
print(id(list0[3]))
print(id(list1[3]))
print(id(list2[3]))
print(id(list3[3]))
print(id(list4[3]))
print(id(listd[3]))
print(list0)
print(list1)
print(list2)
print(list3)
print(list4)
print(listd)