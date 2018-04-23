# -*- conding:UTF-8 -*-
# 假如我们创建了两个任务：听音乐（music)和看电影（movie)。在单线程中，我们只能按先后顺序来执行这两个任务。
# from time import *
# def music(name):
#     print('您正在听的音乐是%s'%name)
#     sleep(2)
#     print(ctime())
# def movie(name):
#     print('您正在看的电影是%s'%name)
#     sleep(2)
#     print(ctime())
# if __name__=='__main__':
#     music('天蓝')
#     movie('阿凡达')
#     print(ctime())
# 首先music和movie作为播放器，在用户使用时，可以根据用户的需求来播放任意的歌曲和影片，
# 并且我们希望播放器能够提供循环播放的功能，尤其对于音乐播放器来说这个很重要

# from time import *
# def music(name,loop):
#     for i in range(loop):
#         print('您正在听的音乐是%s'%name)
#         sleep(2)
#     print(ctime())
# def movie(name,loop):
#     for i in range(loop):
#         print('您正在看的电影是%s'%name)
#         sleep(2)
#     print(ctime())
# if __name__=='__main__':
#     music('天蓝',5)
#     movie('阿凡达',5)
#     print(ctime())

# 自定义一个听音乐的函数,利用for循环,将活动添加到线程中.
from time import *
# import threading
# def music(name,loop):
#     for i in range(loop):
#         print('您正在听的音乐是%s'%name)
#         sleep(2)
#     print(ctime())
# def movie(name,loop):
#     for i in range(loop):
#         print('您正在看的电影是%s'%name)
#         sleep(2)
#     print(ctime())
# if __name__=='__main__':
#     t=[]
#     t1=threading.Thread(target=music,args=('香水有毒',4))#args要用元组
#     t2=threading.Thread(target=movie,args=('机器总动员',4))
#     t.append(t1)
#     t.append(t2)
    #第一种方式启动线程
    # t1.start()
    # t2.start()
    # #join()阻塞线程,直到子线程全部执行完毕,主线程才退出
    # t1.join()
    # t2.join()
    # print('主线程')
    #使用第二个方法启动线程
    # for i in  t:
    #     i.start()
    # for i in t:
    #     i.join()
    # print('主线程')

#threading的属性或者方法
from time import *
import threading
def music(name,loop):
    for i in range(loop):
        print('您正在听的音乐是%s'%name)
        sleep(2)
    print(ctime())
def movie(name,loop):
    for i in range(loop):
        print('您正在看的电影是%s'%name)
        sleep(2)
    print(ctime())
if __name__=='__main__':
    t=[]
    t1=threading.Thread(target=music,name='thread--线程名1',args=('香水有毒',4)) #被调用的函数没有括号，被调用的函数的参数放在args(…)中
    t2=threading.Thread(target=movie,name='thread--线程名2',args=('机器总动员',4))
    t.append(t1)
    t.append(t2)
    #getName()获取线程的名称,类似name
    # print(t1.getName())
    # print(t2.getName())
    # print(t1.name)
    # print(t2.name)
    #setName()设置线程名称
    t1.setName('第一个线程')
    t2.setName('第二个线程')
    print(t1.getName())
    print(t2.getName())
    #setDaemon()守护主线程,主线程结束,子线程直接杀死,不让子线程继续执行
    for i in t:
        i.setDaemon(True)
    #daemon和我们的isDaemon()类似,判断是否守护线程
    # print(t1.daemon)
    # print(t2.daemon)
    # print(t1.isDaemon())
    # print(t2.isDaemon())
    for i in  t:
        i.start()
    #ident返回线程的标识符,is_alive()/alive判断线程存活状态,都在启动线程之后
    # print(t1.ident)
    # print(t2.ident)
    # print(t1.is_alive())
    # print(t2.is_alive())
    for i in t:
        i.join()

    print('主线程')