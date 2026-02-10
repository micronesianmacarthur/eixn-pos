# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'categories_dialog.ui'
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

class Ui_CreateCategoryDialog(object):
    def setupUi(self, CreateCategoryDialog):
        if not CreateCategoryDialog.objectName():
            CreateCategoryDialog.setObjectName(u"CreateCategoryDialog")
        CreateCategoryDialog.setWindowModality(Qt.WindowModality.ApplicationModal)
        CreateCategoryDialog.resize(640, 480)
        CreateCategoryDialog.setMinimumSize(QSize(640, 480))
        CreateCategoryDialog.setMaximumSize(QSize(640, 480))
        CreateCategoryDialog.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(CreateCategoryDialog)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(CreateCategoryDialog)
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

        self.widget_2 = QWidget(CreateCategoryDialog)
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
        self.lb_category_name = QLabel(self.widget_4)
        self.lb_category_name.setObjectName(u"lb_category_name")
        self.lb_category_name.setMinimumSize(QSize(0, 25))
        self.lb_category_name.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout.addWidget(self.lb_category_name)

        self.le_category_name = QLineEdit(self.widget_4)
        self.le_category_name.setObjectName(u"le_category_name")
        self.le_category_name.setMinimumSize(QSize(0, 25))
        self.le_category_name.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout.addWidget(self.le_category_name)

        self.pb_category_save = QPushButton(self.widget_4)
        self.pb_category_save.setObjectName(u"pb_category_save")
        self.pb_category_save.setMinimumSize(QSize(100, 25))
        self.pb_category_save.setMaximumSize(QSize(100, 25))
        icon = QIcon()
        icon.addFile(u":/Icons/tick.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_category_save.setIcon(icon)
        self.pb_category_save.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.pb_category_save)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.widget_4)

        self.tbl_categories = QTableView(self.widget_3)
        self.tbl_categories.setObjectName(u"tbl_categories")

        self.verticalLayout_2.addWidget(self.tbl_categories)


        self.horizontalLayout_22.addWidget(self.widget_3)

        self.dlg_menu = QWidget(self.widget_2)
        self.dlg_menu.setObjectName(u"dlg_menu")
        self.dlg_menu.setMinimumSize(QSize(150, 0))
        self.dlg_menu.setMaximumSize(QSize(150, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.dlg_menu)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 10)
        self.pb_category_modify = QPushButton(self.dlg_menu)
        self.pb_category_modify.setObjectName(u"pb_category_modify")
        self.pb_category_modify.setMinimumSize(QSize(0, 25))
        self.pb_category_modify.setMaximumSize(QSize(16777215, 25))
        icon1 = QIcon()
        icon1.addFile(u":/Icons/edit.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_category_modify.setIcon(icon1)
        self.pb_category_modify.setIconSize(QSize(25, 25))

        self.verticalLayout_3.addWidget(self.pb_category_modify)

        self.pb_category_delete = QPushButton(self.dlg_menu)
        self.pb_category_delete.setObjectName(u"pb_category_delete")
        self.pb_category_delete.setMinimumSize(QSize(0, 25))
        self.pb_category_delete.setMaximumSize(QSize(16777215, 25))
        icon2 = QIcon()
        icon2.addFile(u":/Icons/trash.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_category_delete.setIcon(icon2)
        self.pb_category_delete.setIconSize(QSize(25, 25))

        self.verticalLayout_3.addWidget(self.pb_category_delete)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.pb_category_cancel = QPushButton(self.dlg_menu)
        self.pb_category_cancel.setObjectName(u"pb_category_cancel")
        self.pb_category_cancel.setMinimumSize(QSize(0, 25))
        self.pb_category_cancel.setMaximumSize(QSize(16777215, 25))
        icon3 = QIcon()
        icon3.addFile(u":/Icons/cross.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_category_cancel.setIcon(icon3)
        self.pb_category_cancel.setIconSize(QSize(25, 25))

        self.verticalLayout_3.addWidget(self.pb_category_cancel)


        self.horizontalLayout_22.addWidget(self.dlg_menu)


        self.verticalLayout_4.addWidget(self.widget_2)


        self.retranslateUi(CreateCategoryDialog)

        QMetaObject.connectSlotsByName(CreateCategoryDialog)
    # setupUi

    def retranslateUi(self, CreateCategoryDialog):
        CreateCategoryDialog.setWindowTitle(QCoreApplication.translate("CreateCategoryDialog", u"Category", None))
        self.lb_dialog_title.setText(QCoreApplication.translate("CreateCategoryDialog", u"Categories", None))
        self.lb_section_header.setText(QCoreApplication.translate("CreateCategoryDialog", u"Create New Category", None))
        self.lb_category_name.setText(QCoreApplication.translate("CreateCategoryDialog", u"Category Name:", None))
        self.pb_category_save.setText(QCoreApplication.translate("CreateCategoryDialog", u"Save", None))
        self.pb_category_modify.setText(QCoreApplication.translate("CreateCategoryDialog", u"Modify", None))
        self.pb_category_delete.setText(QCoreApplication.translate("CreateCategoryDialog", u"Delete", None))
        self.pb_category_cancel.setText(QCoreApplication.translate("CreateCategoryDialog", u"Cancel", None))
    # retranslateUi

