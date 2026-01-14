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
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_CustomerFormDialog(object):
    def setupUi(self, CustomerFormDialog):
        if not CustomerFormDialog.objectName():
            CustomerFormDialog.setObjectName(u"CustomerFormDialog")
        CustomerFormDialog.setWindowModality(Qt.WindowModality.ApplicationModal)
        CustomerFormDialog.resize(600, 600)
        CustomerFormDialog.setMinimumSize(QSize(600, 600))
        CustomerFormDialog.setMaximumSize(QSize(600, 600))
        CustomerFormDialog.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(CustomerFormDialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_3 = QWidget(CustomerFormDialog)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMaximumSize(QSize(16777215, 35))
        self.gridLayout = QGridLayout(self.widget_3)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lb_form_title = QLabel(self.widget_3)
        self.lb_form_title.setObjectName(u"lb_form_title")
        self.lb_form_title.setMinimumSize(QSize(0, 35))
        self.lb_form_title.setMaximumSize(QSize(16777215, 35))
        self.lb_form_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lb_form_title, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.widget_3)

        self.widget = QWidget(CustomerFormDialog)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.grp_personal_info = QGroupBox(self.widget)
        self.grp_personal_info.setObjectName(u"grp_personal_info")
        self.grp_personal_info.setMinimumSize(QSize(0, 0))
        self.verticalLayout = QVBoxLayout(self.grp_personal_info)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 20, 5, 5)
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(10)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lb_first_name = QLabel(self.grp_personal_info)
        self.lb_first_name.setObjectName(u"lb_first_name")
        self.lb_first_name.setMinimumSize(QSize(80, 35))
        self.lb_first_name.setMaximumSize(QSize(16777215, 35))
        self.lb_first_name.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.lb_first_name)

        self.le_first_name = QLineEdit(self.grp_personal_info)
        self.le_first_name.setObjectName(u"le_first_name")
        self.le_first_name.setMinimumSize(QSize(0, 35))
        self.le_first_name.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout.addWidget(self.le_first_name)


        self.horizontalLayout_11.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lb_last_name = QLabel(self.grp_personal_info)
        self.lb_last_name.setObjectName(u"lb_last_name")
        self.lb_last_name.setMinimumSize(QSize(80, 35))
        self.lb_last_name.setMaximumSize(QSize(16777215, 35))
        self.lb_last_name.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.lb_last_name)

        self.le_last_name = QLineEdit(self.grp_personal_info)
        self.le_last_name.setObjectName(u"le_last_name")
        self.le_last_name.setMinimumSize(QSize(0, 35))
        self.le_last_name.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_2.addWidget(self.le_last_name)


        self.horizontalLayout_11.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(10)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lb_phone = QLabel(self.grp_personal_info)
        self.lb_phone.setObjectName(u"lb_phone")
        self.lb_phone.setMinimumSize(QSize(80, 35))
        self.lb_phone.setMaximumSize(QSize(16777215, 35))
        self.lb_phone.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.lb_phone)

        self.le_phone = QLineEdit(self.grp_personal_info)
        self.le_phone.setObjectName(u"le_phone")
        self.le_phone.setMinimumSize(QSize(0, 35))
        self.le_phone.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_3.addWidget(self.le_phone)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lb_email = QLabel(self.grp_personal_info)
        self.lb_email.setObjectName(u"lb_email")
        self.lb_email.setMinimumSize(QSize(80, 35))
        self.lb_email.setMaximumSize(QSize(16777215, 35))
        self.lb_email.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.lb_email)

        self.le_email = QLineEdit(self.grp_personal_info)
        self.le_email.setObjectName(u"le_email")
        self.le_email.setMinimumSize(QSize(0, 35))
        self.le_email.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_4.addWidget(self.le_email)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_4)


        self.verticalLayout.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lb_address = QLabel(self.grp_personal_info)
        self.lb_address.setObjectName(u"lb_address")
        self.lb_address.setMinimumSize(QSize(80, 35))
        self.lb_address.setMaximumSize(QSize(16777215, 35))
        self.lb_address.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.lb_address)

        self.le_address = QLineEdit(self.grp_personal_info)
        self.le_address.setObjectName(u"le_address")
        self.le_address.setMinimumSize(QSize(0, 35))
        self.le_address.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_5.addWidget(self.le_address)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.verticalLayout_4.addWidget(self.grp_personal_info)

        self.grp_account = QGroupBox(self.widget)
        self.grp_account.setObjectName(u"grp_account")
        self.verticalLayout_2 = QVBoxLayout(self.grp_account)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 20, 5, 5)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lb_charge_account = QLabel(self.grp_account)
        self.lb_charge_account.setObjectName(u"lb_charge_account")
        self.lb_charge_account.setMinimumSize(QSize(130, 35))
        self.lb_charge_account.setMaximumSize(QSize(100, 35))
        self.lb_charge_account.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.lb_charge_account)

        self.cb_charge_account = QComboBox(self.grp_account)
        self.cb_charge_account.addItem("")
        self.cb_charge_account.addItem("")
        self.cb_charge_account.setObjectName(u"cb_charge_account")
        self.cb_charge_account.setMinimumSize(QSize(0, 35))
        self.cb_charge_account.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_6.addWidget(self.cb_charge_account)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(10)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lb_system_limit = QLabel(self.grp_account)
        self.lb_system_limit.setObjectName(u"lb_system_limit")
        self.lb_system_limit.setMinimumSize(QSize(130, 35))
        self.lb_system_limit.setMaximumSize(QSize(130, 35))
        self.lb_system_limit.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.lb_system_limit)

        self.chk_system_limit = QCheckBox(self.grp_account)
        self.chk_system_limit.setObjectName(u"chk_system_limit")
        self.chk_system_limit.setMinimumSize(QSize(130, 35))
        self.chk_system_limit.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_7.addWidget(self.chk_system_limit)


        self.horizontalLayout_13.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lb_custom_limit = QLabel(self.grp_account)
        self.lb_custom_limit.setObjectName(u"lb_custom_limit")
        self.lb_custom_limit.setMinimumSize(QSize(100, 35))
        self.lb_custom_limit.setMaximumSize(QSize(100, 35))
        self.lb_custom_limit.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.lb_custom_limit)

        self.le_custom_limit = QLineEdit(self.grp_account)
        self.le_custom_limit.setObjectName(u"le_custom_limit")
        self.le_custom_limit.setMinimumSize(QSize(0, 35))
        self.le_custom_limit.setMaximumSize(QSize(120, 35))

        self.horizontalLayout_8.addWidget(self.le_custom_limit)


        self.horizontalLayout_13.addLayout(self.horizontalLayout_8)


        self.verticalLayout_2.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lb_disable_limit = QLabel(self.grp_account)
        self.lb_disable_limit.setObjectName(u"lb_disable_limit")
        self.lb_disable_limit.setMinimumSize(QSize(130, 35))
        self.lb_disable_limit.setMaximumSize(QSize(130, 35))

        self.horizontalLayout_9.addWidget(self.lb_disable_limit)

        self.chk_disable_limit = QCheckBox(self.grp_account)
        self.chk_disable_limit.setObjectName(u"chk_disable_limit")
        self.chk_disable_limit.setMinimumSize(QSize(0, 35))
        self.chk_disable_limit.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_9.addWidget(self.chk_disable_limit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)


        self.verticalLayout_4.addWidget(self.grp_account)


        self.verticalLayout_3.addWidget(self.widget)

        self.verticalSpacer = QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.widget_2 = QWidget(CustomerFormDialog)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 35))
        self.widget_2.setMaximumSize(QSize(16777215, 35))
        self.horizontalLayout_10 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.pb_save_customer = QPushButton(self.widget_2)
        self.pb_save_customer.setObjectName(u"pb_save_customer")
        self.pb_save_customer.setMinimumSize(QSize(0, 35))
        self.pb_save_customer.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_10.addWidget(self.pb_save_customer)

        self.pb_close_form = QPushButton(self.widget_2)
        self.pb_close_form.setObjectName(u"pb_close_form")
        self.pb_close_form.setMinimumSize(QSize(0, 35))
        self.pb_close_form.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_10.addWidget(self.pb_close_form)


        self.verticalLayout_3.addWidget(self.widget_2)


        self.retranslateUi(CustomerFormDialog)

        QMetaObject.connectSlotsByName(CustomerFormDialog)
    # setupUi

    def retranslateUi(self, CustomerFormDialog):
        CustomerFormDialog.setWindowTitle(QCoreApplication.translate("CustomerFormDialog", u"Create Customer Form", None))
        self.lb_form_title.setText(QCoreApplication.translate("CustomerFormDialog", u"Create New Customer", None))
        self.grp_personal_info.setTitle(QCoreApplication.translate("CustomerFormDialog", u"Personal Information", None))
        self.lb_first_name.setText(QCoreApplication.translate("CustomerFormDialog", u"First Name:", None))
        self.le_first_name.setPlaceholderText(QCoreApplication.translate("CustomerFormDialog", u"e.g. John", None))
        self.lb_last_name.setText(QCoreApplication.translate("CustomerFormDialog", u"Last Name:", None))
        self.le_last_name.setPlaceholderText(QCoreApplication.translate("CustomerFormDialog", u"Doe", None))
        self.lb_phone.setText(QCoreApplication.translate("CustomerFormDialog", u"Phone:", None))
        self.le_phone.setPlaceholderText(QCoreApplication.translate("CustomerFormDialog", u"320-1234", None))
        self.lb_email.setText(QCoreApplication.translate("CustomerFormDialog", u"Email:", None))
        self.le_email.setPlaceholderText(QCoreApplication.translate("CustomerFormDialog", u"john@example.email", None))
        self.lb_address.setText(QCoreApplication.translate("CustomerFormDialog", u"Address:", None))
        self.le_address.setPlaceholderText(QCoreApplication.translate("CustomerFormDialog", u"P.O. Box 123, Kolonia, Pohnpei, FM 96941", None))
        self.grp_account.setTitle(QCoreApplication.translate("CustomerFormDialog", u"Account", None))
        self.lb_charge_account.setText(QCoreApplication.translate("CustomerFormDialog", u"Charge to Account:", None))
        self.cb_charge_account.setItemText(0, QCoreApplication.translate("CustomerFormDialog", u"Disabled", None))
        self.cb_charge_account.setItemText(1, QCoreApplication.translate("CustomerFormDialog", u"Enabled", None))

        self.lb_system_limit.setText(QCoreApplication.translate("CustomerFormDialog", u"Use System Limit:", None))
        self.chk_system_limit.setText(QCoreApplication.translate("CustomerFormDialog", u"$50.00", None))
        self.lb_custom_limit.setText(QCoreApplication.translate("CustomerFormDialog", u"Charge Limit:", None))
        self.lb_disable_limit.setText("")
        self.chk_disable_limit.setText(QCoreApplication.translate("CustomerFormDialog", u"No Charge Limit", None))
        self.pb_save_customer.setText(QCoreApplication.translate("CustomerFormDialog", u"Save Customer", None))
        self.pb_close_form.setText(QCoreApplication.translate("CustomerFormDialog", u"Close", None))
    # retranslateUi

