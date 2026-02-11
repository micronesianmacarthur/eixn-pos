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
        self.gridLayout = QGridLayout(HomeWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lb_welcome = QLabel(HomeWindow)
        self.lb_welcome.setObjectName(u"lb_welcome")
        self.lb_welcome.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lb_welcome, 0, 0, 1, 1)


        self.retranslateUi(HomeWindow)

        QMetaObject.connectSlotsByName(HomeWindow)
    # setupUi

    def retranslateUi(self, HomeWindow):
        HomeWindow.setWindowTitle(QCoreApplication.translate("HomeWindow", u"Home", None))
        self.lb_welcome.setText(QCoreApplication.translate("HomeWindow", u"Welcome to EixnPOS", None))
    # retranslateUi

