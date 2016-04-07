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

	memo='中國23個省之一'#实例和类

	def __init__(self,name,capital,leader,flag=False):
		self.name=name
		self.capital=capital
		self.leader=leader

		self.__Thailand=flag #私有字段

	def sorts_meet(self):
		print self.name+"开运动会"

	@staticmethod#属于实例和类
	def Foo():
		print '每个省都反腐'

	@property #属于实例
	def getProp(self):
		return "test"

	def show(self):
		print self.__Thailand

	@property#调用私有变量
	def getPrivateVari(self):
		return self.show()

	def __privMethod(self):#私有方法
		print "我是私有的"

	@property#调用私有方法
	def getPrivateMeth(self):
		return self.__privMethod()

hb=Province("河北","石家莊","李洋")
# sd=Province("山東","濟南","孔子")
japan=Province("日本","九州","山本",True)
japan.show()
japan.getPrivateVari
japan.getPrivateMeth
japan._Province__privMethod()#直接调用私有方法
# print hb.capital
# hb.sorts_meet()
# print hb.memo
# hb.Foo()
# print hb.getProp
# print ("\n")

# print Province.memo
# Province.Foo()
#靜態類不嗯給你訪問靜態字段
# print Province.name
