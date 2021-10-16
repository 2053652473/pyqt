from functools import partial

import matplotlib.pyplot as plt
import numpy as np
from PySide2.QtCore import QCoreApplication, Slot, QTimer
from PySide2.QtWidgets import QWidget
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from matplotlib.backends.backend_qt5agg  import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from matplotlib.ticker import MultipleLocator
import matplotlib
from control.recv import recv
# matplotlib.rc("font",family='songti')
# control_arry = []
# plt.rcParams['font.sans-serif']=['SimHei']
# plt.rcParams['axes.unicode_minus']=False
class Second_Tab(QWidget):
    def __init__(self,parent = None):
        super(Second_Tab,self).__init__(parent)
        self.btn_id_flag = None
        self.time_all = QTimer()
        self.time_all.setInterval(100)
        self.time_all.timeout.connect(lambda :self.updata_canv())
        self.data = []
        self.x = []
        for i in range(20):
            self.x.append(i)

        self.main_v_layout = QVBoxLayout()  #整体页面的垂直分布
        self.main_v_layout.setObjectName("整体页面垂直分布")

        self.up_h_layout = QHBoxLayout() #上面按钮的水平分布
        self.up_h_layout.setObjectName("上面的控件水平分布")

        self.finger_all = QPushButton()
        self.finger_all.setObjectName("五根手指")

        self.up_h_layout.addWidget(self.finger_all)

        self.finger_first =  QPushButton()
        self.finger_first.setObjectName("大拇指")

        self.up_h_layout.addWidget(self.finger_first)

        self.finger_second = QPushButton()
        self.finger_second.setObjectName("食指")
        self.up_h_layout.addWidget(self.finger_second)

        self.finger_third = QPushButton()
        self.finger_third.setObjectName("中指")
        self.up_h_layout.addWidget(self.finger_third)
        self.finger_fourth = QPushButton()
        self.finger_second.setObjectName("无名指")
        self.up_h_layout.addWidget(self.finger_fourth)
        self.finger_fifth = QPushButton()
        self.finger_fifth.setObjectName("小拇指")
        self.up_h_layout.addWidget(self.finger_fifth)
        self.main_v_layout.addLayout(self.up_h_layout)
        self.down_frame = QFrame()
        # self.frame_var_layout = QVBoxLayout(self.down_frame)
        self.main_v_layout.addWidget(self.down_frame)
        self.setLayout(self.main_v_layout)
        self.reset()
        self.canv = FigureCanvas(Figure())
        self.czbj = QVBoxLayout(self.down_frame)
        self.czbj.addWidget(self.canv)
        self.axes = self.canv.figure.subplots(5, 1, sharex=True)

        # print("axes的类型：",len(self.axes))
        for i in range(20):
            self.recv_data()
        self.draw_canv(all)
        self.finger_name = ['Thumbs up','Index finger','Middle finger','Ring finger','Little finger']
        self.finger_all.clicked.connect(self.init_canv)
        self.finger_first.clicked.connect(self.init_canv)
        self.finger_second.clicked.connect(self.init_canv)
        self.finger_third.clicked.connect(self.init_canv)
        self.finger_fourth.clicked.connect(self.init_canv)
        self.finger_fifth.clicked.connect(self.init_canv)
        # self.vd= sencond_page_control(self)
    def reset(self):
        _translater = QCoreApplication.translate
        self.finger_all.setText(_translater("Form","全部",None))
        self.finger_first.setText(_translater("Form","大拇指",None))
        self.finger_second.setText(_translater("Form", "食指", None))
        self.finger_third.setText(_translater("Form", "中指", None))
        self.finger_fourth.setText(_translater("Form", "无名指", None))
        self.finger_fifth.setText(_translater("Form", "小拇指", None))
    def recv_data(self):
        original_data = recv()
        for i in original_data:
            self.data.append(float(i.replace(" ",'')))
    def init_canv(self):
        sender = self.sender()

        if sender.text() == '全部':
            self.del_canv()
            self.add_canv()
            self.axes = self.canv.figure.subplots(5,1,sharex=True)
            self.axes = self.axes.flatten()
            # self.axes[0].set_title(sender.text() + '手指 information', fontsize=25)
            self.draw_canv(all)
            self.btn_id_flag = all
            # self.time_all.timeout.connect(self.updata_canv)
        elif sender.text() == '大拇指':
            print("大拇指被点击了")
            self.del_canv()
            self.add_canv()
            self.axes = self.canv.figure.subplots(1, 1)
            print("axes的类型",type(self.axes))
            # self.axes.set_title(sender.text() + 'information', fontsize=25)
            self.draw_canv(0)
            self.btn_id_flag = 0
        elif sender.text() == '食指':
            self.del_canv()
            self.add_canv()
            self.axes = self.canv.figure.subplots(1, 1)
            # self.axes.set_title(sender.text() + 'information', fontsize=25)
            self.draw_canv(1)
            self.btn_id_flag = 1
        elif sender.text() == '中指':
            self.del_canv()
            self.add_canv()
            self.axes = self.canv.figure.subplots(1, 1)
            # self.axes.set_title(sender.text() + 'information',fontsize=25)
            self.draw_canv(2)
            self.btn_id_flag = 2
        elif sender.text() == '无名指':
            self.del_canv()
            self.add_canv()
            self.axes = self.canv.figure.subplots(1, 1)
            # self.axes.set_title(sender.text()+'information',fontsize=25)
            self.draw_canv(3)
            self.btn_id_flag = 3
        elif sender.text() == '小拇指':
            self.del_canv()
            self.add_canv()
            self.axes = self.canv.figure.subplots(1, 1)
            # self.axes.set_title(sender.text() + 'information',fontsize=25)
            self.draw_canv(4)
            self.btn_id_flag = 4
        self.time_all.start()
    def updata_canv(self):
        del self.data[0:5]
        self.recv_data()
        del self.x[0]
        self.x.append(self.x[-1]+1)
        self.draw_canv(self.btn_id_flag)
        self.canv.draw()
    def draw_canv(self,btn_ID):
        if btn_ID == all:
            self.axes = self.axes.flatten()
            for i in range(5):
                self.axes[i].cla()
                self.axes[0].set_title("All fingers",fontsize = 25)
                self.axes[i].xaxis.set_major_locator(MultipleLocator(2))
                self.axes[i].plot(self.x, self.data[i::5])
        else:
            self.axes.cla()
            self.axes.set_title(self.finger_name[btn_ID], fontsize=25)
            self.axes.xaxis.set_major_locator(MultipleLocator(1))
            self.axes.plot(self.x,self.data[btn_ID::5])

    def del_canv(self):
        self.canv.setParent(None)
        self.czbj.removeWidget(self.canv)

    def add_canv(self):
        self.canv =  FigureCanvas(Figure())
        self.czbj.addWidget(self.canv)





