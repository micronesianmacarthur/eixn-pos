# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customer_manager_window.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QListView, QPushButton,
    QSizePolicy, QSpacerItem, QTableView, QVBoxLayout,
    QWidget)
import icons_rc

class Ui_CustomerManagerWindow(object):
    def setupUi(self, CustomerManagerWindow):
        if not CustomerManagerWindow.objectName():
            CustomerManagerWindow.setObjectName(u"CustomerManagerWindow")
        CustomerManagerWindow.resize(980, 1000)
        CustomerManagerWindow.setMinimumSize(QSize(980, 980))
        CustomerManagerWindow.setStyleSheet(u"QWidget{\n"
"	border: 1px solid #ccc;\n"
"}\n"
"\n"
"QComboBox {\n"
"	background-color: #9f9f9f;\n"
"	color: #1a1a1a;\n"
"	border: None;\n"
"	border-top-right-radius: 10px;\n"
"	bprder-bottom-right-radius: 10px;\n"
"}\n"
"QComboBox::drop-down {\n"
"	border: None;\n"
"}")
        self.verticalLayout = QVBoxLayout(CustomerManagerWindow)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.wd_customer_win_header = QWidget(CustomerManagerWindow)
        self.wd_customer_win_header.setObjectName(u"wd_customer_win_header")
        self.wd_customer_win_header.setMinimumSize(QSize(0, 45))
        self.wd_customer_win_header.setMaximumSize(QSize(16777215, 45))
        self.horizontalLayout = QHBoxLayout(self.wd_customer_win_header)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lb_customer_win_title = QLabel(self.wd_customer_win_header)
        self.lb_customer_win_title.setObjectName(u"lb_customer_win_title")
        self.lb_customer_win_title.setMinimumSize(QSize(0, 45))
        self.lb_customer_win_title.setMaximumSize(QSize(16777215, 45))
        self.lb_customer_win_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.lb_customer_win_title)

        self.pb_customer_win_close = QPushButton(self.wd_customer_win_header)
        self.pb_customer_win_close.setObjectName(u"pb_customer_win_close")
        self.pb_customer_win_close.setMinimumSize(QSize(120, 45))
        self.pb_customer_win_close.setMaximumSize(QSize(120, 45))
        icon = QIcon()
        icon.addFile(u":/Icons/close_white.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_customer_win_close.setIcon(icon)
        self.pb_customer_win_close.setIconSize(QSize(18, 18))

        self.horizontalLayout.addWidget(self.pb_customer_win_close)


        self.verticalLayout.addWidget(self.wd_customer_win_header)

        self.widget_2 = QWidget(CustomerManagerWindow)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.wd_customer_win_main = QWidget(self.widget_2)
        self.wd_customer_win_main.setObjectName(u"wd_customer_win_main")
        self.verticalLayout_5 = QVBoxLayout(self.wd_customer_win_main)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.wd_customer_win_main)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pb_create_customer = QPushButton(self.widget_5)
        self.pb_create_customer.setObjectName(u"pb_create_customer")
        self.pb_create_customer.setMinimumSize(QSize(180, 35))
        self.pb_create_customer.setMaximumSize(QSize(180, 35))
        icon1 = QIcon()
        icon1.addFile(u":/Icons/add_white.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_create_customer.setIcon(icon1)
        self.pb_create_customer.setIconSize(QSize(18, 18))

        self.horizontalLayout_4.addWidget(self.pb_create_customer)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.le_search_customer = QLineEdit(self.widget_5)
        self.le_search_customer.setObjectName(u"le_search_customer")
        self.le_search_customer.setMinimumSize(QSize(200, 35))
        self.le_search_customer.setMaximumSize(QSize(200, 35))

        self.horizontalLayout_4.addWidget(self.le_search_customer)

        self.pb_search_customer = QPushButton(self.widget_5)
        self.pb_search_customer.setObjectName(u"pb_search_customer")
        self.pb_search_customer.setMinimumSize(QSize(50, 35))
        self.pb_search_customer.setMaximumSize(QSize(50, 35))
        icon2 = QIcon()
        icon2.addFile(u":/Icons/search_white.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_search_customer.setIcon(icon2)
        self.pb_search_customer.setIconSize(QSize(18, 18))

        self.horizontalLayout_4.addWidget(self.pb_search_customer)


        self.verticalLayout_5.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.wd_customer_win_main)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_4 = QVBoxLayout(self.widget_6)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_8 = QWidget(self.widget_6)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_3 = QVBoxLayout(self.widget_8)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_9 = QWidget(self.widget_8)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.lb_customer_table = QLabel(self.widget_9)
        self.lb_customer_table.setObjectName(u"lb_customer_table")
        self.lb_customer_table.setMinimumSize(QSize(100, 35))
        self.lb_customer_table.setMaximumSize(QSize(100, 35))

        self.horizontalLayout_5.addWidget(self.lb_customer_table)

        self.widget_7 = QWidget(self.widget_9)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.horizontalLayout_5.addWidget(self.widget_7)


        self.verticalLayout_3.addWidget(self.widget_9)

        self.tbl_customer = QTableView(self.widget_8)
        self.tbl_customer.setObjectName(u"tbl_customer")

        self.verticalLayout_3.addWidget(self.tbl_customer)


        self.verticalLayout_4.addWidget(self.widget_8)


        self.verticalLayout_5.addWidget(self.widget_6)


        self.horizontalLayout_2.addWidget(self.wd_customer_win_main)

        self.wd_customer_win_side = QWidget(self.widget_2)
        self.wd_customer_win_side.setObjectName(u"wd_customer_win_side")
        self.wd_customer_win_side.setMinimumSize(QSize(400, 0))
        self.wd_customer_win_side.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.wd_customer_win_side)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.wd_detail_view = QWidget(self.wd_customer_win_side)
        self.wd_detail_view.setObjectName(u"wd_detail_view")
        self.wd_detail_view.setMinimumSize(QSize(0, 100))
        self.verticalLayout_6 = QVBoxLayout(self.wd_detail_view)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget = QWidget(self.wd_detail_view)
        self.widget.setObjectName(u"widget")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 54, 17))
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 10, 54, 17))

        self.verticalLayout_6.addWidget(self.widget)

        self.pushButton = QPushButton(self.wd_detail_view)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_6.addWidget(self.pushButton)


        self.verticalLayout_2.addWidget(self.wd_detail_view)

        self.wd_transactions_view = QWidget(self.wd_customer_win_side)
        self.wd_transactions_view.setObjectName(u"wd_transactions_view")
        self.wd_transactions_view.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_7 = QVBoxLayout(self.wd_transactions_view)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.lb_sales_list = QLabel(self.wd_transactions_view)
        self.lb_sales_list.setObjectName(u"lb_sales_list")

        self.verticalLayout_7.addWidget(self.lb_sales_list)

        self.ls_sales = QListView(self.wd_transactions_view)
        self.ls_sales.setObjectName(u"ls_sales")

        self.verticalLayout_7.addWidget(self.ls_sales)

        self.pb_open_transaction = QPushButton(self.wd_transactions_view)
        self.pb_open_transaction.setObjectName(u"pb_open_transaction")
        self.pb_open_transaction.setMinimumSize(QSize(0, 35))
        self.pb_open_transaction.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_7.addWidget(self.pb_open_transaction)


        self.verticalLayout_2.addWidget(self.wd_transactions_view)

        self.wd_actions_view = QWidget(self.wd_customer_win_side)
        self.wd_actions_view.setObjectName(u"wd_actions_view")
        self.wd_actions_view.setMaximumSize(QSize(16777215, 160))
        self.verticalLayout_8 = QVBoxLayout(self.wd_actions_view)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.lb_charge_label = QLabel(self.wd_actions_view)
        self.lb_charge_label.setObjectName(u"lb_charge_label")
        self.lb_charge_label.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_8.addWidget(self.lb_charge_label)

        self.line = QFrame(self.wd_actions_view)
        self.line.setObjectName(u"line")
        self.line.setMaximumSize(QSize(16777215, 1))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_8.addWidget(self.line)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.lb_dollar_sign = QLabel(self.wd_actions_view)
        self.lb_dollar_sign.setObjectName(u"lb_dollar_sign")
        self.lb_dollar_sign.setMinimumSize(QSize(0, 45))
        self.lb_dollar_sign.setMaximumSize(QSize(45, 45))

        self.horizontalLayout_11.addWidget(self.lb_dollar_sign)

        self.lb_charge_balance = QLabel(self.wd_actions_view)
        self.lb_charge_balance.setObjectName(u"lb_charge_balance")
        self.lb_charge_balance.setMinimumSize(QSize(0, 45))
        self.lb_charge_balance.setMaximumSize(QSize(16777215, 45))
        self.lb_charge_balance.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.lb_charge_balance)


        self.verticalLayout_8.addLayout(self.horizontalLayout_11)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)

        self.pb_make_payment = QPushButton(self.wd_actions_view)
        self.pb_make_payment.setObjectName(u"pb_make_payment")
        self.pb_make_payment.setMinimumSize(QSize(0, 45))
        self.pb_make_payment.setMaximumSize(QSize(16777215, 45))

        self.verticalLayout_8.addWidget(self.pb_make_payment)


        self.verticalLayout_2.addWidget(self.wd_actions_view)


        self.horizontalLayout_2.addWidget(self.wd_customer_win_side)


        self.verticalLayout.addWidget(self.widget_2)


        self.retranslateUi(CustomerManagerWindow)

        QMetaObject.connectSlotsByName(CustomerManagerWindow)
    # setupUi

    def retranslateUi(self, CustomerManagerWindow):
        CustomerManagerWindow.setWindowTitle(QCoreApplication.translate("CustomerManagerWindow", u"Customer Manager", None))
        self.lb_customer_win_title.setText(QCoreApplication.translate("CustomerManagerWindow", u"Customer Manager", None))
        self.pb_customer_win_close.setText(QCoreApplication.translate("CustomerManagerWindow", u"Close", None))
        self.pb_create_customer.setText(QCoreApplication.translate("CustomerManagerWindow", u"Create New Customer", None))
        self.le_search_customer.setPlaceholderText(QCoreApplication.translate("CustomerManagerWindow", u"Search Customer by Name", None))
        self.pb_search_customer.setText("")
        self.lb_customer_table.setText(QCoreApplication.translate("CustomerManagerWindow", u"Customer Table", None))
        self.label.setText(QCoreApplication.translate("CustomerManagerWindow", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("CustomerManagerWindow", u"TextLabel", None))
        self.pushButton.setText(QCoreApplication.translate("CustomerManagerWindow", u"PushButton", None))
        self.lb_sales_list.setText(QCoreApplication.translate("CustomerManagerWindow", u"TextLabel", None))
        self.pb_open_transaction.setText(QCoreApplication.translate("CustomerManagerWindow", u"PushButton", None))
        self.lb_charge_label.setText(QCoreApplication.translate("CustomerManagerWindow", u"TextLabel", None))
        self.lb_dollar_sign.setText(QCoreApplication.translate("CustomerManagerWindow", u"TextLabel", None))
        self.lb_charge_balance.setText(QCoreApplication.translate("CustomerManagerWindow", u"TextLabel", None))
        self.pb_make_payment.setText(QCoreApplication.translate("CustomerManagerWindow", u"PushButton", None))
    # retranslateUi

