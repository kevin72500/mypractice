#coding:utf-8
'''測試'''

# def outer(fun):
# 	def warpper():
# 		print "驗證"
# 		fun()
# 		print "檢查\n"
# 	return warpper

# @outer
# def func1():
# 	print 'func1', 


# func1()
#################裝飾器 帶 參數 ######################

# def outer(fun):
# 	def warpper(arg):
# 		print "驗證"
# 		fun(arg)
# 		print "檢查\n"
# 	return warpper

# @outer
# def func1(arg):
# 	print 'func1', arg



# func1("參數")

#################裝飾器 帶 參數 返回值######################

def outer(fun):
	def warpper(arg):
		print "驗證"#包裝
		ret=fun(arg)#加參數
		print "檢查\n"
		return ret #返回原返回值
	return warpper

@outer
def func1(arg):
	print 'func1', arg
	return "返回值"
	


a=func1("參數")
print a
