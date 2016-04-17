#encoding:utf8
import sys
aList=["你们","cc","你妹","aa","bb"]
for a in aList:
	print type(a)
	a=a.decode('UTF-8').encode('gbk') 
	print type(a)
	print "".join(a)