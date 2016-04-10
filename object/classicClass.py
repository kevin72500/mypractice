#coding:utf8
class grandFather():
	def __init__(self):
		print 'grand father init'
	def save(self):
		print 'save from grand father'

class father(grandFather):
	def __init__(self):
		print 'father init'
	def save(self):
		print 'save from father'

class stepfather(grandFather):
	def __init__(self):
		print 'step father init'
	# def save(self):
	# 	print 'save from step father'

class son(stepfather,father):
	def __init__(self):
		print 'this is son'

s=son()
s.save()
#添加object到grandfather(object)

# output###########
# this is son
# save from grand father