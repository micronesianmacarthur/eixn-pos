# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'receiving_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTableView, QVBoxLayout, QWidget)
import icons_rc

class Ui_ReceivingDialog(object):
    def setupUi(self, ReceivingDialog):
        if not ReceivingDialog.objectName():
            ReceivingDialog.setObjectName(u"ReceivingDialog")
        ReceivingDialog.setWindowModality(Qt.WindowModality.ApplicationModal)
        ReceivingDialog.resize(850, 690)
        ReceivingDialog.setMinimumSize(QSize(850, 690))
        ReceivingDialog.setMaximumSize(QSize(850, 690))
        ReceivingDialog.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(ReceivingDialog)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(ReceivingDialog)
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

        self.widget_2 = QWidget(ReceivingDialog)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_22 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_22.setSpacing(5)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.dlg_main = QWidget(self.widget_2)
        self.dlg_main.setObjectName(u"dlg_main")
        self.verticalLayout = QVBoxLayout(self.dlg_main)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 10, 5, 10)
        self.tbl_receiving_list = QTableView(self.dlg_main)
        self.tbl_receiving_list.setObjectName(u"tbl_receiving_list")

        self.verticalLayout.addWidget(self.tbl_receiving_list)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lb_item_count_label = QLabel(self.dlg_main)
        self.lb_item_count_label.setObjectName(u"lb_item_count_label")
        self.lb_item_count_label.setMinimumSize(QSize(0, 25))
        self.lb_item_count_label.setMaximumSize(QSize(100, 25))

        self.horizontalLayout.addWidget(self.lb_item_count_label)

        self.lb_item_count = QLabel(self.dlg_main)
        self.lb_item_count.setObjectName(u"lb_item_count")
        self.lb_item_count.setMinimumSize(QSize(35, 25))
        self.lb_item_count.setMaximumSize(QSize(35, 25))
        self.lb_item_count.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.lb_item_count)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_22.addWidget(self.dlg_main)

        self.dlg_menu = QWidget(self.widget_2)
        self.dlg_menu.setObjectName(u"dlg_menu")
        self.dlg_menu.setMinimumSize(QSize(150, 0))
        self.dlg_menu.setMaximumSize(QSize(150, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.dlg_menu)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 10, 0, 10)
        self.pb_new_item = QPushButton(self.dlg_menu)
        self.pb_new_item.setObjectName(u"pb_new_item")
        self.pb_new_item.setMinimumSize(QSize(0, 35))
        self.pb_new_item.setMaximumSize(QSize(16777215, 35))
        icon = QIcon()
        icon.addFile(u":/Icons/plus.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_new_item.setIcon(icon)

        self.verticalLayout_2.addWidget(self.pb_new_item)

        self.pb_modify_item = QPushButton(self.dlg_menu)
        self.pb_modify_item.setObjectName(u"pb_modify_item")
        self.pb_modify_item.setMinimumSize(QSize(0, 35))
        self.pb_modify_item.setMaximumSize(QSize(16777215, 35))
        icon1 = QIcon()
        icon1.addFile(u":/Icons/edit.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_modify_item.setIcon(icon1)

        self.verticalLayout_2.addWidget(self.pb_modify_item)

        self.pb_find_item = QPushButton(self.dlg_menu)
        self.pb_find_item.setObjectName(u"pb_find_item")
        self.pb_find_item.setMinimumSize(QSize(0, 35))
        self.pb_find_item.setMaximumSize(QSize(16777215, 35))
        icon2 = QIcon()
        icon2.addFile(u":/Icons/search.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_find_item.setIcon(icon2)

        self.verticalLayout_2.addWidget(self.pb_find_item)

        self.pb_deleteitem = QPushButton(self.dlg_menu)
        self.pb_deleteitem.setObjectName(u"pb_deleteitem")
        self.pb_deleteitem.setMinimumSize(QSize(0, 35))
        self.pb_deleteitem.setMaximumSize(QSize(16777215, 35))
        icon3 = QIcon()
        icon3.addFile(u":/Icons/trash.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_deleteitem.setIcon(icon3)

        self.verticalLayout_2.addWidget(self.pb_deleteitem)

        self.pb_submit_all = QPushButton(self.dlg_menu)
        self.pb_submit_all.setObjectName(u"pb_submit_all")
        self.pb_submit_all.setMinimumSize(QSize(0, 35))
        self.pb_submit_all.setMaximumSize(QSize(16777215, 35))
        icon4 = QIcon()
        icon4.addFile(u":/Icons/tick.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_submit_all.setIcon(icon4)

        self.verticalLayout_2.addWidget(self.pb_submit_all)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.pb_close = QPushButton(self.dlg_menu)
        self.pb_close.setObjectName(u"pb_close")
        self.pb_close.setMinimumSize(QSize(0, 35))
        self.pb_close.setMaximumSize(QSize(16777215, 35))
        icon5 = QIcon()
        icon5.addFile(u":/Icons/cross.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_close.setIcon(icon5)

        self.verticalLayout_2.addWidget(self.pb_close)


        self.horizontalLayout_22.addWidget(self.dlg_menu)


        self.verticalLayout_4.addWidget(self.widget_2)


        self.retranslateUi(ReceivingDialog)

        QMetaObject.connectSlotsByName(ReceivingDialog)
    # setupUi

    def retranslateUi(self, ReceivingDialog):
        ReceivingDialog.setWindowTitle(QCoreApplication.translate("ReceivingDialog", u"Receiving Items", None))
        self.lb_dialog_title.setText(QCoreApplication.translate("ReceivingDialog", u"Receiving Items List", None))
        self.lb_item_count_label.setText(QCoreApplication.translate("ReceivingDialog", u"List Item Count:", None))
        self.lb_item_count.setText(QCoreApplication.translate("ReceivingDialog", u"0", None))
        self.pb_new_item.setText(QCoreApplication.translate("ReceivingDialog", u"New Item", None))
        self.pb_modify_item.setText(QCoreApplication.translate("ReceivingDialog", u"Modify Item", None))
        self.pb_find_item.setText(QCoreApplication.translate("ReceivingDialog", u"Find Item", None))
        self.pb_deleteitem.setText(QCoreApplication.translate("ReceivingDialog", u"Delete Item", None))
        self.pb_submit_all.setText(QCoreApplication.translate("ReceivingDialog", u"Submit All", None))
        self.pb_close.setText(QCoreApplication.translate("ReceivingDialog", u"Close", None))
    # retranslateUi

