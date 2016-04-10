# from abc import ABCMeta, abstractmethod
class Alert:
	# __metaclass__ = ABCMeta
	@abstractmethod
	def send(self):
		pass

class Foo(Alert):
	def __init__(self):
		print 'init '

	def send(self):
		print 'send'
try:
	f1=Foo()
	f1.send()
except Exception, e:
	print 1,e