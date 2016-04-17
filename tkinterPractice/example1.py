import Tkinter as tk
from Tkinter import *
class Application (tk.Frame):
	def __init__(self,master=None):
		tk.Frame.__init__(self,master)
		self.grid()
		self.createWidgets()
		
	def createWidgets(self):
		self.quitButton=tk.Button(self,text='quit',command=self.quit)
		self.quitButton.grid()
		self.checkbut=tk.Checkbutton(self,text='python').grid()
		
app=Application()
app.master.title('sample')
app.mainloop()