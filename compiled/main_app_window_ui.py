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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QSizePolicy,
    QSpacerItem, QStackedWidget, QToolButton, QVBoxLayout,
    QWidget)
import icons_rc

class Ui_MainAppWindow(object):
    def setupUi(self, MainAppWindow):
        if not MainAppWindow.objectName():
            MainAppWindow.setObjectName(u"MainAppWindow")
        MainAppWindow.resize(720, 1020)
        MainAppWindow.setMinimumSize(QSize(0, 1020))
        font = QFont()
        font.setFamilies([u"Lexend"])
        font.setPointSize(10)
        MainAppWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/Icons/register.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainAppWindow.setWindowIcon(icon)
        MainAppWindow.setStyleSheet(u"#centralwidget {\n"
"	background-color: #1a1a1a;\n"
"}\n"
"#wd_menu {}\n"
"#wd_content {}\n"
"#container {}\n"
"QToolButton {\n"
"	background-color: #3f3f3f;\n"
"	color: #fff;\n"
"	border-radius: 0;\n"
"}\n"
"QToolButton:hover {\n"
"	background-color: #cfcfcf;\n"
"	color: #1b1b1b;\n"
"}\n"
"#wd_stacked {\n"
"	background-color: #1a1a1a;\n"
"}")
        MainAppWindow.setIconSize(QSize(25, 25))
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
        self.wd_menu.setMinimumSize(QSize(140, 980))
        self.wd_menu.setMaximumSize(QSize(140, 16777215))
        self.verticalLayout = QVBoxLayout(self.wd_menu)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 5, 0, 0)
        self.label = QLabel(self.wd_menu)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(140, 40))
        self.label.setMaximumSize(QSize(140, 40))
        font1 = QFont()
        font1.setFamilies([u"Lexend"])
        font1.setPointSize(24)
        font1.setBold(True)
        self.label.setFont(font1)

        self.verticalLayout.addWidget(self.label)

        self.wd_menu_button = QWidget(self.wd_menu)
        self.wd_menu_button.setObjectName(u"wd_menu_button")
        self.verticalLayout_2 = QVBoxLayout(self.wd_menu_button)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tb_new_sale = QToolButton(self.wd_menu_button)
        self.tb_new_sale.setObjectName(u"tb_new_sale")
        self.tb_new_sale.setMinimumSize(QSize(140, 90))
        self.tb_new_sale.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u":/Icons/shopping_basket.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tb_new_sale.setIcon(icon1)
        self.tb_new_sale.setIconSize(QSize(35, 35))
        self.tb_new_sale.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.verticalLayout_2.addWidget(self.tb_new_sale)

        self.tb_inventory = QToolButton(self.wd_menu_button)
        self.tb_inventory.setObjectName(u"tb_inventory")
        self.tb_inventory.setMinimumSize(QSize(140, 90))
        self.tb_inventory.setFont(font)
        icon2 = QIcon()
        icon2.addFile(u":/Icons/inventory.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tb_inventory.setIcon(icon2)
        self.tb_inventory.setIconSize(QSize(35, 35))
        self.tb_inventory.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.verticalLayout_2.addWidget(self.tb_inventory)

        self.tb_customers = QToolButton(self.wd_menu_button)
        self.tb_customers.setObjectName(u"tb_customers")
        self.tb_customers.setMinimumSize(QSize(140, 90))
        self.tb_customers.setFont(font)
        icon3 = QIcon()
        icon3.addFile(u":/Icons/customers.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tb_customers.setIcon(icon3)
        self.tb_customers.setIconSize(QSize(35, 35))
        self.tb_customers.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.verticalLayout_2.addWidget(self.tb_customers)

        self.tb_sales = QToolButton(self.wd_menu_button)
        self.tb_sales.setObjectName(u"tb_sales")
        self.tb_sales.setMinimumSize(QSize(140, 90))
        self.tb_sales.setFont(font)
        icon4 = QIcon()
        icon4.addFile(u":/Icons/price_tag.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tb_sales.setIcon(icon4)
        self.tb_sales.setIconSize(QSize(35, 35))
        self.tb_sales.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.verticalLayout_2.addWidget(self.tb_sales)

        self.tb_vendors = QToolButton(self.wd_menu_button)
        self.tb_vendors.setObjectName(u"tb_vendors")
        self.tb_vendors.setMinimumSize(QSize(140, 90))
        self.tb_vendors.setFont(font)
        icon5 = QIcon()
        icon5.addFile(u":/Icons/vendor.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tb_vendors.setIcon(icon5)
        self.tb_vendors.setIconSize(QSize(35, 35))
        self.tb_vendors.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.verticalLayout_2.addWidget(self.tb_vendors)

        self.tb_cash_count = QToolButton(self.wd_menu_button)
        self.tb_cash_count.setObjectName(u"tb_cash_count")
        self.tb_cash_count.setMinimumSize(QSize(140, 90))
        self.tb_cash_count.setFont(font)
        icon6 = QIcon()
        icon6.addFile(u":/Icons/performance.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tb_cash_count.setIcon(icon6)
        self.tb_cash_count.setIconSize(QSize(35, 35))
        self.tb_cash_count.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.verticalLayout_2.addWidget(self.tb_cash_count)

        self.tb_settings = QToolButton(self.wd_menu_button)
        self.tb_settings.setObjectName(u"tb_settings")
        self.tb_settings.setMinimumSize(QSize(140, 90))
        self.tb_settings.setFont(font)
        icon7 = QIcon()
        icon7.addFile(u":/Icons/settings_2.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tb_settings.setIcon(icon7)
        self.tb_settings.setIconSize(QSize(35, 35))
        self.tb_settings.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.verticalLayout_2.addWidget(self.tb_settings)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.tb_exit = QToolButton(self.wd_menu_button)
        self.tb_exit.setObjectName(u"tb_exit")
        self.tb_exit.setMinimumSize(QSize(140, 90))
        self.tb_exit.setFont(font)
        icon8 = QIcon()
        icon8.addFile(u":/Icons/power.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tb_exit.setIcon(icon8)
        self.tb_exit.setIconSize(QSize(35, 35))
        self.tb_exit.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.verticalLayout_2.addWidget(self.tb_exit)


        self.verticalLayout.addWidget(self.wd_menu_button)


        self.horizontalLayout.addWidget(self.wd_menu)

        self.wd_stacked = QStackedWidget(self.centralwidget)
        self.wd_stacked.setObjectName(u"wd_stacked")
        self.wd_stacked.setMinimumSize(QSize(0, 0))
        self.wd_stacked.setFont(font)
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.gridLayout = QGridLayout(self.home)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.wd_stacked.addWidget(self.home)
        self.custom = QWidget()
        self.custom.setObjectName(u"custom")
        self.wd_stacked.addWidget(self.custom)

        self.horizontalLayout.addWidget(self.wd_stacked)

        MainAppWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainAppWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 720, 22))
        self.menubar.setMinimumSize(QSize(0, 0))
        self.menubar.setMaximumSize(QSize(16777215, 16777215))
        self.menu_file = QMenu(self.menubar)
        self.menu_file.setObjectName(u"menu_file")
        self.menu_file.setFont(font)
        MainAppWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu_file.menuAction())
        self.menu_file.addAction(self.act_user_manager)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.act_exit)

        self.retranslateUi(MainAppWindow)

        self.wd_stacked.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainAppWindow)
    # setupUi

    def retranslateUi(self, MainAppWindow):
        MainAppWindow.setWindowTitle(QCoreApplication.translate("MainAppWindow", u"Eixn Point of Sale", None))
        self.act_user_manager.setText(QCoreApplication.translate("MainAppWindow", u"User Manager", None))
        self.act_exit.setText(QCoreApplication.translate("MainAppWindow", u"Exit", None))
        self.label.setText(QCoreApplication.translate("MainAppWindow", u"EixnPOS", None))
        self.tb_new_sale.setText(QCoreApplication.translate("MainAppWindow", u"New Sale", None))
        self.tb_inventory.setText(QCoreApplication.translate("MainAppWindow", u"Inventory", None))
        self.tb_customers.setText(QCoreApplication.translate("MainAppWindow", u"Customers", None))
        self.tb_sales.setText(QCoreApplication.translate("MainAppWindow", u"Sales Manager", None))
        self.tb_vendors.setText(QCoreApplication.translate("MainAppWindow", u"Vendors", None))
        self.tb_cash_count.setText(QCoreApplication.translate("MainAppWindow", u"Cash Count", None))
        self.tb_settings.setText(QCoreApplication.translate("MainAppWindow", u"Settings", None))
        self.tb_exit.setText(QCoreApplication.translate("MainAppWindow", u"Exit", None))
        self.menu_file.setTitle(QCoreApplication.translate("MainAppWindow", u"File", None))
    # retranslateUi

