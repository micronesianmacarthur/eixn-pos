# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_customer_dialog.ui'
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
    QDoubleSpinBox, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)
import icons_rc

class Ui_CreateCustomerDialog(object):
    def setupUi(self, CreateCustomerDialog):
        if not CreateCustomerDialog.objectName():
            CreateCustomerDialog.setObjectName(u"CreateCustomerDialog")
        CreateCustomerDialog.setWindowModality(Qt.WindowModality.ApplicationModal)
        CreateCustomerDialog.resize(850, 690)
        CreateCustomerDialog.setMinimumSize(QSize(850, 690))
        CreateCustomerDialog.setMaximumSize(QSize(850, 690))
        CreateCustomerDialog.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(CreateCustomerDialog)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(CreateCustomerDialog)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 35))
        self.widget.setMaximumSize(QSize(16777215, 35))
        self.horizontalLayout_10 = QHBoxLayout(self.widget)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.lb_dialog_title = QLabel(self.widget)
        self.lb_dialog_title.setObjectName(u"lb_dialog_title")
        self.lb_dialog_title.setMinimumSize(QSize(0, 35))
        self.lb_dialog_title.setMaximumSize(QSize(16777215, 35))
        self.lb_dialog_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_10.addWidget(self.lb_dialog_title)


        self.verticalLayout_4.addWidget(self.widget)

        self.widget_2 = QWidget(CreateCustomerDialog)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_22 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_22.setSpacing(5)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_3 = QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 10, 5, 10)
        self.grp_bill_to = QGroupBox(self.widget_3)
        self.grp_bill_to.setObjectName(u"grp_bill_to")
        self.grp_bill_to.setMaximumSize(QSize(16777215, 280))
        self.verticalLayout = QVBoxLayout(self.grp_bill_to)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 20, 5, 5)
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(20)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lb_last_name = QLabel(self.grp_bill_to)
        self.lb_last_name.setObjectName(u"lb_last_name")
        self.lb_last_name.setMinimumSize(QSize(75, 25))
        self.lb_last_name.setMaximumSize(QSize(75, 25))

        self.horizontalLayout.addWidget(self.lb_last_name)

        self.le_last_name = QLineEdit(self.grp_bill_to)
        self.le_last_name.setObjectName(u"le_last_name")
        self.le_last_name.setMinimumSize(QSize(0, 25))
        self.le_last_name.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout.addWidget(self.le_last_name)


        self.horizontalLayout_13.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lb_first_name = QLabel(self.grp_bill_to)
        self.lb_first_name.setObjectName(u"lb_first_name")
        self.lb_first_name.setMinimumSize(QSize(75, 25))
        self.lb_first_name.setMaximumSize(QSize(75, 25))

        self.horizontalLayout_2.addWidget(self.lb_first_name)

        self.le_first_name = QLineEdit(self.grp_bill_to)
        self.le_first_name.setObjectName(u"le_first_name")
        self.le_first_name.setMinimumSize(QSize(0, 25))
        self.le_first_name.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_2.addWidget(self.le_first_name)


        self.horizontalLayout_13.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lb_company = QLabel(self.grp_bill_to)
        self.lb_company.setObjectName(u"lb_company")
        self.lb_company.setMinimumSize(QSize(75, 25))
        self.lb_company.setMaximumSize(QSize(75, 25))

        self.horizontalLayout_3.addWidget(self.lb_company)

        self.le_company = QLineEdit(self.grp_bill_to)
        self.le_company.setObjectName(u"le_company")
        self.le_company.setMinimumSize(QSize(0, 25))
        self.le_company.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_3.addWidget(self.le_company)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lb_street_1 = QLabel(self.grp_bill_to)
        self.lb_street_1.setObjectName(u"lb_street_1")
        self.lb_street_1.setMinimumSize(QSize(75, 25))
        self.lb_street_1.setMaximumSize(QSize(75, 25))

        self.horizontalLayout_4.addWidget(self.lb_street_1)

        self.le_street_1 = QLineEdit(self.grp_bill_to)
        self.le_street_1.setObjectName(u"le_street_1")
        self.le_street_1.setMinimumSize(QSize(0, 25))
        self.le_street_1.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_4.addWidget(self.le_street_1)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lb_street_2 = QLabel(self.grp_bill_to)
        self.lb_street_2.setObjectName(u"lb_street_2")
        self.lb_street_2.setMinimumSize(QSize(75, 25))
        self.lb_street_2.setMaximumSize(QSize(75, 25))

        self.horizontalLayout_5.addWidget(self.lb_street_2)

        self.le_street_2 = QLineEdit(self.grp_bill_to)
        self.le_street_2.setObjectName(u"le_street_2")
        self.le_street_2.setMinimumSize(QSize(0, 25))
        self.le_street_2.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_5.addWidget(self.le_street_2)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setSpacing(20)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lb_city = QLabel(self.grp_bill_to)
        self.lb_city.setObjectName(u"lb_city")
        self.lb_city.setMinimumSize(QSize(75, 25))
        self.lb_city.setMaximumSize(QSize(75, 25))

        self.horizontalLayout_6.addWidget(self.lb_city)

        self.le_city = QLineEdit(self.grp_bill_to)
        self.le_city.setObjectName(u"le_city")
        self.le_city.setMinimumSize(QSize(0, 25))
        self.le_city.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_6.addWidget(self.le_city)


        self.horizontalLayout_25.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lb_state = QLabel(self.grp_bill_to)
        self.lb_state.setObjectName(u"lb_state")
        self.lb_state.setMinimumSize(QSize(75, 25))
        self.lb_state.setMaximumSize(QSize(75, 25))

        self.horizontalLayout_7.addWidget(self.lb_state)

        self.cb_state = QComboBox(self.grp_bill_to)
        self.cb_state.setObjectName(u"cb_state")
        self.cb_state.setMinimumSize(QSize(235, 25))
        self.cb_state.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_7.addWidget(self.cb_state)


        self.horizontalLayout_25.addLayout(self.horizontalLayout_7)


        self.verticalLayout.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(20)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lb_country = QLabel(self.grp_bill_to)
        self.lb_country.setObjectName(u"lb_country")
        self.lb_country.setMinimumSize(QSize(75, 25))
        self.lb_country.setMaximumSize(QSize(75, 25))

        self.horizontalLayout_9.addWidget(self.lb_country)

        self.cb_country = QComboBox(self.grp_bill_to)
        self.cb_country.setObjectName(u"cb_country")
        self.cb_country.setMinimumSize(QSize(300, 25))
        self.cb_country.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_9.addWidget(self.cb_country)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_9)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lb_zip_code = QLabel(self.grp_bill_to)
        self.lb_zip_code.setObjectName(u"lb_zip_code")
        self.lb_zip_code.setMinimumSize(QSize(75, 25))
        self.lb_zip_code.setMaximumSize(QSize(75, 25))

        self.horizontalLayout_8.addWidget(self.lb_zip_code)

        self.sb_zip_code = QSpinBox(self.grp_bill_to)
        self.sb_zip_code.setObjectName(u"sb_zip_code")
        self.sb_zip_code.setMinimumSize(QSize(100, 25))
        self.sb_zip_code.setMaximumSize(QSize(100, 25))
        self.sb_zip_code.setMaximum(999999999)

        self.horizontalLayout_8.addWidget(self.sb_zip_code)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_8)


        self.verticalLayout.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(5)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.lb_phone = QLabel(self.grp_bill_to)
        self.lb_phone.setObjectName(u"lb_phone")
        self.lb_phone.setMinimumSize(QSize(75, 25))
        self.lb_phone.setMaximumSize(QSize(75, 25))

        self.horizontalLayout_11.addWidget(self.lb_phone)

        self.le_phone = QLineEdit(self.grp_bill_to)
        self.le_phone.setObjectName(u"le_phone")
        self.le_phone.setMinimumSize(QSize(0, 25))
        self.le_phone.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_11.addWidget(self.le_phone)


        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(5)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.lb_email = QLabel(self.grp_bill_to)
        self.lb_email.setObjectName(u"lb_email")
        self.lb_email.setMinimumSize(QSize(75, 25))
        self.lb_email.setMaximumSize(QSize(75, 25))

        self.horizontalLayout_12.addWidget(self.lb_email)

        self.le_email = QLineEdit(self.grp_bill_to)
        self.le_email.setObjectName(u"le_email")
        self.le_email.setMinimumSize(QSize(0, 25))
        self.le_email.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_12.addWidget(self.le_email)


        self.verticalLayout.addLayout(self.horizontalLayout_12)


        self.verticalLayout_3.addWidget(self.grp_bill_to)

        self.grp_account = QGroupBox(self.widget_3)
        self.grp_account.setObjectName(u"grp_account")
        self.grp_account.setMaximumSize(QSize(16777215, 180))
        self.verticalLayout_2 = QVBoxLayout(self.grp_account)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 20, 5, 5)
        self.chk_allow_account_charge = QCheckBox(self.grp_account)
        self.chk_allow_account_charge.setObjectName(u"chk_allow_account_charge")
        self.chk_allow_account_charge.setMinimumSize(QSize(180, 25))
        self.chk_allow_account_charge.setMaximumSize(QSize(180, 25))

        self.verticalLayout_2.addWidget(self.chk_allow_account_charge)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setSpacing(5)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.lb_system_charge_limit_label = QLabel(self.grp_account)
        self.lb_system_charge_limit_label.setObjectName(u"lb_system_charge_limit_label")
        self.lb_system_charge_limit_label.setMinimumSize(QSize(155, 25))
        self.lb_system_charge_limit_label.setMaximumSize(QSize(155, 25))

        self.horizontalLayout_17.addWidget(self.lb_system_charge_limit_label)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(5)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.system_charge_limit_dollar_label = QLabel(self.grp_account)
        self.system_charge_limit_dollar_label.setObjectName(u"system_charge_limit_dollar_label")
        self.system_charge_limit_dollar_label.setMinimumSize(QSize(0, 25))
        self.system_charge_limit_dollar_label.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_15.addWidget(self.system_charge_limit_dollar_label)

        self.lb_system_charge_limit = QLabel(self.grp_account)
        self.lb_system_charge_limit.setObjectName(u"lb_system_charge_limit")
        self.lb_system_charge_limit.setMinimumSize(QSize(100, 25))
        self.lb_system_charge_limit.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_15.addWidget(self.lb_system_charge_limit)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer)


        self.horizontalLayout_17.addLayout(self.horizontalLayout_15)


        self.verticalLayout_2.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setSpacing(5)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.lb_custom_charge_limit_label = QLabel(self.grp_account)
        self.lb_custom_charge_limit_label.setObjectName(u"lb_custom_charge_limit_label")
        self.lb_custom_charge_limit_label.setMinimumSize(QSize(155, 25))
        self.lb_custom_charge_limit_label.setMaximumSize(QSize(155, 25))

        self.horizontalLayout_18.addWidget(self.lb_custom_charge_limit_label)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setSpacing(5)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.custom_charge_limit_dollar_label = QLabel(self.grp_account)
        self.custom_charge_limit_dollar_label.setObjectName(u"custom_charge_limit_dollar_label")
        self.custom_charge_limit_dollar_label.setMinimumSize(QSize(0, 25))
        self.custom_charge_limit_dollar_label.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_16.addWidget(self.custom_charge_limit_dollar_label)

        self.dbl_custom_charge_limit = QDoubleSpinBox(self.grp_account)
        self.dbl_custom_charge_limit.setObjectName(u"dbl_custom_charge_limit")
        self.dbl_custom_charge_limit.setMinimumSize(QSize(100, 25))
        self.dbl_custom_charge_limit.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_16.addWidget(self.dbl_custom_charge_limit)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_2)


        self.horizontalLayout_18.addLayout(self.horizontalLayout_16)


        self.verticalLayout_2.addLayout(self.horizontalLayout_18)

        self.chk_disable_charge_limit = QCheckBox(self.grp_account)
        self.chk_disable_charge_limit.setObjectName(u"chk_disable_charge_limit")
        self.chk_disable_charge_limit.setMinimumSize(QSize(180, 25))
        self.chk_disable_charge_limit.setMaximumSize(QSize(180, 25))

        self.verticalLayout_2.addWidget(self.chk_disable_charge_limit)


        self.verticalLayout_3.addWidget(self.grp_account)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout_22.addWidget(self.widget_3)

        self.dlg_menu = QWidget(self.widget_2)
        self.dlg_menu.setObjectName(u"dlg_menu")
        self.dlg_menu.setMinimumSize(QSize(150, 0))
        self.dlg_menu.setMaximumSize(QSize(150, 16777215))
        self.verticalLayout_6 = QVBoxLayout(self.dlg_menu)
        self.verticalLayout_6.setSpacing(20)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 10, 0, 10)
        self.pb_customer_save = QPushButton(self.dlg_menu)
        self.pb_customer_save.setObjectName(u"pb_customer_save")
        self.pb_customer_save.setMinimumSize(QSize(0, 35))
        self.pb_customer_save.setMaximumSize(QSize(16777215, 35))
        icon = QIcon()
        icon.addFile(u":/Icons/tick.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_customer_save.setIcon(icon)
        self.pb_customer_save.setIconSize(QSize(16, 16))

        self.verticalLayout_6.addWidget(self.pb_customer_save)

        self.pb_customer_cancel = QPushButton(self.dlg_menu)
        self.pb_customer_cancel.setObjectName(u"pb_customer_cancel")
        self.pb_customer_cancel.setMinimumSize(QSize(0, 35))
        self.pb_customer_cancel.setMaximumSize(QSize(16777215, 35))
        icon1 = QIcon()
        icon1.addFile(u":/Icons/cross.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_customer_cancel.setIcon(icon1)
        self.pb_customer_cancel.setIconSize(QSize(16, 16))

        self.verticalLayout_6.addWidget(self.pb_customer_cancel)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)

        self.wid_info = QWidget(self.dlg_menu)
        self.wid_info.setObjectName(u"wid_info")
        self.wid_info.setMinimumSize(QSize(0, 400))
        self.wid_info.setMaximumSize(QSize(16777215, 400))
        self.verticalLayout_5 = QVBoxLayout(self.wid_info)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.lb_information = QLabel(self.wid_info)
        self.lb_information.setObjectName(u"lb_information")

        self.verticalLayout_5.addWidget(self.lb_information)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.lb_created_label = QLabel(self.wid_info)
        self.lb_created_label.setObjectName(u"lb_created_label")
        self.lb_created_label.setMinimumSize(QSize(60, 0))
        self.lb_created_label.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_19.addWidget(self.lb_created_label)

        self.lb_created = QLabel(self.wid_info)
        self.lb_created.setObjectName(u"lb_created")

        self.horizontalLayout_19.addWidget(self.lb_created)


        self.verticalLayout_5.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.lb_updated_label = QLabel(self.wid_info)
        self.lb_updated_label.setObjectName(u"lb_updated_label")
        self.lb_updated_label.setMinimumSize(QSize(60, 0))
        self.lb_updated_label.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_20.addWidget(self.lb_updated_label)

        self.lb_updated = QLabel(self.wid_info)
        self.lb_updated.setObjectName(u"lb_updated")

        self.horizontalLayout_20.addWidget(self.lb_updated)


        self.verticalLayout_5.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.lb_customer_id_label = QLabel(self.wid_info)
        self.lb_customer_id_label.setObjectName(u"lb_customer_id_label")
        self.lb_customer_id_label.setMinimumSize(QSize(60, 0))
        self.lb_customer_id_label.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_24.addWidget(self.lb_customer_id_label)

        self.lb_customer_id = QLabel(self.wid_info)
        self.lb_customer_id.setObjectName(u"lb_customer_id")

        self.horizontalLayout_24.addWidget(self.lb_customer_id)


        self.verticalLayout_5.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.lb_charge_balance_label = QLabel(self.wid_info)
        self.lb_charge_balance_label.setObjectName(u"lb_charge_balance_label")
        self.lb_charge_balance_label.setMinimumSize(QSize(60, 0))
        self.lb_charge_balance_label.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_21.addWidget(self.lb_charge_balance_label)

        self.lb_charge_balance = QLabel(self.wid_info)
        self.lb_charge_balance.setObjectName(u"lb_charge_balance")

        self.horizontalLayout_21.addWidget(self.lb_charge_balance)


        self.verticalLayout_5.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.lb_store_credit_label = QLabel(self.wid_info)
        self.lb_store_credit_label.setObjectName(u"lb_store_credit_label")
        self.lb_store_credit_label.setMinimumSize(QSize(60, 0))
        self.lb_store_credit_label.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_23.addWidget(self.lb_store_credit_label)

        self.lb_store_credit = QLabel(self.wid_info)
        self.lb_store_credit.setObjectName(u"lb_store_credit")

        self.horizontalLayout_23.addWidget(self.lb_store_credit)


        self.verticalLayout_5.addLayout(self.horizontalLayout_23)


        self.verticalLayout_6.addWidget(self.wid_info)


        self.horizontalLayout_22.addWidget(self.dlg_menu)


        self.verticalLayout_4.addWidget(self.widget_2)


        self.retranslateUi(CreateCustomerDialog)

        QMetaObject.connectSlotsByName(CreateCustomerDialog)
    # setupUi

    def retranslateUi(self, CreateCustomerDialog):
        CreateCustomerDialog.setWindowTitle(QCoreApplication.translate("CreateCustomerDialog", u"New Customer Form", None))
        self.lb_dialog_title.setText(QCoreApplication.translate("CreateCustomerDialog", u"Create New Customer", None))
        self.grp_bill_to.setTitle(QCoreApplication.translate("CreateCustomerDialog", u"Bill To", None))
        self.lb_last_name.setText(QCoreApplication.translate("CreateCustomerDialog", u"Last Name:", None))
        self.lb_first_name.setText(QCoreApplication.translate("CreateCustomerDialog", u"First Name:", None))
        self.lb_company.setText(QCoreApplication.translate("CreateCustomerDialog", u"Company:", None))
        self.lb_street_1.setText(QCoreApplication.translate("CreateCustomerDialog", u"Street 1:", None))
        self.lb_street_2.setText(QCoreApplication.translate("CreateCustomerDialog", u"Street 2:", None))
        self.lb_city.setText(QCoreApplication.translate("CreateCustomerDialog", u"City:", None))
        self.lb_state.setText(QCoreApplication.translate("CreateCustomerDialog", u"State:", None))
        self.lb_country.setText(QCoreApplication.translate("CreateCustomerDialog", u"Country:", None))
        self.lb_zip_code.setText(QCoreApplication.translate("CreateCustomerDialog", u"Zip Code:", None))
        self.lb_phone.setText(QCoreApplication.translate("CreateCustomerDialog", u"Phone:", None))
        self.lb_email.setText(QCoreApplication.translate("CreateCustomerDialog", u"Email:", None))
        self.grp_account.setTitle(QCoreApplication.translate("CreateCustomerDialog", u"Account", None))
        self.chk_allow_account_charge.setText(QCoreApplication.translate("CreateCustomerDialog", u"Allow Charge to Account", None))
        self.lb_system_charge_limit_label.setText(QCoreApplication.translate("CreateCustomerDialog", u"Use System Charge Limit:", None))
        self.system_charge_limit_dollar_label.setText(QCoreApplication.translate("CreateCustomerDialog", u"$", None))
        self.lb_system_charge_limit.setText(QCoreApplication.translate("CreateCustomerDialog", u"0.00", None))
        self.lb_custom_charge_limit_label.setText(QCoreApplication.translate("CreateCustomerDialog", u"Custom Charge Limit:", None))
        self.custom_charge_limit_dollar_label.setText(QCoreApplication.translate("CreateCustomerDialog", u"$", None))
        self.chk_disable_charge_limit.setText(QCoreApplication.translate("CreateCustomerDialog", u"No Charge Limit", None))
        self.pb_customer_save.setText(QCoreApplication.translate("CreateCustomerDialog", u"Save", None))
        self.pb_customer_cancel.setText(QCoreApplication.translate("CreateCustomerDialog", u"Cancel", None))
        self.lb_information.setText(QCoreApplication.translate("CreateCustomerDialog", u"Information:", None))
        self.lb_created_label.setText(QCoreApplication.translate("CreateCustomerDialog", u"Created:", None))
        self.lb_created.setText(QCoreApplication.translate("CreateCustomerDialog", u"N/A", None))
        self.lb_updated_label.setText(QCoreApplication.translate("CreateCustomerDialog", u"Updated:", None))
        self.lb_updated.setText(QCoreApplication.translate("CreateCustomerDialog", u"N/A", None))
        self.lb_customer_id_label.setText(QCoreApplication.translate("CreateCustomerDialog", u"Cust. ID:", None))
        self.lb_customer_id.setText(QCoreApplication.translate("CreateCustomerDialog", u"N/A", None))
        self.lb_charge_balance_label.setText(QCoreApplication.translate("CreateCustomerDialog", u"Charge Bal:", None))
        self.lb_charge_balance.setText(QCoreApplication.translate("CreateCustomerDialog", u"N/A", None))
        self.lb_store_credit_label.setText(QCoreApplication.translate("CreateCustomerDialog", u"Store Credit:", None))
        self.lb_store_credit.setText(QCoreApplication.translate("CreateCustomerDialog", u"N/A", None))
    # retranslateUi

