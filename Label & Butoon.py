#导入tkinter
import tkinter as tk
#定义全局变量，控制显示隐藏
on_hit = True
#定义按钮点击后执行的函数，必须定义在按钮的前面
def hit_me():
	#函数内给全局变量赋值，需要使用global
	global on_hit
	''' 直接改变label的text值
	if on_hit:
		l['text'] = 'you hit me'
		on_hit = False
	else:
		l['text'] = ''
		on_hit = True
	'''
	# 将label的text设置为变量
	if on_hit:
		var.set('you hit me')
		on_hit = False
	else:
		var.set('')
		on_hit = True
#创建顶级窗口
root  = tk.Tk()
#设置窗口标题
root.title('Label & Button')

#使窗口居中显示
#获取屏幕宽
ws = root.winfo_screenwidth()
#获取屏幕高
hs = root.winfo_screenheight()
#计算窗口左上角的点宽和高的偏移量
x = ws/2 - 200/2
y = hs/2 - 100/2
#设置窗口尺寸，格式：长x宽+x偏移量+y偏移量，必须为整数。偏移量指距离屏幕左上角
root.geometry('200x100+%d+%d'% (x, y))

#设置窗口大小是否可变化，mac中一个为True后，均可变
root.resizable(width=False, height=False)
#定义变量，必须在窗口创建完后
var = tk.StringVar()
#创建标签组件
l = tk.Label(root, textvariable=var, background='green', 
			font=('Arial', 12), width=15, height=2)
l.pack()
#创建按钮组件
b = tk.Button(root, text='hit me', width=15, height=2, command=hit_me)
b.pack()
#进入消息循环
root.mainloop()