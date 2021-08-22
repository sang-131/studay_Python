#这是系统的登录界面
import tkinter
from tkinter import messagebox



class Login(object):
	def __init__(self):
		# 创建主窗口,用于容纳其它组件
		self.root = tkinter.Tk()
		# 给主窗口设置标题内容
		self.root.title("测试系统")
		self.root.geometry('700x400')
		#运行代码时记得添加一个gif图片文件，不然是会出错的
		# self.canvas = tkinter.Canvas(self.root, height=400, width=700)#创建画布
		# self.image_file = tkinter.PhotoImage(file="D:\图片\Twitter-GIF.gif")#加载图片文件
		# self.image = self.canvas.create_image(0,0, anchor='nw', image=self.image_file)#将图片置于画布上
		# self.canvas.pack(side='top')#放置画布（为上端）
		self.frame_output1 = tkinter.Frame(self.root,bd=5,bg='Ivory',height=50,width=300,relief='ridge')
		self.frame_labe1 = tkinter.Label(self.frame_output1,text='输 出 窗 口',bd=5,height=1,width=50,relief='groove')
		self.frame_text1 = tkinter.Text(self.frame_output1,bd=5,bg='Khaki',height=100,width=50)
		self.frame_func1 = tkinter.Frame(self.root,bd=3,bg='lightblue',height=50,width=300,relief='ridge')
		self.frame_labe2 = tkinter.Label(self.frame_func1,text='功 能 区 域',bd=5,height=1,width=100,relief='groove')
		# self.frame_btn1 = ttk.Button(self.frame_func1,-bd=3,bg='blue',height=1,width=20)
		# self.frame_btn2 = ttk.Button(self.frame_func1,-bd=3,bg='blue',height=1,width=20)
		# self.frame_btn3 = ttk.Button(self.frame_func1,-bd=3,bg='blue',height=1,width=20)
		# self.frame_btn4 = ttk.Button(self.frame_func1,-bd=3,bg='blue',height=1,width=20)
		self.frame_btn1 = tkinter.Button(self.frame_func1,width=20,text='当日报表准备',)
		self.frame_btn2 = tkinter.Button(self.frame_func1,width=20)
		self.frame_btn3 = tkinter.Button(self.frame_func1,width=20)
		self.frame_btn4 = tkinter.Button(self.frame_func1,width=20)
		self.frame_btn5 = tkinter.Button(self.frame_func1,height=1,width=20)
		self.frame_btn6 = tkinter.Button(self.frame_func1,height=1,width=20)
		self.frame_btn7 = tkinter.Button(self.frame_func1,height=1,width=20)

	# 完成布局
	def gui_arrang(self):
		self.frame_output1.pack(side='left',fill='both',expand=True)
		self.frame_labe1.pack(side='top',fill='x')
		self.frame_text1.pack(side='top',fill='x')
		self.frame_func1.pack(side='right',fill='y')
		self.frame_labe2.pack()
		self.frame_btn1.place(x=30,y=30)
		self.frame_btn2.place(x=30,y=80)
		self.frame_btn3.place(x=30,y=130)
		self.frame_btn4.place(x=30,y=180)
		self.frame_btn5.place(x=30,y=230)
		self.frame_btn6.place(x=30,y=280)
		self.frame_btn7.place(x=30,y=330)



def main():
	# 初始化对象
	L = Login()
	# 进行布局
	L.gui_arrang()
	# 主程序执行
	tkinter.mainloop()


if __name__ == '__main__':
	main()

