import tkinter as tk
from tkinter import messagebox
import pickle

root = tk.Tk()
root.title('登录')
root.geometry('450x300')
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
			sign_up()

def sign_up():
	pass

btn_login = tk.Button(root, text='登录', command=login, width=8)
btn_login.place(x=170, y=250, anchor='center')
btn_sign_up = tk.Button(root, text='注册', command=sign_up, width=8)
btn_sign_up.place(x=290, y=250, anchor='center')
root.mainloop()