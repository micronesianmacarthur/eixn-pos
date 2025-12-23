# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_form_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_CreateUserDialog(object):
    def setupUi(self, CreateUserDialog):
        if not CreateUserDialog.objectName():
            CreateUserDialog.setObjectName(u"CreateUserDialog")
        CreateUserDialog.resize(800, 642)
        CreateUserDialog.setMaximumSize(QSize(800, 16777215))
        CreateUserDialog.setStyleSheet(u"QWidget {\n"
"	font-family: \"Lexend\";\n"
"	font-size: 12px;\n"
"/*	border: 1px solid white;*/\n"
"}\n"
"\n"
"QLabel {\n"
"	background-color: #9f9f9f;\n"
"	border: None;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"	padding-right: 1px;\n"
"	color: #1a1a1a;\n"
"}\n"
"QLineEdit {\n"
"	background-color: #9f9f9f;\n"
"	border: None;\n"
"	border-top-right-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"	padding-left: 10px;\n"
"	color: #1a1a1a;\n"
"}\n"
"QComboBox {\n"
"	background-color: #9f9f9f;\n"
"	border: None;\n"
"	border-top-right-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"	padding-left: 10px;\n"
"	color: #1a1a1a;\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(CreateUserDialog)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(10, 10, 10, 10)
        self.widget = QWidget(CreateUserDialog)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 24))
        self.widget_3.setMaximumSize(QSize(16777215, 24))
        self.horizontalLayout_16 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_16.setSpacing(10)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.lb_title_label = QLabel(self.widget_3)
        self.lb_title_label.setObjectName(u"lb_title_label")
        self.lb_title_label.setMinimumSize(QSize(0, 24))
        self.lb_title_label.setMaximumSize(QSize(16777215, 24))
        self.lb_title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_16.addWidget(self.lb_title_label)


        self.verticalLayout_4.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_3 = QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.grp_personal_info = QGroupBox(self.widget_4)
        self.grp_personal_info.setObjectName(u"grp_personal_info")
        self.grp_personal_info.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.grp_personal_info.setFlat(False)
        self.verticalLayout_2 = QVBoxLayout(self.grp_personal_info)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(30, 10, 30, 10)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lb_username = QLabel(self.grp_personal_info)
        self.lb_username.setObjectName(u"lb_username")
        self.lb_username.setMinimumSize(QSize(80, 35))
        self.lb_username.setMaximumSize(QSize(80, 35))
        self.lb_username.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.lb_username)

        self.le_usename = QLineEdit(self.grp_personal_info)
        self.le_usename.setObjectName(u"le_usename")
        self.le_usename.setMinimumSize(QSize(0, 35))
        self.le_usename.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout.addWidget(self.le_usename)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(30)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lb_first_name = QLabel(self.grp_personal_info)
        self.lb_first_name.setObjectName(u"lb_first_name")
        self.lb_first_name.setMinimumSize(QSize(80, 35))
        self.lb_first_name.setMaximumSize(QSize(80, 35))
        self.lb_first_name.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.lb_first_name)

        self.le_first_name = QLineEdit(self.grp_personal_info)
        self.le_first_name.setObjectName(u"le_first_name")
        self.le_first_name.setMinimumSize(QSize(0, 35))
        self.le_first_name.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_2.addWidget(self.le_first_name)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lb_last_name = QLabel(self.grp_personal_info)
        self.lb_last_name.setObjectName(u"lb_last_name")
        self.lb_last_name.setMinimumSize(QSize(80, 35))
        self.lb_last_name.setMaximumSize(QSize(80, 35))
        self.lb_last_name.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.lb_last_name)

        self.le_last_name = QLineEdit(self.grp_personal_info)
        self.le_last_name.setObjectName(u"le_last_name")
        self.le_last_name.setMinimumSize(QSize(0, 35))
        self.le_last_name.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_3.addWidget(self.le_last_name)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setSpacing(30)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lb_phone = QLabel(self.grp_personal_info)
        self.lb_phone.setObjectName(u"lb_phone")
        self.lb_phone.setMinimumSize(QSize(80, 35))
        self.lb_phone.setMaximumSize(QSize(80, 35))
        self.lb_phone.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.lb_phone)

        self.le_phone = QLineEdit(self.grp_personal_info)
        self.le_phone.setObjectName(u"le_phone")
        self.le_phone.setMinimumSize(QSize(0, 35))
        self.le_phone.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_8.addWidget(self.le_phone)


        self.horizontalLayout_17.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lb_email = QLabel(self.grp_personal_info)
        self.lb_email.setObjectName(u"lb_email")
        self.lb_email.setMinimumSize(QSize(80, 35))
        self.lb_email.setMaximumSize(QSize(80, 35))
        self.lb_email.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.lb_email)

        self.le_email = QLineEdit(self.grp_personal_info)
        self.le_email.setObjectName(u"le_email")
        self.le_email.setMinimumSize(QSize(0, 35))
        self.le_email.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_9.addWidget(self.le_email)


        self.horizontalLayout_17.addLayout(self.horizontalLayout_9)


        self.verticalLayout_2.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lb_address = QLabel(self.grp_personal_info)
        self.lb_address.setObjectName(u"lb_address")
        self.lb_address.setMinimumSize(QSize(80, 35))
        self.lb_address.setMaximumSize(QSize(80, 35))
        self.lb_address.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.lb_address)

        self.le_address = QLineEdit(self.grp_personal_info)
        self.le_address.setObjectName(u"le_address")
        self.le_address.setMinimumSize(QSize(0, 35))
        self.le_address.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_10.addWidget(self.le_address)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)


        self.verticalLayout_3.addWidget(self.grp_personal_info)

        self.grp_auth_security = QGroupBox(self.widget_4)
        self.grp_auth_security.setObjectName(u"grp_auth_security")
        self.grp_auth_security.setFlat(False)
        self.grp_auth_security.setCheckable(False)
        self.verticalLayout = QVBoxLayout(self.grp_auth_security)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 10, 30, 10)
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lb_role = QLabel(self.grp_auth_security)
        self.lb_role.setObjectName(u"lb_role")
        self.lb_role.setMinimumSize(QSize(80, 35))
        self.lb_role.setMaximumSize(QSize(80, 35))
        self.lb_role.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.lb_role)

        self.cb_role = QComboBox(self.grp_auth_security)
        self.cb_role.setObjectName(u"cb_role")
        self.cb_role.setMinimumSize(QSize(0, 35))
        self.cb_role.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_4.addWidget(self.cb_role)


        self.horizontalLayout_18.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.lb_status = QLabel(self.grp_auth_security)
        self.lb_status.setObjectName(u"lb_status")
        self.lb_status.setMinimumSize(QSize(80, 35))
        self.lb_status.setMaximumSize(QSize(80, 35))
        self.lb_status.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.lb_status)

        self.cb_status = QComboBox(self.grp_auth_security)
        self.cb_status.setObjectName(u"cb_status")
        self.cb_status.setMinimumSize(QSize(0, 35))
        self.cb_status.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_12.addWidget(self.cb_status)


        self.horizontalLayout_18.addLayout(self.horizontalLayout_12)


        self.verticalLayout.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.lb_charge_account = QLabel(self.grp_auth_security)
        self.lb_charge_account.setObjectName(u"lb_charge_account")
        self.lb_charge_account.setMinimumSize(QSize(130, 35))
        self.lb_charge_account.setMaximumSize(QSize(130, 35))
        self.lb_charge_account.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.lb_charge_account)

        self.cb_charge_account = QComboBox(self.grp_auth_security)
        self.cb_charge_account.setObjectName(u"cb_charge_account")
        self.cb_charge_account.setMinimumSize(QSize(0, 35))
        self.cb_charge_account.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_11.addWidget(self.cb_charge_account)


        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lb_pin = QLabel(self.grp_auth_security)
        self.lb_pin.setObjectName(u"lb_pin")
        self.lb_pin.setMinimumSize(QSize(80, 35))
        self.lb_pin.setMaximumSize(QSize(80, 35))
        self.lb_pin.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.lb_pin)

        self.le_pin = QLineEdit(self.grp_auth_security)
        self.le_pin.setObjectName(u"le_pin")
        self.le_pin.setMinimumSize(QSize(0, 35))
        self.le_pin.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_5.addWidget(self.le_pin)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(30)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lb_password = QLabel(self.grp_auth_security)
        self.lb_password.setObjectName(u"lb_password")
        self.lb_password.setMinimumSize(QSize(80, 35))
        self.lb_password.setMaximumSize(QSize(80, 35))
        self.lb_password.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.lb_password)

        self.le_password = QLineEdit(self.grp_auth_security)
        self.le_password.setObjectName(u"le_password")
        self.le_password.setMinimumSize(QSize(0, 35))
        self.le_password.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_6.addWidget(self.le_password)


        self.horizontalLayout_13.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lb_password_2 = QLabel(self.grp_auth_security)
        self.lb_password_2.setObjectName(u"lb_password_2")
        self.lb_password_2.setMinimumSize(QSize(100, 35))
        self.lb_password_2.setMaximumSize(QSize(130, 35))
        self.lb_password_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.lb_password_2)

        self.le_password_2 = QLineEdit(self.grp_auth_security)
        self.le_password_2.setObjectName(u"le_password_2")
        self.le_password_2.setMinimumSize(QSize(0, 35))
        self.le_password_2.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_7.addWidget(self.le_password_2)


        self.horizontalLayout_13.addLayout(self.horizontalLayout_7)


        self.verticalLayout.addLayout(self.horizontalLayout_13)


        self.verticalLayout_3.addWidget(self.grp_auth_security)


        self.verticalLayout_4.addWidget(self.widget_4)


        self.verticalLayout_5.addWidget(self.widget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.widget_2 = QWidget(CreateUserDialog)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 35))
        self.widget_2.setMaximumSize(QSize(16777215, 35))
        self.horizontalLayout_15 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_15.setSpacing(10)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(30, 0, 30, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.widget_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(160, 35))
        self.pushButton.setMaximumSize(QSize(160, 35))

        self.horizontalLayout_15.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.widget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(160, 35))
        self.pushButton_2.setMaximumSize(QSize(160, 35))

        self.horizontalLayout_15.addWidget(self.pushButton_2)


        self.verticalLayout_5.addWidget(self.widget_2)


        self.retranslateUi(CreateUserDialog)

        QMetaObject.connectSlotsByName(CreateUserDialog)
    # setupUi

    def retranslateUi(self, CreateUserDialog):
        CreateUserDialog.setWindowTitle(QCoreApplication.translate("CreateUserDialog", u"Create New User Form", None))
        self.lb_title_label.setText(QCoreApplication.translate("CreateUserDialog", u"Create New User", None))
        self.grp_personal_info.setTitle(QCoreApplication.translate("CreateUserDialog", u"Personal Information", None))
        self.lb_username.setText(QCoreApplication.translate("CreateUserDialog", u"Username:", None))
        self.le_usename.setPlaceholderText(QCoreApplication.translate("CreateUserDialog", u"john", None))
        self.lb_first_name.setText(QCoreApplication.translate("CreateUserDialog", u"First Name:", None))
        self.le_first_name.setPlaceholderText(QCoreApplication.translate("CreateUserDialog", u"John", None))
        self.lb_last_name.setText(QCoreApplication.translate("CreateUserDialog", u"Last Name:", None))
        self.le_last_name.setPlaceholderText(QCoreApplication.translate("CreateUserDialog", u"Doe", None))
        self.lb_phone.setText(QCoreApplication.translate("CreateUserDialog", u"Phone:", None))
        self.le_phone.setPlaceholderText(QCoreApplication.translate("CreateUserDialog", u"000-0000", None))
        self.lb_email.setText(QCoreApplication.translate("CreateUserDialog", u"Email:", None))
        self.le_email.setPlaceholderText(QCoreApplication.translate("CreateUserDialog", u"example@email.com", None))
        self.lb_address.setText(QCoreApplication.translate("CreateUserDialog", u"Address:", None))
        self.le_address.setPlaceholderText(QCoreApplication.translate("CreateUserDialog", u"PO Box # City, State, ZIP", None))
        self.grp_auth_security.setTitle(QCoreApplication.translate("CreateUserDialog", u"Security and Authorization", None))
        self.lb_role.setText(QCoreApplication.translate("CreateUserDialog", u"Role:", None))
        self.cb_role.setPlaceholderText(QCoreApplication.translate("CreateUserDialog", u"Select Role...", None))
        self.lb_status.setText(QCoreApplication.translate("CreateUserDialog", u"Status:", None))
        self.cb_status.setPlaceholderText(QCoreApplication.translate("CreateUserDialog", u"Select Status...", None))
        self.lb_charge_account.setText(QCoreApplication.translate("CreateUserDialog", u"Charge to Account:", None))
        self.lb_pin.setText(QCoreApplication.translate("CreateUserDialog", u"PIN:", None))
        self.lb_password.setText(QCoreApplication.translate("CreateUserDialog", u"Password:", None))
        self.lb_password_2.setText(QCoreApplication.translate("CreateUserDialog", u"Confirm Password:", None))
        self.pushButton.setText(QCoreApplication.translate("CreateUserDialog", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("CreateUserDialog", u"PushButton", None))
    # retranslateUi

