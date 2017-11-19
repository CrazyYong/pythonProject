# -*- conding:UTF-8 -*-
import multiprocessing
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

mm=multiprocessing.Queue(5)
mm.put(1)
mm.put(2)
mm.put(3)
mm.put(4)
mm.put(5)
# mm.put(6,timeout=2)
# mm.put_nowait(6)
print(mm.get())
print(mm.qsize())
print(mm.get_nowait())
print(mm.get_nowait())
print(mm.get_nowait())
print(mm.get_nowait())
# print(mm.get(timeout=2))







