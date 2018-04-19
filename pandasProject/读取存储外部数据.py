import numpy as np
import pandas as pd

'''
pandas可以读取的数据格式
read_csv  to_csv
read_excel to_excel
red_hdf    to_hdf
read_sql   to_sql
read_json  to_json
read_msgpack  to_msgpack
read_html   to_html
read_gbq    to_gbq
read_stata  to_stata
read_sas    to_sas
read_clipboard  to_clipboard
read_pickle   to_pickle
'''

data=pd.read_csv('data01.csv')
print(data)

data.to_pickle('student.pickle')#保存为python内部格式pickle