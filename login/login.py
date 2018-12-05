import tkinter as tk
from tkinter import messagebox
import pickle

root = tk.Tk()
root.title('登录')
ws = root.winfo_screenwidth()
#获取屏幕高
hs = root.winfo_screenheight()
#计算窗口左上角的点宽和高的偏移量
x = ws/2 - 450/2
y = hs/2 - 300/2
#设置窗口尺寸，格式：长x宽+x偏移量+y偏移量，必须为整数。偏移量指距离屏幕左上角
root.geometry('450x300+%d+%d'% (x, y))
root.resizable(False, False)

canvas = tk.Canvas(root, width=450, height=200)
canvas.pack(side='top')
image_file = tk.PhotoImage(file='welcome.gif')
image = canvas.create_image(10, 0, anchor='nw', image=image_file)

tk.Label(root, text='用户名：').place(x=100, y=170, anchor='center')
tk.Label(root, text='密码：').place(x=106, y=210, anchor='center')

var_username = tk.StringVar()
var_username.set('example@python.com')
entry_username = tk.Entry(root, textvariable=var_username, width=25)
entry_username.place(x=250, y=170, anchor='center')

var_password = tk.StringVar()
entry_password = tk.Entry(root, textvariable=var_password, show='*', width=25)
entry_password.place(x=250, y=210, anchor='center')

def login():
	username = var_username.get()
	password = var_password.get()

	try:
		with open('user_info.pickle', 'rb') as user_file:
			user_info = pickle.load(user_file)
	except FileNotFoundError:
		with open('user_info.pickle', 'wb') as user_file:
			user_info = {'admin': 'admin'}
			pickle.dump(user_info, user_file)

	if username in user_info:
		if password == user_info[username]:
			messagebox.showinfo(title='登录成功', message='欢迎回来！' + username)
		else:
			messagebox.showerror(message='您的密码错误，请重新输入！')
	else:
		is_sign_up = messagebox.askyesno('注册','您的用户名不存在，是否现在注册？')
		if is_sign_up:
			window_sign_up()
			

def window_sign_up():
	def sign_up():
		np = new_pwd.get()
		npf = new_pwd_confirm.get()
		nn = new_name.get()
		with open('user_info.pickle', 'rb') as usr_file:
			exist_usr_info = pickle.load(usr_file)
		if not(nn and np):
			messagebox.showerror('错误', '用户名和密码不能为空！')
		elif np != npf:
			messagebox.showerror('错误', '您两次输入的密码不一致，请重新输入！')
		elif nn in exist_usr_info:
			messagebox.showerror('错误', '用户名已经存在，请重新输入！')
		else:
			exist_usr_info[nn] = np
			with open('user_info.pickle', 'wb') as usr_file:
				pickle.dump(exist_usr_info, usr_file)
			messagebox.showinfo('恭喜', '注册成功！')
			root_sign_up.destroy()
	root_sign_up = tk.Toplevel(root)
	root_sign_up.title('注册')
	ws = root.winfo_screenwidth()
	#获取屏幕高
	hs = root.winfo_screenheight()
	#计算窗口左上角的点宽和高的偏移量
	x = ws/2 - 350/2
	y = hs/2 - 200/2
	#设置窗口尺寸，格式：长x宽+x偏移量+y偏移量，必须为整数。偏移量指距离屏幕左上角
	root_sign_up.geometry('350x200+%d+%d'% (x, y))
	root_sign_up.resizable(False, False)
	
	tk.Label(root_sign_up, text='用户名：').place(x=62, y=40, anchor='center')
	tk.Label(root_sign_up, text='密码：').place(x=68, y=80, anchor='center')
	tk.Label(root_sign_up, text='确认密码：').place(x=55, y=120, anchor='center')
        
	new_name = tk.StringVar()
	new_name.set('example@python.com')
	entry_new_name = tk.Entry(root_sign_up, textvariable=new_name, width=25)
	entry_new_name.place(x=205, y=40, anchor='center')

	new_pwd = tk.StringVar()
	entry_new_pwd = tk.Entry(root_sign_up, textvariable=new_pwd, show='*', width=25)
	entry_new_pwd.place(x=205, y=80, anchor='center')

	new_pwd_confirm = tk.StringVar()
	entry_new_pwd_confirm = tk.Entry(root_sign_up, textvariable=new_pwd_confirm, show='*', width=25)
	entry_new_pwd_confirm.place(x=205, y=120, anchor='center')
	
	btn_comfirm_sign_up = tk.Button(root_sign_up, text='注册', width=8, command=sign_up)
	btn_comfirm_sign_up.place(x=140, y=140)

btn_login = tk.Button(root, text='登录', command=login, width=8)
btn_login.place(x=170, y=250, anchor='center')
btn_sign_up = tk.Button(root, text='注册', command=window_sign_up, width=8)
btn_sign_up.place(x=290, y=250, anchor='center')
root.mainloop()
