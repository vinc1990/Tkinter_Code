#导入tkinter
import tkinter as tk
from tkinter import messagebox

#创建顶层窗口并初始化
root = tk.Tk()
root.title('messagebox')
root.geometry('200x200')

#按钮点击执行函数
def hit_me():
	#messagebox.showinfo(title='Hi', message='hahahaha')
	#messagebox.showerror(title='Hi', message='hahahaha')
	#messagebox.showwarning(title='Hi', message='hahahaha')
	#返回‘yes’ ‘no’
	#print(messagebox.askquestion(title='Hi', message='hahahaha'))
	#返回 True False
	#print(messagebox.askokcancel(title='Hi', message='hahahaha'))
	#返回 True False
	#print(messagebox.askretrycancel(title='Hi', message='hahahaha'))
	#返回 True False
	print(messagebox.askyesno(title='Hi', message='hahahaha'))

#创建按钮
tk.Button(root, text='hit me', command=hit_me).pack()

#进入消息循环
root.mainloop()