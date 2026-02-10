# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inventory_manager.ui'
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

class Ui_InventoryManager(object):
    def setupUi(self, InventoryManager):
        if not InventoryManager.objectName():
            InventoryManager.setObjectName(u"InventoryManager")
        InventoryManager.resize(940, 940)
        InventoryManager.setMinimumSize(QSize(940, 940))
        InventoryManager.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(InventoryManager)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(InventoryManager)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 35))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lb_window_title = QLabel(self.widget)
        self.lb_window_title.setObjectName(u"lb_window_title")
        self.lb_window_title.setMinimumSize(QSize(0, 35))
        self.lb_window_title.setMaximumSize(QSize(16777215, 35))
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

        self.widget_2 = QWidget(InventoryManager)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.main_content = QWidget(self.widget_2)
        self.main_content.setObjectName(u"main_content")
        self.verticalLayout = QVBoxLayout(self.main_content)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tbl_products = QTableView(self.main_content)
        self.tbl_products.setObjectName(u"tbl_products")

        self.verticalLayout.addWidget(self.tbl_products)

        self.tab_product_details = QTabWidget(self.main_content)
        self.tab_product_details.setObjectName(u"tab_product_details")
        self.tab_product_details.setMinimumSize(QSize(0, 300))
        self.tab_product_details.setMaximumSize(QSize(16777215, 400))
        self.tab_stock = QWidget()
        self.tab_stock.setObjectName(u"tab_stock")
        self.gridLayout = QGridLayout(self.tab_stock)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.tbl_product_stock = QTableView(self.tab_stock)
        self.tbl_product_stock.setObjectName(u"tbl_product_stock")

        self.gridLayout.addWidget(self.tbl_product_stock, 0, 0, 1, 1)

        self.tab_product_details.addTab(self.tab_stock, "")
        self.tab_sales = QWidget()
        self.tab_sales.setObjectName(u"tab_sales")
        self.gridLayout_3 = QGridLayout(self.tab_sales)
        self.gridLayout_3.setSpacing(5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(5, 5, 5, 5)
        self.tbl_product_sales = QTableView(self.tab_sales)
        self.tbl_product_sales.setObjectName(u"tbl_product_sales")

        self.gridLayout_3.addWidget(self.tbl_product_sales, 0, 0, 1, 1)

        self.tab_product_details.addTab(self.tab_sales, "")
        self.tab_receiving = QWidget()
        self.tab_receiving.setObjectName(u"tab_receiving")
        self.gridLayout_2 = QGridLayout(self.tab_receiving)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.tbl_product_receiving = QTableView(self.tab_receiving)
        self.tbl_product_receiving.setObjectName(u"tbl_product_receiving")

        self.gridLayout_2.addWidget(self.tbl_product_receiving, 0, 0, 1, 1)

        self.tab_product_details.addTab(self.tab_receiving, "")

        self.verticalLayout.addWidget(self.tab_product_details)


        self.horizontalLayout_2.addWidget(self.main_content)

        self.side_menu = QWidget(self.widget_2)
        self.side_menu.setObjectName(u"side_menu")
        self.side_menu.setMinimumSize(QSize(300, 0))
        self.side_menu.setMaximumSize(QSize(300, 16777215))
        self.side_menu.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.verticalLayout_2 = QVBoxLayout(self.side_menu)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pb_add = QPushButton(self.side_menu)
        self.pb_add.setObjectName(u"pb_add")
        self.pb_add.setMinimumSize(QSize(0, 35))
        self.pb_add.setMaximumSize(QSize(16777215, 35))
        icon1 = QIcon()
        icon1.addFile(u":/Icons/add.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_add.setIcon(icon1)
        self.pb_add.setIconSize(QSize(25, 25))

        self.verticalLayout_2.addWidget(self.pb_add)

        self.pb_modify = QPushButton(self.side_menu)
        self.pb_modify.setObjectName(u"pb_modify")
        self.pb_modify.setMinimumSize(QSize(0, 35))
        self.pb_modify.setMaximumSize(QSize(16777215, 35))
        icon2 = QIcon()
        icon2.addFile(u":/Icons/edit.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_modify.setIcon(icon2)
        self.pb_modify.setIconSize(QSize(25, 25))

        self.verticalLayout_2.addWidget(self.pb_modify)

        self.pb_find = QPushButton(self.side_menu)
        self.pb_find.setObjectName(u"pb_find")
        self.pb_find.setMinimumSize(QSize(0, 35))
        self.pb_find.setMaximumSize(QSize(16777215, 35))
        icon3 = QIcon()
        icon3.addFile(u":/Icons/search.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_find.setIcon(icon3)
        self.pb_find.setIconSize(QSize(25, 25))

        self.verticalLayout_2.addWidget(self.pb_find)

        self.pb_filter = QPushButton(self.side_menu)
        self.pb_filter.setObjectName(u"pb_filter")
        self.pb_filter.setMinimumSize(QSize(0, 35))
        self.pb_filter.setMaximumSize(QSize(16777215, 35))
        icon4 = QIcon()
        icon4.addFile(u":/Icons/filter.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_filter.setIcon(icon4)
        self.pb_filter.setIconSize(QSize(25, 25))

        self.verticalLayout_2.addWidget(self.pb_filter)

        self.pb_receive = QPushButton(self.side_menu)
        self.pb_receive.setObjectName(u"pb_receive")
        self.pb_receive.setMinimumSize(QSize(0, 35))
        self.pb_receive.setMaximumSize(QSize(16777215, 35))
        icon5 = QIcon()
        icon5.addFile(u":/Icons/receive.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_receive.setIcon(icon5)
        self.pb_receive.setIconSize(QSize(25, 25))

        self.verticalLayout_2.addWidget(self.pb_receive)

        self.pb_use_in_sale = QPushButton(self.side_menu)
        self.pb_use_in_sale.setObjectName(u"pb_use_in_sale")
        self.pb_use_in_sale.setMinimumSize(QSize(0, 35))
        self.pb_use_in_sale.setMaximumSize(QSize(16777215, 35))
        icon6 = QIcon()
        icon6.addFile(u":/Icons/shopping_cart.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_use_in_sale.setIcon(icon6)
        self.pb_use_in_sale.setIconSize(QSize(25, 25))

        self.verticalLayout_2.addWidget(self.pb_use_in_sale)

        self.pb_delete = QPushButton(self.side_menu)
        self.pb_delete.setObjectName(u"pb_delete")
        self.pb_delete.setMinimumSize(QSize(0, 35))
        self.pb_delete.setMaximumSize(QSize(16777215, 35))
        icon7 = QIcon()
        icon7.addFile(u":/Icons/trash.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_delete.setIcon(icon7)
        self.pb_delete.setIconSize(QSize(25, 25))

        self.verticalLayout_2.addWidget(self.pb_delete)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addWidget(self.side_menu)


        self.verticalLayout_3.addWidget(self.widget_2)


        self.retranslateUi(InventoryManager)

        self.tab_product_details.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(InventoryManager)
    # setupUi

    def retranslateUi(self, InventoryManager):
        InventoryManager.setWindowTitle(QCoreApplication.translate("InventoryManager", u"Inventory Manager", None))
        self.lb_window_title.setText(QCoreApplication.translate("InventoryManager", u"Inventory Manager", None))
        self.pb_window_close.setText(QCoreApplication.translate("InventoryManager", u"Close", None))
        self.tab_product_details.setTabText(self.tab_product_details.indexOf(self.tab_stock), QCoreApplication.translate("InventoryManager", u"Stock", None))
        self.tab_product_details.setTabText(self.tab_product_details.indexOf(self.tab_sales), QCoreApplication.translate("InventoryManager", u"Sales", None))
        self.tab_product_details.setTabText(self.tab_product_details.indexOf(self.tab_receiving), QCoreApplication.translate("InventoryManager", u"Receiving", None))
        self.pb_add.setText(QCoreApplication.translate("InventoryManager", u"Add", None))
        self.pb_modify.setText(QCoreApplication.translate("InventoryManager", u"Modify", None))
        self.pb_find.setText(QCoreApplication.translate("InventoryManager", u"Find", None))
        self.pb_filter.setText(QCoreApplication.translate("InventoryManager", u"Filter", None))
        self.pb_receive.setText(QCoreApplication.translate("InventoryManager", u"Receive", None))
        self.pb_use_in_sale.setText(QCoreApplication.translate("InventoryManager", u"Use in New Sale", None))
        self.pb_delete.setText(QCoreApplication.translate("InventoryManager", u"Delete", None))
    # retranslateUi

