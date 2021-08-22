# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 10:34:10 2018
@author: Administrator
"""
import tkinter as tk
import tkinter.messagebox
import pickle

# 窗口
window = tk.Tk()
window.title('欢迎进入报表辅助系统')
window.geometry('400x500')
window.resizable(False,False)
# 画布放置图片
canvas = tk.Canvas(window, height=600, width=600)
imagefile = tk.PhotoImage(file=r'D:\文档\python_code\工作\bg1.png',)
image = canvas.create_image(0, 0, anchor='nw', image=imagefile)
canvas.pack(side='top')
# 标签 用户名密码
tk.Label(window, text='用户名:').place(x=100, y=150)
tk.Label(window, text='密  码:').place(x=100, y=190)
# 用户名输入框
var_usr_name = tk.StringVar()
entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
entry_usr_name.place(x=160, y=150)
# 密码输入框
var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
entry_usr_pwd.place(x=160, y=190)


# 登录函数
def usr_log_in():
    # 输入框获取用户名密码
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    # 从本地字典获取用户信息，如果没有则新建本地数据库
    try:
        with open('usr_info.pickle', 'rb') as usr_file:
            usrs_info = pickle.load(usr_file)
    except FileNotFoundError:
        with open('usr_info.pickle', 'wb') as usr_file:
            usrs_info = {'admin': 'admin'}
            pickle.dump(usrs_info, usr_file)
    # 判断用户名和密码是否匹配
    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            tk.messagebox.showinfo(title='welcome',message='欢迎您：' + usr_name)
            #window.destroy()
            info_o = tk.Toplevel(window)
            info_o.geometry('350x200')
            info_o.title('注册')
            window.destroy()
            func_part()
        else:
            tk.messagebox.showerror(message='密码错误')
    # 用户名密码不能为空
    elif usr_name == '' or usr_pwd == '':
        tk.messagebox.showerror(message='用户名或密码为空')
    # 不在数据库中弹出是否注册的框
    else:
        is_signup = tk.messagebox.askyesno('欢迎', '您还没有注册，是否现在注册')
        if is_signup:
            usr_sign_up()
    
# 注册函数
def usr_sign_up():
    # 确认注册时的相应函数
    def signtowcg():
        # 获取输入框内的内容
        nn = new_name.get()
        np = new_pwd.get()
        npf = new_pwd_confirm.get()

        # 本地加载已有用户信息,如果没有则已有用户信息为空
        try:
            with open('usr_info.pickle', 'rb') as usr_file:
                exist_usr_info = pickle.load(usr_file)
        except FileNotFoundError:
            exist_usr_info = {}

            # 检查用户名存在、密码为空、密码前后不一致
        if nn in exist_usr_info:
            tk.messagebox.showerror('错误', '用户名已存在')
        elif np == '' or nn == '':
            tk.messagebox.showerror('错误', '用户名或密码为空')
        elif np != npf:
            tk.messagebox.showerror('错误', '密码前后不一致')
        # 注册信息没有问题则将用户名密码写入数据库
        else:
            exist_usr_info[nn] = np
            with open('usr_info.pickle', 'wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)
            tk.messagebox.showinfo('欢迎', '注册成功')
            # 注册成功关闭注册框
            window_sign_up.destroy()
        

    # 新建注册界面
    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('350x200')
    window_sign_up.title('注册')
    # 用户名变量及标签、输入框
    new_name = tk.StringVar()
    tk.Label(window_sign_up, text='用户名：').place(x=10, y=10)
    tk.Entry(window_sign_up, textvariable=new_name).place(x=150, y=10)
    # 密码变量及标签、输入框
    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='请输入密码：').place(x=10, y=50)
    tk.Entry(window_sign_up, textvariable=new_pwd, show='*').place(x=150, y=50)
    # 重复密码变量及标签、输入框
    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='请再次输入密码：').place(x=10, y=90)
    tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*').place(x=150, y=90)
    # 确认注册按钮及位置
    bt_confirm_sign_up = tk.Button(window_sign_up, text='确认注册',
                                   command=signtowcg)
    bt_confirm_sign_up.place(x=150, y=130)


# 退出的函数
def usr_sign_quit():
    window.destroy()

# 登录 注册按钮
bt_login = tk.Button(window, text='登录', command=usr_log_in)
bt_login.place(x=140, y=230)
bt_logup = tk.Button(window, text='注册', command=usr_sign_up)
bt_logup.place(x=210, y=230)
bt_logquit = tk.Button(window, text='退出', command=usr_sign_quit)
bt_logquit.place(x=280, y=230)

#操作界面
def func_part():
    root = tk.Tk()
    # 给主窗口设置标题内容
    root.title("报表辅助系统")
    root.geometry('700x400')
    #运行代码时记得添加一个gif图片文件，不然是会出错的
    # canvas = tk.Canvas(root, height=400, width=700)#创建画布
    # image_file = tk.PhotoImage(file="D:\图片\Twitter-GIF.gif")#加载图片文件
    # image = canvas.create_image(0,0, anchor='nw', image=image_file)#将图片置于画布上
    # canvas.grid(row=0,column=0)#放置画布（为上端）
    frame_output1 = tk.Frame(root,bd=3,bg='Ivory',height=50,width=100,relief='ridge')
    frame_labe1 = tk.Label(frame_output1,text='输 出 窗 口',bd=3,width=50,relief='groove')
    frame_text1 = tk.Text(frame_output1,bd=3,bg='Khaki',height=50,width=50)
    frame_func1 = tk.Frame(root,bd=3,bg='lightblue',height=100,width=50,relief='ridge')
    frame_labe2 = tk.Label(frame_func1,text='功 能 区 域',bd=3,width=50,relief='groove')
    frame_btn1 = tk.Button(frame_func1,width=20,text='当日报表准备',)
    frame_btn2 = tk.Button(frame_func1,width=20,text='提取当日数据')
    frame_btn3 = tk.Button(frame_func1,width=20,text='凭证/报表录入辅助')
    frame_btn4 = tk.Button(frame_func1,width=20,text='应收表比对')
    frame_btn5 = tk.Button(frame_func1,width=20,text='应收表/简报制作')
    frame_btn6 = tk.Button(frame_func1,width=20)
    frame_btn7 = tk.Button(frame_func1,width=20)
# 完成布局
    frame_output1.grid(row=0,column=0,sticky=tk.NSEW)
    frame_labe1.grid(row=0,column=0,sticky=tk.NS)
    frame_text1.grid(row=1,column=0,sticky=tk.NS)
    frame_func1.grid(row=0,column=1,sticky=tk.NSEW)
    frame_labe2.grid(row=0,column=0,sticky=tk.NS)
    frame_btn1.grid(row=1,column=0,pady=10)
    frame_btn2.grid(row=2,column=0,pady=10)
    frame_btn3.grid(row=3,column=0,pady=10)
    frame_btn4.grid(row=4,column=0,pady=10)
    frame_btn5.grid(row=5,column=0,pady=10)
    frame_btn6.grid(row=6,column=0,pady=10)
    frame_btn7.grid(row=7,column=0,pady=10)
# 主循环
window.mainloop()
