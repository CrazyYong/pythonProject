# -*- conding:UTF-8 -*-

#########################创建函数并将其作为单进程
import multiprocessing
import time
# def write1(filename):
#     with open(filename,'w',encoding='utf_8') as file:
#         file.write('我们正在学习python\n')
#         file.write('接下来我们将进入正科学习\n')
# if __name__=='__main__':
#     write1('lianxi1.txt')


########################创建函数并将其作为多个进程
# import multiprocessing
# import time
# def write1(filename):
#     with open(filename,'a',encoding='utf_8') as file:
#         file.write('我们正在学习python\n')
#         file.write('接下来我们将进入正科学习\n')
# if __name__=='__main__':
#     for i in range(5):
#         p=multiprocessing.Process(target=write1,name='进程--{0}'.format(i),args=('lianxi2.txt',)) #被调用的函数没有括号，被调用的函数的参数放在args(…)中
#         p.start()
#         #ident和pid一样都是返回进程标识符
#         # print(p.ident)
#         # print(p.pid)
#
#         print(p.name)


#########################将进程定义为类
import multiprocessing
import time
class clockprocess(multiprocessing.Process):
    def __init__(self,name):
        #类名.__init__这个父类的调用
        multiprocessing.Process.__init__(self)
        #super是个超级函数,传递类的实例
        # super(clockprocess,self).__init__()
        self.name=name
    def run(self):
        for i in range(4):
            print('正在听%s'%self.name)
if __name__=='__main__':
    p=clockprocess('凤凰传奇')
    p.start()

