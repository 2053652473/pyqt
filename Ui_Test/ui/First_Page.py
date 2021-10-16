import threading
from time import sleep
import  pygame
import PySide2
from PySide2.QtCore import QCoreApplication, QSize, QObject, Signal
from PySide2.QtWidgets import QWidget
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from control.recv import recv

class  First_Page(QWidget,):
    def __init__(self,parent=None):
        super(First_Page, self).__init__(parent)
        self.horizontalLayout = QHBoxLayout()  # 水平布局  第一页整体上是水平布局
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.number = QVBoxLayout()  # 左半边是垂直布局的
        self.number.setObjectName(u"number")

        self.damuzhi = QHBoxLayout()  # 大拇指的标签和文本显示是水平布局的
        self.damuzhi.setObjectName(u"damuzhi")
        self.label = QLabel(self)  # 大拇指的标签在第一页中
        self.label.setObjectName(u"label")
        self.label.setMouseTracking(False)  # 鼠标监控
        self.damuzhi.addWidget(self.label)
        self.lineEdit = QLineEdit()
        self.lineEdit.setObjectName(u"lineEdit")
        self.damuzhi.addWidget(self.lineEdit)
        self.number.addLayout(self.damuzhi)  # 把大拇指加到垂直布局中去


        self.shizhi = QHBoxLayout()  # 食指标签和文本的水平布局
        self.shizhi.setObjectName(u"shizhi")  # 设置水平布局的名字
        self.label_2 = QLabel(self)  # 食指标签
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMouseTracking(False)
        self.shizhi.addWidget(self.label_2)
        self.lineEdit_2 = QLineEdit()
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.shizhi.addWidget(self.lineEdit_2)
        self.number.addLayout(self.shizhi)  # 把食指的标签和文本添加进竖直布局中

        # 中指部分
        self.zhongzhi = QHBoxLayout()
        self.zhongzhi.setObjectName(u"zhongzhi")
        self.label_3 = QLabel(self)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMouseTracking(False)
        self.zhongzhi.addWidget(self.label_3)
        self.lineEdit_3 = QLineEdit()
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.zhongzhi.addWidget(self.lineEdit_3)
        self.number.addLayout(self.zhongzhi)

        # 无名指部分
        self.wumingzhi = QHBoxLayout()
        self.wumingzhi.setObjectName(u"wumingzhi")
        self.label_4 = QLabel(self)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMouseTracking(False)
        self.wumingzhi.addWidget(self.label_4)
        self.lineEdit_4 = QLineEdit()
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.wumingzhi.addWidget(self.lineEdit_4)
        self.number.addLayout(self.wumingzhi)

        # 小拇指部分
        self.xiaomuzhi = QHBoxLayout()
        self.xiaomuzhi.setObjectName(u"xiaomuzhi")
        self.label_5 = QLabel(self)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMouseTracking(False)
        self.xiaomuzhi.addWidget(self.label_5)
        self.lineEdit_5 = QLineEdit()
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.xiaomuzhi.addWidget(self.lineEdit_5)
        self.number.addLayout(self.xiaomuzhi)

        self.horizontalLayout.addLayout(self.number)  # 将左半边部分添加进第一个水平布局中去
        '第一页左右两半边分割线---------------------------------------------------------------------'
        self.image = QVBoxLayout()  # 右半边整体上是竖直布局
        self.image.setObjectName(u"image")
        self.image_2 = QLabel(self)  # 图片展示区
        self.image_2.setObjectName(u"image_2")
        self.image_2.setMinimumSize(QSize(560, 560))  # 设置最大最小区域
        self.image_2.setMaximumSize(QSize(560, 560))
        self.image_2.setFrameShape(QFrame.Box)  # 为lable加边框
        self.image_2.setPixmap(QPixmap("../static/image/0.jpg"))
        self.image_2.setScaledContents(True)  # 图片可缩放
        self.image.addWidget(self.image_2)
        self.sound = QHBoxLayout()  # 右下部分水平布局
        self.sound.setObjectName(u"sound")
        self.laba = QLabel(self)
        self.laba.setObjectName(u"laba")
        self.laba.setMinimumSize(QSize(76, 76))
        self.laba.setMaximumSize(QSize(76, 76))
        self.laba.setPixmap(QPixmap("../static/image/喇叭.png"))
        self.laba.setScaledContents(True)
        self.sound.addWidget(self.laba)

        self.sound_doc = QLineEdit()
        self.sound_doc.setObjectName(u"sound_doc")
        self.sound_doc.setMinimumSize(QSize(460, 76))
        self.sound_doc.setMaximumSize(QSize(460, 76))
        # self.sound_doc.setAlignment()
        font1 = QFont()
        font1.setFamily(u"Times New Roman")
        font1.setPointSize(36)
        self.sound_doc.setFont(font1)
        self.sound.addWidget(self.sound_doc)
        self.image.addLayout(self.sound)
        self.horizontalLayout.addLayout(self.image)  # 将右半部分添加到第一页的水平布局中
        self.setLayout(self.horizontalLayout)

        self.v = First_page_num_control_sigtnal(self,False)
        self.v.updata_num_signal.connect(self.v.updata_num_fuc)
        self.v.start()
        self.retranslateUi()


    def retranslateUi(self):
        self.label.setText(QCoreApplication.translate("finger", u"\u5927\u62c7\u6307", None))
        self.lineEdit.setText("")
        self.label_2.setText(QCoreApplication.translate("finger", u"\u98df    \u6307", None))
        self.lineEdit_2.setText("")
        self.label_3.setText(QCoreApplication.translate("finger", u"\u4e2d    \u6307", None))
        self.lineEdit_3.setText("")
        self.label_5.setText(QCoreApplication.translate("finger", u"\u65e0\u540d\u6307", None))
        self.lineEdit_5.setText("")
        self.label_4.setText(QCoreApplication.translate("finger", u"\u5c0f    \u6307", None))
        self.lineEdit_4.setText("")


