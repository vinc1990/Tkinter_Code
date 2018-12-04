#导入tkinter
import tkinter as tk

#创建顶层窗口并初始化
root = tk.Tk()
root.title('Checkbutton')
root.geometry('200x200')

#创建标签
l = tk.Label(root, bg='yellow', width=20)
l.pack()

#勾选时执行的函数
def print_selection():
	if var1.get()==1 and var2.get()==0:
		l['text'] = 'I love only python'
	elif var1.get()==0 and var2.get()==1:
		l['text'] = 'I love only java'
	elif var1.get()==0 and var2.get()==0:
		l['text'] = 'I don\'t love either'
	else:
		l['text'] = 'I love both'
#创建多选按钮
#勾选时将onvalue的值赋给var1，取消勾选时，将offvalue的值赋给var1
var1 = tk.IntVar()
c1 = tk.Checkbutton(root, text='Python', variable=var1, onvalue=1, offvalue=0, command=print_selection)
c1.pack()
#创建多选按钮
#勾选时将onvalue的值赋给var2，取消勾选时，将offvalue的值赋给var2
var2 = tk.IntVar()
c2 = tk.Checkbutton(root, text='Java', variable=var2, onvalue=1, offvalue=0, command=print_selection)
c2.pack()

#进入消息循环
root.mainloop()
