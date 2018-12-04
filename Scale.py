#导入tkinter
import tkinter as tk

#创建顶层窗口并初始化
root = tk.Tk()
root.title('Scale')
root.geometry('200x200')

#创建标签
l = tk.Label(root, bg='yellow', width=20)
l.pack()

#比例尺滑动时执行的函数，滑动时会自动传入当前值
def print_selection(v):
    l['text'] = 'you have selected ' + v

#创建比例尺
#from_：最小值 to：最大值
#orient=tk.HORIZONTAL 设置比例尺方向 HORIZONTAL：水平方向  VERTICAL:竖直方向
#length 长度 与width不一样，width是字符单位 length是像素单位
#showvalue 0：不显示当前值 1：在上方显示当前值
#tickinterval 坐标间隔
#resolution 精度
s = tk.Scale(root, label='try me', from_=5, to=11, orient=tk.HORIZONTAL,
             length=200, showvalue=0, tickinterval=2, resolution=0.01, command=print_selection)
s.pack()

#进入消息循环
root.mainloop()
