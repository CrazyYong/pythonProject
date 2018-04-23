# -*- conding:UTF-8 -*-
'''
进程池就是我们将所要运行的东西，放到池子里，Python会自行解决多进程的问题

有了池子之后，就可以让池子对应某一个函数，我们向池子里丢数据，池子就会返回函数返回的值。
Pool和之前的Process的不同点是丢向Pool的函数有返回值，而Process的没有返回值。
'''


####################################################apply 阻塞进行，当一个线程池执行完之后另一个线程池才开始执行

import multiprocessing
import time
def music(name,loop):
    print(time.ctime())
    for i in range(loop):
        time.sleep(2)
        print('您现在正在听的音乐是%s'%name)

def movie(name,loop):
    print(time.ctime())
    for i in range(loop):
        time.sleep(2)
        print('您现在正在看的电影是%s'%name)

if __name__=='__main__':
    pool=multiprocessing.Pool(2)#可以自定义CPU核数量
    pool.apply(func=music,args=('花太香',3))
    pool.apply(func=movie,args=('王牌特工',2))
    # pool.close()
    pool.terminate()
    #join阻塞主进程,当子进程执行完毕的时候会继续往后执行,使用join必须进程池使用terminate或者close
    pool.join()
    print('结束时间是%s'%time.ctime())

#################################################apply_async非阻塞进行，线程池同时开始执行，由系统调度

# import multiprocessing
# import time
# def music(name,loop):
#     print(time.ctime())
#     for i in range(loop):
#         time.sleep(2)
#         print('您现在正在听的音乐是%s'%name)
#
# def movie(name,loop):
#     print(time.ctime())
#     for i in range(loop):
#         time.sleep(2)
#         print('您现在正在看的电影是%s'%name)
#
# if __name__=='__main__':
#     pool=multiprocessing.Pool(2)#可以自定义CPU核数量
#     pool.apply_async(func=music,args=('花太香',3))
#     pool.apply_async(func=movie,args=('王牌特工',2))
#     pool.close()
#     # pool.terminate()
#     # 比较危险,不要轻易用,直接杀死进程池
#     #join阻塞主进程,当子进程执行完毕的时候会继续往后执行,使用join必须进程池使用terminate或者close
#     pool.join()
#     print('结束时间是%s'%time.ctime())

#####################################################待返回值的apply_async()
'''
apply_async()只能输入一组参数(也就是每次只能放入一个任务，如果想放入多个任务可以使用map/map_async方法
'''
# import multiprocessing as mp
#
# def job(l):
#     return l
#
# def multicore():
#     pool=mp.Pool()
#     res=[pool.apply_async(job,(i,)) for i in range(10)]
#
#     print([out.get() for out in res])
# if __name__=='__main__':
#     multicore()

##################################################### map()
'''
用map()获取结果，在map()中需要放入函数和需要迭代运算的值，然后它会自动分配给CPU核，返回结果
map方法每次可以处理一个任务序列，每个任务的执行方法相同。
'''
# import multiprocessing as mp
#
# def job(l):
#     return l
#
# def multicore():
#     pool=mp.Pool()
#     res=pool.map(job,range(10))
#     print(res)
# if __name__=='__main__':
#     multicore()
