 # -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class CnblogsPipeline(object):
    def process_item(self, item, spider):
        return item
		
# 存储处理
import pandas as pd
class SaveCsvPipeline(object):
	#spider 启动的时候执行
	def open_spider(self,spider):
		pass
	#spider 关闭的时候执行
	def close_spider(self,spider):
		pass
		
	#构建管道
	@classmethod
	def from_crawler(cls,crawler):
		return cls()
	
	def __init__(self):
		pass
	
	# 默认处理
	
	def process_item(self, item, spider):
        # 1.接收item，把item转换为dataframe
		df1=pd.DataFrame(item)
		# 2.读取原来的csv，拼接新的内容
		df2=pd.read_csv('1.csv')
		#df=df1+df2
		pd.concat([df1, df2])
		# 3.调用to_csv进行保存
		df.to_csv('1.csv')