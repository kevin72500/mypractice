#coding:utf8
class MyException(Exception):
	def __init__(self,msg):
		self.error=msg
	def __str__(self):
		return self.error

obj=MyException('错误')
print obj