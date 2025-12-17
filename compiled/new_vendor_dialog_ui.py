# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_vendor_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_NewVendorDialog(object):
    def setupUi(self, NewVendorDialog):
        if not NewVendorDialog.objectName():
            NewVendorDialog.setObjectName(u"NewVendorDialog")
        NewVendorDialog.setWindowModality(Qt.WindowModality.ApplicationModal)
        NewVendorDialog.resize(800, 580)
        NewVendorDialog.setMinimumSize(QSize(800, 580))
        NewVendorDialog.setMaximumSize(QSize(800, 580))
        NewVendorDialog.setStyleSheet(u"#NewVendorDialog {\n"
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
        self.verticalLayout = QVBoxLayout(NewVendorDialog)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.lb_page_title = QLabel(NewVendorDialog)
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

        self.container = QWidget(NewVendorDialog)
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
        self.lb_vendor_name = QLabel(self.wd_form_labels)
        self.lb_vendor_name.setObjectName(u"lb_vendor_name")
        self.lb_vendor_name.setMinimumSize(QSize(0, 45))
        self.lb_vendor_name.setMaximumSize(QSize(16777215, 45))
        font1 = QFont()
        font1.setFamilies([u"Lexend"])
        font1.setPointSize(10)
        self.lb_vendor_name.setFont(font1)

        self.verticalLayout_3.addWidget(self.lb_vendor_name)

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
        self.le_vendor_name = QLineEdit(self.wd_fullname)
        self.le_vendor_name.setObjectName(u"le_vendor_name")
        self.le_vendor_name.setMinimumSize(QSize(0, 45))
        self.le_vendor_name.setMaximumSize(QSize(16777215, 45))
        self.le_vendor_name.setFont(font1)

        self.horizontalLayout_3.addWidget(self.le_vendor_name)


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
        self.te_address.setAcceptDrops(False)
        self.te_address.setStyleSheet(u"#te_address {\n"
"	background-color: #3f3f3f;\n"
"	color: white;\n"
"	border: None;\n"
"	border-radius: 5px;\n"
"}")

        self.verticalLayout_2.addWidget(self.te_address)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.wd_form_edit)


        self.verticalLayout.addWidget(self.container)

        self.wd_form_buttons = QWidget(NewVendorDialog)
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


        self.retranslateUi(NewVendorDialog)

        QMetaObject.connectSlotsByName(NewVendorDialog)
    # setupUi

    def retranslateUi(self, NewVendorDialog):
        NewVendorDialog.setWindowTitle(QCoreApplication.translate("NewVendorDialog", u"New Customer Form", None))
        self.lb_page_title.setText(QCoreApplication.translate("NewVendorDialog", u"Create New Vendor", None))
        self.lb_vendor_name.setText(QCoreApplication.translate("NewVendorDialog", u"Name", None))
        self.lb_phone.setText(QCoreApplication.translate("NewVendorDialog", u"Phone", None))
        self.lb_email.setText(QCoreApplication.translate("NewVendorDialog", u"Email", None))
        self.lb_address.setText(QCoreApplication.translate("NewVendorDialog", u"Address", None))
        self.le_vendor_name.setText("")
        self.le_vendor_name.setPlaceholderText(QCoreApplication.translate("NewVendorDialog", u"Company Name", None))
        self.le_phone.setPlaceholderText(QCoreApplication.translate("NewVendorDialog", u"Phone Number", None))
        self.le_email.setPlaceholderText(QCoreApplication.translate("NewVendorDialog", u"Email Address", None))
        self.te_address.setPlaceholderText(QCoreApplication.translate("NewVendorDialog", u"Street or Mailing Address", None))
        self.pb_save.setText(QCoreApplication.translate("NewVendorDialog", u"Save Vendor", None))
        self.pb_cancel.setText(QCoreApplication.translate("NewVendorDialog", u"Cancel", None))
    # retranslateUi

