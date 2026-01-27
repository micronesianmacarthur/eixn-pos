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
        CustomerManagerWindow.resize(980, 980)
        CustomerManagerWindow.setMinimumSize(QSize(940, 940))
        icon = QIcon()
        icon.addFile(u":/Icons/customers.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        CustomerManagerWindow.setWindowIcon(icon)
        CustomerManagerWindow.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(CustomerManagerWindow)
        self.verticalLayout_10.setSpacing(10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.wd_page_header = QWidget(CustomerManagerWindow)
        self.wd_page_header.setObjectName(u"wd_page_header")
        self.wd_page_header.setMinimumSize(QSize(0, 45))
        self.horizontalLayout = QHBoxLayout(self.wd_page_header)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lb_page_title = QLabel(self.wd_page_header)
        self.lb_page_title.setObjectName(u"lb_page_title")
        self.lb_page_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.lb_page_title)

        self.pb_close_page = QPushButton(self.wd_page_header)
        self.pb_close_page.setObjectName(u"pb_close_page")
        self.pb_close_page.setMinimumSize(QSize(0, 35))
        self.pb_close_page.setMaximumSize(QSize(120, 16777215))
        icon1 = QIcon()
        icon1.addFile(u":/Icons/close_white.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_close_page.setIcon(icon1)
        self.pb_close_page.setIconSize(QSize(18, 18))

        self.horizontalLayout.addWidget(self.pb_close_page)


        self.verticalLayout_10.addWidget(self.wd_page_header)

        self.wd_page_content = QWidget(CustomerManagerWindow)
        self.wd_page_content.setObjectName(u"wd_page_content")
        self.horizontalLayout_7 = QHBoxLayout(self.wd_page_content)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.wd_content_main = QWidget(self.wd_page_content)
        self.wd_content_main.setObjectName(u"wd_content_main")
        self.verticalLayout_9 = QVBoxLayout(self.wd_content_main)
        self.verticalLayout_9.setSpacing(10)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.wd_search_section = QWidget(self.wd_content_main)
        self.wd_search_section.setObjectName(u"wd_search_section")
        self.wd_search_section.setMinimumSize(QSize(0, 40))
        self.wd_search_section.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_3 = QHBoxLayout(self.wd_search_section)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pb_create_customer = QPushButton(self.wd_search_section)
        self.pb_create_customer.setObjectName(u"pb_create_customer")
        self.pb_create_customer.setMinimumSize(QSize(180, 35))
        self.pb_create_customer.setMaximumSize(QSize(180, 35))
        icon2 = QIcon()
        icon2.addFile(u":/Icons/add_white.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_create_customer.setIcon(icon2)
        self.pb_create_customer.setIconSize(QSize(18, 18))

        self.horizontalLayout_3.addWidget(self.pb_create_customer)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.le_search_customer = QLineEdit(self.wd_search_section)
        self.le_search_customer.setObjectName(u"le_search_customer")
        self.le_search_customer.setMinimumSize(QSize(140, 35))
        self.le_search_customer.setMaximumSize(QSize(240, 35))

        self.horizontalLayout_3.addWidget(self.le_search_customer)


        self.verticalLayout_9.addWidget(self.wd_search_section)

        self.wd_table_section = QWidget(self.wd_content_main)
        self.wd_table_section.setObjectName(u"wd_table_section")
        self.verticalLayout = QVBoxLayout(self.wd_table_section)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lb_customer_table = QLabel(self.wd_table_section)
        self.lb_customer_table.setObjectName(u"lb_customer_table")
        self.lb_customer_table.setMinimumSize(QSize(0, 18))
        self.lb_customer_table.setMaximumSize(QSize(16777215, 18))

        self.verticalLayout.addWidget(self.lb_customer_table)

        self.tbl_customers = QTableView(self.wd_table_section)
        self.tbl_customers.setObjectName(u"tbl_customers")

        self.verticalLayout.addWidget(self.tbl_customers)


        self.verticalLayout_9.addWidget(self.wd_table_section)


        self.horizontalLayout_7.addWidget(self.wd_content_main)

        self.wd_content_side = QWidget(self.wd_page_content)
        self.wd_content_side.setObjectName(u"wd_content_side")
        self.wd_content_side.setMinimumSize(QSize(400, 0))
        self.wd_content_side.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout_8 = QVBoxLayout(self.wd_content_side)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.wd_detail_view = QWidget(self.wd_content_side)
        self.wd_detail_view.setObjectName(u"wd_detail_view")
        self.wd_detail_view.setMinimumSize(QSize(0, 250))
        self.wd_detail_view.setMaximumSize(QSize(16777215, 250))
        self.verticalLayout_6 = QVBoxLayout(self.wd_detail_view)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.wd_detail_labels = QWidget(self.wd_detail_view)
        self.wd_detail_labels.setObjectName(u"wd_detail_labels")
        self.wd_detail_labels.setMinimumSize(QSize(0, 200))
        self.wd_detail_labels.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.wd_detail_labels)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lb_first_name = QLabel(self.wd_detail_labels)
        self.lb_first_name.setObjectName(u"lb_first_name")
        self.lb_first_name.setMinimumSize(QSize(120, 25))
        self.lb_first_name.setMaximumSize(QSize(120, 25))

        self.horizontalLayout_2.addWidget(self.lb_first_name)

        self.lb_first_name_val = QLabel(self.wd_detail_labels)
        self.lb_first_name_val.setObjectName(u"lb_first_name_val")
        self.lb_first_name_val.setMinimumSize(QSize(0, 25))
        self.lb_first_name_val.setMaximumSize(QSize(16777215, 25))
        font = QFont()
        font.setFamilies([u"Lexend"])
        font.setPointSize(9)
        font.setBold(True)
        self.lb_first_name_val.setFont(font)
        self.lb_first_name_val.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.lb_first_name_val)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lb_last_name = QLabel(self.wd_detail_labels)
        self.lb_last_name.setObjectName(u"lb_last_name")
        self.lb_last_name.setMinimumSize(QSize(120, 25))
        self.lb_last_name.setMaximumSize(QSize(120, 25))

        self.horizontalLayout_4.addWidget(self.lb_last_name)

        self.lb_last_name_val = QLabel(self.wd_detail_labels)
        self.lb_last_name_val.setObjectName(u"lb_last_name_val")
        self.lb_last_name_val.setMinimumSize(QSize(0, 25))
        self.lb_last_name_val.setMaximumSize(QSize(16777215, 25))
        self.lb_last_name_val.setFont(font)
        self.lb_last_name_val.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.lb_last_name_val)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lb_phone = QLabel(self.wd_detail_labels)
        self.lb_phone.setObjectName(u"lb_phone")
        self.lb_phone.setMinimumSize(QSize(120, 25))
        self.lb_phone.setMaximumSize(QSize(120, 25))

        self.horizontalLayout_5.addWidget(self.lb_phone)

        self.lb_phone_val = QLabel(self.wd_detail_labels)
        self.lb_phone_val.setObjectName(u"lb_phone_val")
        self.lb_phone_val.setMinimumSize(QSize(0, 25))
        self.lb_phone_val.setMaximumSize(QSize(16777215, 25))
        self.lb_phone_val.setFont(font)
        self.lb_phone_val.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.lb_phone_val)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lb_email = QLabel(self.wd_detail_labels)
        self.lb_email.setObjectName(u"lb_email")
        self.lb_email.setMinimumSize(QSize(120, 25))
        self.lb_email.setMaximumSize(QSize(120, 25))

        self.horizontalLayout_8.addWidget(self.lb_email)

        self.lb_email_val = QLabel(self.wd_detail_labels)
        self.lb_email_val.setObjectName(u"lb_email_val")
        self.lb_email_val.setMinimumSize(QSize(0, 25))
        self.lb_email_val.setMaximumSize(QSize(16777215, 25))
        self.lb_email_val.setFont(font)
        self.lb_email_val.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.lb_email_val)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lb_address = QLabel(self.wd_detail_labels)
        self.lb_address.setObjectName(u"lb_address")
        self.lb_address.setMinimumSize(QSize(120, 50))
        self.lb_address.setMaximumSize(QSize(120, 50))
        self.lb_address.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_9.addWidget(self.lb_address)

        self.lb_address_val = QLabel(self.wd_detail_labels)
        self.lb_address_val.setObjectName(u"lb_address_val")
        self.lb_address_val.setMinimumSize(QSize(0, 50))
        self.lb_address_val.setMaximumSize(QSize(16777215, 50))
        self.lb_address_val.setFont(font)
        self.lb_address_val.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignTrailing)
        self.lb_address_val.setWordWrap(True)

        self.horizontalLayout_9.addWidget(self.lb_address_val)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)


        self.verticalLayout_6.addWidget(self.wd_detail_labels)

        self.pb_edit_customer = QPushButton(self.wd_detail_view)
        self.pb_edit_customer.setObjectName(u"pb_edit_customer")
        self.pb_edit_customer.setMinimumSize(QSize(0, 35))
        icon3 = QIcon()
        icon3.addFile(u":/Icons/edit_white.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_edit_customer.setIcon(icon3)
        self.pb_edit_customer.setIconSize(QSize(18, 18))

        self.verticalLayout_6.addWidget(self.pb_edit_customer)


        self.verticalLayout_8.addWidget(self.wd_detail_view)

        self.wd_transaction_list = QWidget(self.wd_content_side)
        self.wd_transaction_list.setObjectName(u"wd_transaction_list")
        self.verticalLayout_5 = QVBoxLayout(self.wd_transaction_list)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.wd_list_section = QWidget(self.wd_transaction_list)
        self.wd_list_section.setObjectName(u"wd_list_section")
        self.verticalLayout_3 = QVBoxLayout(self.wd_list_section)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lb_transaction_list = QLabel(self.wd_list_section)
        self.lb_transaction_list.setObjectName(u"lb_transaction_list")
        self.lb_transaction_list.setMinimumSize(QSize(0, 18))
        self.lb_transaction_list.setMaximumSize(QSize(16777215, 18))

        self.verticalLayout_3.addWidget(self.lb_transaction_list)

        self.ls_transactions = QListView(self.wd_list_section)
        self.ls_transactions.setObjectName(u"ls_transactions")

        self.verticalLayout_3.addWidget(self.ls_transactions)


        self.verticalLayout_5.addWidget(self.wd_list_section)

        self.pb_open_transaction = QPushButton(self.wd_transaction_list)
        self.pb_open_transaction.setObjectName(u"pb_open_transaction")
        self.pb_open_transaction.setMinimumSize(QSize(0, 35))
        self.pb_open_transaction.setMaximumSize(QSize(16777215, 35))
        icon4 = QIcon()
        icon4.addFile(u":/Icons/dollar_white.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_open_transaction.setIcon(icon4)
        self.pb_open_transaction.setIconSize(QSize(18, 18))

        self.verticalLayout_5.addWidget(self.pb_open_transaction)


        self.verticalLayout_8.addWidget(self.wd_transaction_list)

        self.wd_charge_view = QWidget(self.wd_content_side)
        self.wd_charge_view.setObjectName(u"wd_charge_view")
        self.verticalLayout_7 = QVBoxLayout(self.wd_charge_view)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.widget_10 = QWidget(self.wd_charge_view)
        self.widget_10.setObjectName(u"widget_10")
        self.verticalLayout_4 = QVBoxLayout(self.widget_10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lb_charge_balance = QLabel(self.widget_10)
        self.lb_charge_balance.setObjectName(u"lb_charge_balance")

        self.verticalLayout_4.addWidget(self.lb_charge_balance)

        self.line = QFrame(self.widget_10)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(0, 1))
        self.line.setMaximumSize(QSize(16777215, 1))
        self.line.setStyleSheet(u"background-color: white;")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lb_dollar_sign = QLabel(self.widget_10)
        self.lb_dollar_sign.setObjectName(u"lb_dollar_sign")
        self.lb_dollar_sign.setMinimumSize(QSize(45, 45))
        self.lb_dollar_sign.setMaximumSize(QSize(45, 45))
        self.lb_dollar_sign.setStyleSheet(u"font-size: 32px;")
        self.lb_dollar_sign.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.lb_dollar_sign)

        self.lb_charge_amount = QLabel(self.widget_10)
        self.lb_charge_amount.setObjectName(u"lb_charge_amount")
        self.lb_charge_amount.setMinimumSize(QSize(0, 45))
        self.lb_charge_amount.setMaximumSize(QSize(16777215, 45))
        self.lb_charge_amount.setStyleSheet(u"font-size: 32px;")
        self.lb_charge_amount.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.lb_charge_amount)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)


        self.verticalLayout_7.addWidget(self.widget_10)

        self.pb_make_payment = QPushButton(self.wd_charge_view)
        self.pb_make_payment.setObjectName(u"pb_make_payment")
        self.pb_make_payment.setMinimumSize(QSize(0, 35))

        self.verticalLayout_7.addWidget(self.pb_make_payment)


        self.verticalLayout_8.addWidget(self.wd_charge_view)


        self.horizontalLayout_7.addWidget(self.wd_content_side)


        self.verticalLayout_10.addWidget(self.wd_page_content)


        self.retranslateUi(CustomerManagerWindow)

        QMetaObject.connectSlotsByName(CustomerManagerWindow)
    # setupUi

    def retranslateUi(self, CustomerManagerWindow):
        CustomerManagerWindow.setWindowTitle(QCoreApplication.translate("CustomerManagerWindow", u"Customer Manager", None))
        self.lb_page_title.setText(QCoreApplication.translate("CustomerManagerWindow", u"Customer Manager", None))
        self.pb_close_page.setText(QCoreApplication.translate("CustomerManagerWindow", u"Close", None))
        self.pb_create_customer.setText(QCoreApplication.translate("CustomerManagerWindow", u"Create New Customer", None))
        self.le_search_customer.setPlaceholderText(QCoreApplication.translate("CustomerManagerWindow", u"\U0001f50d Quick Search", None))
        self.lb_customer_table.setText(QCoreApplication.translate("CustomerManagerWindow", u"Customers", None))
        self.lb_first_name.setText(QCoreApplication.translate("CustomerManagerWindow", u"First Name:", None))
        self.lb_first_name_val.setText(QCoreApplication.translate("CustomerManagerWindow", u"MacArthur", None))
        self.lb_last_name.setText(QCoreApplication.translate("CustomerManagerWindow", u"Last Name:", None))
        self.lb_last_name_val.setText(QCoreApplication.translate("CustomerManagerWindow", u"James", None))
        self.lb_phone.setText(QCoreApplication.translate("CustomerManagerWindow", u"Phone:", None))
        self.lb_phone_val.setText(QCoreApplication.translate("CustomerManagerWindow", u"926-2404", None))
        self.lb_email.setText(QCoreApplication.translate("CustomerManagerWindow", u"Email:", None))
        self.lb_email_val.setText(QCoreApplication.translate("CustomerManagerWindow", u"jmacarthur92@gmail.com", None))
        self.lb_address.setText(QCoreApplication.translate("CustomerManagerWindow", u"Shipping Address:", None))
        self.lb_address_val.setText(QCoreApplication.translate("CustomerManagerWindow", u"PO Box 388, Kolonia Pohnpei FM 96941", None))
        self.pb_edit_customer.setText(QCoreApplication.translate("CustomerManagerWindow", u"Edit Customer", None))
        self.lb_transaction_list.setText(QCoreApplication.translate("CustomerManagerWindow", u"Transactions", None))
        self.pb_open_transaction.setText(QCoreApplication.translate("CustomerManagerWindow", u"Open Transaction", None))
        self.lb_charge_balance.setText(QCoreApplication.translate("CustomerManagerWindow", u"Charge Balance", None))
        self.lb_dollar_sign.setText(QCoreApplication.translate("CustomerManagerWindow", u"$", None))
        self.lb_charge_amount.setText(QCoreApplication.translate("CustomerManagerWindow", u"0.00", None))
        self.pb_make_payment.setText(QCoreApplication.translate("CustomerManagerWindow", u"Pay Now", None))
    # retranslateUi

