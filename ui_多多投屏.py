# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_多多投屏.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(454, 258)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_shuaxin = QPushButton(self.centralwidget)
        self.pushButton_shuaxin.setObjectName(u"pushButton_shuaxin")

        self.gridLayout.addWidget(self.pushButton_shuaxin, 1, 1, 1, 1)

        self.comboBox_shebeiliebiao = QComboBox(self.centralwidget)
        self.comboBox_shebeiliebiao.setObjectName(u"comboBox_shebeiliebiao")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_shebeiliebiao.sizePolicy().hasHeightForWidth())
        self.comboBox_shebeiliebiao.setSizePolicy(sizePolicy)
        self.comboBox_shebeiliebiao.setMinimumSize(QSize(0, 32))

        self.gridLayout.addWidget(self.comboBox_shebeiliebiao, 1, 0, 1, 1)

        self.lineEdit_lujing = QLineEdit(self.centralwidget)
        self.lineEdit_lujing.setObjectName(u"lineEdit_lujing")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_lujing.sizePolicy().hasHeightForWidth())
        self.lineEdit_lujing.setSizePolicy(sizePolicy1)
        self.lineEdit_lujing.setMinimumSize(QSize(0, 32))

        self.gridLayout.addWidget(self.lineEdit_lujing, 3, 0, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setMaximumSize(QSize(16777215, 24))

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.pushButton_xuanzewenjjian = QPushButton(self.centralwidget)
        self.pushButton_xuanzewenjjian.setObjectName(u"pushButton_xuanzewenjjian")

        self.gridLayout.addWidget(self.pushButton_xuanzewenjjian, 3, 1, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)
        self.label.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.pushButton_jianchagengxin = QPushButton(self.centralwidget)
        self.pushButton_jianchagengxin.setObjectName(u"pushButton_jianchagengxin")
        sizePolicy2.setHeightForWidth(self.pushButton_jianchagengxin.sizePolicy().hasHeightForWidth())
        self.pushButton_jianchagengxin.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.pushButton_jianchagengxin)

        self.pushButton_kaishibofang = QPushButton(self.centralwidget)
        self.pushButton_kaishibofang.setObjectName(u"pushButton_kaishibofang")
        sizePolicy2.setHeightForWidth(self.pushButton_kaishibofang.sizePolicy().hasHeightForWidth())
        self.pushButton_kaishibofang.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.pushButton_kaishibofang)

        self.pushButton_tingzhibofang = QPushButton(self.centralwidget)
        self.pushButton_tingzhibofang.setObjectName(u"pushButton_tingzhibofang")
        sizePolicy2.setHeightForWidth(self.pushButton_tingzhibofang.sizePolicy().hasHeightForWidth())
        self.pushButton_tingzhibofang.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.pushButton_tingzhibofang)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 454, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u591a\u591a\u6295\u5c4f", None))
        self.pushButton_shuaxin.setText(QCoreApplication.translate("MainWindow", u"\u5237\u65b0", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u6295\u5c4f\u7684\u6587\u4ef6\u8def\u5f84 / Url \u5730\u5740", None))
        self.pushButton_xuanzewenjjian.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u5907\u5217\u8868", None))
        self.pushButton_jianchagengxin.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u67e5\u66f4\u65b0", None))
        self.pushButton_kaishibofang.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u64ad\u653e", None))
        self.pushButton_tingzhibofang.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62\u64ad\u653e", None))
    # retranslateUi

