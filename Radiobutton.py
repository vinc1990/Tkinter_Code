#导入tkinter
import tkinter as tk

#创建顶层窗口并初始化
root = tk.Tk()
root.title('Radiobutton')
root.geometry('200x200')
#创建标签
l = tk.Label(root, width=20, bg='yellow')
l.pack()

#print selection按钮执行函数
def print_selection():
	l.config(text='you have selected ' + var.get())

var = tk.StringVar()
#设置变量默认值为None
#var.set(None)
#创建单选按钮A
r1 = tk.Radiobutton(root, text='Option A', variable=var, value='A',
					command=print_selection)
r1.pack()
#创建单选按钮B
r2 = tk.Radiobutton(root, text='Option B', variable=var, value='B',
					command=print_selection)
r2.pack()
#创建单选按钮C
r3 = tk.Radiobutton(root, text='Option C', variable=var, value='C',
					command=print_selection)
r3.pack()
#进入消息循环
root.mainloop()