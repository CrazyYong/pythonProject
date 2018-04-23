import multiprocessing
import queue

'''
Queue的功能是将每个核或线程的运算结果放在队里中， 等到每个线程或核运行完毕后再从队列中取出结果， 
继续加载运算。原因很简单, 多线程调用的函数不能有返回值, 所以使用Queue存储多个线程运算的结果

队列是一种先入先出的数据类型
'''
#######################案例一

# def q1(q):
#     msg='queue first'
#     q.put(msg)
#     print('队列里面的数据量%d'%(q.qsize()))
#
# def q2(q):
#     print('取出q里面的值%s'%(q.get()))
#
#
# if __name__=='__main__':
#     q=multiprocessing.Queue()
#     process1=multiprocessing.Process(target=q1,args=(q,))
#     process2=multiprocessing.Process(target=q2,args=(q,))
#
#     process1.start()
#     process2.start()
#     process1.join()
#     process2.join()
#     print(q.empty())#队列是否已经空了
#     print('队列里面的数据量%d'%(q.qsize()))
#     print(q.full())#判断是否满，满返回True


##################################案例二
import time
# def put_data(qu,loop):
#     print(time.ctime())
#     for i in loop:
#         qu.put(i)
#
# def get_data(qu,loop):
#     print(time.ctime())
#     for i in loop:
#         value=qu.get()
#         print('得到的值是%s'%value)
#
# if __name__=='__main__':
#     qu=multiprocessing.Queue()
#     loop=['蒲公英','葵花','狗尾巴','月季']
#     p1=multiprocessing.Process(target=put_data,args=(qu,loop))
#     p2=multiprocessing.Process(target=get_data,args=(qu,loop))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     print(qu.empty())
#     print(qu.qsize())
#     print(qu.full())


###################################
# 设置具有长度限制的队列
# mm=multiprocessing.Queue(5)
# mm.put(1)
# mm.put(2)
# mm.put(3)
# mm.put(4)
# mm.put(5)
#
# print(mm.get())
# print(mm.qsize())
# print(mm.get_nowait())
# print(mm.get_nowait())
# print(mm.get_nowait())
# print(mm.get_nowait())

#######################################

# q = queue.Queue()  # 先入先出
# print(q.empty())  # 判断是否为空，空返回True
# q.put("d1")
# q.put("d2")
# q.put("d3")
# # for i in range(q.qsize()):
# #     print('循环获取queue里面的值%s'%(q.get()))
# print(q.full())  # 判断是否满，满返回True
# print(q.get())  # d1
# print(q.get())  # d2
# print(q.get())  # d3

# print(q.get(timeout=1))  # 阻塞 可以使用q.get(timeout = 1)设置超时来解决阻塞问题，抛出queue.Empty异常
# print(q.get_nowait())  # 接上一行的例子，还可以设置不要等待，没有数据即刻抛出异常,类似get(false)
# print(q.qsize())  # 或者使用if判断qsize是否等于0
# print(q.get(block=False))  # block参数False也可以解决程序阻塞问题

#######################################设置有长度限制的队列
q = queue.Queue(maxsize=3)  # 长度为3
q.put(1)
q.put(2)
q.put(3)
# q.put(4, block=False)  # 这里程序又阻塞了,所以可以使用block,timeout参数解决阻塞问题,异常queue.Full

q = queue.PriorityQueue()  # 设置优先级队列，数字小的优先级高
q.put((1, "King"))
q.put((-1, "Jeson"))
q.put((10, "Tim"))
q.put((5, "Mike"))
print(q.get())
print(q.get())
print(q.get())
print(q.get())

q = queue.LifoQueue() #设置后入先出队列
q.put(1)
q.put(2)
q.put(3)
print(q.get())
print(q.get())
print(q.get())