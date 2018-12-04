#导入tkinter
import tkinter as tk

#创建顶层窗口并初始化
root = tk.Tk()
root.title('Canvas')
root.geometry('200x200')

#创建画布
canvas = tk.Canvas(root, bg='blue', width=200, height=100)
canvas.pack()

#定义存放ins.gif的变量
image_file = tk.PhotoImage(file='ins.gif')
#在画布上创建图片，10 10为顶点坐标，anchor将图片左上角作为锚点
image = canvas.create_image(10, 10, anchor='nw', image=image_file)

#定义一个点
x0, y0, x1, y1 = 50, 50, 80, 100
#在画布上画一条直线从（x0,y0)到（x1,y1)
line = canvas.create_line(x0, y0, x1, y1)

#在画布上创建椭圆，椭圆为以(x0,y0)(x1,y1)为顶点的矩形的内切椭圆
oval = canvas.create_oval(x0, y0, x1, y1, fill='red')
#在画布上创建扇形，原理与椭圆相同
arc = canvas.create_arc(x0+40, y0+20, x1+60, y1+30, start=0, extent=180, fill='green')
#在画布上创建矩形，两个对角顶点
rect = canvas.create_rectangle(100, 30, 100+30, 30+20, fill='orange')
#点击按钮执行的函数，矩形每次下移2个单位，横向不变
def moveit():
    canvas.move(rect, 0, 2)
#创建按钮
b = tk.Button(root, text='move', command=moveit)
b.pack()
#进入消息循环
root.mainloop()
