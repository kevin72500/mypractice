#coding:utf-8
recordHand=open('C:\\Users\\oupeng\\Desktop\\car.txt','r')
importHand=open('C:\\Users\\oupeng\\Desktop\\car.txt','r')
rbuffer=recordHand.readlines()
ibuffer=importHand.readlines()

setr=set(rbuffer)
seti=set(ibuffer)

print len(setr & seti)
print len(setr - seti)

# for rone in rbuffer:
# 	if rone in ibuffer:
# 		continue
# 	else:
# 		print rone,




