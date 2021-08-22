import tkinter as tk
import tkinter.ttk as ttk
import threading
import time

def test():
    for i in range(10):
        print(threading.current_thread().name+' test ',i)
        time.sleep(1)
    pb_hD.stop()

def run():
    pb_hD.start()
    # global thread
    thread = threading.Thread(target=test,name='TestThread')
    thread.start()


root = tk.Tk()
root.geometry('200x50')
# ft = ttk.Frame(height=30,width=30)
# ft.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
pb_hD = ttk.Progressbar(orient='horizontal', mode='indeterminate')
pb_hD.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
bt =ttk.Button(root,text='开始',command=run).pack()
root.mainloop()    