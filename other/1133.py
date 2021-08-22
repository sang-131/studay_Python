from PySide2 import QtWidgets
import sys


class App(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        file_menu = QtWidgets.QMenuBar(self) # 实例化一个菜单栏
        file_menu.setFixedWidth(200) # 设置菜单栏的宽度
        file_menu.addMenu("文件") # 添加一个菜单按钮
        file_menu.addMenu("编辑") # 添加一个菜单按钮
        file_menu.addMenu("关于") # 添加一个菜单按钮
        view_toolbar = self.addToolBar("View")
        view_toolbar.addAction("打开")
        view_toolbar.addAction("保存")
        view_toolbar.addAction("撤回")
        status = self.statusBar()
        status.showMessage("这是一个状态栏消息")
        main_widget = QtWidgets.QWidget() # 实例化一个widget控件
        main_layout = QtWidgets.QHBoxLayout() # 实例化一个水平布局层
        main_widget.setLayout(main_layout) # 设置widget控件布局为水平布局
        # 实例化3个按钮
        button_1 = QtWidgets.QPushButton('按钮一')
        button_2 = QtWidgets.QPushButton('按钮二')
        button_3 = QtWidgets.QPushButton('按钮三')
        # 将按钮添加到水平布局中
        main_layout.addWidget(button_1)
        main_layout.addWidget(button_2)
        main_layout.addWidget(button_3)

        self.setCentralWidget(main_widget) # 设置窗口的中央部件
        

def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = App()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()