#coding:utf8
import time

class Foo:
	def __init__(self):
		pass
	def __del__(self):
		print '释放资源'
	def go(self):
		print 'go'
	def __call__(self):
		print 'call'

f1=Foo()#调用__init__方法
f1.go()
# time.sleep(100)
f1()#默认调用__call__方法
(Foo())
Foo()()