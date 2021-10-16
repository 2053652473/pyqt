import sys
import threading

from PySide2 import QtWidgets
from PySide2.QtCore import QMetaObject, QCoreApplication
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QVBoxLayout, QTabWidget

from ui.First_Page import First_Page, First_page_num_control_sigtnal
from ui.Second_Page import Second_Tab



class Ui_MainWindow:
    def set_ui(self,main_window):
        self.t = None
        if not main_window.objectName():
            main_window.setObjectName("智能识别系统")
        main_window.resize(949,736)
        self.main_ver_layout = QVBoxLayout(main_window)
        self.main_ver_layout.setObjectName("最外层——垂直分布")
        self.main_TabWidget = QTabWidget(main_window)
        self.main_TabWidget.setObjectName("Tab组合页面")
        self.main_ver_layout.addWidget(self.main_TabWidget)
        self.retranslateUi(main_window)

        font = QFont()
        font.setFamily(u"Times New Roman")
        font.setPointSize(18)
        self.main_TabWidget.setFont(font)
        self.zhuangpei()
        self.main_TabWidget.currentChanged.connect(self.select_tab)

    def retranslateUi(self,main_window):
        _translate = QCoreApplication.translate
        main_window.setWindowTitle(_translate("Form","智能手势识别系统"))
    def zhuangpei(self):
        self.first_page = First_Page()
        self.second_page = Second_Tab()
        self.main_TabWidget.addTab(self.first_page,"first_tab")
        self.main_TabWidget.addTab(self.second_page,"second_tab")
        self.main_TabWidget.setCurrentIndex(0)

    def select_tab(self):
        print(self.main_TabWidget.currentIndex())
        if self.main_TabWidget.currentIndex() == 0:
            self.second_page.time_all.stop()
            self.first_page.v.kill_thread_flag =False
            # self.first_page.v.start()
            print(self.first_page.v.is_alive())
            if self.first_page.v.is_alive() == False:
                self.t = First_page_num_control_sigtnal(self.first_page,False)
                self.t.updata_num_signal.connect(self.t.updata_num_fuc)
                self.t.start()
            print("当前再第一页")
            # self.second_page.vd.timer_all.stop()
            # for i in self.second_page.vd.time:
            #     i.stop()
        elif self.main_TabWidget.currentIndex() == 1 :
            print("当前第二页")
            self.first_page.v.kill_thread_flag = True
            if self.t != None:
                self.t.kill_thread_flag = True
            # self.first_page.v.terminate()
            # self.second_page.vd.start_up()
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    widget  = QtWidgets.QWidget()
    ui.set_ui(widget)
    widget.show()
    sys.exit(app.exec_())

