from PySide6 import QtWidgets as qtw
from PySide6.QtGui import QStandardItemModel, QStandardItem

from src.ui.receiving_dialog_ui import Ui_ReceivingDialog
from src.dialogs.products import AddProductDialog, EditProductDialog
from src.dialogs.find import FindDialog
from src.config.ui_config import Styles
from src.models.dummy_receiving_data import columns, dummy_receiving_data

from src.logic.utils import open_dialog, dialog_connect

import os


class ReceivingDialog(qtw.QDialog, Ui_ReceivingDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ReceivingDialog()
        self.ui.setupUi(self)

        # assign class
        widgets_to_style = {
            "dialog-title": [self.ui.lb_dialog_title],
            "dialog-button": [
                self.ui.pb_new_item,
                self.ui.pb_modify_item,
                self.ui.pb_find_item,
                self.ui.pb_submit_all,
                self.ui.pb_close,
                self.ui.pb_deleteitem,
            ],
            "dialog-menu": [self.ui.dlg_menu],
            "table": [self.ui.tbl_receiving_list],
            "non-shift-display": [self.ui.lb_item_count],
            
        }

        Styles.apply(widgets_to_style)

        # populate table with dummy data
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(columns)
        for data_row in dummy_receiving_data:
            items = [QStandardItem(str(value)) for value in data_row]
            self.model.appendRow(items)
        self.ui.tbl_receiving_list.setModel(self.model)
        self.ui.tbl_receiving_list.resizeColumnsToContents()

        # connect signals
        self.ui.pb_close.clicked.connect(self.close)
        dialog_connect(self.ui.pb_new_item, open_dialog, AddProductDialog, self)
        dialog_connect(self.ui.pb_modify_item, open_dialog, EditProductDialog, self)
        dialog_connect(self.ui.pb_find_item, open_dialog, FindDialog, self)
