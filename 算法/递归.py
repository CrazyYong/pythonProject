#coding=utf-8

'''
递归有两个基本要素：
（1）边界条件：确定递归到何时终止，也成递归出口
（2）递归模式：大问题是如何分解为小问题的，也成递归体
'''

'''
求一个整数n的阶乘
（1）边界条件：n=1的时候返回1
（2）递归模式：n(n-1)!  n>1
'''
def factorial(n):
    print(n)
    if n==1:
        return 1;

    return n*factorial(n-1)

# print(factorial(10))


'''
斐波拉切数列
0、1、1、2、3、5、8、13、21、……。 
斐波拉契数列的核心思想是: 
从第三项起，每一项都等于前两项的和，即F(N) = F(N - 1) + F(N - 2) (N >= 2) 
并且规定F(0) = 0，F(1) = 1
'''
# def fib_list(n) :
#   if n == 1 or n == 2 :
#     return 1
#   else :
#     m = fib_list(n - 1) + fib_list(n - 2)
#     return m
#
#
# try :
#   n = int(input("enter:"))
# except ValueError :
#   print ("请输入一个整数！")
#   exit()
# list2 = [0]
# tmp = 1
# while(tmp <= n):
#   list2.append(fib_list(tmp))
#   tmp += 1
# print (list2)


'''

'''

def Fibonacci(n):
    if(n<=1):
        return n;
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
print(Fibonacci(5))