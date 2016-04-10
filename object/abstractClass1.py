from abc import ABCMeta, abstractmethod
class Alert:
	__metaclass__ = ABCMeta
	@abstractmethod
	def send(self):
		pass

class Foo(Alert):
	def __init__(self):
		print 'init '

	def send(self):
		print 'send'

f=Foo()
f.send()