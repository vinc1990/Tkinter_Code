#导入tkinter
import tkinter as tk

#创建顶层窗口并初始化
root = tk.Tk()
root.title('Frame')
root.geometry('200x200')
#创建标签
l = tk.Label(root, text='on the window')
l.pack()
#在root窗口上创建一个框架frm
frm = tk.Frame(root)
frm.pack()
#在frm框架上创建两个frm
frm_l = tk.Frame(frm)
frm_r = tk.Frame(frm)
#frm_l居左，frm_r居右
frm_l.pack(side='left')
frm_r.pack(side='right')
#在两个frm上创建标签
tk.Label(frm_l, text='on the frm_l1').pack()
tk.Label(frm_l, text='on the frm_l2').pack()
tk.Label(frm_r, text='on the frm_r1').pack()
#进入消息循环
root.mainloop()