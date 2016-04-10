#coding:utf-8
recordHand=open('C:\\Users\\oupeng\\Desktop\\recorded.txt','r')
importHand=open('C:\\Users\\oupeng\\Desktop\\imported.txt','r')
rbuffer=recordHand.readlines()
ibuffer=importHand.readlines()

for rone in rbuffer:
	if rone in ibuffer:
		continue
	else:
		print rone,

print "\n###########################"
for ione in ibuffer:
	if ione in rbuffer:
		continue
	else:
		print ione,


