# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_user_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import icons_rc

class Ui_NewUserDialog(object):
    def setupUi(self, NewUserDialog):
        if not NewUserDialog.objectName():
            NewUserDialog.setObjectName(u"NewUserDialog")
        NewUserDialog.setWindowModality(Qt.WindowModality.ApplicationModal)
        NewUserDialog.resize(800, 580)
        NewUserDialog.setMinimumSize(QSize(800, 580))
        NewUserDialog.setMaximumSize(QSize(800, 580))
        NewUserDialog.setStyleSheet(u"#NewUserDialog {\n"
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
        self.verticalLayout = QVBoxLayout(NewUserDialog)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.lb_page_title = QLabel(NewUserDialog)
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

        self.container = QWidget(NewUserDialog)
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

        self.lb_username = QLabel(self.wd_form_labels)
        self.lb_username.setObjectName(u"lb_username")
        self.lb_username.setMinimumSize(QSize(0, 45))
        self.lb_username.setMaximumSize(QSize(16777215, 45))
        self.lb_username.setFont(font1)

        self.verticalLayout_3.addWidget(self.lb_username)

        self.lb_role = QLabel(self.wd_form_labels)
        self.lb_role.setObjectName(u"lb_role")
        self.lb_role.setMinimumSize(QSize(0, 45))
        self.lb_role.setMaximumSize(QSize(16777215, 45))
        self.lb_role.setFont(font1)

        self.verticalLayout_3.addWidget(self.lb_role)

        self.lb_pin = QLabel(self.wd_form_labels)
        self.lb_pin.setObjectName(u"lb_pin")
        self.lb_pin.setMinimumSize(QSize(0, 45))
        self.lb_pin.setMaximumSize(QSize(16777215, 45))
        self.lb_pin.setFont(font1)

        self.verticalLayout_3.addWidget(self.lb_pin)

        self.lb_password = QLabel(self.wd_form_labels)
        self.lb_password.setObjectName(u"lb_password")
        self.lb_password.setMinimumSize(QSize(0, 45))
        self.lb_password.setMaximumSize(QSize(16777215, 45))
        self.lb_password.setFont(font1)

        self.verticalLayout_3.addWidget(self.lb_password)

        self.lb_password2 = QLabel(self.wd_form_labels)
        self.lb_password2.setObjectName(u"lb_password2")
        self.lb_password2.setMinimumSize(QSize(0, 45))
        self.lb_password2.setMaximumSize(QSize(16777215, 45))
        self.lb_password2.setFont(font1)

        self.verticalLayout_3.addWidget(self.lb_password2)

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

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.wd_form_labels)

        self.wd_form_edit = QWidget(self.container)
        self.wd_form_edit.setObjectName(u"wd_form_edit")
        self.wd_form_edit.setStyleSheet(u"#wd_form_edit QLineEdit, QComboBox {\n"
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

        self.le_username = QLineEdit(self.wd_form_edit)
        self.le_username.setObjectName(u"le_username")
        self.le_username.setMinimumSize(QSize(0, 45))
        self.le_username.setMaximumSize(QSize(16777215, 45))
        self.le_username.setFont(font1)

        self.verticalLayout_2.addWidget(self.le_username)

        self.cb_role = QComboBox(self.wd_form_edit)
        self.cb_role.addItem("")
        self.cb_role.addItem("")
        self.cb_role.addItem("")
        self.cb_role.addItem("")
        self.cb_role.setObjectName(u"cb_role")
        self.cb_role.setMinimumSize(QSize(0, 45))
        self.cb_role.setMaximumSize(QSize(16777215, 45))
        self.cb_role.setFont(font1)
        self.cb_role.setStyleSheet(u"#cb_role {\n"
"	padding-left: 10px;\n"
"}\n"
"#cb_role::drop-down {\n"
"	border: None;\n"
"}\n"
"#cb_role::down-arrow {\n"
"	image: url(:/Icons/drop_arrow_white.svg);\n"
"	width: 20px;\n"
"	height: 20px;\n"
"	margin-right: 20px;\n"
"}\n"
"#cb_role::on {\n"
"	border: 1px solid #ccc;\n"
"}\n"
"#cb_role QListView {\n"
"	font-size: 18px;\n"
"	padding: 5px;\n"
"	background-color: #9f9f9f;\n"
"	border: 1px solid #1a1a1a;\n"
"	outline: None;\n"
"}\n"
"#cb_role QListView::item {\n"
"	background-color: #fff;\n"
"	padding-left: 10px;\n"
"}\n"
"#cb_role QListView::item:hover {\n"
"	background-color: #1e90ff;\n"
"}")

        self.verticalLayout_2.addWidget(self.cb_role)

        self.le_pin = QLineEdit(self.wd_form_edit)
        self.le_pin.setObjectName(u"le_pin")
        self.le_pin.setMinimumSize(QSize(0, 45))
        self.le_pin.setMaximumSize(QSize(16777215, 45))
        self.le_pin.setFont(font1)

        self.verticalLayout_2.addWidget(self.le_pin)

        self.le_password = QLineEdit(self.wd_form_edit)
        self.le_password.setObjectName(u"le_password")
        self.le_password.setMinimumSize(QSize(0, 45))
        self.le_password.setMaximumSize(QSize(16777215, 45))
        self.le_password.setFont(font1)

        self.verticalLayout_2.addWidget(self.le_password)

        self.le_password2 = QLineEdit(self.wd_form_edit)
        self.le_password2.setObjectName(u"le_password2")
        self.le_password2.setMinimumSize(QSize(0, 45))
        self.le_password2.setMaximumSize(QSize(16777215, 45))
        self.le_password2.setFont(font1)

        self.verticalLayout_2.addWidget(self.le_password2)

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

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.wd_form_edit)


        self.verticalLayout.addWidget(self.container)

        self.wd_form_buttons = QWidget(NewUserDialog)
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


        self.retranslateUi(NewUserDialog)

        QMetaObject.connectSlotsByName(NewUserDialog)
    # setupUi

    def retranslateUi(self, NewUserDialog):
        NewUserDialog.setWindowTitle(QCoreApplication.translate("NewUserDialog", u"New User Form", None))
        self.lb_page_title.setText(QCoreApplication.translate("NewUserDialog", u"Create New User", None))
        self.lb_fullname.setText(QCoreApplication.translate("NewUserDialog", u"Full name", None))
        self.lb_username.setText(QCoreApplication.translate("NewUserDialog", u"Username", None))
        self.lb_role.setText(QCoreApplication.translate("NewUserDialog", u"Role", None))
        self.lb_pin.setText(QCoreApplication.translate("NewUserDialog", u"PIN", None))
        self.lb_password.setText(QCoreApplication.translate("NewUserDialog", u"Password", None))
        self.lb_password2.setText(QCoreApplication.translate("NewUserDialog", u"Confirm Password", None))
        self.lb_phone.setText(QCoreApplication.translate("NewUserDialog", u"Phone", None))
        self.lb_email.setText(QCoreApplication.translate("NewUserDialog", u"Email", None))
        self.le_first_name.setPlaceholderText(QCoreApplication.translate("NewUserDialog", u"First Name", None))
        self.le_last_name.setPlaceholderText(QCoreApplication.translate("NewUserDialog", u"Last Name", None))
        self.le_username.setPlaceholderText(QCoreApplication.translate("NewUserDialog", u"Username", None))
        self.cb_role.setItemText(0, QCoreApplication.translate("NewUserDialog", u"Select Role", None))
        self.cb_role.setItemText(1, QCoreApplication.translate("NewUserDialog", u"Admin", None))
        self.cb_role.setItemText(2, QCoreApplication.translate("NewUserDialog", u"Manager", None))
        self.cb_role.setItemText(3, QCoreApplication.translate("NewUserDialog", u"Clerk", None))

        self.le_pin.setPlaceholderText(QCoreApplication.translate("NewUserDialog", u"Personal Identification Number", None))
        self.le_password.setPlaceholderText(QCoreApplication.translate("NewUserDialog", u"Enter Password", None))
        self.le_password2.setPlaceholderText(QCoreApplication.translate("NewUserDialog", u"Confirm Password", None))
        self.le_phone.setPlaceholderText(QCoreApplication.translate("NewUserDialog", u"Phone Number", None))
        self.le_email.setPlaceholderText(QCoreApplication.translate("NewUserDialog", u"Email Address", None))
        self.pb_save.setText(QCoreApplication.translate("NewUserDialog", u"Save User", None))
        self.pb_cancel.setText(QCoreApplication.translate("NewUserDialog", u"Cancel", None))
    # retranslateUi

