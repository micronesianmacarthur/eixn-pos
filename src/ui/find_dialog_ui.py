# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'find_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTableView, QVBoxLayout,
    QWidget)
import icons_rc

class Ui_FindDialog(object):
    def setupUi(self, FindDialog):
        if not FindDialog.objectName():
            FindDialog.setObjectName(u"FindDialog")
        FindDialog.setWindowModality(Qt.WindowModality.ApplicationModal)
        FindDialog.resize(700, 540)
        FindDialog.setMinimumSize(QSize(700, 540))
        FindDialog.setMaximumSize(QSize(700, 540))
        FindDialog.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(FindDialog)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(FindDialog)
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

        self.widget_2 = QWidget(FindDialog)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_22 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_22.setSpacing(5)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.dlg_main = QWidget(self.widget_2)
        self.dlg_main.setObjectName(u"dlg_main")
        self.verticalLayout_2 = QVBoxLayout(self.dlg_main)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 10, 5, 5)
        self.widget_4 = QWidget(self.dlg_main)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(0, 45))
        self.widget_4.setMaximumSize(QSize(16777215, 45))
        self.gridLayout = QGridLayout(self.widget_4)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lb_search_label = QLabel(self.widget_4)
        self.lb_search_label.setObjectName(u"lb_search_label")
        self.lb_search_label.setMinimumSize(QSize(85, 25))
        self.lb_search_label.setMaximumSize(QSize(85, 25))

        self.horizontalLayout_2.addWidget(self.lb_search_label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.le_search = QLineEdit(self.widget_4)
        self.le_search.setObjectName(u"le_search")
        self.le_search.setMinimumSize(QSize(0, 25))
        self.le_search.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout.addWidget(self.le_search)

        self.pb_search = QPushButton(self.widget_4)
        self.pb_search.setObjectName(u"pb_search")
        self.pb_search.setMinimumSize(QSize(100, 25))
        self.pb_search.setMaximumSize(QSize(100, 25))
        icon = QIcon()
        icon.addFile(u":/Icons/search_white.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_search.setIcon(icon)

        self.horizontalLayout.addWidget(self.pb_search)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.dlg_main)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout = QVBoxLayout(self.widget_5)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lb_results_label = QLabel(self.widget_5)
        self.lb_results_label.setObjectName(u"lb_results_label")
        self.lb_results_label.setMinimumSize(QSize(0, 25))
        self.lb_results_label.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout.addWidget(self.lb_results_label)

        self.tbl_find_results = QTableView(self.widget_5)
        self.tbl_find_results.setObjectName(u"tbl_find_results")

        self.verticalLayout.addWidget(self.tbl_find_results)


        self.verticalLayout_2.addWidget(self.widget_5)


        self.horizontalLayout_22.addWidget(self.dlg_main)

        self.dlg_menu = QWidget(self.widget_2)
        self.dlg_menu.setObjectName(u"dlg_menu")
        self.dlg_menu.setMinimumSize(QSize(150, 0))
        self.dlg_menu.setMaximumSize(QSize(150, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.dlg_menu)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 10)
        self.pb_find_ok = QPushButton(self.dlg_menu)
        self.pb_find_ok.setObjectName(u"pb_find_ok")
        self.pb_find_ok.setMinimumSize(QSize(0, 35))
        self.pb_find_ok.setMaximumSize(QSize(16777215, 35))
        icon1 = QIcon()
        icon1.addFile(u":/Icons/tick.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_find_ok.setIcon(icon1)

        self.verticalLayout_3.addWidget(self.pb_find_ok)

        self.pb_find_cancel = QPushButton(self.dlg_menu)
        self.pb_find_cancel.setObjectName(u"pb_find_cancel")
        self.pb_find_cancel.setMinimumSize(QSize(0, 35))
        self.pb_find_cancel.setMaximumSize(QSize(16777215, 35))
        icon2 = QIcon()
        icon2.addFile(u":/Icons/cross.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_find_cancel.setIcon(icon2)

        self.verticalLayout_3.addWidget(self.pb_find_cancel)

        self.verticalSpacer = QSpacerItem(20, 392, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout_22.addWidget(self.dlg_menu)


        self.verticalLayout_4.addWidget(self.widget_2)


        self.retranslateUi(FindDialog)

        QMetaObject.connectSlotsByName(FindDialog)
    # setupUi

    def retranslateUi(self, FindDialog):
        FindDialog.setWindowTitle("")
        self.lb_dialog_title.setText(QCoreApplication.translate("FindDialog", u"Find {}", None))
        self.lb_search_label.setText(QCoreApplication.translate("FindDialog", u"Search For:", None))
        self.pb_search.setText(QCoreApplication.translate("FindDialog", u"Find", None))
        self.lb_results_label.setText(QCoreApplication.translate("FindDialog", u"Results:", None))
        self.pb_find_ok.setText(QCoreApplication.translate("FindDialog", u"OK", None))
        self.pb_find_cancel.setText(QCoreApplication.translate("FindDialog", u"Cancel", None))
    # retranslateUi

