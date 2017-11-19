# -*- conding:UTF-8 -*-
# apply 阻塞进行
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

# if __name__=='__main__':
#     pool=multiprocessing.Pool(2)
#     pool.apply(func=music,args=('花太香',3))
#     pool.apply(func=movie,args=('王牌特工',2))
#     # pool.close()
#     pool.terminate()
#     #join阻塞主进程,当子进程执行完毕的时候会继续往后执行,使用join必须进程池使用terminate或者close
#     pool.join()
#     print('结束时间是%s'%time.ctime())

#apply_async非阻塞进行

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
    pool=multiprocessing.Pool(2)
    pool.apply_async(func=music,args=('花太香',3))
    pool.apply_async(func=movie,args=('王牌特工',2))
    pool.close()
    # pool.terminate()
    # 比较危险,不要轻易用,直接杀死进程池
    #join阻塞主进程,当子进程执行完毕的时候会继续往后执行,使用join必须进程池使用terminate或者close
    pool.join()
    print('结束时间是%s'%time.ctime())