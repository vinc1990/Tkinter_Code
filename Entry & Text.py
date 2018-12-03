#导入tkinter
import tkinter as tk

#创建顶层窗口并初始化
root = tk.Tk()
root.title('Entry & Text')
root.geometry('200x200')

#创建输入框，show属性可以指定显示字符
e = tk.Entry(root, show=None)
e.pack()

#insert point按钮执行函数
def insert_point():
	#获取输入框的内容
	var = e.get()
	#插入到文本框中，insert插入到光标处
	t.insert('insert', var)

#inset end按钮的执行函数
def insert_end():
	#获取输入框的内容
	var = e.get()
	#插入到文本框中，end插入到文末
	t.insert('end', var)
#创建按钮insert point
b1 = tk.Button(root, text='insert point', command=insert_point)
b1.pack()
#创建按钮insert end
b2 = tk.Button(root, text='insert end', command=insert_end)
b2.pack()
#创建文本框
t = tk.Text(root, height=2)
t.pack()
#进入消息循环
root.mainloop()