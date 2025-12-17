# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home_window.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QSizePolicy,
    QWidget)

class Ui_HomeWindow(object):
    def setupUi(self, HomeWindow):
        if not HomeWindow.objectName():
            HomeWindow.setObjectName(u"HomeWindow")
        HomeWindow.resize(980, 980)
        HomeWindow.setMinimumSize(QSize(980, 980))
        font = QFont()
        font.setFamilies([u"Lexend"])
        font.setPointSize(10)
        HomeWindow.setFont(font)
        HomeWindow.setStyleSheet(u"QWidget {\n"
"	background-color: #1a1a1a;\n"
"}")
        self.gridLayout = QGridLayout(HomeWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lb_home = QLabel(HomeWindow)
        self.lb_home.setObjectName(u"lb_home")
        self.lb_home.setMinimumSize(QSize(0, 75))
        self.lb_home.setMaximumSize(QSize(16777215, 75))
        font1 = QFont()
        font1.setFamilies([u"Lexend"])
        font1.setPointSize(36)
        font1.setBold(True)
        self.lb_home.setFont(font1)
        self.lb_home.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lb_home, 0, 0, 1, 1)


        self.retranslateUi(HomeWindow)

        QMetaObject.connectSlotsByName(HomeWindow)
    # setupUi

    def retranslateUi(self, HomeWindow):
        HomeWindow.setWindowTitle(QCoreApplication.translate("HomeWindow", u"Form", None))
        self.lb_home.setText(QCoreApplication.translate("HomeWindow", u"Welcome to EixnPOS", None))
    # retranslateUi

