# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_manager_window.ui'
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

class Ui_UserManagerWindow(object):
    def setupUi(self, UserManagerWindow):
        if not UserManagerWindow.objectName():
            UserManagerWindow.setObjectName(u"UserManagerWindow")
        UserManagerWindow.resize(980, 980)
        UserManagerWindow.setMinimumSize(QSize(940, 940))
        icon = QIcon()
        icon.addFile(u":/Icons/user.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        UserManagerWindow.setWindowIcon(icon)
        UserManagerWindow.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(UserManagerWindow)
        self.verticalLayout_10.setSpacing(10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.wd_page_header = QWidget(UserManagerWindow)
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

        self.wd_page_content = QWidget(UserManagerWindow)
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
        self.pb_create_user = QPushButton(self.wd_search_section)
        self.pb_create_user.setObjectName(u"pb_create_user")
        self.pb_create_user.setMinimumSize(QSize(180, 35))
        self.pb_create_user.setMaximumSize(QSize(180, 35))
        icon2 = QIcon()
        icon2.addFile(u":/Icons/add_white.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_create_user.setIcon(icon2)
        self.pb_create_user.setIconSize(QSize(18, 18))

        self.horizontalLayout_3.addWidget(self.pb_create_user)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.le_search_user = QLineEdit(self.wd_search_section)
        self.le_search_user.setObjectName(u"le_search_user")
        self.le_search_user.setMinimumSize(QSize(140, 35))
        self.le_search_user.setMaximumSize(QSize(240, 35))

        self.horizontalLayout_3.addWidget(self.le_search_user)


        self.verticalLayout_9.addWidget(self.wd_search_section)

        self.wd_table_section = QWidget(self.wd_content_main)
        self.wd_table_section.setObjectName(u"wd_table_section")
        self.verticalLayout = QVBoxLayout(self.wd_table_section)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lb_user_table = QLabel(self.wd_table_section)
        self.lb_user_table.setObjectName(u"lb_user_table")
        self.lb_user_table.setMinimumSize(QSize(0, 18))
        self.lb_user_table.setMaximumSize(QSize(16777215, 18))

        self.verticalLayout.addWidget(self.lb_user_table)

        self.tbl_users = QTableView(self.wd_table_section)
        self.tbl_users.setObjectName(u"tbl_users")

        self.verticalLayout.addWidget(self.tbl_users)


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
        self.wd_detail_labels.setMinimumSize(QSize(0, 0))
        self.wd_detail_labels.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.wd_detail_labels)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
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

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lb_role = QLabel(self.wd_detail_labels)
        self.lb_role.setObjectName(u"lb_role")
        self.lb_role.setMinimumSize(QSize(120, 0))
        self.lb_role.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_10.addWidget(self.lb_role)

        self.lb_role_val = QLabel(self.wd_detail_labels)
        self.lb_role_val.setObjectName(u"lb_role_val")
        font1 = QFont()
        font1.setFamilies([u"Lexend"])
        font1.setBold(True)
        self.lb_role_val.setFont(font1)
        self.lb_role_val.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.lb_role_val)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.lb_status = QLabel(self.wd_detail_labels)
        self.lb_status.setObjectName(u"lb_status")
        self.lb_status.setMinimumSize(QSize(120, 0))
        self.lb_status.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_11.addWidget(self.lb_status)

        self.lb_status_val = QLabel(self.wd_detail_labels)
        self.lb_status_val.setObjectName(u"lb_status_val")
        self.lb_status_val.setFont(font1)
        self.lb_status_val.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.lb_status_val)


        self.verticalLayout_2.addLayout(self.horizontalLayout_11)

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

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.lb_created = QLabel(self.wd_detail_labels)
        self.lb_created.setObjectName(u"lb_created")
        self.lb_created.setMinimumSize(QSize(120, 0))
        self.lb_created.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_12.addWidget(self.lb_created)

        self.lb_created_val = QLabel(self.wd_detail_labels)
        self.lb_created_val.setObjectName(u"lb_created_val")
        self.lb_created_val.setFont(font1)
        self.lb_created_val.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.lb_created_val)


        self.verticalLayout_2.addLayout(self.horizontalLayout_12)


        self.verticalLayout_6.addWidget(self.wd_detail_labels)

        self.pb_edit_user = QPushButton(self.wd_detail_view)
        self.pb_edit_user.setObjectName(u"pb_edit_user")
        self.pb_edit_user.setMinimumSize(QSize(0, 35))
        icon3 = QIcon()
        icon3.addFile(u":/Icons/edit_white.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_edit_user.setIcon(icon3)
        self.pb_edit_user.setIconSize(QSize(18, 18))

        self.verticalLayout_6.addWidget(self.pb_edit_user)


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


        self.retranslateUi(UserManagerWindow)

        QMetaObject.connectSlotsByName(UserManagerWindow)
    # setupUi

    def retranslateUi(self, UserManagerWindow):
        UserManagerWindow.setWindowTitle(QCoreApplication.translate("UserManagerWindow", u"User Manager", None))
        self.lb_page_title.setText(QCoreApplication.translate("UserManagerWindow", u"User Manager", None))
        self.pb_close_page.setText(QCoreApplication.translate("UserManagerWindow", u"Close", None))
        self.pb_create_user.setText(QCoreApplication.translate("UserManagerWindow", u"Create New User", None))
        self.le_search_user.setPlaceholderText(QCoreApplication.translate("UserManagerWindow", u"\U0001f50d Quick Search", None))
        self.lb_user_table.setText(QCoreApplication.translate("UserManagerWindow", u"Users", None))
        self.lb_first_name.setText(QCoreApplication.translate("UserManagerWindow", u"First Name:", None))
        self.lb_first_name_val.setText(QCoreApplication.translate("UserManagerWindow", u"MacArthur", None))
        self.lb_last_name.setText(QCoreApplication.translate("UserManagerWindow", u"Last Name:", None))
        self.lb_last_name_val.setText(QCoreApplication.translate("UserManagerWindow", u"James", None))
        self.lb_role.setText(QCoreApplication.translate("UserManagerWindow", u"Role:", None))
        self.lb_role_val.setText(QCoreApplication.translate("UserManagerWindow", u"Admin", None))
        self.lb_status.setText(QCoreApplication.translate("UserManagerWindow", u"Status:", None))
        self.lb_status_val.setText(QCoreApplication.translate("UserManagerWindow", u"Active", None))
        self.lb_phone.setText(QCoreApplication.translate("UserManagerWindow", u"Phone:", None))
        self.lb_phone_val.setText(QCoreApplication.translate("UserManagerWindow", u"926-2404", None))
        self.lb_email.setText(QCoreApplication.translate("UserManagerWindow", u"Email:", None))
        self.lb_email_val.setText(QCoreApplication.translate("UserManagerWindow", u"jmacarthur92@gmail.com", None))
        self.lb_address.setText(QCoreApplication.translate("UserManagerWindow", u"Shipping Address:", None))
        self.lb_address_val.setText(QCoreApplication.translate("UserManagerWindow", u"PO Box 388, Kolonia Pohnpei FM 96941", None))
        self.lb_created.setText(QCoreApplication.translate("UserManagerWindow", u"Created:", None))
        self.lb_created_val.setText(QCoreApplication.translate("UserManagerWindow", u"2025-12-22", None))
        self.pb_edit_user.setText(QCoreApplication.translate("UserManagerWindow", u"Edit User", None))
        self.lb_transaction_list.setText(QCoreApplication.translate("UserManagerWindow", u"Transactions", None))
        self.pb_open_transaction.setText(QCoreApplication.translate("UserManagerWindow", u"Open Transaction", None))
        self.lb_charge_balance.setText(QCoreApplication.translate("UserManagerWindow", u"Charge Balance", None))
        self.lb_dollar_sign.setText(QCoreApplication.translate("UserManagerWindow", u"$", None))
        self.lb_charge_amount.setText(QCoreApplication.translate("UserManagerWindow", u"0.00", None))
        self.pb_make_payment.setText(QCoreApplication.translate("UserManagerWindow", u"Pay Now", None))
    # retranslateUi

