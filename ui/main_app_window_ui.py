# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_app_window.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QSpacerItem,
    QStackedWidget, QToolButton, QVBoxLayout, QWidget)
import icons_rc

class Ui_MainAppWindow(object):
    def setupUi(self, MainAppWindow):
        if not MainAppWindow.objectName():
            MainAppWindow.setObjectName(u"MainAppWindow")
        MainAppWindow.resize(1032, 1000)
        MainAppWindow.setMinimumSize(QSize(0, 1000))
        font = QFont()
        font.setFamilies([u"Lexend"])
        font.setPointSize(12)
        MainAppWindow.setFont(font)
        MainAppWindow.setStyleSheet(u"")
        self.actionSample = QAction(MainAppWindow)
        self.actionSample.setObjectName(u"actionSample")
        self.act_user_manager = QAction(MainAppWindow)
        self.act_user_manager.setObjectName(u"act_user_manager")
        self.act_exit = QAction(MainAppWindow)
        self.act_exit.setObjectName(u"act_exit")
        self.centralwidget = QWidget(MainAppWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.wd_menu = QWidget(self.centralwidget)
        self.wd_menu.setObjectName(u"wd_menu")
        self.wd_menu.setMinimumSize(QSize(140, 0))
        self.wd_menu.setMaximumSize(QSize(140, 16777215))
        self.verticalLayout = QVBoxLayout(self.wd_menu)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lb_app_name = QLabel(self.wd_menu)
        self.lb_app_name.setObjectName(u"lb_app_name")
        self.lb_app_name.setMinimumSize(QSize(0, 45))
        self.lb_app_name.setMaximumSize(QSize(16777215, 45))
        font1 = QFont()
        font1.setFamilies([u"Lexend"])
        font1.setPointSize(24)
        font1.setBold(True)
        self.lb_app_name.setFont(font1)

        self.verticalLayout.addWidget(self.lb_app_name)

        self.widget_3 = QWidget(self.wd_menu)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_2 = QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tb_new_sale = QToolButton(self.widget_3)
        self.tb_new_sale.setObjectName(u"tb_new_sale")
        self.tb_new_sale.setMinimumSize(QSize(140, 80))
        icon = QIcon()
        icon.addFile(u":/Icons/shopping_basket.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tb_new_sale.setIcon(icon)
        self.tb_new_sale.setIconSize(QSize(30, 30))
        self.tb_new_sale.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.verticalLayout_2.addWidget(self.tb_new_sale)

        self.tb_inventory = QToolButton(self.widget_3)
        self.tb_inventory.setObjectName(u"tb_inventory")
        self.tb_inventory.setMinimumSize(QSize(140, 80))
        icon1 = QIcon()
        icon1.addFile(u":/Icons/inventory.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tb_inventory.setIcon(icon1)
        self.tb_inventory.setIconSize(QSize(30, 30))
        self.tb_inventory.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.verticalLayout_2.addWidget(self.tb_inventory)

        self.tb_customers = QToolButton(self.widget_3)
        self.tb_customers.setObjectName(u"tb_customers")
        self.tb_customers.setMinimumSize(QSize(140, 80))
        icon2 = QIcon()
        icon2.addFile(u":/Icons/customers.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tb_customers.setIcon(icon2)
        self.tb_customers.setIconSize(QSize(30, 30))
        self.tb_customers.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.verticalLayout_2.addWidget(self.tb_customers)

        self.tb_sales_manager = QToolButton(self.widget_3)
        self.tb_sales_manager.setObjectName(u"tb_sales_manager")
        self.tb_sales_manager.setMinimumSize(QSize(140, 80))
        icon3 = QIcon()
        icon3.addFile(u":/Icons/price_tag.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tb_sales_manager.setIcon(icon3)
        self.tb_sales_manager.setIconSize(QSize(30, 30))
        self.tb_sales_manager.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.verticalLayout_2.addWidget(self.tb_sales_manager)

        self.tb_vendors = QToolButton(self.widget_3)
        self.tb_vendors.setObjectName(u"tb_vendors")
        self.tb_vendors.setMinimumSize(QSize(140, 80))
        icon4 = QIcon()
        icon4.addFile(u":/Icons/vendor.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tb_vendors.setIcon(icon4)
        self.tb_vendors.setIconSize(QSize(30, 30))
        self.tb_vendors.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.verticalLayout_2.addWidget(self.tb_vendors)

        self.tb_cash_count = QToolButton(self.widget_3)
        self.tb_cash_count.setObjectName(u"tb_cash_count")
        self.tb_cash_count.setMinimumSize(QSize(140, 80))
        icon5 = QIcon()
        icon5.addFile(u":/Icons/performance.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tb_cash_count.setIcon(icon5)
        self.tb_cash_count.setIconSize(QSize(30, 30))
        self.tb_cash_count.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.verticalLayout_2.addWidget(self.tb_cash_count)

        self.tb_settings = QToolButton(self.widget_3)
        self.tb_settings.setObjectName(u"tb_settings")
        self.tb_settings.setMinimumSize(QSize(140, 80))
        icon6 = QIcon()
        icon6.addFile(u":/Icons/settings.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tb_settings.setIcon(icon6)
        self.tb_settings.setIconSize(QSize(30, 30))
        self.tb_settings.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.verticalLayout_2.addWidget(self.tb_settings)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.tb_exit = QToolButton(self.widget_3)
        self.tb_exit.setObjectName(u"tb_exit")
        self.tb_exit.setMinimumSize(QSize(140, 80))
        icon7 = QIcon()
        icon7.addFile(u":/Icons/power.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tb_exit.setIcon(icon7)
        self.tb_exit.setIconSize(QSize(30, 30))
        self.tb_exit.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.verticalLayout_2.addWidget(self.tb_exit)


        self.verticalLayout.addWidget(self.widget_3)


        self.horizontalLayout.addWidget(self.wd_menu)

        self.wd_stacked = QStackedWidget(self.centralwidget)
        self.wd_stacked.setObjectName(u"wd_stacked")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.wd_stacked.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.wd_stacked.addWidget(self.page_2)

        self.horizontalLayout.addWidget(self.wd_stacked)

        MainAppWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainAppWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1032, 25))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainAppWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.act_user_manager)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.act_exit)

        self.retranslateUi(MainAppWindow)

        QMetaObject.connectSlotsByName(MainAppWindow)
    # setupUi

    def retranslateUi(self, MainAppWindow):
        MainAppWindow.setWindowTitle(QCoreApplication.translate("MainAppWindow", u"Eixn Point of Sale", None))
        self.actionSample.setText(QCoreApplication.translate("MainAppWindow", u"Sample", None))
        self.act_user_manager.setText(QCoreApplication.translate("MainAppWindow", u"User Manager", None))
        self.act_exit.setText(QCoreApplication.translate("MainAppWindow", u"Exit", None))
        self.lb_app_name.setText(QCoreApplication.translate("MainAppWindow", u"EixnPOS", None))
        self.tb_new_sale.setText(QCoreApplication.translate("MainAppWindow", u"New Sale", None))
        self.tb_inventory.setText(QCoreApplication.translate("MainAppWindow", u"Inventory", None))
        self.tb_customers.setText(QCoreApplication.translate("MainAppWindow", u"Customers", None))
        self.tb_sales_manager.setText(QCoreApplication.translate("MainAppWindow", u"Sales Manager", None))
        self.tb_vendors.setText(QCoreApplication.translate("MainAppWindow", u"Vendors", None))
        self.tb_cash_count.setText(QCoreApplication.translate("MainAppWindow", u"Cash Count", None))
        self.tb_settings.setText(QCoreApplication.translate("MainAppWindow", u"Settings", None))
        self.tb_exit.setText(QCoreApplication.translate("MainAppWindow", u"Exit", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainAppWindow", u"File", None))
    # retranslateUi