# class sencond_page_control:
#     def __init__(self,ui):
#         self.ui = ui
#         self.time = [1,2,3,4,5]
#         self.x = []
#         self.singl_finger_data = []
#         self.finger = []
#         for i in range(1,21):
#             self.x.append(i)
#         for i in range(5):
#             self.time[i] = QTimer()
#             self.time[i].setInterval(100)
#             self.time[i].timeout.connect(self.updata_wave)
#
#         self.timer_all = QTimer()
#         self.timer_all.setInterval(100)
#         self.timer_all.timeout.connect(self.update_charts_all)
#         self.canv = FigureCanvas(Figure())
#         self.czbj = QVBoxLayout(self.ui.down_frame)
#         self.czbj.addWidget(self.canv)
#         self.canv.figure.subplots(1,1)
#         self.flag = 0
#         self.click_flag = 0
#         self.time_control_flag = 10
#         self.finger_name = ['Thumbs up','Index finger','Middle finger','Ring finger','Little finger']
#         self.text_sender()
#     # def  text_sender(self):
#
#
#     def start_up(self):
#         self.ui.finger_all.clicked.connect(lambda: self.time_all_start())
#         self.add_finger()
#     def add_finger(self):
#         self.finger.append(self.ui.finger_first)
#         self.finger.append(self.ui.finger_second)
#         self.finger.append(self.ui.finger_third)
#         self.finger.append(self.ui.finger_fourth)
#         self.finger.append(self.ui.finger_fifth)
#         for i  in range(len(self.finger)):
#             self.finger[i].clicked.connect(partial(self.time_control, i))
#     def del_canv(self):
#         self.canv.setParent(None)
#         self.czbj.removeWidget(self.canv)
#     def init_add_cav(self):
#         self.canv = FigureCanvas(Figure())
#         self.czbj = QVBoxLayout(self.ui.down_frame)
#         self.czbj.addWidget(self.canv)
#     def add_canv(self):
#         self.canv =  FigureCanvas(Figure())
#         self.czbj.addWidget(self.canv)
#     def time_control(self,i):
#         self.flag = i
#         print("第",i+1,"根手指弯曲了")
#         self.click_flag += 1
#         if self.click_flag % 2 ==0:
#             self.time[i].stop()
#         else:
#             self.time[i].start()
#         self.timer_all.stop()
#         # for t in range(5):
#         #     if t != i:
#         #         self.time[t].stop()
#         self.del_canv()
#         self.add_canv()
#         self.ax = self.canv.figure.subplots(1,1)
#         self.ax.set_title(self.finger_name[i]+'information',fontsize=25)
#         self.singl_x = []
#         for i in range(20):
#             self.singl_x .append(i)
#         self.singl_finger_data = []
#         for i in range(20):
#             self.data = recv()
#             self.singl_finger_data.append(float(self.data[self.flag]))
#             self.data = []
#         self.ax.plot(self.singl_x,self.singl_finger_data)
#         # self.click_flag  = 0
#     def updata_wave(self):
#         # print("nihao")
#         self.data = []
#         self.data = recv()
#         v = self.flag
#         if len(self.singl_finger_data)>=20:
#             del self.singl_finger_data[0]
#             del self.singl_x[0]
#             self.singl_finger_data.append(float(self.data[v]))
#             self.singl_x.append(self.singl_x[-1] + 1)
#         else:
#             self.singl_finger_data.append(float(self.data[v]))
#             self.singl_x.append(self.singl_x[-1] + 1)
#         self.ax.cla()
#         self.ax.set_title(self.finger_name[v] + 'information',fontsize=25)
#         # self.ax.xaxis.set_major_locator(MultipleLocator(1))  # X轴刻度步长
#         self.ax.plot(self.singl_x,self.singl_finger_data)
#         self.canv.draw()
#     def time_all_start(self):
#         self.del_canv()
#         self.add_canv()
#         self.axes = self.canv.figure.subplots(5,1,sharex=True)
#         self.axes = self.axes.flatten()
#         self.axes[0].set_title('All Finger Information',fontsize=25)
#         self.data = []
#         self.data_num = []
#         for i in range(20):
#             self.data = recv()
#             self.data_num.extend(self.data)
#         for i in range(len(self.data_num)):
#             self.data_num[i] = float(self.data_num[i].replace(" ", ''))
#         for i in range(5):
#             self.axes[i].plot(self.x, self.data_num[i::5])
#         self.data = []
#         self.timer_all.start()
#         for i in self.time:
#             i.stop()
#
#     def update_charts_all(self):
#         self.data = recv()
#         del self.data_num[0:5]
#         del self.x[0]
#         self.x.append(self.x[18]+1)
#         for i in self.data:
#             self.data_num.append(float(i.replace(' ','')))
#         for i in range(5):
#             self.axes[i].cla()
#             self.axes[i].plot(self.x,self.data_num[i::5])
#             self.axes[i].xaxis.set_major_locator(MultipleLocator(1))  # X轴刻度步长
#         self.axes[0].set_title('All Finger Information',fontsize=25)
#         self.data = []
#         self.canv.draw()

