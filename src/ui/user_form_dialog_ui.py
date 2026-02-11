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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_UserFormDialog(object):
    def setupUi(self, UserFormDialog):
        if not UserFormDialog.objectName():
            UserFormDialog.setObjectName(u"UserFormDialog")
        UserFormDialog.setWindowModality(Qt.WindowModality.ApplicationModal)
        UserFormDialog.resize(600, 600)
        UserFormDialog.setMinimumSize(QSize(600, 600))
        UserFormDialog.setMaximumSize(QSize(600, 600))
        UserFormDialog.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(UserFormDialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget = QWidget(UserFormDialog)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 35))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lb_form_title = QLabel(self.widget)
        self.lb_form_title.setObjectName(u"lb_form_title")
        self.lb_form_title.setMaximumSize(QSize(16777215, 35))
        self.lb_form_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lb_form_title, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.widget)

        self.widget_2 = QWidget(UserFormDialog)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_4 = QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.grp_personal_info = QGroupBox(self.widget_2)
        self.grp_personal_info.setObjectName(u"grp_personal_info")
        self.verticalLayout = QVBoxLayout(self.grp_personal_info)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 20, 5, 5)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lb_username = QLabel(self.grp_personal_info)
        self.lb_username.setObjectName(u"lb_username")
        self.lb_username.setMinimumSize(QSize(80, 35))
        self.lb_username.setMaximumSize(QSize(16777215, 35))
        self.lb_username.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.lb_username)

        self.le_username = QLineEdit(self.grp_personal_info)
        self.le_username.setObjectName(u"le_username")
        self.le_username.setMinimumSize(QSize(0, 35))
        self.le_username.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout.addWidget(self.le_username)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(10)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lb_first_name = QLabel(self.grp_personal_info)
        self.lb_first_name.setObjectName(u"lb_first_name")
        self.lb_first_name.setMinimumSize(QSize(80, 35))
        self.lb_first_name.setMaximumSize(QSize(16777215, 35))
        self.lb_first_name.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.lb_first_name)

        self.le_first_name = QLineEdit(self.grp_personal_info)
        self.le_first_name.setObjectName(u"le_first_name")
        self.le_first_name.setMinimumSize(QSize(0, 35))
        self.le_first_name.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_2.addWidget(self.le_first_name)


        self.horizontalLayout_15.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lb_last_name = QLabel(self.grp_personal_info)
        self.lb_last_name.setObjectName(u"lb_last_name")
        self.lb_last_name.setMinimumSize(QSize(80, 35))
        self.lb_last_name.setMaximumSize(QSize(16777215, 35))
        self.lb_last_name.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.lb_last_name)

        self.le_last_name = QLineEdit(self.grp_personal_info)
        self.le_last_name.setObjectName(u"le_last_name")
        self.le_last_name.setMinimumSize(QSize(0, 35))
        self.le_last_name.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_3.addWidget(self.le_last_name)


        self.horizontalLayout_15.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setSpacing(10)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lb_phone = QLabel(self.grp_personal_info)
        self.lb_phone.setObjectName(u"lb_phone")
        self.lb_phone.setMinimumSize(QSize(80, 35))
        self.lb_phone.setMaximumSize(QSize(16777215, 35))
        self.lb_phone.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.lb_phone)

        self.le_phone = QLineEdit(self.grp_personal_info)
        self.le_phone.setObjectName(u"le_phone")
        self.le_phone.setMinimumSize(QSize(0, 35))
        self.le_phone.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_4.addWidget(self.le_phone)


        self.horizontalLayout_16.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lb_email = QLabel(self.grp_personal_info)
        self.lb_email.setObjectName(u"lb_email")
        self.lb_email.setMinimumSize(QSize(80, 35))
        self.lb_email.setMaximumSize(QSize(16777215, 35))
        self.lb_email.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.lb_email)

        self.le_email = QLineEdit(self.grp_personal_info)
        self.le_email.setObjectName(u"le_email")
        self.le_email.setMinimumSize(QSize(0, 35))
        self.le_email.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_5.addWidget(self.le_email)


        self.horizontalLayout_16.addLayout(self.horizontalLayout_5)


        self.verticalLayout.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lb_address = QLabel(self.grp_personal_info)
        self.lb_address.setObjectName(u"lb_address")
        self.lb_address.setMinimumSize(QSize(80, 35))
        self.lb_address.setMaximumSize(QSize(16777215, 35))
        self.lb_address.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.lb_address)

        self.le_address = QLineEdit(self.grp_personal_info)
        self.le_address.setObjectName(u"le_address")
        self.le_address.setMinimumSize(QSize(0, 35))
        self.le_address.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_6.addWidget(self.le_address)


        self.verticalLayout.addLayout(self.horizontalLayout_6)


        self.verticalLayout_4.addWidget(self.grp_personal_info)

        self.grp_security_auth = QGroupBox(self.widget_2)
        self.grp_security_auth.setObjectName(u"grp_security_auth")
        self.verticalLayout_2 = QVBoxLayout(self.grp_security_auth)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 20, 5, 5)
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(10)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lb_role = QLabel(self.grp_security_auth)
        self.lb_role.setObjectName(u"lb_role")
        self.lb_role.setMinimumSize(QSize(120, 35))
        self.lb_role.setMaximumSize(QSize(120, 35))
        self.lb_role.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.lb_role)

        self.cb_role = QComboBox(self.grp_security_auth)
        self.cb_role.setObjectName(u"cb_role")
        self.cb_role.setMinimumSize(QSize(0, 35))
        self.cb_role.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_7.addWidget(self.cb_role)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lb_status = QLabel(self.grp_security_auth)
        self.lb_status.setObjectName(u"lb_status")
        self.lb_status.setMinimumSize(QSize(80, 35))
        self.lb_status.setMaximumSize(QSize(120, 35))
        self.lb_status.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.lb_status)

        self.cb_status = QComboBox(self.grp_security_auth)
        self.cb_status.addItem("")
        self.cb_status.addItem("")
        self.cb_status.setObjectName(u"cb_status")
        self.cb_status.setMinimumSize(QSize(0, 35))
        self.cb_status.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_8.addWidget(self.cb_status)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_8)


        self.verticalLayout_2.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lb_pin = QLabel(self.grp_security_auth)
        self.lb_pin.setObjectName(u"lb_pin")
        self.lb_pin.setMinimumSize(QSize(120, 35))
        self.lb_pin.setMaximumSize(QSize(120, 35))
        self.lb_pin.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.lb_pin)

        self.le_pin = QLineEdit(self.grp_security_auth)
        self.le_pin.setObjectName(u"le_pin")
        self.le_pin.setMinimumSize(QSize(0, 35))
        self.le_pin.setMaximumSize(QSize(16777215, 35))
        self.le_pin.setEchoMode(QLineEdit.EchoMode.Password)

        self.horizontalLayout_10.addWidget(self.le_pin)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(10)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.lb_password = QLabel(self.grp_security_auth)
        self.lb_password.setObjectName(u"lb_password")
        self.lb_password.setMinimumSize(QSize(120, 35))
        self.lb_password.setMaximumSize(QSize(120, 35))
        self.lb_password.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.lb_password)

        self.le_password = QLineEdit(self.grp_security_auth)
        self.le_password.setObjectName(u"le_password")
        self.le_password.setMinimumSize(QSize(0, 35))
        self.le_password.setMaximumSize(QSize(16777215, 35))
        self.le_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.horizontalLayout_11.addWidget(self.le_password)


        self.horizontalLayout_13.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.lb_password_2 = QLabel(self.grp_security_auth)
        self.lb_password_2.setObjectName(u"lb_password_2")
        self.lb_password_2.setMinimumSize(QSize(120, 35))
        self.lb_password_2.setMaximumSize(QSize(120, 35))
        self.lb_password_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.lb_password_2)

        self.le_password_2 = QLineEdit(self.grp_security_auth)
        self.le_password_2.setObjectName(u"le_password_2")
        self.le_password_2.setMinimumSize(QSize(0, 35))
        self.le_password_2.setMaximumSize(QSize(16777215, 35))
        self.le_password_2.setEchoMode(QLineEdit.EchoMode.Password)

        self.horizontalLayout_12.addWidget(self.le_password_2)


        self.horizontalLayout_13.addLayout(self.horizontalLayout_12)


        self.verticalLayout_2.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lb_charge_account = QLabel(self.grp_security_auth)
        self.lb_charge_account.setObjectName(u"lb_charge_account")
        self.lb_charge_account.setMinimumSize(QSize(120, 35))
        self.lb_charge_account.setMaximumSize(QSize(120, 35))
        self.lb_charge_account.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.lb_charge_account)

        self.cb_charge_account = QComboBox(self.grp_security_auth)
        self.cb_charge_account.addItem("")
        self.cb_charge_account.addItem("")
        self.cb_charge_account.setObjectName(u"cb_charge_account")
        self.cb_charge_account.setMinimumSize(QSize(0, 35))
        self.cb_charge_account.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_9.addWidget(self.cb_charge_account)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setSpacing(10)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.lb_system_limit = QLabel(self.grp_security_auth)
        self.lb_system_limit.setObjectName(u"lb_system_limit")
        self.lb_system_limit.setMinimumSize(QSize(120, 35))
        self.lb_system_limit.setMaximumSize(QSize(16777215, 16777215))
        self.lb_system_limit.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_18.addWidget(self.lb_system_limit)

        self.chk_system_limit = QCheckBox(self.grp_security_auth)
        self.chk_system_limit.setObjectName(u"chk_system_limit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chk_system_limit.sizePolicy().hasHeightForWidth())
        self.chk_system_limit.setSizePolicy(sizePolicy)
        self.chk_system_limit.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_18.addWidget(self.chk_system_limit)


        self.horizontalLayout_21.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.lb_custom_limit = QLabel(self.grp_security_auth)
        self.lb_custom_limit.setObjectName(u"lb_custom_limit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lb_custom_limit.sizePolicy().hasHeightForWidth())
        self.lb_custom_limit.setSizePolicy(sizePolicy1)
        self.lb_custom_limit.setMinimumSize(QSize(120, 35))
        self.lb_custom_limit.setMaximumSize(QSize(120, 16777215))
        self.lb_custom_limit.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_19.addWidget(self.lb_custom_limit)

        self.le_custom_limit = QLineEdit(self.grp_security_auth)
        self.le_custom_limit.setObjectName(u"le_custom_limit")
        self.le_custom_limit.setMinimumSize(QSize(0, 35))
        self.le_custom_limit.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_19.addWidget(self.le_custom_limit)


        self.horizontalLayout_21.addLayout(self.horizontalLayout_19)


        self.verticalLayout_2.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.lb_disable_limit = QLabel(self.grp_security_auth)
        self.lb_disable_limit.setObjectName(u"lb_disable_limit")
        self.lb_disable_limit.setMinimumSize(QSize(120, 35))
        self.lb_disable_limit.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_20.addWidget(self.lb_disable_limit)

        self.chk_disable_limit = QCheckBox(self.grp_security_auth)
        self.chk_disable_limit.setObjectName(u"chk_disable_limit")
        self.chk_disable_limit.setMinimumSize(QSize(140, 35))

        self.horizontalLayout_20.addWidget(self.chk_disable_limit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_20)


        self.verticalLayout_4.addWidget(self.grp_security_auth)


        self.verticalLayout_3.addWidget(self.widget_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.widget_3 = QWidget(UserFormDialog)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 0))
        self.widget_3.setMaximumSize(QSize(16777215, 35))
        self.horizontalLayout_17 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_17.setSpacing(10)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.pb_save_user = QPushButton(self.widget_3)
        self.pb_save_user.setObjectName(u"pb_save_user")
        self.pb_save_user.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_17.addWidget(self.pb_save_user)

        self.pb_close_form = QPushButton(self.widget_3)
        self.pb_close_form.setObjectName(u"pb_close_form")
        self.pb_close_form.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_17.addWidget(self.pb_close_form)


        self.verticalLayout_3.addWidget(self.widget_3)


        self.retranslateUi(UserFormDialog)

        QMetaObject.connectSlotsByName(UserFormDialog)
    # setupUi

    def retranslateUi(self, UserFormDialog):
        UserFormDialog.setWindowTitle(QCoreApplication.translate("UserFormDialog", u"Create User Form", None))
        self.lb_form_title.setText(QCoreApplication.translate("UserFormDialog", u"Create New User", None))
        self.grp_personal_info.setTitle(QCoreApplication.translate("UserFormDialog", u"Personal Information", None))
        self.lb_username.setText(QCoreApplication.translate("UserFormDialog", u"Username:", None))
        self.le_username.setPlaceholderText(QCoreApplication.translate("UserFormDialog", u"e.g. john", None))
        self.lb_first_name.setText(QCoreApplication.translate("UserFormDialog", u"First Name:", None))
        self.le_first_name.setPlaceholderText(QCoreApplication.translate("UserFormDialog", u"John", None))
        self.lb_last_name.setText(QCoreApplication.translate("UserFormDialog", u"Last Name:", None))
        self.le_last_name.setPlaceholderText(QCoreApplication.translate("UserFormDialog", u"Doe", None))
        self.lb_phone.setText(QCoreApplication.translate("UserFormDialog", u"Phone:", None))
        self.le_phone.setPlaceholderText(QCoreApplication.translate("UserFormDialog", u"320-1234", None))
        self.lb_email.setText(QCoreApplication.translate("UserFormDialog", u"Email:", None))
        self.le_email.setPlaceholderText(QCoreApplication.translate("UserFormDialog", u"john@example.email", None))
        self.lb_address.setText(QCoreApplication.translate("UserFormDialog", u"Address:", None))
        self.le_address.setPlaceholderText(QCoreApplication.translate("UserFormDialog", u"P.O. Box 123, Kolonia, Pohnpei, FM 96941", None))
        self.grp_security_auth.setTitle(QCoreApplication.translate("UserFormDialog", u"Security and Authorization", None))
        self.lb_role.setText(QCoreApplication.translate("UserFormDialog", u"Role:", None))
        self.lb_status.setText(QCoreApplication.translate("UserFormDialog", u"Status:", None))
        self.cb_status.setItemText(0, QCoreApplication.translate("UserFormDialog", u"Active", None))
        self.cb_status.setItemText(1, QCoreApplication.translate("UserFormDialog", u"Inactive", None))

        self.lb_pin.setText(QCoreApplication.translate("UserFormDialog", u"PIN:", None))
        self.le_pin.setPlaceholderText(QCoreApplication.translate("UserFormDialog", u"Enter PIN here...", None))
        self.lb_password.setText(QCoreApplication.translate("UserFormDialog", u"Password:", None))
        self.le_password.setPlaceholderText(QCoreApplication.translate("UserFormDialog", u"Enter Password here...", None))
        self.lb_password_2.setText(QCoreApplication.translate("UserFormDialog", u"Confirm Password:", None))
        self.le_password_2.setPlaceholderText(QCoreApplication.translate("UserFormDialog", u"Confirm Password here...", None))
        self.lb_charge_account.setText(QCoreApplication.translate("UserFormDialog", u"Charge to Account:", None))
        self.cb_charge_account.setItemText(0, QCoreApplication.translate("UserFormDialog", u"Disabled", None))
        self.cb_charge_account.setItemText(1, QCoreApplication.translate("UserFormDialog", u"Enabled", None))

        self.lb_system_limit.setText(QCoreApplication.translate("UserFormDialog", u"Use System Limit:", None))
        self.chk_system_limit.setText(QCoreApplication.translate("UserFormDialog", u"CheckBox", None))
        self.lb_custom_limit.setText(QCoreApplication.translate("UserFormDialog", u"Custom Limit:", None))
        self.le_custom_limit.setPlaceholderText(QCoreApplication.translate("UserFormDialog", u"0.00", None))
        self.lb_disable_limit.setText("")
        self.chk_disable_limit.setText(QCoreApplication.translate("UserFormDialog", u"No Charge Limit", None))
        self.pb_save_user.setText(QCoreApplication.translate("UserFormDialog", u"Save User", None))
        self.pb_close_form.setText(QCoreApplication.translate("UserFormDialog", u"Close", None))
    # retranslateUi

