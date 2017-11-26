
class Bank:
    __openNum=0
    __cardNumBank=[]
    __passwordBank=[]
    __userNameBank=[]
    __banlanceBank=[]


    def __init__(self,cardNum,password,userName,banlance):
        self.cardNum=cardNum
        self.password=password
        self.userName=userName
        self.banlance=banlance
        Bank.__openNum+=1
        Bank.__cardNumBank.append(cardNum)
        Bank.__passwordBank.append(password)
        Bank.__userNameBank.append(userName)
        Bank.__banlanceBank.append(banlance)

    #本银行开户数
    def openUserNum(self):
        print ('开户数是%d'%(Bank.__openNum))

    #个人信息
    def personInfo(self):
        print ('卡号%s,用户密码%s,用户名%s,余额%s'%(Bank.__cardNumBank,
                                        Bank.__passwordBank,Bank.__userNameBank,Bank.__banlanceBank))

    #取款
    def drawMoney(self,cardNum,password,drawNum):
        if cardNum in Bank.__cardNumBank and password in Bank.__passwordBank:
            index_card=Bank.__cardNumBank.index(cardNum)
            if drawNum>Bank.__banlanceBank[index_card]:
                print ('余额不足')
            else:
                banlanceMoney=Bank.__banlanceBank[index_card]-drawNum
                Bank.__banlanceBank[index_card]=banlanceMoney
                print ('取钱成功')
        else:
            print ('输入的账号或密码错误，请重新输入')


    #存款
    def saveMoney(self,cardNum,password,moneyNum):
        if cardNum in Bank.__cardNumBank and password in Bank.__passwordBank:
            index_card=Bank.__cardNumBank.index(cardNum)
            Bank.__banlanceBank[index_card]=Bank.__banlanceBank[index_card]+moneyNum
            print ('存钱成功,余额%d'%(Bank.__banlanceBank[index_card]))
        else:
            print ('输入的账号或密码错误，请重新输入')


    #查看个人信息
    def oneSelfInfo(self,cardNum,password):
        if cardNum in Bank.__cardNumBank and password in Bank.__passwordBank:
            index_card=Bank.__cardNumBank.index(cardNum)
            name=Bank.__userNameBank[index_card]
            balanceMoney=Bank.__banlanceBank[index_card]
            print ('卡号:%s,用户名:%s,余额:%s'%(cardNum,name,balanceMoney))
        else:
            print ('ddd')

# if __name__ == '__main__':
#     xiaowang = Bank(3452323,123123,'小王',10000)
#     xiaobai = Bank(232323, 121323, '小白', 23434)
#     xiaowang.drawMoney(3452323,123123,200)
#     xiaowang.saveMoney(3452323,123123,2003)
#     xiaowang.oneSelfInfo(3452323,123123)
#     xiaowang.openUserNum()
#     xiaowang.personInfo()



'''
1.bc
2.acd
3.abd
4.abcd
5.c
6.abd
7.abd
8.cd
9.abd
10.ac (有歧义)
11.ac
12.acd
13.cd
14.bd
15.ac
16.ac
17.bc
18.cd
19.ad
20.abd
21.
try:
  <语句>
except <异常类型1>[,异常参数名1]:
  <异常处理代码1>
except <异常类型2>[,异常参数名2]:
  <异常处理代码2>
else:
  <没有异常的是进行处理的地方>
finally:
  <不管是不是有异常发生，都会执行这里>
  
22.
列表：
修改列表：
list1 = [1,2,4]
list1[0]=3
删除列表元素：
list1 = [1,2,4]
del list1[0]
增加列表元素：
list1 = [1,2,4]
list1.append(5)

字典：
修改字典：
dict2 = { 'abc': 123, 1: 37 };
dict2 ['abc']='ccc'
删除字典元素
dict2 = { 'abc': 123, 1: 37 };
del dict2['abc']
增加字典元素
dict2 = { 'abc': 123, 1: 37 };
dict2['aaa']=456

集合：
删除集合元素：
set1={1,2,3,4}
set1.remove(1)
增加集合元素：
set1={1,2,3,4}
set1.add('aaa')

赋值：
str1='hello world'
str2=str1
str1='new hello world'
此时str2仍然为hello world
str1中存储的地址发生了改变，指向了新建的值，此时str2变量存储的内存地址并未改变，所以不受影响。

浅拷贝
import copy
lst=['str1','str2','str3','str4','str5']
sourceLst=['str1','str2','str3','str4','str5',lst]
copyLst=copy.copy(sourceLst)
print ('sourceLst:%s'%(sourceLst))
print ('copyLst:%s'%(copyLst))
sourceLst.append('sourcestr')
copyLst.append('copystr')
print ('copyLst:%s'%(sourceLst))
print ('copyLst:%s'%(copyLst))
sourceLst[0]='changeSource'
print ('sourceLst:%s'%(sourceLst))
print ('copyLst:%s'%(copyLst))
lst.append('testAppend')
print ('sourceLst:%s'%(sourceLst))
print ('copyLst:%s'%(copyLst))
我们可以知道sourceLst和copyLst列表中都存储了一坨地址，当我们修改了sourceLst1的元素时，
相当于用'sourceChange'的地址替换了原来'str1'的地址，所以sourceLst的第一个元素发生了变化。
而copyLst还是存储了str1的地址，所以copyLst不会发生改变。

当sourceLst列表发生变化，copyLst中存储的lst内存地址没有改变，所以当lst发生改变的时候，
sourceLst和copyLst两个列表就都发生了改变

深拷贝：
import copy
lst=['str1','str2','str3','str4','str5']
sourceLst=['str1','str2','str3','str4','str5',lst]
deepcoypLst=copy.deepcopy(sourceLst)
print ('sourceLst:%s'%(sourceLst))
print ('deepcoypLst:%s'%(deepcoypLst))
sourceLst.append('sourcestr')
deepcoypLst.append('deepcopystr')
print ('sourceLst:%s'%(sourceLst))
print ('deepcoypLst:%s'%(deepcoypLst))
lst.append('test')
print ('sourceLst:%s'%(sourceLst))
print ('deepcoypLst:%s'%(deepcoypLst))
深拷贝就是在内存中重新开辟一块空间

23.
a=1
n=1
while n<=6:
    n+=1
    a=(a+1)*2
print(a)

24.
input_txt=input('请输入不少于五个数字，数字之间用空格隔开')
list_num=input_txt.split(' ')

array = [int(x) for x in list_num]
for i in range(len(array))[::-1]:
    for j in range(i):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
print (array)

25.
26.
while True:
    txt=input('请输入#号')
    if txt=='#':
        with open('czy.txt','w+',encoding='utf-8') as file:
            try:
                file.write(txt)
                file.write('\n')
                file.flush()
                file.seek(0)
                txt_read = file.read()
                print (txt_read)
                break
            except FileNotFound:
                file.close
                break
                

'''


def listOper(list1):
    list_new=[]
    for i in range(1,len(list1)):
        if list1[i]==list1[i-1]:
            list_new.append(list1[i])
            list_new.append(list1[i-1])
        else:
            list_new.append(list1[i])
        print (list_new)


# lists=[1,1,0,2,2,2,3,4,0,0,1,1]
lists=[1,1,2]
listOper(lists)