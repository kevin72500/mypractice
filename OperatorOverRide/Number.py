# class Number:
# 	def __init__(self,start):
# 		self.data=start
# 	def __sub__(self,other):
# 		return Number(self.data-other)

# x=Number(5)
# y=x-2
# print y.data








# class Indexer:
# 	def __getitem__(self,index):
# 		return index **2

# x=Indexer()
# print x[2]

# for i in range(5):
# 	print x[i],






class Indexer:
	data=[4,5,6,7,8]
	def __getitem__(self,index):
		print ('getitem:', index)
		return self.data[index]
x=Indexer()
for i in range(5):
	print x[i]