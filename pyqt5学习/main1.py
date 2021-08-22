from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget,QFileDialog
from UI_layout_demo_LayoutManage import Ui_MainWindow
import sys
class LayoutDemo(QMainWindow,Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self,parent=None):
        """
        Constructor
        @param parent reference to the parent widget
        @type Qwidget
        """
        super(LayoutDemo,self).__init__(parent)
        self.setupUi(self)
        self.fileCloseAction.triggered.connect(self.close)
        self.fileOpenAction.triggered.connect(self.openMsg)
    def openMsg(self):
        file,ok = QFileDialog.getOpenFileName(self,'打开','c:/','All Files(*);;Text Files(*.txt)')
        self.statusbar.showMessage(file)


    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        print('收益_min:',self.doubleSpinBox_returns_min.text())
        print('收益_max:',self.doubleSpinBox_returns_max.text())
        print('最大回撤_min:',self.doubleSpinBox_maxdrawdown_min.text())
        print('最大回撤_max:',self.doubleSpinBox_maxdrawdown_max.text())
        print('sharp_min:',self.doubleSpinBox_sharp_min.text())
        print('sharp_max:',self.doubleSpinBox_sharp_max.text())
if __name__=='__main__':
    app = QApplication(sys.argv)
    ui = LayoutDemo()
    ui.show()
    sys.exit(app.exec_())