class  First_page_num_control_sigtnal(QObject,threading.Thread):
    def __init__(self,ui,kill_flag):
        super(First_page_num_control_sigtnal, self).__init__()
        threading.Thread.__init__(self)
        self.ui = ui
        self.sound_play_flag = []
        pygame.init()
        self.kill_thread_flag = kill_flag
        self.setName("page_one-threading")
    updata_num_signal = Signal(list)
    def run(self):
        # print('页面一线程开始执行')
        sleep_flag_array = []   #里面存两个数,分别为前一次和本次弯曲手指的数量。  判断标准，如果这两个数据不同，则延迟0.1秒，否则延迟4秒
        while 1:
            sleep_flag  = 0
            self.data = recv()
            print("数据接受成功")
            self.updata_num_signal.emit(self.data)   #更新数据
            #判断弯曲手指的数量
            for i in self.data:
                if float(i.replace(' ', '')) > 175:
                    sleep_flag += 1
            #删掉上上次，添加本次  查看本次和上一次是否不同
            if  len(sleep_flag_array) == 2:
                del sleep_flag_array[0]
                sleep_flag_array.append(sleep_flag)
                #如果不同更改图片
                if sleep_flag_array[0] != sleep_flag_array[1]:
                    self.updata_imag(self.data)
                    sleep(4)
                else:
                    sleep(0.1)
            else:
                sleep_flag_array.append(sleep_flag)
                sleep(0.1)
            self.data = []
            if self.kill_thread_flag :
                break


    def updata_num_fuc(self,data):
        print("lalal")
        self.ui.lineEdit.setText(data[0])
        self.ui.lineEdit_2.setText(data[1])
        self.ui.lineEdit_3.setText(data[2])
        self.ui.lineEdit_4.setText(data[3])
        self.ui.lineEdit_5.setText(data[4])
        # self.updata_imag(data)

    def updata_imag(self,data):
        current_falg = 0  #弯曲手指的个数
        for i in data:
            if float(i.replace(' ',''))>175:
                current_falg += 1

        if 5 - current_falg == 0:  # 五根手指弯曲
            self.ui.image_2.setPixmap("../static/image/握拳.png")
            self.ui.sound_doc.setText("zero")
            pygame.mixer.music.load('../static/sound/zero.mp3')
        elif 5 - current_falg == 1:  # 四根手指弯曲
            self.ui.image_2.setPixmap("../static/image/一.png")
            self.ui.sound_doc.setText("one")
            pygame.mixer.music.load('../static/sound/one.mp3')
        elif 5 - current_falg == 2:  # 三根手指弯曲
            self.ui.image_2.setPixmap("../static/image/二.png")
            self.ui.sound_doc.setText("two")
            pygame.mixer.music.load('../static/sound/two2.mp3')
        elif 5 - current_falg == 3:  # 两根手指弯曲
            self.ui.image_2.setPixmap("../static/image/三.png")
            self.ui.sound_doc.setText("three")
            pygame.mixer.music.load('../static/sound/three.mp3')
        elif 5 - current_falg == 4:  # 一根手指弯曲
            self.ui.image_2.setPixmap("../static/image/四.png")
            self.ui.sound_doc.setText("four")
            pygame.mixer.music.load('../static/sound/four.mp3')
        elif 5 - current_falg == 5:  # 无手指弯曲
            self.ui.image_2.setPixmap("../static/image/五.png")
            self.ui.sound_doc.setText("five")
            pygame.mixer.music.load('../static/sound/five.mp3')
        pygame.mixer.music.play()
            # sleep(4)
        self.ui.image_2.setScaledContents(True)
        current_falg = 0

