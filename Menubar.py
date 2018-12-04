#导入tkinter
import tkinter as tk

#创建顶层窗口并初始化
root = tk.Tk()
root.title('Menubar')
root.geometry('200x200')
#创建标签
l = tk.Label(root, width=20, bg='yellow')
l.pack()
#点击菜单执行的函数，每次点击counter加1
counter = 0
def do_job():
	global counter
	l.config(text='do' + str(counter))
	counter += 1
#创建一个菜单栏
menubar = tk.Menu(root)
#在菜单栏上创建一个空菜单，tearoff=0菜单不可以独立，为1时可以独立，会出现一个横线
filemenu = tk.Menu(menubar, tearoff=0)
#将空菜单命名为'File',放入菜单栏中
menubar.add_cascade(label='File', menu=filemenu)
#在File中加入子菜单，点击后触发do_job函数
filemenu.add_command(label='New',command=do_job)
filemenu.add_command(label='Open',command=do_job)
filemenu.add_command(label='Save',command=do_job)
filemenu.add_command(label='Save as',command=do_job)
#分割线
filemenu.add_separator()
filemenu.add_command(label='Exit',command=root.quit)

submenu = tk.Menu(filemenu, tearoff=0)
filemenu.add_cascade(label='Import', menu=submenu)
submenu.add_command(label='Submenu1', command=do_job)

root.config(menu=menubar)
#进入消息循环
root.mainloop()
