#coding:utf-8

# class Alex:
	
# 	xx='沒心沒肺'

# class Person:
	
# 	xue='血'

# 	def __init__(self,name):
# 		self.name=name



# p1=Person("李洋")
# print p1.name
# p2=Person("老狗")
# print p2.name


class Province:

	memo='中國23個省之一'

	def __init__(self,name,capital,leader):
		self.name=name
		self.capital=capital
		self.leader=leader

	def sorts_meet(self):
		print self.name+"开运动会"

	@staticmethod
	def Foo():
		print '每个省都反腐'

	@property
	def getProp(self):
		return "test"

hb=Province("河北","石家莊","李洋")
# sd=Province("山東","濟南","孔子")

print hb.capital
hb.sorts_meet()
print hb.memo
hb.Foo()
hb.getProp
Province.getProp
print ("\n")

print Province.memo
Province.Foo()
#靜態類不嗯給你訪問靜態字段
# print Province.name
