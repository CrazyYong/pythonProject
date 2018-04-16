import numpy as np

arr=np.array(
    [
        [0,-1,-2],
        [1,-4,3],
        [0,-6,7]
    ]
)
print(arr)
print(np.abs(arr))#计算整数、浮点数或者复数的绝对值

##
arr1=np.arange(10).reshape(2,5)
print(np.sqrt(arr1))#计算各个元素的平方根，相当于arr**0.5,要求arr的每个元素必须是非负数

##
arr2=np.array(
    [
        [0.6,-1.9,-2.1],
        [1.0,-4.5,3.1],
        [0.2,-6.9,7.7]
    ]
)

print(np.rint(arr2))#将各个元素值四舍五入到最接近的整数，保留dtype的类型

##
arr3=np.array(
    [
        [0.6,-1.9,-2.1],
        [1.0,-4.5,3.1],
        [0.2,-6.9,7.7]
    ]
)
print(np.floor(arr3))#计算各个元素的floor值，即小于等于改值的最大整数

##

arr4=np.array(
    [
        [0.6,-1.9,-2.1],
        [1.0,-4.5,3.1],
        [0.2,-6.9,7.7]
    ]
)
print(np.ceil(arr4))#计算各个元素的ceilling值，即大于等于该值的最小整数

##
arr5=np.array(
    [
        [0.6,-1.9,-2.1],
        [1.0,-4.5,3.1],
        [0.2,-6.9,7.7]
    ]
)
print(np.modf(arr5))#将数组中的元素的小数位和整数位以两部分独立数组的形式返回

##
arr6=np.array(
    [
        [0,-1.9,-2.1],
        [1.0,0,3.1],
        [0.2,-6.9,0]
    ]
)
print(np.isnan(arr6))#返回一个表示“那些值是NaN(不是一个数)”的布尔类型数组

##
'''
sign:计算各个元素的正负号：1正数，0：零，-1：负数
log、log10、log2、log1p：分别计算自然对数、底数为10的log、底数为2的log以及log(1+x);要求arr中的每个元素必须为正数
exp:计算各个元素的指数e的x次方
modf:将数组中的元素的小数位和整数位以两部分独立数组的形式返回
isfinite、isinf：分别一个表示“那些元素是有穷的（非inf、非NaN）”或者“那些元素是无穷的”的布尔型数组
cos、cosh、sin、sinh、tan、tanh:普通以及双曲型三角函数
arccos、arccosh、arcsin、arcsinh、arctan、arctanh：反三角函数
'''
