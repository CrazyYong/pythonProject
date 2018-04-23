import multiprocessing
import os,time,random

'''
join的作用就是阻塞当前线程往下执行，放的位置不一样效果也不一样
'''
def r1(process_name):
    for i in range(5):
        print('当前线程名:'+process_name,'当前线程id:%d'%(os.getpid()))
        time.sleep(random.random())


def r2(process_name):
    for i in range(5):
        print('当前线程名:'+process_name,'当前线程id:%d'%(os.getpid()))
        time.sleep(random.random()*2)

if __name__=='__main__':
    print('main process run...')
    p1=multiprocessing.Process(target=r1,args=('process1',))
    p2=multiprocessing.Process(target=r2,args=('process2',))

    p1.start()
    p2.start()
    p1.join()
    #p2.join()

    print('main process runned all lines...')

'''
main process run...
当前线程名:process1 当前线程id:12696
当前线程名:process2 当前线程id:12720
当前线程名:process1 当前线程id:12696
当前线程名:process2 当前线程id:12720
当前线程名:process1 当前线程id:12696
当前线程名:process1 当前线程id:12696
当前线程名:process1 当前线程id:12696
当前线程名:process2 当前线程id:12720
当前线程名:process2 当前线程id:12720
main process runned all lines...
当前线程名:process2 当前线程id:12720
'''

'''
通过结果可以看到，主线程只是等待p1完成了，就会向下执行，而不会等待p2是否完成。
那个线程调用了join，那么主线程就会等待该线程执行完再往下执行
'''

