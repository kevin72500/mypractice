class Squares:
	def __init__(self,start,stop):
		self.value=start-1
		self.stop=stop
	def __iter__(self):
		return self
	def __next__(self):
		if self.value==self.stop:
			raise StopIteration
		self.value+=1
		return self.value **2

# from iters import Squares
# for i in Squares(1,5):
# 	print i,

x=Squares(1,5)
print [n for n in x]