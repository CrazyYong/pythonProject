# -*- conding:UTF-8 -*-
import multiprocessing
import time
# def send_data(pipe,message):
#     pipe.send(message)
#
# def recv_data(pipe):
#     value=pipe.recv()
#     print('接收的一个值是%s'%value)
#
# if __name__=='__main__':
#     Pipe里面的duplex默认的值True,全双工管道
#     pipe=multiprocessing.Pipe()
#     message='Python'
#     p1=multiprocessing.Process(target=send_data,args=(pipe[1],message))
#     p2=multiprocessing.Process(target=recv_data,args=(pipe[0],))
#     p1.start()
#     p2.start()



#当duplex为false时,左边收,右边发
def send_data(pipe,message):
    pipe.send(message)

def recv_data(pipe):
    value=pipe.recv()
    print('接收的一个值是%s'%value)

if __name__=='__main__':
    pipe = multiprocessing.Pipe(duplex=False)
    message = 'Python'
    p1 = multiprocessing.Process(target=send_data, args=(pipe[0], message))
    p2 = multiprocessing.Process(target=recv_data, args=(pipe[1],))
    p1.start()
    p2.start()