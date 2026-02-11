# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customer_manager.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QTableView, QVBoxLayout, QWidget)
import icons_rc

class Ui_CustomerManager(object):
    def setupUi(self, CustomerManager):
        if not CustomerManager.objectName():
            CustomerManager.setObjectName(u"CustomerManager")
        CustomerManager.resize(940, 940)
        CustomerManager.setMinimumSize(QSize(940, 940))
        CustomerManager.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(CustomerManager)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(CustomerManager)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lb_window_title = QLabel(self.widget)
        self.lb_window_title.setObjectName(u"lb_window_title")
        self.lb_window_title.setMinimumSize(QSize(0, 35))
        self.lb_window_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.lb_window_title)

        self.pb_window_close = QPushButton(self.widget)
        self.pb_window_close.setObjectName(u"pb_window_close")
        self.pb_window_close.setMinimumSize(QSize(120, 35))
        self.pb_window_close.setMaximumSize(QSize(120, 35))
        icon = QIcon()
        icon.addFile(u":/Icons/close_white.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_window_close.setIcon(icon)
        self.pb_window_close.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.pb_window_close)


        self.verticalLayout_3.addWidget(self.widget)

        self.widget_2 = QWidget(CustomerManager)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout = QVBoxLayout(self.widget_3)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tbl_customers = QTableView(self.widget_3)
        self.tbl_customers.setObjectName(u"tbl_customers")

        self.verticalLayout.addWidget(self.tbl_customers)

        self.tab_details = QTabWidget(self.widget_3)
        self.tab_details.setObjectName(u"tab_details")
        self.tab_details.setMinimumSize(QSize(0, 300))
        self.tab_sales = QWidget()
        self.tab_sales.setObjectName(u"tab_sales")
        self.gridLayout_3 = QGridLayout(self.tab_sales)
        self.gridLayout_3.setSpacing(5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(5, 5, 5, 5)
        self.tbl_customer_sales = QTableView(self.tab_sales)
        self.tbl_customer_sales.setObjectName(u"tbl_customer_sales")

        self.gridLayout_3.addWidget(self.tbl_customer_sales, 0, 0, 1, 1)

        self.tab_details.addTab(self.tab_sales, "")
        self.tab_items = QWidget()
        self.tab_items.setObjectName(u"tab_items")
        self.gridLayout_2 = QGridLayout(self.tab_items)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.tbl_customer_items = QTableView(self.tab_items)
        self.tbl_customer_items.setObjectName(u"tbl_customer_items")

        self.gridLayout_2.addWidget(self.tbl_customer_items, 0, 0, 1, 1)

        self.tab_details.addTab(self.tab_items, "")
        self.tab_charges = QWidget()
        self.tab_charges.setObjectName(u"tab_charges")
        self.gridLayout = QGridLayout(self.tab_charges)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.tbl_customer_charges = QTableView(self.tab_charges)
        self.tbl_customer_charges.setObjectName(u"tbl_customer_charges")

        self.gridLayout.addWidget(self.tbl_customer_charges, 0, 0, 1, 1)

        self.tab_details.addTab(self.tab_charges, "")

        self.verticalLayout.addWidget(self.tab_details)


        self.horizontalLayout_2.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(300, 0))
        self.widget_4.setMaximumSize(QSize(300, 16777215))
        self.widget_4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.verticalLayout_2 = QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pb_add = QPushButton(self.widget_4)
        self.pb_add.setObjectName(u"pb_add")
        self.pb_add.setMinimumSize(QSize(165, 35))
        self.pb_add.setMaximumSize(QSize(16777215, 35))
        self.pb_add.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pb_add.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.pb_add.setAutoFillBackground(False)
        icon1 = QIcon()
        icon1.addFile(u":/Icons/add.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_add.setIcon(icon1)
        self.pb_add.setIconSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.pb_add)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pb_modify = QPushButton(self.widget_4)
        self.pb_modify.setObjectName(u"pb_modify")
        self.pb_modify.setMinimumSize(QSize(165, 35))
        self.pb_modify.setMaximumSize(QSize(16777215, 35))
        self.pb_modify.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pb_modify.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.pb_modify.setAutoFillBackground(False)
        icon2 = QIcon()
        icon2.addFile(u":/Icons/edit.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_modify.setIcon(icon2)
        self.pb_modify.setIconSize(QSize(25, 25))

        self.horizontalLayout_4.addWidget(self.pb_modify)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pb_find = QPushButton(self.widget_4)
        self.pb_find.setObjectName(u"pb_find")
        self.pb_find.setMinimumSize(QSize(165, 35))
        self.pb_find.setMaximumSize(QSize(16777215, 35))
        self.pb_find.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pb_find.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.pb_find.setAutoFillBackground(False)
        icon3 = QIcon()
        icon3.addFile(u":/Icons/search.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_find.setIcon(icon3)
        self.pb_find.setIconSize(QSize(25, 25))

        self.horizontalLayout_5.addWidget(self.pb_find)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pb_filter = QPushButton(self.widget_4)
        self.pb_filter.setObjectName(u"pb_filter")
        self.pb_filter.setMinimumSize(QSize(165, 35))
        self.pb_filter.setMaximumSize(QSize(16777215, 35))
        self.pb_filter.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pb_filter.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.pb_filter.setAutoFillBackground(False)
        icon4 = QIcon()
        icon4.addFile(u":/Icons/filter.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_filter.setIcon(icon4)
        self.pb_filter.setIconSize(QSize(25, 25))

        self.horizontalLayout_6.addWidget(self.pb_filter)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pb_new_sale = QPushButton(self.widget_4)
        self.pb_new_sale.setObjectName(u"pb_new_sale")
        self.pb_new_sale.setMinimumSize(QSize(165, 35))
        self.pb_new_sale.setMaximumSize(QSize(16777215, 35))
        self.pb_new_sale.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pb_new_sale.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.pb_new_sale.setAutoFillBackground(False)
        icon5 = QIcon()
        icon5.addFile(u":/Icons/shopping_cart.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_new_sale.setIcon(icon5)
        self.pb_new_sale.setIconSize(QSize(25, 25))

        self.horizontalLayout_7.addWidget(self.pb_new_sale)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.pb_delete = QPushButton(self.widget_4)
        self.pb_delete.setObjectName(u"pb_delete")
        self.pb_delete.setMinimumSize(QSize(165, 35))
        self.pb_delete.setMaximumSize(QSize(16777215, 35))
        self.pb_delete.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pb_delete.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.pb_delete.setAutoFillBackground(False)
        icon6 = QIcon()
        icon6.addFile(u":/Icons/trash.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_delete.setIcon(icon6)
        self.pb_delete.setIconSize(QSize(25, 25))

        self.horizontalLayout_8.addWidget(self.pb_delete)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addWidget(self.widget_4)


        self.verticalLayout_3.addWidget(self.widget_2)


        self.retranslateUi(CustomerManager)

        self.tab_details.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(CustomerManager)
    # setupUi

    def retranslateUi(self, CustomerManager):
        CustomerManager.setWindowTitle(QCoreApplication.translate("CustomerManager", u"Customer Manager", None))
        self.lb_window_title.setText(QCoreApplication.translate("CustomerManager", u"Customer Manager", None))
        self.pb_window_close.setText(QCoreApplication.translate("CustomerManager", u"Close", None))
        self.tab_details.setTabText(self.tab_details.indexOf(self.tab_sales), QCoreApplication.translate("CustomerManager", u"Sales", None))
        self.tab_details.setTabText(self.tab_details.indexOf(self.tab_items), QCoreApplication.translate("CustomerManager", u"Items", None))
        self.tab_details.setTabText(self.tab_details.indexOf(self.tab_charges), QCoreApplication.translate("CustomerManager", u"Charges", None))
        self.pb_add.setText(QCoreApplication.translate("CustomerManager", u"Add", None))
        self.pb_modify.setText(QCoreApplication.translate("CustomerManager", u"Modify", None))
        self.pb_find.setText(QCoreApplication.translate("CustomerManager", u"Find", None))
        self.pb_filter.setText(QCoreApplication.translate("CustomerManager", u"Filter", None))
        self.pb_new_sale.setText(QCoreApplication.translate("CustomerManager", u"Use in New Sale", None))
        self.pb_delete.setText(QCoreApplication.translate("CustomerManager", u"Delete", None))
    # retranslateUi

