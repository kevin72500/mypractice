# encoding:utf8
import os


def startCheck(path):
    # path=raw_input("请输入需要开始的路径：").strip()

    #更改路径
    os.chdir(path)
    #获取当前路径
    path = os.getcwd()
    #遍历路径
    record = os.walk(path)
    #所有路径
    allpath = []
    #前缀路径集合
    prePathList = []
    #文件集合
    fileList = []
    #重复文件列表
    dupFileList = []
    #排序后重复文件下标列表
    dupFileListIndex=[]

    #获取文件路径，子目录，文件名
    for dirpath, subdir, filenames in record:
        #琢一添加文件名
        for oneFile in filenames:
            #填加集合列表
            allpath.append(dirpath + os.path.sep + oneFile)#文件全路径
            prePathList.append(dirpath)#文件前置路径
            fileList.append(oneFile)#文件名

    # uniqList=set(fileList)

    #添加重复文件到重复文件列表
    for index, fileName in enumerate(fileList):
    	# a 查找重复数据并输出
    	# if fileList.count(fileName) > 1:
    	# 	dupFileList.append(allpath[index])
    	# b 查找重复数据 ，并排序输出
        if fileList.count(fileName) > 1:
            dupIndex=[i for i,v in enumerate(fileList) if fileName == fileList[i]]
            for i in dupIndex:
	            if i not in dupFileListIndex:
	            	dupFileListIndex.append(i)

    for index in dupFileListIndex:
    	print unicode(allpath[index],'gbk')
    	dupFileList.append(allpath[index])
    return dupFileList

if __name__ == '__main__':
    path = raw_input("请输入需要开始的路径：").strip()
    startCheck(path="C:/Users/oupeng/Desktop/ptest/test_git/mypractice")
