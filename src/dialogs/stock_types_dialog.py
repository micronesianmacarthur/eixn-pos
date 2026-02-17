from PySide6 import QtWidgets as qtw
from src.ui.stock_types_dialog_ui import Ui_StockTypesDialog
from src.config.ui_config import Styles


class StockTypesDialog(qtw.QDialog, Ui_StockTypesDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_StockTypesDialog()
        self.ui.setupUi(self)

        # assign class
        widgets_to_style = {
            "dialog-title": [self.ui.lb_dialog_title],
            "section-header": [self.ui.lb_section_header],
            "new-button": [self.ui.pb_stock_type_save],
            "dialog-button": [
                self.ui.pb_stock_type_modify,
                self.ui.pb_stock_type_delete,
                self.ui.pb_stock_type_cancel,
            ],
            "table": [self.ui.tbl_stock_types],
            "dialog-menu": [self.ui.dlg_menu],
        }

        # connect signals
        Styles.apply(widgets_to_style)
        self.ui.pb_stock_type_cancel.clicked.connect(self.close)