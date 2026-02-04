# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cash_counter.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QDoubleSpinBox, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)
import icons_rc

class Ui_CashCounter(object):
    def setupUi(self, CashCounter):
        if not CashCounter.objectName():
            CashCounter.setObjectName(u"CashCounter")
        CashCounter.setWindowModality(Qt.WindowModality.ApplicationModal)
        CashCounter.resize(640, 480)
        CashCounter.setMinimumSize(QSize(640, 480))
        CashCounter.setMaximumSize(QSize(640, 480))
        CashCounter.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(CashCounter)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 10)
        self.widget = QWidget(CashCounter)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 35))
        self.widget.setMaximumSize(QSize(16777215, 35))
        self.horizontalLayout_10 = QHBoxLayout(self.widget)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.lb_dialog_title = QLabel(self.widget)
        self.lb_dialog_title.setObjectName(u"lb_dialog_title")
        self.lb_dialog_title.setMinimumSize(QSize(0, 35))
        self.lb_dialog_title.setMaximumSize(QSize(16777215, 35))
        self.lb_dialog_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_10.addWidget(self.lb_dialog_title)


        self.verticalLayout_4.addWidget(self.widget)

        self.widget_2 = QWidget(CashCounter)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_22 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_22.setSpacing(5)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.widget_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.countCash = QWidget()
        self.countCash.setObjectName(u"countCash")
        self.verticalLayout_5 = QVBoxLayout(self.countCash)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 10, 0, 0)
        self.widget_4 = QWidget(self.countCash)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_23 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_23.setSpacing(5)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.widget_6 = QWidget(self.widget_4)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_6 = QVBoxLayout(self.widget_6)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.grp_coins = QGroupBox(self.widget_6)
        self.grp_coins.setObjectName(u"grp_coins")
        font = QFont()
        font.setBold(True)
        self.grp_coins.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(self.grp_coins)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 15, 5, 5)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.label_5 = QLabel(self.grp_coins)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(75, 0))
        self.label_5.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout.addWidget(self.label_5)

        self.lb_coins_count = QLabel(self.grp_coins)
        self.lb_coins_count.setObjectName(u"lb_coins_count")
        self.lb_coins_count.setMinimumSize(QSize(60, 0))
        self.lb_coins_count.setMaximumSize(QSize(60, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Lexend"])
        font1.setBold(True)
        self.lb_coins_count.setFont(font1)
        self.lb_coins_count.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.lb_coins_count)

        self.lb_coins_amount = QLabel(self.grp_coins)
        self.lb_coins_amount.setObjectName(u"lb_coins_amount")
        self.lb_coins_amount.setMinimumSize(QSize(60, 0))
        self.lb_coins_amount.setMaximumSize(QSize(60, 16777215))
        self.lb_coins_amount.setFont(font1)
        self.lb_coins_amount.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.lb_coins_amount)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.lb_pennies = QLabel(self.grp_coins)
        self.lb_pennies.setObjectName(u"lb_pennies")
        self.lb_pennies.setMinimumSize(QSize(75, 0))
        self.lb_pennies.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_2.addWidget(self.lb_pennies)

        self.le_pennies = QLineEdit(self.grp_coins)
        self.le_pennies.setObjectName(u"le_pennies")
        self.le_pennies.setMinimumSize(QSize(60, 0))
        self.le_pennies.setMaximumSize(QSize(60, 16777215))
        self.le_pennies.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.le_pennies)

        self.lb_pennies_amt = QLabel(self.grp_coins)
        self.lb_pennies_amt.setObjectName(u"lb_pennies_amt")
        self.lb_pennies_amt.setMinimumSize(QSize(60, 0))
        self.lb_pennies_amt.setMaximumSize(QSize(60, 16777215))
        self.lb_pennies_amt.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.lb_pennies_amt)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.lb_nickels = QLabel(self.grp_coins)
        self.lb_nickels.setObjectName(u"lb_nickels")
        self.lb_nickels.setMinimumSize(QSize(75, 0))
        self.lb_nickels.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_3.addWidget(self.lb_nickels)

        self.le_nickels = QLineEdit(self.grp_coins)
        self.le_nickels.setObjectName(u"le_nickels")
        self.le_nickels.setMinimumSize(QSize(40, 0))
        self.le_nickels.setMaximumSize(QSize(60, 16777215))
        self.le_nickels.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.le_nickels)

        self.lb_nickels_amt = QLabel(self.grp_coins)
        self.lb_nickels_amt.setObjectName(u"lb_nickels_amt")
        self.lb_nickels_amt.setMinimumSize(QSize(60, 0))
        self.lb_nickels_amt.setMaximumSize(QSize(60, 16777215))
        self.lb_nickels_amt.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.lb_nickels_amt)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, -1, -1, -1)
        self.lb_dimes = QLabel(self.grp_coins)
        self.lb_dimes.setObjectName(u"lb_dimes")
        self.lb_dimes.setMinimumSize(QSize(75, 0))
        self.lb_dimes.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_4.addWidget(self.lb_dimes)

        self.le_dimes = QLineEdit(self.grp_coins)
        self.le_dimes.setObjectName(u"le_dimes")
        self.le_dimes.setMinimumSize(QSize(40, 0))
        self.le_dimes.setMaximumSize(QSize(60, 16777215))
        self.le_dimes.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.le_dimes)

        self.lb_dimes_amt = QLabel(self.grp_coins)
        self.lb_dimes_amt.setObjectName(u"lb_dimes_amt")
        self.lb_dimes_amt.setMinimumSize(QSize(60, 0))
        self.lb_dimes_amt.setMaximumSize(QSize(60, 16777215))
        self.lb_dimes_amt.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.lb_dimes_amt)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, -1, -1, -1)
        self.lb_quarters = QLabel(self.grp_coins)
        self.lb_quarters.setObjectName(u"lb_quarters")
        self.lb_quarters.setMinimumSize(QSize(75, 0))
        self.lb_quarters.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_5.addWidget(self.lb_quarters)

        self.le_quarters = QLineEdit(self.grp_coins)
        self.le_quarters.setObjectName(u"le_quarters")
        self.le_quarters.setMinimumSize(QSize(40, 0))
        self.le_quarters.setMaximumSize(QSize(60, 16777215))
        self.le_quarters.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.le_quarters)

        self.lb_quarters_amt = QLabel(self.grp_coins)
        self.lb_quarters_amt.setObjectName(u"lb_quarters_amt")
        self.lb_quarters_amt.setMinimumSize(QSize(60, 0))
        self.lb_quarters_amt.setMaximumSize(QSize(60, 16777215))
        self.lb_quarters_amt.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.lb_quarters_amt)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, -1, -1, -1)
        self.lb_half_dollars = QLabel(self.grp_coins)
        self.lb_half_dollars.setObjectName(u"lb_half_dollars")
        self.lb_half_dollars.setMinimumSize(QSize(75, 0))
        self.lb_half_dollars.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_6.addWidget(self.lb_half_dollars)

        self.le_half_dollars = QLineEdit(self.grp_coins)
        self.le_half_dollars.setObjectName(u"le_half_dollars")
        self.le_half_dollars.setMinimumSize(QSize(40, 0))
        self.le_half_dollars.setMaximumSize(QSize(60, 16777215))
        self.le_half_dollars.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.le_half_dollars)

        self.lb_half_dollars_amt = QLabel(self.grp_coins)
        self.lb_half_dollars_amt.setObjectName(u"lb_half_dollars_amt")
        self.lb_half_dollars_amt.setMinimumSize(QSize(60, 0))
        self.lb_half_dollars_amt.setMaximumSize(QSize(60, 16777215))
        self.lb_half_dollars_amt.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.lb_half_dollars_amt)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, -1, -1, -1)
        self.lb_dollars = QLabel(self.grp_coins)
        self.lb_dollars.setObjectName(u"lb_dollars")
        self.lb_dollars.setMinimumSize(QSize(75, 0))
        self.lb_dollars.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_7.addWidget(self.lb_dollars)

        self.le_dollars = QLineEdit(self.grp_coins)
        self.le_dollars.setObjectName(u"le_dollars")
        self.le_dollars.setMinimumSize(QSize(40, 0))
        self.le_dollars.setMaximumSize(QSize(60, 16777215))
        self.le_dollars.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.le_dollars)

        self.lb_dollars_amt = QLabel(self.grp_coins)
        self.lb_dollars_amt.setObjectName(u"lb_dollars_amt")
        self.lb_dollars_amt.setMinimumSize(QSize(60, 0))
        self.lb_dollars_amt.setMaximumSize(QSize(60, 16777215))
        self.lb_dollars_amt.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.lb_dollars_amt)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, -1, -1, -1)
        self.lb_two_dollars = QLabel(self.grp_coins)
        self.lb_two_dollars.setObjectName(u"lb_two_dollars")
        self.lb_two_dollars.setMinimumSize(QSize(75, 0))
        self.lb_two_dollars.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_9.addWidget(self.lb_two_dollars)

        self.le_two_dollars = QLineEdit(self.grp_coins)
        self.le_two_dollars.setObjectName(u"le_two_dollars")
        self.le_two_dollars.setMinimumSize(QSize(40, 0))
        self.le_two_dollars.setMaximumSize(QSize(60, 16777215))
        self.le_two_dollars.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.le_two_dollars)

        self.lb_two_dollars_amt = QLabel(self.grp_coins)
        self.lb_two_dollars_amt.setObjectName(u"lb_two_dollars_amt")
        self.lb_two_dollars_amt.setMinimumSize(QSize(60, 0))
        self.lb_two_dollars_amt.setMaximumSize(QSize(60, 16777215))
        self.lb_two_dollars_amt.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.lb_two_dollars_amt)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_20 = QLabel(self.grp_coins)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(75, 0))
        self.label_20.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_8.addWidget(self.label_20)

        self.label_22 = QLabel(self.grp_coins)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(60, 0))
        self.label_22.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_8.addWidget(self.label_22)

        self.lb_coins_total = QLabel(self.grp_coins)
        self.lb_coins_total.setObjectName(u"lb_coins_total")
        self.lb_coins_total.setMinimumSize(QSize(60, 0))
        self.lb_coins_total.setMaximumSize(QSize(60, 16777215))
        self.lb_coins_total.setFont(font1)
        self.lb_coins_total.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.lb_coins_total)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)


        self.verticalLayout_6.addWidget(self.grp_coins)


        self.horizontalLayout_23.addWidget(self.widget_6)

        self.widget_7 = QWidget(self.widget_4)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_7 = QVBoxLayout(self.widget_7)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.grp_bills = QGroupBox(self.widget_7)
        self.grp_bills.setObjectName(u"grp_bills")
        self.grp_bills.setFont(font)
        self.verticalLayout_3 = QVBoxLayout(self.grp_bills)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 15, 5, 5)
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, -1, -1, -1)
        self.label_25 = QLabel(self.grp_bills)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(75, 0))
        self.label_25.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_13.addWidget(self.label_25)

        self.lb_bills_count = QLabel(self.grp_bills)
        self.lb_bills_count.setObjectName(u"lb_bills_count")
        self.lb_bills_count.setMinimumSize(QSize(60, 0))
        self.lb_bills_count.setMaximumSize(QSize(60, 16777215))
        self.lb_bills_count.setFont(font1)
        self.lb_bills_count.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.lb_bills_count)

        self.lb_bills_amount = QLabel(self.grp_bills)
        self.lb_bills_amount.setObjectName(u"lb_bills_amount")
        self.lb_bills_amount.setMinimumSize(QSize(60, 0))
        self.lb_bills_amount.setMaximumSize(QSize(60, 16777215))
        self.lb_bills_amount.setFont(font1)
        self.lb_bills_amount.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.lb_bills_amount)


        self.verticalLayout_3.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(5)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, -1, -1, -1)
        self.lb_ones = QLabel(self.grp_bills)
        self.lb_ones.setObjectName(u"lb_ones")
        self.lb_ones.setMinimumSize(QSize(75, 0))
        self.lb_ones.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_14.addWidget(self.lb_ones)

        self.le_ones = QLineEdit(self.grp_bills)
        self.le_ones.setObjectName(u"le_ones")
        self.le_ones.setMinimumSize(QSize(60, 0))
        self.le_ones.setMaximumSize(QSize(60, 16777215))
        self.le_ones.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_14.addWidget(self.le_ones)

        self.lb_ones_amt = QLabel(self.grp_bills)
        self.lb_ones_amt.setObjectName(u"lb_ones_amt")
        self.lb_ones_amt.setMinimumSize(QSize(60, 0))
        self.lb_ones_amt.setMaximumSize(QSize(60, 16777215))
        self.lb_ones_amt.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_14.addWidget(self.lb_ones_amt)


        self.verticalLayout_3.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(5)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, -1, -1, -1)
        self.lb_twos = QLabel(self.grp_bills)
        self.lb_twos.setObjectName(u"lb_twos")
        self.lb_twos.setMinimumSize(QSize(75, 0))
        self.lb_twos.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_15.addWidget(self.lb_twos)

        self.le_twos = QLineEdit(self.grp_bills)
        self.le_twos.setObjectName(u"le_twos")
        self.le_twos.setMinimumSize(QSize(40, 0))
        self.le_twos.setMaximumSize(QSize(60, 16777215))
        self.le_twos.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_15.addWidget(self.le_twos)

        self.lb_twos_amt = QLabel(self.grp_bills)
        self.lb_twos_amt.setObjectName(u"lb_twos_amt")
        self.lb_twos_amt.setMinimumSize(QSize(60, 0))
        self.lb_twos_amt.setMaximumSize(QSize(60, 16777215))
        self.lb_twos_amt.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_15.addWidget(self.lb_twos_amt)


        self.verticalLayout_3.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setSpacing(5)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, -1, -1, -1)
        self.lb_fives = QLabel(self.grp_bills)
        self.lb_fives.setObjectName(u"lb_fives")
        self.lb_fives.setMinimumSize(QSize(75, 0))
        self.lb_fives.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_16.addWidget(self.lb_fives)

        self.le_fives = QLineEdit(self.grp_bills)
        self.le_fives.setObjectName(u"le_fives")
        self.le_fives.setMinimumSize(QSize(40, 0))
        self.le_fives.setMaximumSize(QSize(60, 16777215))
        self.le_fives.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.le_fives)

        self.lb_fives_amt = QLabel(self.grp_bills)
        self.lb_fives_amt.setObjectName(u"lb_fives_amt")
        self.lb_fives_amt.setMinimumSize(QSize(60, 0))
        self.lb_fives_amt.setMaximumSize(QSize(60, 16777215))
        self.lb_fives_amt.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.lb_fives_amt)


        self.verticalLayout_3.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setSpacing(5)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, -1, -1, -1)
        self.lb_tens = QLabel(self.grp_bills)
        self.lb_tens.setObjectName(u"lb_tens")
        self.lb_tens.setMinimumSize(QSize(75, 0))
        self.lb_tens.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_17.addWidget(self.lb_tens)

        self.le_tens = QLineEdit(self.grp_bills)
        self.le_tens.setObjectName(u"le_tens")
        self.le_tens.setMinimumSize(QSize(40, 0))
        self.le_tens.setMaximumSize(QSize(60, 16777215))
        self.le_tens.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_17.addWidget(self.le_tens)

        self.lb_tens_amt = QLabel(self.grp_bills)
        self.lb_tens_amt.setObjectName(u"lb_tens_amt")
        self.lb_tens_amt.setMinimumSize(QSize(60, 0))
        self.lb_tens_amt.setMaximumSize(QSize(60, 16777215))
        self.lb_tens_amt.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_17.addWidget(self.lb_tens_amt)


        self.verticalLayout_3.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setSpacing(5)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, -1, -1, -1)
        self.lb_twenties = QLabel(self.grp_bills)
        self.lb_twenties.setObjectName(u"lb_twenties")
        self.lb_twenties.setMinimumSize(QSize(75, 0))
        self.lb_twenties.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_18.addWidget(self.lb_twenties)

        self.le_twenties = QLineEdit(self.grp_bills)
        self.le_twenties.setObjectName(u"le_twenties")
        self.le_twenties.setMinimumSize(QSize(40, 0))
        self.le_twenties.setMaximumSize(QSize(60, 16777215))
        self.le_twenties.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_18.addWidget(self.le_twenties)

        self.lb_twenties_amt = QLabel(self.grp_bills)
        self.lb_twenties_amt.setObjectName(u"lb_twenties_amt")
        self.lb_twenties_amt.setMinimumSize(QSize(60, 0))
        self.lb_twenties_amt.setMaximumSize(QSize(60, 16777215))
        self.lb_twenties_amt.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_18.addWidget(self.lb_twenties_amt)


        self.verticalLayout_3.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setSpacing(5)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, -1, -1, -1)
        self.lb_fifties = QLabel(self.grp_bills)
        self.lb_fifties.setObjectName(u"lb_fifties")
        self.lb_fifties.setMinimumSize(QSize(75, 0))
        self.lb_fifties.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_19.addWidget(self.lb_fifties)

        self.le_fifties = QLineEdit(self.grp_bills)
        self.le_fifties.setObjectName(u"le_fifties")
        self.le_fifties.setMinimumSize(QSize(40, 0))
        self.le_fifties.setMaximumSize(QSize(60, 16777215))
        self.le_fifties.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_19.addWidget(self.le_fifties)

        self.lb_fifties_amt = QLabel(self.grp_bills)
        self.lb_fifties_amt.setObjectName(u"lb_fifties_amt")
        self.lb_fifties_amt.setMinimumSize(QSize(60, 0))
        self.lb_fifties_amt.setMaximumSize(QSize(60, 16777215))
        self.lb_fifties_amt.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_19.addWidget(self.lb_fifties_amt)


        self.verticalLayout_3.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setSpacing(5)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, -1, -1, -1)
        self.lb_hundreds = QLabel(self.grp_bills)
        self.lb_hundreds.setObjectName(u"lb_hundreds")
        self.lb_hundreds.setMinimumSize(QSize(75, 0))
        self.lb_hundreds.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_20.addWidget(self.lb_hundreds)

        self.le_hundreds = QLineEdit(self.grp_bills)
        self.le_hundreds.setObjectName(u"le_hundreds")
        self.le_hundreds.setMinimumSize(QSize(40, 0))
        self.le_hundreds.setMaximumSize(QSize(60, 16777215))
        self.le_hundreds.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_20.addWidget(self.le_hundreds)

        self.lb_hundreds_amt = QLabel(self.grp_bills)
        self.lb_hundreds_amt.setObjectName(u"lb_hundreds_amt")
        self.lb_hundreds_amt.setMinimumSize(QSize(60, 0))
        self.lb_hundreds_amt.setMaximumSize(QSize(60, 16777215))
        self.lb_hundreds_amt.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_20.addWidget(self.lb_hundreds_amt)


        self.verticalLayout_3.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setSpacing(5)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_42 = QLabel(self.grp_bills)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(75, 0))
        self.label_42.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_21.addWidget(self.label_42)

        self.label_43 = QLabel(self.grp_bills)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMinimumSize(QSize(60, 0))
        self.label_43.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_21.addWidget(self.label_43)

        self.lb_bills_total = QLabel(self.grp_bills)
        self.lb_bills_total.setObjectName(u"lb_bills_total")
        self.lb_bills_total.setMinimumSize(QSize(60, 0))
        self.lb_bills_total.setMaximumSize(QSize(60, 16777215))
        self.lb_bills_total.setFont(font1)
        self.lb_bills_total.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_21.addWidget(self.lb_bills_total)


        self.verticalLayout_3.addLayout(self.horizontalLayout_21)


        self.verticalLayout_7.addWidget(self.grp_bills)


        self.horizontalLayout_23.addWidget(self.widget_7)


        self.verticalLayout_5.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.countCash)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(0, 90))
        self.widget_5.setMaximumSize(QSize(16777215, 90))
        self.widget_5.setStyleSheet(u"")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_12.setSpacing(5)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(10, 0, 10, 0)
        self.widget_8 = QWidget(self.widget_5)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_8 = QVBoxLayout(self.widget_8)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_12.addWidget(self.widget_8)

        self.cash_drawer_total = QLabel(self.widget_5)
        self.cash_drawer_total.setObjectName(u"cash_drawer_total")
        self.cash_drawer_total.setMinimumSize(QSize(0, 0))
        self.cash_drawer_total.setMaximumSize(QSize(16777215, 16777215))
        self.cash_drawer_total.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_12.addWidget(self.cash_drawer_total)


        self.verticalLayout_5.addWidget(self.widget_5)

        self.stackedWidget.addWidget(self.countCash)
        self.removeCash = QWidget()
        self.removeCash.setObjectName(u"removeCash")
        self.verticalLayout_12 = QVBoxLayout(self.removeCash)
        self.verticalLayout_12.setSpacing(5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 10, 0, 0)
        self.widget_9 = QWidget(self.removeCash)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_42 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_42.setSpacing(5)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.grp_coins_remove = QGroupBox(self.widget_9)
        self.grp_coins_remove.setObjectName(u"grp_coins_remove")
        self.grp_coins_remove.setFont(font1)
        self.verticalLayout_9 = QVBoxLayout(self.grp_coins_remove)
        self.verticalLayout_9.setSpacing(5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 15, 5, 5)
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setSpacing(5)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_4 = QLabel(self.grp_coins_remove)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(75, 0))
        self.label_4.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_24.addWidget(self.label_4)

        self.lb_coins_remove = QLabel(self.grp_coins_remove)
        self.lb_coins_remove.setObjectName(u"lb_coins_remove")
        self.lb_coins_remove.setMinimumSize(QSize(60, 0))
        self.lb_coins_remove.setMaximumSize(QSize(60, 16777215))
        self.lb_coins_remove.setFont(font1)
        self.lb_coins_remove.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_24.addWidget(self.lb_coins_remove)

        self.lb_coins_amount_remove = QLabel(self.grp_coins_remove)
        self.lb_coins_amount_remove.setObjectName(u"lb_coins_amount_remove")
        self.lb_coins_amount_remove.setMinimumSize(QSize(60, 0))
        self.lb_coins_amount_remove.setMaximumSize(QSize(60, 16777215))
        self.lb_coins_amount_remove.setFont(font1)
        self.lb_coins_amount_remove.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_24.addWidget(self.lb_coins_amount_remove)


        self.verticalLayout_9.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setSpacing(5)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.lb_pennies_remove = QLabel(self.grp_coins_remove)
        self.lb_pennies_remove.setObjectName(u"lb_pennies_remove")
        self.lb_pennies_remove.setMinimumSize(QSize(75, 0))
        self.lb_pennies_remove.setMaximumSize(QSize(75, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Lexend"])
        font2.setBold(False)
        self.lb_pennies_remove.setFont(font2)

        self.horizontalLayout_25.addWidget(self.lb_pennies_remove)

        self.le_pennies_remove = QLineEdit(self.grp_coins_remove)
        self.le_pennies_remove.setObjectName(u"le_pennies_remove")
        self.le_pennies_remove.setMinimumSize(QSize(60, 0))
        self.le_pennies_remove.setMaximumSize(QSize(60, 16777215))
        self.le_pennies_remove.setFont(font2)
        self.le_pennies_remove.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_25.addWidget(self.le_pennies_remove)

        self.lb_pennies_amt_remove = QLabel(self.grp_coins_remove)
        self.lb_pennies_amt_remove.setObjectName(u"lb_pennies_amt_remove")
        self.lb_pennies_amt_remove.setMinimumSize(QSize(60, 0))
        self.lb_pennies_amt_remove.setMaximumSize(QSize(60, 16777215))
        self.lb_pennies_amt_remove.setFont(font2)
        self.lb_pennies_amt_remove.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_25.addWidget(self.lb_pennies_amt_remove)


        self.verticalLayout_9.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setSpacing(5)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.lb_nickels_remove = QLabel(self.grp_coins_remove)
        self.lb_nickels_remove.setObjectName(u"lb_nickels_remove")
        self.lb_nickels_remove.setMinimumSize(QSize(75, 0))
        self.lb_nickels_remove.setMaximumSize(QSize(75, 16777215))
        self.lb_nickels_remove.setFont(font2)

        self.horizontalLayout_27.addWidget(self.lb_nickels_remove)

        self.le_nickels_remove = QLineEdit(self.grp_coins_remove)
        self.le_nickels_remove.setObjectName(u"le_nickels_remove")
        self.le_nickels_remove.setMinimumSize(QSize(60, 0))
        self.le_nickels_remove.setMaximumSize(QSize(60, 16777215))
        self.le_nickels_remove.setFont(font2)
        self.le_nickels_remove.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_27.addWidget(self.le_nickels_remove)

        self.lb_nickels_amt_remove = QLabel(self.grp_coins_remove)
        self.lb_nickels_amt_remove.setObjectName(u"lb_nickels_amt_remove")
        self.lb_nickels_amt_remove.setMinimumSize(QSize(60, 0))
        self.lb_nickels_amt_remove.setMaximumSize(QSize(60, 16777215))
        self.lb_nickels_amt_remove.setFont(font2)
        self.lb_nickels_amt_remove.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_27.addWidget(self.lb_nickels_amt_remove)


        self.verticalLayout_9.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setSpacing(5)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.lb_dimes_remove = QLabel(self.grp_coins_remove)
        self.lb_dimes_remove.setObjectName(u"lb_dimes_remove")
        self.lb_dimes_remove.setMinimumSize(QSize(75, 0))
        self.lb_dimes_remove.setMaximumSize(QSize(75, 16777215))
        self.lb_dimes_remove.setFont(font2)

        self.horizontalLayout_28.addWidget(self.lb_dimes_remove)

        self.le_dimes_remove = QLineEdit(self.grp_coins_remove)
        self.le_dimes_remove.setObjectName(u"le_dimes_remove")
        self.le_dimes_remove.setMinimumSize(QSize(60, 0))
        self.le_dimes_remove.setMaximumSize(QSize(60, 16777215))
        self.le_dimes_remove.setFont(font2)
        self.le_dimes_remove.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_28.addWidget(self.le_dimes_remove)

        self.lb_dimes_amt_remove = QLabel(self.grp_coins_remove)
        self.lb_dimes_amt_remove.setObjectName(u"lb_dimes_amt_remove")
        self.lb_dimes_amt_remove.setMinimumSize(QSize(60, 0))
        self.lb_dimes_amt_remove.setMaximumSize(QSize(60, 16777215))
        self.lb_dimes_amt_remove.setFont(font2)
        self.lb_dimes_amt_remove.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_28.addWidget(self.lb_dimes_amt_remove)


        self.verticalLayout_9.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setSpacing(5)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.lb_quarters_remove = QLabel(self.grp_coins_remove)
        self.lb_quarters_remove.setObjectName(u"lb_quarters_remove")
        self.lb_quarters_remove.setMinimumSize(QSize(75, 0))
        self.lb_quarters_remove.setMaximumSize(QSize(75, 16777215))
        self.lb_quarters_remove.setFont(font2)

        self.horizontalLayout_29.addWidget(self.lb_quarters_remove)

        self.le_quarters_remove = QLineEdit(self.grp_coins_remove)
        self.le_quarters_remove.setObjectName(u"le_quarters_remove")
        self.le_quarters_remove.setMinimumSize(QSize(60, 0))
        self.le_quarters_remove.setMaximumSize(QSize(60, 16777215))
        self.le_quarters_remove.setFont(font2)
        self.le_quarters_remove.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_29.addWidget(self.le_quarters_remove)

        self.lb_quarters_amt_remove = QLabel(self.grp_coins_remove)
        self.lb_quarters_amt_remove.setObjectName(u"lb_quarters_amt_remove")
        self.lb_quarters_amt_remove.setMinimumSize(QSize(60, 0))
        self.lb_quarters_amt_remove.setMaximumSize(QSize(60, 16777215))
        self.lb_quarters_amt_remove.setFont(font2)
        self.lb_quarters_amt_remove.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_29.addWidget(self.lb_quarters_amt_remove)


        self.verticalLayout_9.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setSpacing(5)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.lb_half_dollars_remove = QLabel(self.grp_coins_remove)
        self.lb_half_dollars_remove.setObjectName(u"lb_half_dollars_remove")
        self.lb_half_dollars_remove.setMinimumSize(QSize(75, 0))
        self.lb_half_dollars_remove.setMaximumSize(QSize(75, 16777215))
        self.lb_half_dollars_remove.setFont(font2)

        self.horizontalLayout_30.addWidget(self.lb_half_dollars_remove)

        self.le_half_dollars_remove = QLineEdit(self.grp_coins_remove)
        self.le_half_dollars_remove.setObjectName(u"le_half_dollars_remove")
        self.le_half_dollars_remove.setMinimumSize(QSize(60, 0))
        self.le_half_dollars_remove.setMaximumSize(QSize(60, 16777215))
        self.le_half_dollars_remove.setFont(font2)
        self.le_half_dollars_remove.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_30.addWidget(self.le_half_dollars_remove)

        self.lb_half_dollars_amt_remove = QLabel(self.grp_coins_remove)
        self.lb_half_dollars_amt_remove.setObjectName(u"lb_half_dollars_amt_remove")
        self.lb_half_dollars_amt_remove.setMinimumSize(QSize(60, 0))
        self.lb_half_dollars_amt_remove.setMaximumSize(QSize(60, 16777215))
        self.lb_half_dollars_amt_remove.setFont(font2)
        self.lb_half_dollars_amt_remove.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_30.addWidget(self.lb_half_dollars_amt_remove)


        self.verticalLayout_9.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setSpacing(5)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.lb_dollar_remove = QLabel(self.grp_coins_remove)
        self.lb_dollar_remove.setObjectName(u"lb_dollar_remove")
        self.lb_dollar_remove.setMinimumSize(QSize(75, 0))
        self.lb_dollar_remove.setMaximumSize(QSize(75, 16777215))
        self.lb_dollar_remove.setFont(font2)

        self.horizontalLayout_31.addWidget(self.lb_dollar_remove)

        self.le_dollar_remove = QLineEdit(self.grp_coins_remove)
        self.le_dollar_remove.setObjectName(u"le_dollar_remove")
        self.le_dollar_remove.setMinimumSize(QSize(60, 0))
        self.le_dollar_remove.setMaximumSize(QSize(60, 16777215))
        self.le_dollar_remove.setFont(font2)
        self.le_dollar_remove.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_31.addWidget(self.le_dollar_remove)

        self.lb_dollar_amt_remove = QLabel(self.grp_coins_remove)
        self.lb_dollar_amt_remove.setObjectName(u"lb_dollar_amt_remove")
        self.lb_dollar_amt_remove.setMinimumSize(QSize(60, 0))
        self.lb_dollar_amt_remove.setMaximumSize(QSize(60, 16777215))
        self.lb_dollar_amt_remove.setFont(font2)
        self.lb_dollar_amt_remove.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_31.addWidget(self.lb_dollar_amt_remove)


        self.verticalLayout_9.addLayout(self.horizontalLayout_31)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setSpacing(5)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.lb_two_dollars_remove = QLabel(self.grp_coins_remove)
        self.lb_two_dollars_remove.setObjectName(u"lb_two_dollars_remove")
        self.lb_two_dollars_remove.setMinimumSize(QSize(75, 0))
        self.lb_two_dollars_remove.setMaximumSize(QSize(75, 16777215))
        self.lb_two_dollars_remove.setFont(font2)

        self.horizontalLayout_32.addWidget(self.lb_two_dollars_remove)

        self.le_two_dollars_remove = QLineEdit(self.grp_coins_remove)
        self.le_two_dollars_remove.setObjectName(u"le_two_dollars_remove")
        self.le_two_dollars_remove.setMinimumSize(QSize(60, 0))
        self.le_two_dollars_remove.setMaximumSize(QSize(60, 16777215))
        self.le_two_dollars_remove.setFont(font2)
        self.le_two_dollars_remove.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_32.addWidget(self.le_two_dollars_remove)

        self.lb_two_dollars_amt_remove = QLabel(self.grp_coins_remove)
        self.lb_two_dollars_amt_remove.setObjectName(u"lb_two_dollars_amt_remove")
        self.lb_two_dollars_amt_remove.setMinimumSize(QSize(60, 0))
        self.lb_two_dollars_amt_remove.setMaximumSize(QSize(60, 16777215))
        self.lb_two_dollars_amt_remove.setFont(font2)
        self.lb_two_dollars_amt_remove.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_32.addWidget(self.lb_two_dollars_amt_remove)


        self.verticalLayout_9.addLayout(self.horizontalLayout_32)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setSpacing(5)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_8 = QLabel(self.grp_coins_remove)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(75, 0))
        self.label_8.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_26.addWidget(self.label_8)

        self.label_9 = QLabel(self.grp_coins_remove)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(60, 0))
        self.label_9.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_26.addWidget(self.label_9)

        self.lb_coins_total_remove = QLabel(self.grp_coins_remove)
        self.lb_coins_total_remove.setObjectName(u"lb_coins_total_remove")
        self.lb_coins_total_remove.setMinimumSize(QSize(60, 0))
        self.lb_coins_total_remove.setMaximumSize(QSize(60, 16777215))
        self.lb_coins_total_remove.setFont(font1)
        self.lb_coins_total_remove.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_26.addWidget(self.lb_coins_total_remove)


        self.verticalLayout_9.addLayout(self.horizontalLayout_26)


        self.horizontalLayout_42.addWidget(self.grp_coins_remove)

        self.grp_bills_remove = QGroupBox(self.widget_9)
        self.grp_bills_remove.setObjectName(u"grp_bills_remove")
        self.grp_bills_remove.setFont(font1)
        self.verticalLayout_10 = QVBoxLayout(self.grp_bills_remove)
        self.verticalLayout_10.setSpacing(5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(5, 15, 5, 5)
        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setSpacing(5)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_26 = QLabel(self.grp_bills_remove)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(75, 0))
        self.label_26.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_33.addWidget(self.label_26)

        self.lb_bills_remove = QLabel(self.grp_bills_remove)
        self.lb_bills_remove.setObjectName(u"lb_bills_remove")
        self.lb_bills_remove.setMinimumSize(QSize(60, 0))
        self.lb_bills_remove.setMaximumSize(QSize(60, 16777215))
        self.lb_bills_remove.setFont(font1)
        self.lb_bills_remove.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_33.addWidget(self.lb_bills_remove)

        self.lb_bills_amount_remove = QLabel(self.grp_bills_remove)
        self.lb_bills_amount_remove.setObjectName(u"lb_bills_amount_remove")
        self.lb_bills_amount_remove.setMinimumSize(QSize(60, 0))
        self.lb_bills_amount_remove.setMaximumSize(QSize(60, 16777215))
        self.lb_bills_amount_remove.setFont(font1)
        self.lb_bills_amount_remove.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_33.addWidget(self.lb_bills_amount_remove)


        self.verticalLayout_10.addLayout(self.horizontalLayout_33)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setSpacing(5)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.lb_ones_remove = QLabel(self.grp_bills_remove)
        self.lb_ones_remove.setObjectName(u"lb_ones_remove")
        self.lb_ones_remove.setMinimumSize(QSize(75, 0))
        self.lb_ones_remove.setMaximumSize(QSize(75, 16777215))
        self.lb_ones_remove.setFont(font2)

        self.horizontalLayout_34.addWidget(self.lb_ones_remove)

        self.le_ones_remove = QLineEdit(self.grp_bills_remove)
        self.le_ones_remove.setObjectName(u"le_ones_remove")
        self.le_ones_remove.setMinimumSize(QSize(60, 0))
        self.le_ones_remove.setMaximumSize(QSize(60, 16777215))
        self.le_ones_remove.setFont(font2)
        self.le_ones_remove.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_34.addWidget(self.le_ones_remove)

        self.lb_ones_amt_remove = QLabel(self.grp_bills_remove)
        self.lb_ones_amt_remove.setObjectName(u"lb_ones_amt_remove")
        self.lb_ones_amt_remove.setMinimumSize(QSize(60, 0))
        self.lb_ones_amt_remove.setMaximumSize(QSize(60, 16777215))
        self.lb_ones_amt_remove.setFont(font2)
        self.lb_ones_amt_remove.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_34.addWidget(self.lb_ones_amt_remove)


        self.verticalLayout_10.addLayout(self.horizontalLayout_34)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setSpacing(5)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.lb_twos_remove = QLabel(self.grp_bills_remove)
        self.lb_twos_remove.setObjectName(u"lb_twos_remove")
        self.lb_twos_remove.setMinimumSize(QSize(75, 0))
        self.lb_twos_remove.setMaximumSize(QSize(75, 16777215))
        self.lb_twos_remove.setFont(font2)

        self.horizontalLayout_35.addWidget(self.lb_twos_remove)

        self.le_twos_remove = QLineEdit(self.grp_bills_remove)
        self.le_twos_remove.setObjectName(u"le_twos_remove")
        self.le_twos_remove.setMinimumSize(QSize(60, 0))
        self.le_twos_remove.setMaximumSize(QSize(60, 16777215))
        self.le_twos_remove.setFont(font2)
        self.le_twos_remove.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_35.addWidget(self.le_twos_remove)

        self.lb_twos_amt_remove = QLabel(self.grp_bills_remove)
        self.lb_twos_amt_remove.setObjectName(u"lb_twos_amt_remove")
        self.lb_twos_amt_remove.setMinimumSize(QSize(60, 0))
        self.lb_twos_amt_remove.setMaximumSize(QSize(60, 16777215))
        self.lb_twos_amt_remove.setFont(font2)
        self.lb_twos_amt_remove.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_35.addWidget(self.lb_twos_amt_remove)


        self.verticalLayout_10.addLayout(self.horizontalLayout_35)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setSpacing(5)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.lb_fives_remove = QLabel(self.grp_bills_remove)
        self.lb_fives_remove.setObjectName(u"lb_fives_remove")
        self.lb_fives_remove.setMinimumSize(QSize(75, 0))
        self.lb_fives_remove.setMaximumSize(QSize(75, 16777215))
        self.lb_fives_remove.setFont(font2)

        self.horizontalLayout_36.addWidget(self.lb_fives_remove)

        self.le_fives_remove = QLineEdit(self.grp_bills_remove)
        self.le_fives_remove.setObjectName(u"le_fives_remove")
        self.le_fives_remove.setMinimumSize(QSize(60, 0))
        self.le_fives_remove.setMaximumSize(QSize(60, 16777215))
        self.le_fives_remove.setFont(font2)
        self.le_fives_remove.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_36.addWidget(self.le_fives_remove)

        self.lb_fives_amt_remove = QLabel(self.grp_bills_remove)
        self.lb_fives_amt_remove.setObjectName(u"lb_fives_amt_remove")
        self.lb_fives_amt_remove.setMinimumSize(QSize(60, 0))
        self.lb_fives_amt_remove.setMaximumSize(QSize(60, 16777215))
        self.lb_fives_amt_remove.setFont(font2)
        self.lb_fives_amt_remove.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_36.addWidget(self.lb_fives_amt_remove)


        self.verticalLayout_10.addLayout(self.horizontalLayout_36)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setSpacing(5)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.lb_tens_remove = QLabel(self.grp_bills_remove)
        self.lb_tens_remove.setObjectName(u"lb_tens_remove")
        self.lb_tens_remove.setMinimumSize(QSize(75, 0))
        self.lb_tens_remove.setMaximumSize(QSize(75, 16777215))
        self.lb_tens_remove.setFont(font2)

        self.horizontalLayout_37.addWidget(self.lb_tens_remove)

        self.le_tens_remove = QLineEdit(self.grp_bills_remove)
        self.le_tens_remove.setObjectName(u"le_tens_remove")
        self.le_tens_remove.setMinimumSize(QSize(60, 0))
        self.le_tens_remove.setMaximumSize(QSize(60, 16777215))
        self.le_tens_remove.setFont(font2)
        self.le_tens_remove.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_37.addWidget(self.le_tens_remove)

        self.lb_tens_amt_remove = QLabel(self.grp_bills_remove)
        self.lb_tens_amt_remove.setObjectName(u"lb_tens_amt_remove")
        self.lb_tens_amt_remove.setMinimumSize(QSize(60, 0))
        self.lb_tens_amt_remove.setMaximumSize(QSize(60, 16777215))
        self.lb_tens_amt_remove.setFont(font2)
        self.lb_tens_amt_remove.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_37.addWidget(self.lb_tens_amt_remove)


        self.verticalLayout_10.addLayout(self.horizontalLayout_37)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setSpacing(5)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.lb_twenties_remove = QLabel(self.grp_bills_remove)
        self.lb_twenties_remove.setObjectName(u"lb_twenties_remove")
        self.lb_twenties_remove.setMinimumSize(QSize(75, 0))
        self.lb_twenties_remove.setMaximumSize(QSize(75, 16777215))
        self.lb_twenties_remove.setFont(font2)

        self.horizontalLayout_38.addWidget(self.lb_twenties_remove)

        self.le_twenties_remove = QLineEdit(self.grp_bills_remove)
        self.le_twenties_remove.setObjectName(u"le_twenties_remove")
        self.le_twenties_remove.setMinimumSize(QSize(60, 0))
        self.le_twenties_remove.setMaximumSize(QSize(60, 16777215))
        self.le_twenties_remove.setFont(font2)
        self.le_twenties_remove.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_38.addWidget(self.le_twenties_remove)

        self.lb_twenties_amt_remove = QLabel(self.grp_bills_remove)
        self.lb_twenties_amt_remove.setObjectName(u"lb_twenties_amt_remove")
        self.lb_twenties_amt_remove.setMinimumSize(QSize(60, 0))
        self.lb_twenties_amt_remove.setMaximumSize(QSize(60, 16777215))
        self.lb_twenties_amt_remove.setFont(font2)
        self.lb_twenties_amt_remove.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_38.addWidget(self.lb_twenties_amt_remove)


        self.verticalLayout_10.addLayout(self.horizontalLayout_38)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setSpacing(5)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.lb_fifties_remove = QLabel(self.grp_bills_remove)
        self.lb_fifties_remove.setObjectName(u"lb_fifties_remove")
        self.lb_fifties_remove.setMinimumSize(QSize(75, 0))
        self.lb_fifties_remove.setMaximumSize(QSize(75, 16777215))
        self.lb_fifties_remove.setFont(font2)

        self.horizontalLayout_39.addWidget(self.lb_fifties_remove)

        self.le_fifties_remove = QLineEdit(self.grp_bills_remove)
        self.le_fifties_remove.setObjectName(u"le_fifties_remove")
        self.le_fifties_remove.setMinimumSize(QSize(60, 0))
        self.le_fifties_remove.setMaximumSize(QSize(60, 16777215))
        self.le_fifties_remove.setFont(font2)
        self.le_fifties_remove.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_39.addWidget(self.le_fifties_remove)

        self.lb_fifties_amt_remove = QLabel(self.grp_bills_remove)
        self.lb_fifties_amt_remove.setObjectName(u"lb_fifties_amt_remove")
        self.lb_fifties_amt_remove.setMinimumSize(QSize(60, 0))
        self.lb_fifties_amt_remove.setMaximumSize(QSize(60, 16777215))
        self.lb_fifties_amt_remove.setFont(font2)
        self.lb_fifties_amt_remove.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_39.addWidget(self.lb_fifties_amt_remove)


        self.verticalLayout_10.addLayout(self.horizontalLayout_39)

        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setSpacing(5)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.lb_hundreds_remove = QLabel(self.grp_bills_remove)
        self.lb_hundreds_remove.setObjectName(u"lb_hundreds_remove")
        self.lb_hundreds_remove.setMinimumSize(QSize(75, 0))
        self.lb_hundreds_remove.setMaximumSize(QSize(75, 16777215))
        self.lb_hundreds_remove.setFont(font2)

        self.horizontalLayout_40.addWidget(self.lb_hundreds_remove)

        self.le_hundreds_remove = QLineEdit(self.grp_bills_remove)
        self.le_hundreds_remove.setObjectName(u"le_hundreds_remove")
        self.le_hundreds_remove.setMinimumSize(QSize(60, 0))
        self.le_hundreds_remove.setMaximumSize(QSize(60, 16777215))
        self.le_hundreds_remove.setFont(font2)
        self.le_hundreds_remove.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_40.addWidget(self.le_hundreds_remove)

        self.lb_hundreds_amt_remove = QLabel(self.grp_bills_remove)
        self.lb_hundreds_amt_remove.setObjectName(u"lb_hundreds_amt_remove")
        self.lb_hundreds_amt_remove.setMinimumSize(QSize(60, 0))
        self.lb_hundreds_amt_remove.setMaximumSize(QSize(60, 16777215))
        self.lb_hundreds_amt_remove.setFont(font2)
        self.lb_hundreds_amt_remove.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_40.addWidget(self.lb_hundreds_amt_remove)


        self.verticalLayout_10.addLayout(self.horizontalLayout_40)

        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setSpacing(5)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.label_45 = QLabel(self.grp_bills_remove)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setMinimumSize(QSize(75, 0))
        self.label_45.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_41.addWidget(self.label_45)

        self.label_46 = QLabel(self.grp_bills_remove)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMinimumSize(QSize(60, 0))
        self.label_46.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_41.addWidget(self.label_46)

        self.lb_bills_total_remove = QLabel(self.grp_bills_remove)
        self.lb_bills_total_remove.setObjectName(u"lb_bills_total_remove")
        self.lb_bills_total_remove.setMinimumSize(QSize(60, 0))
        self.lb_bills_total_remove.setMaximumSize(QSize(60, 16777215))
        self.lb_bills_total_remove.setFont(font1)
        self.lb_bills_total_remove.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_41.addWidget(self.lb_bills_total_remove)


        self.verticalLayout_10.addLayout(self.horizontalLayout_41)


        self.horizontalLayout_42.addWidget(self.grp_bills_remove)


        self.verticalLayout_12.addWidget(self.widget_9)

        self.widget_10 = QWidget(self.removeCash)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setMinimumSize(QSize(0, 90))
        self.widget_10.setMaximumSize(QSize(16777215, 90))
        self.horizontalLayout_44 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_44.setSpacing(5)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(10, 0, 10, 0)
        self.widget_11 = QWidget(self.widget_10)
        self.widget_11.setObjectName(u"widget_11")
        self.verticalLayout_11 = QVBoxLayout(self.widget_11)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setSpacing(5)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, -1, 0, -1)
        self.lb_starting_cash = QLabel(self.widget_11)
        self.lb_starting_cash.setObjectName(u"lb_starting_cash")
        self.lb_starting_cash.setMinimumSize(QSize(0, 35))
        self.lb_starting_cash.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_43.addWidget(self.lb_starting_cash)

        self.dbl_starting_cash = QDoubleSpinBox(self.widget_11)
        self.dbl_starting_cash.setObjectName(u"dbl_starting_cash")
        self.dbl_starting_cash.setMinimumSize(QSize(0, 35))
        self.dbl_starting_cash.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_43.addWidget(self.dbl_starting_cash)


        self.verticalLayout_11.addLayout(self.horizontalLayout_43)

        self.pb_remove_cash = QPushButton(self.widget_11)
        self.pb_remove_cash.setObjectName(u"pb_remove_cash")
        self.pb_remove_cash.setMinimumSize(QSize(0, 40))
        self.pb_remove_cash.setMaximumSize(QSize(16777215, 40))
        icon = QIcon()
        icon.addFile(u":/Icons/calculator.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_remove_cash.setIcon(icon)
        self.pb_remove_cash.setIconSize(QSize(20, 20))

        self.verticalLayout_11.addWidget(self.pb_remove_cash)


        self.horizontalLayout_44.addWidget(self.widget_11)

        self.lb_cash_drawer_total_remove = QLabel(self.widget_10)
        self.lb_cash_drawer_total_remove.setObjectName(u"lb_cash_drawer_total_remove")
        self.lb_cash_drawer_total_remove.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_44.addWidget(self.lb_cash_drawer_total_remove)


        self.verticalLayout_12.addWidget(self.widget_10)

        self.stackedWidget.addWidget(self.removeCash)

        self.horizontalLayout_22.addWidget(self.stackedWidget)

        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(150, 0))
        self.verticalLayout = QVBoxLayout(self.widget_3)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 10, 0, 10)
        self.pb_next_page = QPushButton(self.widget_3)
        self.pb_next_page.setObjectName(u"pb_next_page")
        self.pb_next_page.setMinimumSize(QSize(150, 35))
        self.pb_next_page.setMaximumSize(QSize(150, 35))
        icon1 = QIcon()
        icon1.addFile(u":/Icons/next.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_next_page.setIcon(icon1)
        self.pb_next_page.setIconSize(QSize(25, 25))

        self.verticalLayout.addWidget(self.pb_next_page)

        self.pb_previous_page = QPushButton(self.widget_3)
        self.pb_previous_page.setObjectName(u"pb_previous_page")
        self.pb_previous_page.setMinimumSize(QSize(150, 35))
        self.pb_previous_page.setMaximumSize(QSize(150, 35))
        icon2 = QIcon()
        icon2.addFile(u":/Icons/previous.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_previous_page.setIcon(icon2)
        self.pb_previous_page.setIconSize(QSize(25, 25))

        self.verticalLayout.addWidget(self.pb_previous_page)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pb_cancel = QPushButton(self.widget_3)
        self.pb_cancel.setObjectName(u"pb_cancel")
        self.pb_cancel.setMinimumSize(QSize(150, 35))
        self.pb_cancel.setMaximumSize(QSize(150, 35))
        icon3 = QIcon()
        icon3.addFile(u":/Icons/cancel.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_cancel.setIcon(icon3)
        self.pb_cancel.setIconSize(QSize(25, 25))

        self.verticalLayout.addWidget(self.pb_cancel)


        self.horizontalLayout_22.addWidget(self.widget_3)


        self.verticalLayout_4.addWidget(self.widget_2)


        self.retranslateUi(CashCounter)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(CashCounter)
    # setupUi

    def retranslateUi(self, CashCounter):
        CashCounter.setWindowTitle(QCoreApplication.translate("CashCounter", u"Cash Counter", None))
        self.lb_dialog_title.setText(QCoreApplication.translate("CashCounter", u"Cash Counter", None))
        self.grp_coins.setTitle(QCoreApplication.translate("CashCounter", u"Coins", None))
        self.label_5.setText("")
        self.lb_coins_count.setText(QCoreApplication.translate("CashCounter", u"COUNT", None))
        self.lb_coins_amount.setText(QCoreApplication.translate("CashCounter", u"AMOUNT", None))
        self.lb_pennies.setText(QCoreApplication.translate("CashCounter", u"Pennies:", None))
        self.lb_pennies_amt.setText(QCoreApplication.translate("CashCounter", u"$ 0.00", None))
        self.lb_nickels.setText(QCoreApplication.translate("CashCounter", u"Nickels:", None))
        self.lb_nickels_amt.setText(QCoreApplication.translate("CashCounter", u"$ 0.00", None))
        self.lb_dimes.setText(QCoreApplication.translate("CashCounter", u"Dimes:", None))
        self.lb_dimes_amt.setText(QCoreApplication.translate("CashCounter", u"$ 0.00", None))
        self.lb_quarters.setText(QCoreApplication.translate("CashCounter", u"Quarters:", None))
        self.lb_quarters_amt.setText(QCoreApplication.translate("CashCounter", u"$ 0.00", None))
        self.lb_half_dollars.setText(QCoreApplication.translate("CashCounter", u"Half Dollars:", None))
        self.lb_half_dollars_amt.setText(QCoreApplication.translate("CashCounter", u"$ 0.00", None))
        self.lb_dollars.setText(QCoreApplication.translate("CashCounter", u"Dollars:", None))
        self.lb_dollars_amt.setText(QCoreApplication.translate("CashCounter", u"$ 0.00", None))
        self.lb_two_dollars.setText(QCoreApplication.translate("CashCounter", u"Two Dollars:", None))
        self.lb_two_dollars_amt.setText(QCoreApplication.translate("CashCounter", u"$ 0.00", None))
        self.label_20.setText("")
        self.label_22.setText("")
        self.lb_coins_total.setText(QCoreApplication.translate("CashCounter", u"$ 0.00", None))
        self.grp_bills.setTitle(QCoreApplication.translate("CashCounter", u"Bills", None))
        self.label_25.setText("")
        self.lb_bills_count.setText(QCoreApplication.translate("CashCounter", u"COUNT", None))
        self.lb_bills_amount.setText(QCoreApplication.translate("CashCounter", u"AMOUNT", None))
        self.lb_ones.setText(QCoreApplication.translate("CashCounter", u"Ones:", None))
        self.lb_ones_amt.setText(QCoreApplication.translate("CashCounter", u"$ 0.00", None))
        self.lb_twos.setText(QCoreApplication.translate("CashCounter", u"Twos:", None))
        self.lb_twos_amt.setText(QCoreApplication.translate("CashCounter", u"$ 0.00", None))
        self.lb_fives.setText(QCoreApplication.translate("CashCounter", u"Fives:", None))
        self.lb_fives_amt.setText(QCoreApplication.translate("CashCounter", u"$ 0.00", None))
        self.lb_tens.setText(QCoreApplication.translate("CashCounter", u"Tens:", None))
        self.lb_tens_amt.setText(QCoreApplication.translate("CashCounter", u"$ 0.00", None))
        self.lb_twenties.setText(QCoreApplication.translate("CashCounter", u"Twenties:", None))
        self.lb_twenties_amt.setText(QCoreApplication.translate("CashCounter", u"$ 0.00", None))
        self.lb_fifties.setText(QCoreApplication.translate("CashCounter", u"Fifties:", None))
        self.lb_fifties_amt.setText(QCoreApplication.translate("CashCounter", u"$ 0.00", None))
        self.lb_hundreds.setText(QCoreApplication.translate("CashCounter", u"Hundreds:", None))
        self.lb_hundreds_amt.setText(QCoreApplication.translate("CashCounter", u"$ 0.00", None))
        self.label_42.setText("")
        self.label_43.setText("")
        self.lb_bills_total.setText(QCoreApplication.translate("CashCounter", u"$ 0.00", None))
        self.cash_drawer_total.setText(QCoreApplication.translate("CashCounter", u"$ 0.00", None))
        self.grp_coins_remove.setTitle(QCoreApplication.translate("CashCounter", u"Coins", None))
        self.label_4.setText("")
        self.lb_coins_remove.setText(QCoreApplication.translate("CashCounter", u"REMOVE", None))
        self.lb_coins_amount_remove.setText(QCoreApplication.translate("CashCounter", u"AMOUNT", None))
        self.lb_pennies_remove.setText(QCoreApplication.translate("CashCounter", u"Pennies:", None))
        self.lb_pennies_amt_remove.setText(QCoreApplication.translate("CashCounter", u"$ 0.00", None))
        self.lb_nickels_remove.setText(QCoreApplication.translate("CashCounter", u"Nickels:", None))
        self.lb_nickels_amt_remove.setText(QCoreApplication.translate("CashCounter", u"$ 0.00", None))
        self.lb_dimes_remove.setText(QCoreApplication.translate("CashCounter", u"Dimes:", None))
        self.lb_dimes_amt_remove.setText(QCoreApplication.translate("CashCounter", u"$ 0.00", None))
        self.lb_quarters_remove.setText(QCoreApplication.translate("CashCounter", u"Quarters:", None))
        self.lb_quarters_amt_remove.setText(QCoreApplication.translate("CashCounter", u"$ 0.00", None))
        self.lb_half_dollars_remove.setText(QCoreApplication.translate("CashCounter", u"Half Dollars:", None))
        self.lb_half_dollars_amt_remove.setText(QCoreApplication.translate("CashCounter", u"$ 0.00", None))
        self.lb_dollar_remove.setText(QCoreApplication.translate("CashCounter", u"Dollars:", None))
        self.lb_dollar_amt_remove.setText(QCoreApplication.translate("CashCounter", u"$ 0.00", None))
        self.lb_two_dollars_remove.setText(QCoreApplication.translate("CashCounter", u"Two Dollars:", None))
        self.lb_two_dollars_amt_remove.setText(QCoreApplication.translate("CashCounter", u"$ 0.00", None))
        self.label_8.setText("")
        self.label_9.setText("")
        self.lb_coins_total_remove.setText(QCoreApplication.translate("CashCounter", u"$ 0.00", None))
        self.grp_bills_remove.setTitle(QCoreApplication.translate("CashCounter", u"Bills", None))
        self.label_26.setText("")
        self.lb_bills_remove.setText(QCoreApplication.translate("CashCounter", u"REMOVE", None))
        self.lb_bills_amount_remove.setText(QCoreApplication.translate("CashCounter", u"AMOUNT", None))
        self.lb_ones_remove.setText(QCoreApplication.translate("CashCounter", u"Ones:", None))
        self.lb_ones_amt_remove.setText(QCoreApplication.translate("CashCounter", u"$ 0.00", None))
        self.lb_twos_remove.setText(QCoreApplication.translate("CashCounter", u"Twos:", None))
        self.lb_twos_amt_remove.setText(QCoreApplication.translate("CashCounter", u"$ 0.00", None))
        self.lb_fives_remove.setText(QCoreApplication.translate("CashCounter", u"Fives:", None))
        self.lb_fives_amt_remove.setText(QCoreApplication.translate("CashCounter", u"$ 0.00", None))
        self.lb_tens_remove.setText(QCoreApplication.translate("CashCounter", u"Tens:", None))
        self.lb_tens_amt_remove.setText(QCoreApplication.translate("CashCounter", u"$ 0.00", None))
        self.lb_twenties_remove.setText(QCoreApplication.translate("CashCounter", u"Twenties:", None))
        self.lb_twenties_amt_remove.setText(QCoreApplication.translate("CashCounter", u"$ 0.00", None))
        self.lb_fifties_remove.setText(QCoreApplication.translate("CashCounter", u"Fifties:", None))
        self.lb_fifties_amt_remove.setText(QCoreApplication.translate("CashCounter", u"$ 0.00", None))
        self.lb_hundreds_remove.setText(QCoreApplication.translate("CashCounter", u"Hundreds:", None))
        self.lb_hundreds_amt_remove.setText(QCoreApplication.translate("CashCounter", u"$ 0.00", None))
        self.label_45.setText("")
        self.label_46.setText("")
        self.lb_bills_total_remove.setText(QCoreApplication.translate("CashCounter", u"$ 0.00", None))
        self.lb_starting_cash.setText(QCoreApplication.translate("CashCounter", u"Starting Cash:", None))
        self.pb_remove_cash.setText(QCoreApplication.translate("CashCounter", u"Calculate Cash to Remove", None))
        self.lb_cash_drawer_total_remove.setText(QCoreApplication.translate("CashCounter", u"$ 0.00", None))
        self.pb_next_page.setText(QCoreApplication.translate("CashCounter", u"Next", None))
        self.pb_previous_page.setText(QCoreApplication.translate("CashCounter", u"Previous", None))
        self.pb_cancel.setText(QCoreApplication.translate("CashCounter", u"Cancel", None))
    # retranslateUi

