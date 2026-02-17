# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stock_types_dialog.ui'
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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTableView, QVBoxLayout, QWidget)
import icons_rc

class Ui_StockTypesDialog(object):
    def setupUi(self, StockTypesDialog):
        if not StockTypesDialog.objectName():
            StockTypesDialog.setObjectName(u"StockTypesDialog")
        StockTypesDialog.setWindowModality(Qt.WindowModality.ApplicationModal)
        StockTypesDialog.resize(640, 480)
        StockTypesDialog.setMinimumSize(QSize(640, 480))
        StockTypesDialog.setMaximumSize(QSize(640, 480))
        StockTypesDialog.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(StockTypesDialog)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(StockTypesDialog)
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

        self.widget_2 = QWidget(StockTypesDialog)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_22 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_22.setSpacing(5)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_2 = QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 0, 5, 0)
        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(0, 80))
        self.widget_4.setMaximumSize(QSize(16777215, 80))
        self.verticalLayout = QVBoxLayout(self.widget_4)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lb_section_header = QLabel(self.widget_4)
        self.lb_section_header.setObjectName(u"lb_section_header")
        self.lb_section_header.setMinimumSize(QSize(0, 25))
        self.lb_section_header.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout.addWidget(self.lb_section_header)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lb_stock_type_name = QLabel(self.widget_4)
        self.lb_stock_type_name.setObjectName(u"lb_stock_type_name")
        self.lb_stock_type_name.setMinimumSize(QSize(0, 25))
        self.lb_stock_type_name.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout.addWidget(self.lb_stock_type_name)

        self.le_stock_type_name = QLineEdit(self.widget_4)
        self.le_stock_type_name.setObjectName(u"le_stock_type_name")
        self.le_stock_type_name.setMinimumSize(QSize(0, 25))
        self.le_stock_type_name.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout.addWidget(self.le_stock_type_name)

        self.pb_stock_type_save = QPushButton(self.widget_4)
        self.pb_stock_type_save.setObjectName(u"pb_stock_type_save")
        self.pb_stock_type_save.setMinimumSize(QSize(100, 25))
        self.pb_stock_type_save.setMaximumSize(QSize(100, 25))
        icon = QIcon()
        icon.addFile(u":/Icons/tick-small.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_stock_type_save.setIcon(icon)
        self.pb_stock_type_save.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.pb_stock_type_save)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.widget_4)

        self.tbl_stock_types = QTableView(self.widget_3)
        self.tbl_stock_types.setObjectName(u"tbl_stock_types")

        self.verticalLayout_2.addWidget(self.tbl_stock_types)


        self.horizontalLayout_22.addWidget(self.widget_3)

        self.dlg_menu = QWidget(self.widget_2)
        self.dlg_menu.setObjectName(u"dlg_menu")
        self.dlg_menu.setMinimumSize(QSize(150, 0))
        self.dlg_menu.setMaximumSize(QSize(150, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.dlg_menu)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 10)
        self.pb_stock_type_modify = QPushButton(self.dlg_menu)
        self.pb_stock_type_modify.setObjectName(u"pb_stock_type_modify")
        self.pb_stock_type_modify.setMinimumSize(QSize(0, 35))
        self.pb_stock_type_modify.setMaximumSize(QSize(16777215, 35))
        icon1 = QIcon()
        icon1.addFile(u":/Icons/edit.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_stock_type_modify.setIcon(icon1)
        self.pb_stock_type_modify.setIconSize(QSize(16, 16))

        self.verticalLayout_3.addWidget(self.pb_stock_type_modify)

        self.pb_stock_type_delete = QPushButton(self.dlg_menu)
        self.pb_stock_type_delete.setObjectName(u"pb_stock_type_delete")
        self.pb_stock_type_delete.setMinimumSize(QSize(0, 35))
        self.pb_stock_type_delete.setMaximumSize(QSize(16777215, 35))
        icon2 = QIcon()
        icon2.addFile(u":/Icons/trash.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_stock_type_delete.setIcon(icon2)
        self.pb_stock_type_delete.setIconSize(QSize(16, 16))

        self.verticalLayout_3.addWidget(self.pb_stock_type_delete)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.pb_stock_type_cancel = QPushButton(self.dlg_menu)
        self.pb_stock_type_cancel.setObjectName(u"pb_stock_type_cancel")
        self.pb_stock_type_cancel.setMinimumSize(QSize(0, 35))
        self.pb_stock_type_cancel.setMaximumSize(QSize(16777215, 35))
        icon3 = QIcon()
        icon3.addFile(u":/Icons/cross.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_stock_type_cancel.setIcon(icon3)
        self.pb_stock_type_cancel.setIconSize(QSize(16, 16))

        self.verticalLayout_3.addWidget(self.pb_stock_type_cancel)


        self.horizontalLayout_22.addWidget(self.dlg_menu)


        self.verticalLayout_4.addWidget(self.widget_2)


        self.retranslateUi(StockTypesDialog)

        QMetaObject.connectSlotsByName(StockTypesDialog)
    # setupUi

    def retranslateUi(self, StockTypesDialog):
        StockTypesDialog.setWindowTitle(QCoreApplication.translate("StockTypesDialog", u"Stock Types", None))
        self.lb_dialog_title.setText(QCoreApplication.translate("StockTypesDialog", u"Stock Types", None))
        self.lb_section_header.setText(QCoreApplication.translate("StockTypesDialog", u"Create New Stock Type", None))
        self.lb_stock_type_name.setText(QCoreApplication.translate("StockTypesDialog", u"Stock Type Name:", None))
        self.pb_stock_type_save.setText(QCoreApplication.translate("StockTypesDialog", u"Save", None))
        self.pb_stock_type_modify.setText(QCoreApplication.translate("StockTypesDialog", u"Modify", None))
        self.pb_stock_type_delete.setText(QCoreApplication.translate("StockTypesDialog", u"Delete", None))
        self.pb_stock_type_cancel.setText(QCoreApplication.translate("StockTypesDialog", u"Cancel", None))
    # retranslateUi

