# -*- conding:utf8 -*-
'''
 input like xxx/xxx
 get done and success
'''
# getOper=raw_input("input")
# getArr=getOper.split('/')
# package=__import__(getArr[0])
# # pack2=__import__(package)
# func=getattr(package,getArr[1])
# func()

'''
 input like xxx/xxx/xxx
 no success
'''
getOper=raw_input("input")
each=getOper.split('/')
package=__import__(each[0]+"."+each[1])
# pack2=__import__(package)
func=getattr(package,each[2])
func()