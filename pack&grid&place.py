#导入tkinter
import tkinter as tk

#创建顶层窗口并初始化
root = tk.Tk()
root.title('messagebox')
root.geometry('200x200')

#pack

# tk.Label(root, text='1').pack(side='top')
# tk.Label(root, text='1').pack(side='bottom')
# tk.Label(root, text='1').pack(side='left')
# tk.Label(root, text='1').pack(side='right')

#grid
# for i in range(4):
# 	for j in range(3):
# 		tk.Label(root, text='1').grid(row=i, column=j, padx=10, pady=10)

#place
tk.Label(root, text='1').place(x=10, y=100, anchor='nw')
#进入消息循环
root.mainloop()