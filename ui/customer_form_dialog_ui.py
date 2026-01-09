# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customer_form_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QGroupBox, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import icons_rc

class Ui_CreateCustomerDialog(object):
    def setupUi(self, CreateCustomerDialog):
        if not CreateCustomerDialog.objectName():
            CreateCustomerDialog.setObjectName(u"CreateCustomerDialog")
        CreateCustomerDialog.resize(600, 500)
        CreateCustomerDialog.setMinimumSize(QSize(600, 500))
        CreateCustomerDialog.setMaximumSize(QSize(800, 600))
        CreateCustomerDialog.setStyleSheet(u"QWidget {\n"
"	font-family: \"Lexend\";\n"
"/*	border: 1px solid white;*/\n"
"}\n"
"\n"
"QCheckBox {\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"	border: None;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"	padding-right: 1px;\n"
"}\n"
"QLineEdit {\n"
"	background-color: #9f9f9f;\n"
"	border: None;\n"
"	border-top-right-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"	padding-left: 10px;\n"
"	color: #1a1a1a;\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(CreateCustomerDialog)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(10, 10, 10, 10)
        self.widget = QWidget(CreateCustomerDialog)
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
        self.grp_personal_info.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.grp_personal_info.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.grp_personal_info.setFlat(False)
        self.verticalLayout_2 = QVBoxLayout(self.grp_personal_info)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.verticalLayout_2.setContentsMargins(30, 10, 30, 10)
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

        self.grp_account = QGroupBox(self.widget_4)
        self.grp_account.setObjectName(u"grp_account")
        self.grp_account.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.grp_account.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.grp_account.setFlat(False)
        self.grp_account.setCheckable(False)
        self.verticalLayout = QVBoxLayout(self.grp_account)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.verticalLayout.setContentsMargins(30, 10, 30, 10)
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.lb_charge_account = QLabel(self.grp_account)
        self.lb_charge_account.setObjectName(u"lb_charge_account")
        self.lb_charge_account.setMinimumSize(QSize(130, 35))
        self.lb_charge_account.setMaximumSize(QSize(130, 35))
        self.lb_charge_account.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.lb_charge_account)

        self.cb_charge_account = QComboBox(self.grp_account)
        self.cb_charge_account.setObjectName(u"cb_charge_account")
        self.cb_charge_account.setMinimumSize(QSize(0, 35))
        self.cb_charge_account.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_11.addWidget(self.cb_charge_account)


        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(30)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lb_system_limit = QLabel(self.grp_account)
        self.lb_system_limit.setObjectName(u"lb_system_limit")
        self.lb_system_limit.setMinimumSize(QSize(130, 35))
        self.lb_system_limit.setMaximumSize(QSize(16777215, 35))
        self.lb_system_limit.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.lb_system_limit)

        self.chk_system_limit = QCheckBox(self.grp_account)
        self.chk_system_limit.setObjectName(u"chk_system_limit")
        self.chk_system_limit.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_5.addWidget(self.chk_system_limit)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lb_custom_limit = QLabel(self.grp_account)
        self.lb_custom_limit.setObjectName(u"lb_custom_limit")
        self.lb_custom_limit.setMinimumSize(QSize(130, 35))
        self.lb_custom_limit.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.lb_custom_limit)

        self.le_custom_limit = QLineEdit(self.grp_account)
        self.le_custom_limit.setObjectName(u"le_custom_limit")
        self.le_custom_limit.setMinimumSize(QSize(0, 35))

        self.horizontalLayout.addWidget(self.le_custom_limit)


        self.horizontalLayout_6.addLayout(self.horizontalLayout)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lb_disable_limit = QLabel(self.grp_account)
        self.lb_disable_limit.setObjectName(u"lb_disable_limit")
        self.lb_disable_limit.setMinimumSize(QSize(0, 35))
        self.lb_disable_limit.setMaximumSize(QSize(130, 16777215))
        self.lb_disable_limit.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.lb_disable_limit)

        self.chk_disable_limit = QCheckBox(self.grp_account)
        self.chk_disable_limit.setObjectName(u"chk_disable_limit")
        self.chk_disable_limit.setMinimumSize(QSize(0, 35))
        self.chk_disable_limit.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.chk_disable_limit)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.verticalLayout_3.addWidget(self.grp_account)


        self.verticalLayout_4.addWidget(self.widget_4)


        self.verticalLayout_5.addWidget(self.widget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.widget_2 = QWidget(CreateCustomerDialog)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 35))
        self.widget_2.setMaximumSize(QSize(16777215, 35))
        self.horizontalLayout_15 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_15.setSpacing(10)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(30, 0, 30, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer)

        self.pb_save_customer = QPushButton(self.widget_2)
        self.pb_save_customer.setObjectName(u"pb_save_customer")
        self.pb_save_customer.setMinimumSize(QSize(160, 35))
        self.pb_save_customer.setMaximumSize(QSize(160, 35))

        self.horizontalLayout_15.addWidget(self.pb_save_customer)

        self.pb_close_form = QPushButton(self.widget_2)
        self.pb_close_form.setObjectName(u"pb_close_form")
        self.pb_close_form.setMinimumSize(QSize(160, 35))
        self.pb_close_form.setMaximumSize(QSize(160, 35))

        self.horizontalLayout_15.addWidget(self.pb_close_form)


        self.verticalLayout_5.addWidget(self.widget_2)


        self.retranslateUi(CreateCustomerDialog)

        QMetaObject.connectSlotsByName(CreateCustomerDialog)
    # setupUi

    def retranslateUi(self, CreateCustomerDialog):
        CreateCustomerDialog.setWindowTitle(QCoreApplication.translate("CreateCustomerDialog", u"Create New User Form", None))
        self.lb_title_label.setText(QCoreApplication.translate("CreateCustomerDialog", u"Create New User", None))
        self.grp_personal_info.setTitle(QCoreApplication.translate("CreateCustomerDialog", u"Personal Information", None))
        self.lb_first_name.setText(QCoreApplication.translate("CreateCustomerDialog", u"First Name:", None))
        self.le_first_name.setPlaceholderText(QCoreApplication.translate("CreateCustomerDialog", u"John", None))
        self.lb_last_name.setText(QCoreApplication.translate("CreateCustomerDialog", u"Last Name:", None))
        self.le_last_name.setPlaceholderText(QCoreApplication.translate("CreateCustomerDialog", u"Doe", None))
        self.lb_phone.setText(QCoreApplication.translate("CreateCustomerDialog", u"Phone:", None))
        self.le_phone.setPlaceholderText(QCoreApplication.translate("CreateCustomerDialog", u"000-0000", None))
        self.lb_email.setText(QCoreApplication.translate("CreateCustomerDialog", u"Email:", None))
        self.le_email.setPlaceholderText(QCoreApplication.translate("CreateCustomerDialog", u"example@email.com", None))
        self.lb_address.setText(QCoreApplication.translate("CreateCustomerDialog", u"Address:", None))
        self.le_address.setPlaceholderText(QCoreApplication.translate("CreateCustomerDialog", u"PO Box # City, State, ZIP", None))
        self.grp_account.setTitle(QCoreApplication.translate("CreateCustomerDialog", u"Account", None))
        self.lb_charge_account.setText(QCoreApplication.translate("CreateCustomerDialog", u"Charge to Account:", None))
        self.cb_charge_account.setPlaceholderText(QCoreApplication.translate("CreateCustomerDialog", u"Please choose one option...", None))
        self.lb_system_limit.setText(QCoreApplication.translate("CreateCustomerDialog", u"Use System Limit:", None))
        self.chk_system_limit.setText(QCoreApplication.translate("CreateCustomerDialog", u"$50.00", None))
        self.lb_custom_limit.setText(QCoreApplication.translate("CreateCustomerDialog", u"Custom Limit:", None))
        self.le_custom_limit.setPlaceholderText(QCoreApplication.translate("CreateCustomerDialog", u"20.00", None))
        self.lb_disable_limit.setText("")
        self.chk_disable_limit.setText(QCoreApplication.translate("CreateCustomerDialog", u"No Charge Limit", None))
        self.pb_save_customer.setText(QCoreApplication.translate("CreateCustomerDialog", u"Save Customer", None))
        self.pb_close_form.setText(QCoreApplication.translate("CreateCustomerDialog", u"Close", None))
    # retranslateUi

