#encoding:utf8
import Tkinter as tk
from Tkinter import *
from fileCheck import startCheck
import tkMessageBox
from tkFileDialog import *
import os
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')


def thanks():
	tkMessageBox.showinfo("about:","作者：kevin\n日期：20160415\n版本：0.1.0\n邮箱：zzkam@126.com")


def choose():
    fileName=""
    fileName=askopenfilename()
    if fileName=="":
        tkMessageBox.showinfo("路径不对！！")
    else:
        path=os.path.dirname(fileName)
        # path2=os.path.dirname(fileName)
        # print path
        # print path2
        # mytext.insert(1.0,text=path)
        mytext_content.set(path)

def getTextPath():
    listbox.delete(0,END)
    retList=[]
    getPath=mytext.get()
    if os.path.isdir(getPath):
        retList=startCheck(getPath)
        for one in retList:
            listbox.insert(END, one)#.decode('utf8').encode('gbk')
    else:
        tkMessageBox.showinfo("路径不对！！")

def processWheel(event):
    if event.delta>0:
        listbox.curselection()
    else:
        listbox.curselection()

def clearTextArea():
    mytext.delete(0, END)
    listbox.delete(0, END)

def delete_selected():
    selected_index=[]
    selected_path=[]
    selected_index=listbox.curselection()
    for i in selected_index:
        selected_path.append(listbox.get(i))
    tkMessageBox.showinfo("以下文件将被删除：\n",selected_path)
    for filePath in selected_path:
        if os.path.isfile(filePath):
            os.remove(filePath)
    tkMessageBox.showinfo("文件删除完毕！！！\n",selected_path)
def select_all():
    listbox.selection_set(0,END)


def unselect_all():
    listbox.selection_clear(0,END)


top=tk.Tk()
top.title('重复文件检测器')
top.geometry("700x300+100+100")
#菜单
menubar=Menu(top)
menubar.add_command(label="选择文件以确定路径(choose)",command=choose)
menubar.add_command(label="退出(quit)",command=top.quit)
menubar.add_command(label="信息(about)",command=thanks)
top.config(menu=menubar)
#一个标签，放入标题和文本框
mainLabel=tk.LabelFrame(top,text='路径：\nPath')
mainLabel.pack(side='top',fill='x')
# #标题标签
# mylabel=tk.Label(mainLabel,text='初始路径：\npath')
# mylabel.pack(side='left',fill='x')
#文本框
mytext_content=StringVar()
mytext=tk.Entry(mainLabel,textvariable=mytext_content)
mytext_content.set("请选择路径：choose")
mytext.pack(side='right',expand='yes', fill='x')
#文本框及拖动条
scrollbar = Scrollbar(mytext)#orient='vertical'
mytext.config(xscrollcommand=scrollbar.set)
scrollbar.config( command = mytext.xview)
scrollbar.pack( side = "right", fill='y')

#第二个标签放入两个按钮
mainLabel2=tk.Label(top)
mainLabel2.pack(side='top',fill='x')
#两个按钮
mybutton_start=Button(mainLabel2,text="开始查询重复文件(start check)",command =getTextPath)
mybutton_clear=Button(mainLabel2,text="清空(clear)",command =clearTextArea)
mybutton_start.pack(side="left",expand='yes',fill='both')
mybutton_clear.pack(side="right",expand='yes',fill='both')

#第三个标签LabelFrame
mainLabel3=tk.LabelFrame(top,text="查询结果：\nResult")
mainLabel3.pack(side='top',expand='yes',fill='both')
#添加列表框
listbox=tk.Listbox(mainLabel3,selectmode='multiple')
listbox.bind("<MouseWheel>", processWheel)
listbox.pack(side='top',expand='yes',fill='both')
listbox.insert(END, "重复文件将以如下方式列出：")
for item in ["文件及路径1.。。", "文件及路径2.。。", "文件及路径3.。。"]:
	listbox.insert(END, item)
#列表框和拖动条
scrollbar2 = Scrollbar(listbox)#orient='vertical'
listbox.config(yscrollcommand=scrollbar2.set)
scrollbar2.config( command = listbox.yview)
scrollbar2.pack( side = "right", fill='y')
#三个按钮
mybutton_del=Button(mainLabel3,text="删除(delete)",command =delete_selected)
mybutton_all=Button(mainLabel3,text="全选(select_all)",command =select_all)
mybutton_unall=Button(mainLabel3,text="反选(unselect_all)",command =unselect_all)
mybutton_del.pack(side="left",expand='yes',fill='x')
mybutton_all.pack(side="right",expand='yes',fill='x')
mybutton_unall.pack(side="right",expand='yes',fill='x')

tk.mainloop()