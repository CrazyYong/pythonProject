import pickle,pprint


'''
pkl是一种特殊的文件类型，如果直接打开会看到一堆乱码（序列化的内容），所有者正确的打开方式
如下 readPkl()
'''

def writePkl():
    data1 = {'a': [1, 2.0, 3, 4 + 6j],
             'b': ('string', u'Unicode string'),
             'c': None}

    selfref_list = [1, 2, 3]
    selfref_list.append(selfref_list)

    output = open('E:\pythonProject\文件异常\pickle.pkl', 'wb')

    pickle.dump(data1, output)

    pickle.dump(selfref_list, output, -1)

    output.close()

    return


def readPkl():
    pkl_file = open('E:\pythonProject\文件异常\pickle.pkl', 'rb')

    data1 = pickle.load(pkl_file)
    pprint.pprint(data1)

    data2 = pickle.load(pkl_file)
    pprint.pprint(data2)

    pkl_file.close()

    return


readPkl();