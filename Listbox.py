#导入tkinter
import tkinter as tk

#创建顶层窗口并初始化
root = tk.Tk()
root.title('Listbox')
root.geometry('200x200')

#定义变量
var1 = tk.StringVar()
#创建标签，并将textvariable设置为var1
l = tk.Label(root, width=5, bg='yellow', textvariable=var1)
l.pack()

#print selection按钮执行函数
def print_selection():
	#获取列表光标选中的内容
	value = lb.get(lb.curselection())
	#在标签中显示选中的内容
	var1.set(value)

#创建按钮print selection
b1 = tk.Button(root, text='print selection', command=print_selection)
b1.pack()

var2 = tk.StringVar()
var2.set([111, 222, 333, 444])
#创建列表框并赋值
lb = tk.Listbox(root, listvariable=var2)
lb.pack()
#在列表框的末尾插入内容
list_items = [1, 2, 3]
for item in list_items:
	lb.insert('end', item)
#在列表框的第一位插入first
lb.insert(0, 'first')
#在列表框的第二位插入second
lb.insert(1, 'second')
#删除列表框第三位的值，也就是111
lb.delete(2)
lb.pack()

#进入消息循环
root.mainloop()