# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customers_list_window.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QListView,
    QPushButton, QSizePolicy, QTableView, QVBoxLayout,
    QWidget)
import icons_rc

class Ui_CustomersListWindow(object):
    def setupUi(self, CustomersListWindow):
        if not CustomersListWindow.objectName():
            CustomersListWindow.setObjectName(u"CustomersListWindow")
        CustomersListWindow.resize(1000, 980)
        CustomersListWindow.setMinimumSize(QSize(980, 980))
        font = QFont()
        font.setFamilies([u"Lexend"])
        font.setPointSize(10)
        CustomersListWindow.setFont(font)
        CustomersListWindow.setStyleSheet(u"#CustomersListWindow {\n"
"	background-color: #1a1a1a;\n"
"}")
        self.verticalLayout = QVBoxLayout(CustomersListWindow)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(CustomersListWindow)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 45))
        self.widget.setMaximumSize(QSize(16777215, 45))
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lb_customer_title = QLabel(self.widget)
        self.lb_customer_title.setObjectName(u"lb_customer_title")
        self.lb_customer_title.setMinimumSize(QSize(0, 35))
        self.lb_customer_title.setMaximumSize(QSize(16777215, 35))
        font1 = QFont()
        font1.setFamilies([u"Lexend"])
        font1.setPointSize(16)
        font1.setBold(True)
        self.lb_customer_title.setFont(font1)
        self.lb_customer_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lb_customer_title)

        self.pb_customer_close = QPushButton(self.widget)
        self.pb_customer_close.setObjectName(u"pb_customer_close")
        self.pb_customer_close.setMinimumSize(QSize(120, 35))
        self.pb_customer_close.setMaximumSize(QSize(120, 35))
        self.pb_customer_close.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/Icons/close_white.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_customer_close.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.pb_customer_close)


        self.verticalLayout.addWidget(self.widget)

        self.wd_content = QWidget(CustomersListWindow)
        self.wd_content.setObjectName(u"wd_content")
        self.horizontalLayout = QHBoxLayout(self.wd_content)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.wd_all_view = QWidget(self.wd_content)
        self.wd_all_view.setObjectName(u"wd_all_view")
        self.verticalLayout_2 = QVBoxLayout(self.wd_all_view)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pb_create_customer = QPushButton(self.wd_all_view)
        self.pb_create_customer.setObjectName(u"pb_create_customer")
        self.pb_create_customer.setMinimumSize(QSize(180, 35))
        self.pb_create_customer.setMaximumSize(QSize(180, 16777215))
        self.pb_create_customer.setFont(font)
        self.pb_create_customer.setStyleSheet(u"#pb_create_customer {\n"
"	background-color: #3f3f3f;\n"
"	color: white;\n"
"	border: None;\n"
"	border-radius: 5px;\n"
"}\n"
"#pb_create_customer:hover {\n"
"	background-color: #4f4f4f;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/add_white.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_create_customer.setIcon(icon1)
        self.pb_create_customer.setFlat(False)

        self.verticalLayout_2.addWidget(self.pb_create_customer)

        self.wd_customer_search = QWidget(self.wd_all_view)
        self.wd_customer_search.setObjectName(u"wd_customer_search")
        self.wd_customer_search.setMinimumSize(QSize(0, 40))
        self.wd_customer_search.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_2 = QHBoxLayout(self.wd_customer_search)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.le_customer_search = QLineEdit(self.wd_customer_search)
        self.le_customer_search.setObjectName(u"le_customer_search")
        self.le_customer_search.setMinimumSize(QSize(0, 35))
        self.le_customer_search.setFont(font)
        self.le_customer_search.setStyleSheet(u"color: #000;\n"
"background-color: #fff;\n"
"border: None;\n"
"border-radius: 5px;")

        self.horizontalLayout_2.addWidget(self.le_customer_search)

        self.pb_customer_search = QPushButton(self.wd_customer_search)
        self.pb_customer_search.setObjectName(u"pb_customer_search")
        self.pb_customer_search.setMinimumSize(QSize(120, 35))
        self.pb_customer_search.setFont(font)
        self.pb_customer_search.setStyleSheet(u"#pb_customer_search {\n"
"	background-color: #3f3f3f;\n"
"	color: #fff;\n"
"	border: None;\n"
"	border-radius: 5px;\n"
"}\n"
"#pb_customer_search:hover {\n"
"	background-color: #4f4f4f;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/search_white.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_customer_search.setIcon(icon2)
        self.pb_customer_search.setIconSize(QSize(16, 16))

        self.horizontalLayout_2.addWidget(self.pb_customer_search)


        self.verticalLayout_2.addWidget(self.wd_customer_search)

        self.tbl_customers = QTableView(self.wd_all_view)
        self.tbl_customers.setObjectName(u"tbl_customers")
        self.tbl_customers.setStyleSheet(u"#tbl_customers {\n"
"	background-color: #2f2f2f;\n"
"	color: white;\n"
"	border: None;\n"
"	border-radius: 5px;\n"
"}")

        self.verticalLayout_2.addWidget(self.tbl_customers)


        self.horizontalLayout.addWidget(self.wd_all_view)

        self.wd_detail_view = QWidget(self.wd_content)
        self.wd_detail_view.setObjectName(u"wd_detail_view")
        self.wd_detail_view.setMinimumSize(QSize(400, 0))
        self.wd_detail_view.setMaximumSize(QSize(400, 16777215))
        self.wd_detail_view.setStyleSheet(u"#wd_detail_view QFrame {\n"
"	border: None;\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.wd_detail_view)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.wd_customer_details = QWidget(self.wd_detail_view)
        self.wd_customer_details.setObjectName(u"wd_customer_details")
        self.wd_customer_details.setMinimumSize(QSize(380, 0))
        self.wd_customer_details.setMaximumSize(QSize(400, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Lexend"])
        self.wd_customer_details.setFont(font2)
        self.wd_customer_details.setStyleSheet(u"#wd_customer_details {\n"
"	background-color: #fff;\n"
"	border: None;\n"
"	border-radius: 10px;\n"
"	color: #1a1a1a;\n"
"}\n"
"\n"
"#wd_customer_details QLabel {\n"
"	border: None;\n"
"	color: #0c0c0c;\n"
"	font-size: 14px;\n"
"	font-weight: Normal;\n"
"}")
        self.formLayout = QFormLayout(self.wd_customer_details)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.lb_first_name = QLabel(self.wd_customer_details)
        self.lb_first_name.setObjectName(u"lb_first_name")
        self.lb_first_name.setMinimumSize(QSize(80, 0))
        font3 = QFont()
        font3.setFamilies([u"Lexend"])
        font3.setBold(False)
        self.lb_first_name.setFont(font3)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lb_first_name)

        self.lb_firstName_val = QLabel(self.wd_customer_details)
        self.lb_firstName_val.setObjectName(u"lb_firstName_val")
        self.lb_firstName_val.setMinimumSize(QSize(120, 0))
        self.lb_firstName_val.setFont(font3)
        self.lb_firstName_val.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lb_firstName_val)

        self.lb_last_name = QLabel(self.wd_customer_details)
        self.lb_last_name.setObjectName(u"lb_last_name")
        self.lb_last_name.setMinimumSize(QSize(80, 0))
        self.lb_last_name.setFont(font3)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lb_last_name)

        self.lb_lastName_val = QLabel(self.wd_customer_details)
        self.lb_lastName_val.setObjectName(u"lb_lastName_val")
        self.lb_lastName_val.setMinimumSize(QSize(120, 0))
        self.lb_lastName_val.setFont(font3)
        self.lb_lastName_val.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.lb_lastName_val)

        self.lb_phone = QLabel(self.wd_customer_details)
        self.lb_phone.setObjectName(u"lb_phone")
        self.lb_phone.setMinimumSize(QSize(80, 0))
        self.lb_phone.setFont(font3)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lb_phone)

        self.lb_phone_val = QLabel(self.wd_customer_details)
        self.lb_phone_val.setObjectName(u"lb_phone_val")
        self.lb_phone_val.setMinimumSize(QSize(120, 0))
        self.lb_phone_val.setFont(font3)
        self.lb_phone_val.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.lb_phone_val)

        self.lb_email = QLabel(self.wd_customer_details)
        self.lb_email.setObjectName(u"lb_email")
        self.lb_email.setMinimumSize(QSize(80, 0))
        self.lb_email.setFont(font3)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lb_email)

        self.lb_email_val = QLabel(self.wd_customer_details)
        self.lb_email_val.setObjectName(u"lb_email_val")
        self.lb_email_val.setMinimumSize(QSize(120, 0))
        self.lb_email_val.setFont(font3)
        self.lb_email_val.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.lb_email_val)


        self.verticalLayout_5.addWidget(self.wd_customer_details)

        self.pb_edit_customer = QPushButton(self.wd_detail_view)
        self.pb_edit_customer.setObjectName(u"pb_edit_customer")
        self.pb_edit_customer.setMinimumSize(QSize(0, 35))
        self.pb_edit_customer.setMaximumSize(QSize(16777215, 35))
        self.pb_edit_customer.setFont(font)
        self.pb_edit_customer.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.pb_edit_customer.setStyleSheet(u"#pb_edit_customer {\n"
"	background-color: #6f6f6f;\n"
"	color: white;\n"
"	border: None;\n"
"	border-radius: 5px;\n"
"}\n"
"#pb_edit_customer:hover {\n"
"	background-color: #8f8f8f;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/Icons/edit_white.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_edit_customer.setIcon(icon3)

        self.verticalLayout_5.addWidget(self.pb_edit_customer)

        self.widget_2 = QWidget(self.wd_detail_view)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lw_customer_sales = QListView(self.widget_2)
        self.lw_customer_sales.setObjectName(u"lw_customer_sales")
        self.lw_customer_sales.setStyleSheet(u"#lw_customer_sales {\n"
"	background-color: #2f2f2f;\n"
"}")

        self.verticalLayout_3.addWidget(self.lw_customer_sales)

        self.pb_open_transaction = QPushButton(self.widget_2)
        self.pb_open_transaction.setObjectName(u"pb_open_transaction")
        self.pb_open_transaction.setMinimumSize(QSize(0, 35))
        self.pb_open_transaction.setMaximumSize(QSize(16777215, 35))
        self.pb_open_transaction.setFont(font)
        self.pb_open_transaction.setStyleSheet(u"#pb_open_transaction {\n"
"	background-color: #6f6f6f;\n"
"	color: #fff;\n"
"	border: None;\n"
"	border-radius: 5px;\n"
"}\n"
"#pb_open_transaction:hover {\n"
"	background-color: #8f8f8f;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/Icons/dollar_white.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_open_transaction.setIcon(icon4)

        self.verticalLayout_3.addWidget(self.pb_open_transaction)


        self.verticalLayout_5.addWidget(self.widget_2)

        self.wd_customer_action = QWidget(self.wd_detail_view)
        self.wd_customer_action.setObjectName(u"wd_customer_action")
        self.verticalLayout_4 = QVBoxLayout(self.wd_customer_action)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lb_balance_txt = QLabel(self.wd_customer_action)
        self.lb_balance_txt.setObjectName(u"lb_balance_txt")
        self.lb_balance_txt.setMinimumSize(QSize(0, 20))
        self.lb_balance_txt.setFont(font2)

        self.verticalLayout_4.addWidget(self.lb_balance_txt)

        self.line = QFrame(self.wd_customer_action)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(400, 1))
        self.line.setMaximumSize(QSize(400, 1))
        self.line.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.line.setStyleSheet(u"background-color: #fff;")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line)

        self.widget_3 = QWidget(self.wd_customer_action)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lb_dollar_sign = QLabel(self.widget_3)
        self.lb_dollar_sign.setObjectName(u"lb_dollar_sign")
        self.lb_dollar_sign.setMinimumSize(QSize(0, 35))
        self.lb_dollar_sign.setMaximumSize(QSize(50, 35))
        font4 = QFont()
        font4.setFamilies([u"Lexend"])
        font4.setPointSize(24)
        font4.setBold(False)
        self.lb_dollar_sign.setFont(font4)

        self.horizontalLayout_4.addWidget(self.lb_dollar_sign)

        self.lb_balance_amount = QLabel(self.widget_3)
        self.lb_balance_amount.setObjectName(u"lb_balance_amount")
        self.lb_balance_amount.setMinimumSize(QSize(0, 35))
        self.lb_balance_amount.setMaximumSize(QSize(16777215, 35))
        font5 = QFont()
        font5.setFamilies([u"Lexend"])
        font5.setPointSize(24)
        font5.setBold(True)
        self.lb_balance_amount.setFont(font5)
        self.lb_balance_amount.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.lb_balance_amount)


        self.verticalLayout_4.addWidget(self.widget_3)

        self.pb_pay_now = QPushButton(self.wd_customer_action)
        self.pb_pay_now.setObjectName(u"pb_pay_now")
        self.pb_pay_now.setMinimumSize(QSize(0, 50))
        self.pb_pay_now.setMaximumSize(QSize(16777215, 50))
        self.pb_pay_now.setStyleSheet(u"#pb_pay_now {\n"
"	background-color: #fff;\n"
"	color: #0a0a0a;\n"
"	font-size: 24px;\n"
"	border: None;\n"
"	border-radius: 25px;\n"
"	font-weight: bold;\n"
"}\n"
"#pb_pay_now:hover {\n"
"	background-color: #efefef;\n"
"}")

        self.verticalLayout_4.addWidget(self.pb_pay_now)


        self.verticalLayout_5.addWidget(self.wd_customer_action)


        self.horizontalLayout.addWidget(self.wd_detail_view)


        self.verticalLayout.addWidget(self.wd_content)


        self.retranslateUi(CustomersListWindow)

        QMetaObject.connectSlotsByName(CustomersListWindow)
    # setupUi

    def retranslateUi(self, CustomersListWindow):
        CustomersListWindow.setWindowTitle(QCoreApplication.translate("CustomersListWindow", u"Users List", None))
        self.lb_customer_title.setText(QCoreApplication.translate("CustomersListWindow", u"Customer Manager", None))
        self.pb_customer_close.setText(QCoreApplication.translate("CustomersListWindow", u"Close", None))
        self.pb_create_customer.setText(QCoreApplication.translate("CustomersListWindow", u"Create New Customer", None))
        self.le_customer_search.setPlaceholderText(QCoreApplication.translate("CustomersListWindow", u"Search Customer by Name", None))
        self.pb_customer_search.setText(QCoreApplication.translate("CustomersListWindow", u"Search", None))
        self.lb_first_name.setText(QCoreApplication.translate("CustomersListWindow", u"First Name:", None))
        self.lb_firstName_val.setText(QCoreApplication.translate("CustomersListWindow", u"MacArthur", None))
        self.lb_last_name.setText(QCoreApplication.translate("CustomersListWindow", u"Last Name:", None))
        self.lb_lastName_val.setText(QCoreApplication.translate("CustomersListWindow", u"James", None))
        self.lb_phone.setText(QCoreApplication.translate("CustomersListWindow", u"Phone:", None))
        self.lb_phone_val.setText(QCoreApplication.translate("CustomersListWindow", u"926-2404", None))
        self.lb_email.setText(QCoreApplication.translate("CustomersListWindow", u"Email:", None))
        self.lb_email_val.setText("")
        self.pb_edit_customer.setText(QCoreApplication.translate("CustomersListWindow", u"Edit Customer", None))
        self.pb_open_transaction.setText(QCoreApplication.translate("CustomersListWindow", u"Open Sale", None))
        self.lb_balance_txt.setText(QCoreApplication.translate("CustomersListWindow", u"Credit Balance", None))
        self.lb_dollar_sign.setText(QCoreApplication.translate("CustomersListWindow", u"$", None))
        self.lb_balance_amount.setText(QCoreApplication.translate("CustomersListWindow", u"0.00", None))
        self.pb_pay_now.setText(QCoreApplication.translate("CustomersListWindow", u"Pay Now", None))
    # retranslateUi

