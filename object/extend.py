#coding:utf8
#经典类
# class Father:
# 	def __init__(self):
# 		self.Fname='ffff'
# 	def Func(self):
# 		print 'father.funct'

# class Son(Father):
# 	def __init__(self):
# 		self.Fname='ssss'
# 	def bar(self):
# 		print 'son.bar'	
# 	def Func(self):
# 		Father.Func(self)
# 		print '子类重写'

# s1=Son()
# s1.bar()
# s1.Func()

#新式类，任何类是从object继承
class Father(object):
	def __init__(self):
		self.Fname='ffff'
	def Func(self):
		print 'father.funct'

class Son(Father):
	def __init__(self):
		self.Fname='ssss'
	def bar(self):
		print 'son.bar'	
	def Func(self):
		# Father.Func(self)
		super(Son,self).Func(self)#新式类调用
		print '子类重写'

s1=Son()
s1.bar()
s1.Func()