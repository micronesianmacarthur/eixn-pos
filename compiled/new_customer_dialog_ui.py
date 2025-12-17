# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_customer_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)
import icons_rc

class Ui_NewCustomerDialog(object):
    def setupUi(self, NewCustomerDialog):
        if not NewCustomerDialog.objectName():
            NewCustomerDialog.setObjectName(u"NewCustomerDialog")
        NewCustomerDialog.setWindowModality(Qt.WindowModality.ApplicationModal)
        NewCustomerDialog.resize(800, 580)
        NewCustomerDialog.setMinimumSize(QSize(800, 580))
        NewCustomerDialog.setMaximumSize(QSize(800, 580))
        NewCustomerDialog.setStyleSheet(u"#NewCustomerDialog {\n"
"	background-color: #222;\n"
"}\n"
"QWidget {\n"
"}\n"
"QPushButton {\n"
"	border: None;\n"
"	border-radius: 5px;\n"
"	background-color: #fff;\n"
"	color: #1a1a1a;\n"
"}")
        self.verticalLayout = QVBoxLayout(NewCustomerDialog)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.lb_page_title = QLabel(NewCustomerDialog)
        self.lb_page_title.setObjectName(u"lb_page_title")
        self.lb_page_title.setMinimumSize(QSize(0, 45))
        self.lb_page_title.setMaximumSize(QSize(16777215, 45))
        font = QFont()
        font.setFamilies([u"Lexend"])
        font.setPointSize(16)
        font.setBold(True)
        self.lb_page_title.setFont(font)
        self.lb_page_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lb_page_title)

        self.container = QWidget(NewCustomerDialog)
        self.container.setObjectName(u"container")
        self.horizontalLayout = QHBoxLayout(self.container)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.wd_form_labels = QWidget(self.container)
        self.wd_form_labels.setObjectName(u"wd_form_labels")
        self.wd_form_labels.setMinimumSize(QSize(200, 0))
        self.wd_form_labels.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.wd_form_labels)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lb_fullname = QLabel(self.wd_form_labels)
        self.lb_fullname.setObjectName(u"lb_fullname")
        self.lb_fullname.setMinimumSize(QSize(0, 45))
        self.lb_fullname.setMaximumSize(QSize(16777215, 45))
        font1 = QFont()
        font1.setFamilies([u"Lexend"])
        font1.setPointSize(10)
        self.lb_fullname.setFont(font1)

        self.verticalLayout_3.addWidget(self.lb_fullname)

        self.lb_phone = QLabel(self.wd_form_labels)
        self.lb_phone.setObjectName(u"lb_phone")
        self.lb_phone.setMinimumSize(QSize(0, 45))
        self.lb_phone.setMaximumSize(QSize(16777215, 45))
        self.lb_phone.setFont(font1)

        self.verticalLayout_3.addWidget(self.lb_phone)

        self.lb_email = QLabel(self.wd_form_labels)
        self.lb_email.setObjectName(u"lb_email")
        self.lb_email.setMinimumSize(QSize(0, 45))
        self.lb_email.setMaximumSize(QSize(16777215, 45))
        self.lb_email.setFont(font1)

        self.verticalLayout_3.addWidget(self.lb_email)

        self.lb_address = QLabel(self.wd_form_labels)
        self.lb_address.setObjectName(u"lb_address")
        self.lb_address.setMinimumSize(QSize(0, 100))
        self.lb_address.setMaximumSize(QSize(16777215, 100))
        self.lb_address.setFont(font1)
        self.lb_address.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_3.addWidget(self.lb_address)

        self.lb_enable_charge = QLabel(self.wd_form_labels)
        self.lb_enable_charge.setObjectName(u"lb_enable_charge")
        self.lb_enable_charge.setMinimumSize(QSize(0, 45))
        self.lb_enable_charge.setMaximumSize(QSize(16777215, 45))
        self.lb_enable_charge.setFont(font1)

        self.verticalLayout_3.addWidget(self.lb_enable_charge)

        self.lb_charge_limit = QLabel(self.wd_form_labels)
        self.lb_charge_limit.setObjectName(u"lb_charge_limit")
        self.lb_charge_limit.setMinimumSize(QSize(0, 45))
        self.lb_charge_limit.setMaximumSize(QSize(16777215, 45))
        self.lb_charge_limit.setFont(font1)

        self.verticalLayout_3.addWidget(self.lb_charge_limit)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.wd_form_labels)

        self.wd_form_edit = QWidget(self.container)
        self.wd_form_edit.setObjectName(u"wd_form_edit")
        self.wd_form_edit.setStyleSheet(u"#wd_form_edit QLineEdit, QComboBox, QTextEdit {\n"
"	background-color: #3f3f3f;\n"
"	color: #fff;\n"
"	border: None;\n"
"	border-radius: 5px;\n"
"	padding-left: 10px;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.wd_form_edit)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.wd_fullname = QWidget(self.wd_form_edit)
        self.wd_fullname.setObjectName(u"wd_fullname")
        self.wd_fullname.setMinimumSize(QSize(0, 45))
        self.wd_fullname.setMaximumSize(QSize(16777215, 40))
        self.wd_fullname.setStyleSheet(u"")
        self.horizontalLayout_3 = QHBoxLayout(self.wd_fullname)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.le_first_name = QLineEdit(self.wd_fullname)
        self.le_first_name.setObjectName(u"le_first_name")
        self.le_first_name.setMinimumSize(QSize(0, 45))
        self.le_first_name.setMaximumSize(QSize(16777215, 45))
        self.le_first_name.setFont(font1)

        self.horizontalLayout_3.addWidget(self.le_first_name)

        self.le_last_name = QLineEdit(self.wd_fullname)
        self.le_last_name.setObjectName(u"le_last_name")
        self.le_last_name.setMinimumSize(QSize(0, 45))
        self.le_last_name.setMaximumSize(QSize(16777215, 45))
        self.le_last_name.setFont(font1)

        self.horizontalLayout_3.addWidget(self.le_last_name)


        self.verticalLayout_2.addWidget(self.wd_fullname)

        self.le_phone = QLineEdit(self.wd_form_edit)
        self.le_phone.setObjectName(u"le_phone")
        self.le_phone.setMinimumSize(QSize(0, 45))
        self.le_phone.setMaximumSize(QSize(16777215, 45))
        self.le_phone.setFont(font1)

        self.verticalLayout_2.addWidget(self.le_phone)

        self.le_email = QLineEdit(self.wd_form_edit)
        self.le_email.setObjectName(u"le_email")
        self.le_email.setMinimumSize(QSize(0, 45))
        self.le_email.setMaximumSize(QSize(16777215, 45))
        self.le_email.setFont(font1)

        self.verticalLayout_2.addWidget(self.le_email)

        self.te_address = QTextEdit(self.wd_form_edit)
        self.te_address.setObjectName(u"te_address")
        self.te_address.setMinimumSize(QSize(0, 100))
        self.te_address.setMaximumSize(QSize(16777215, 100))
        self.te_address.setFont(font1)
        self.te_address.setStyleSheet(u"#te_address {\n"
"	background-color: #3f3f3f;\n"
"	color: white;\n"
"	border: None;\n"
"	border-radius: 5px;\n"
"}")

        self.verticalLayout_2.addWidget(self.te_address)

        self.chk_enable_charge = QCheckBox(self.wd_form_edit)
        self.chk_enable_charge.setObjectName(u"chk_enable_charge")
        self.chk_enable_charge.setMinimumSize(QSize(0, 45))
        self.chk_enable_charge.setMaximumSize(QSize(16777215, 45))
        self.chk_enable_charge.setFont(font1)
        self.chk_enable_charge.setStyleSheet(u"QCheckBox {\n"
"	spacing: 15px;\n"
"}\n"
"QCheckBox::indicator {\n"
"	width: 20px;\n"
"	height: 20px;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"	image: url(:/Icons/checkbox_unchecked.svg)\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"	image: url(:/Icons/checkbox_checked.svg)\n"
"}")

        self.verticalLayout_2.addWidget(self.chk_enable_charge)

        self.le_charge_limit = QLineEdit(self.wd_form_edit)
        self.le_charge_limit.setObjectName(u"le_charge_limit")
        self.le_charge_limit.setMinimumSize(QSize(0, 45))
        self.le_charge_limit.setMaximumSize(QSize(16777215, 45))
        self.le_charge_limit.setFont(font1)

        self.verticalLayout_2.addWidget(self.le_charge_limit)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.wd_form_edit)


        self.verticalLayout.addWidget(self.container)

        self.wd_form_buttons = QWidget(NewCustomerDialog)
        self.wd_form_buttons.setObjectName(u"wd_form_buttons")
        self.wd_form_buttons.setMinimumSize(QSize(0, 50))
        self.wd_form_buttons.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_2 = QHBoxLayout(self.wd_form_buttons)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pb_save = QPushButton(self.wd_form_buttons)
        self.pb_save.setObjectName(u"pb_save")
        self.pb_save.setMinimumSize(QSize(200, 40))
        self.pb_save.setMaximumSize(QSize(200, 16777215))
        self.pb_save.setFont(font1)
        self.pb_save.setStyleSheet(u"#pb_save:hover {\n"
"	background-color: #9c9c9c;\n"
"}")

        self.horizontalLayout_2.addWidget(self.pb_save)

        self.pb_cancel = QPushButton(self.wd_form_buttons)
        self.pb_cancel.setObjectName(u"pb_cancel")
        self.pb_cancel.setMinimumSize(QSize(200, 40))
        self.pb_cancel.setMaximumSize(QSize(200, 16777215))
        self.pb_cancel.setFont(font1)
        self.pb_cancel.setStyleSheet(u"#pb_cancel {\n"
"	background-color: #3c3c3c;\n"
"	color: white;\n"
"}\n"
"#pb_cancel:hover {\n"
"	background-color: #6c6c6c;\n"
"}")

        self.horizontalLayout_2.addWidget(self.pb_cancel)


        self.verticalLayout.addWidget(self.wd_form_buttons)


        self.retranslateUi(NewCustomerDialog)

        QMetaObject.connectSlotsByName(NewCustomerDialog)
    # setupUi

    def retranslateUi(self, NewCustomerDialog):
        NewCustomerDialog.setWindowTitle(QCoreApplication.translate("NewCustomerDialog", u"New Customer Form", None))
        self.lb_page_title.setText(QCoreApplication.translate("NewCustomerDialog", u"Create New Customer", None))
        self.lb_fullname.setText(QCoreApplication.translate("NewCustomerDialog", u"Full name", None))
        self.lb_phone.setText(QCoreApplication.translate("NewCustomerDialog", u"Phone", None))
        self.lb_email.setText(QCoreApplication.translate("NewCustomerDialog", u"Email", None))
        self.lb_address.setText(QCoreApplication.translate("NewCustomerDialog", u"Address", None))
        self.lb_enable_charge.setText("")
        self.lb_charge_limit.setText(QCoreApplication.translate("NewCustomerDialog", u"Charge Amount Limit", None))
        self.le_first_name.setPlaceholderText(QCoreApplication.translate("NewCustomerDialog", u"First Name", None))
        self.le_last_name.setPlaceholderText(QCoreApplication.translate("NewCustomerDialog", u"Last Name", None))
        self.le_phone.setPlaceholderText(QCoreApplication.translate("NewCustomerDialog", u"Phone Number", None))
        self.le_email.setPlaceholderText(QCoreApplication.translate("NewCustomerDialog", u"Email Address", None))
        self.te_address.setPlaceholderText(QCoreApplication.translate("NewCustomerDialog", u"Street or Mailing Address", None))
        self.chk_enable_charge.setText(QCoreApplication.translate("NewCustomerDialog", u"Enable Charge to Account", None))
        self.le_charge_limit.setPlaceholderText(QCoreApplication.translate("NewCustomerDialog", u"Amount Limit (i.e. 20)", None))
        self.pb_save.setText(QCoreApplication.translate("NewCustomerDialog", u"Save Customer", None))
        self.pb_cancel.setText(QCoreApplication.translate("NewCustomerDialog", u"Cancel", None))
    # retranslateUi

