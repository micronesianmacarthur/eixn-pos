# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vendor_form_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_VendorFormDialog(object):
    def setupUi(self, VendorFormDialog):
        if not VendorFormDialog.objectName():
            VendorFormDialog.setObjectName(u"VendorFormDialog")
        VendorFormDialog.setWindowModality(Qt.WindowModality.ApplicationModal)
        VendorFormDialog.resize(600, 340)
        VendorFormDialog.setMinimumSize(QSize(600, 340))
        VendorFormDialog.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(VendorFormDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(VendorFormDialog)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 35))
        self.widget.setMaximumSize(QSize(16777215, 35))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lb_form_title = QLabel(self.widget)
        self.lb_form_title.setObjectName(u"lb_form_title")
        self.lb_form_title.setMinimumSize(QSize(0, 35))
        self.lb_form_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lb_form_title, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.widget)

        self.widget_2 = QWidget(VendorFormDialog)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_2 = QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setVerticalSpacing(10)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.grp_company_info = QGroupBox(self.widget_2)
        self.grp_company_info.setObjectName(u"grp_company_info")
        self.verticalLayout = QVBoxLayout(self.grp_company_info)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 20, 5, 5)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lb_company_name = QLabel(self.grp_company_info)
        self.lb_company_name.setObjectName(u"lb_company_name")
        self.lb_company_name.setMinimumSize(QSize(115, 35))
        self.lb_company_name.setMaximumSize(QSize(16777215, 35))
        self.lb_company_name.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.lb_company_name)

        self.le_company_name = QLineEdit(self.grp_company_info)
        self.le_company_name.setObjectName(u"le_company_name")
        self.le_company_name.setMinimumSize(QSize(0, 35))
        self.le_company_name.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout.addWidget(self.le_company_name)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lb_phone = QLabel(self.grp_company_info)
        self.lb_phone.setObjectName(u"lb_phone")
        self.lb_phone.setMinimumSize(QSize(115, 35))
        self.lb_phone.setMaximumSize(QSize(16777215, 35))
        self.lb_phone.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.lb_phone)

        self.le_phone = QLineEdit(self.grp_company_info)
        self.le_phone.setObjectName(u"le_phone")
        self.le_phone.setMinimumSize(QSize(0, 35))
        self.le_phone.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_2.addWidget(self.le_phone)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lb_email = QLabel(self.grp_company_info)
        self.lb_email.setObjectName(u"lb_email")
        self.lb_email.setMinimumSize(QSize(115, 35))
        self.lb_email.setMaximumSize(QSize(16777215, 35))
        self.lb_email.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.lb_email)

        self.le_email = QLineEdit(self.grp_company_info)
        self.le_email.setObjectName(u"le_email")
        self.le_email.setMinimumSize(QSize(0, 35))
        self.le_email.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_3.addWidget(self.le_email)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lb_address = QLabel(self.grp_company_info)
        self.lb_address.setObjectName(u"lb_address")
        self.lb_address.setMinimumSize(QSize(115, 35))
        self.lb_address.setMaximumSize(QSize(16777215, 35))
        self.lb_address.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.lb_address)

        self.le_address = QLineEdit(self.grp_company_info)
        self.le_address.setObjectName(u"le_address")
        self.le_address.setMinimumSize(QSize(0, 35))
        self.le_address.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_4.addWidget(self.le_address)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.gridLayout_2.addWidget(self.grp_company_info, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.widget_3 = QWidget(VendorFormDialog)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 35))
        self.widget_3.setMaximumSize(QSize(16777215, 35))
        self.horizontalLayout_5 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pb_save_vendor = QPushButton(self.widget_3)
        self.pb_save_vendor.setObjectName(u"pb_save_vendor")
        self.pb_save_vendor.setMinimumSize(QSize(0, 35))
        self.pb_save_vendor.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_5.addWidget(self.pb_save_vendor)

        self.pb_close = QPushButton(self.widget_3)
        self.pb_close.setObjectName(u"pb_close")
        self.pb_close.setMinimumSize(QSize(0, 35))
        self.pb_close.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_5.addWidget(self.pb_close)


        self.verticalLayout_2.addWidget(self.widget_3)


        self.retranslateUi(VendorFormDialog)

        QMetaObject.connectSlotsByName(VendorFormDialog)
    # setupUi

    def retranslateUi(self, VendorFormDialog):
        VendorFormDialog.setWindowTitle(QCoreApplication.translate("VendorFormDialog", u"Create Vendor Form", None))
        self.lb_form_title.setText(QCoreApplication.translate("VendorFormDialog", u"Create New Vendor", None))
        self.grp_company_info.setTitle(QCoreApplication.translate("VendorFormDialog", u"Company Information", None))
        self.lb_company_name.setText(QCoreApplication.translate("VendorFormDialog", u"Name of Company:", None))
        self.le_company_name.setPlaceholderText(QCoreApplication.translate("VendorFormDialog", u"Enter name of Company ", None))
        self.lb_phone.setText(QCoreApplication.translate("VendorFormDialog", u"Phone:", None))
        self.le_phone.setPlaceholderText(QCoreApplication.translate("VendorFormDialog", u"Enter company phone number ", None))
        self.lb_email.setText(QCoreApplication.translate("VendorFormDialog", u"Email:", None))
        self.le_email.setPlaceholderText(QCoreApplication.translate("VendorFormDialog", u"Enter company email ", None))
        self.lb_address.setText(QCoreApplication.translate("VendorFormDialog", u"Address:", None))
        self.le_address.setPlaceholderText(QCoreApplication.translate("VendorFormDialog", u"Enter company mailing address ", None))
        self.pb_save_vendor.setText(QCoreApplication.translate("VendorFormDialog", u"Save Vendor", None))
        self.pb_close.setText(QCoreApplication.translate("VendorFormDialog", u"Close", None))
    # retranslateUi

