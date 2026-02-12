from PySide6 import QtWidgets as qtw
from src.ui.find_dialog_ui import Ui_FindDialog
from src.config.ui_config import Styles

# from src.logic.utils import open_dialog, dialog_connect


class FindDialog(qtw.QDialog, Ui_FindDialog):
    def __init__(self, parent=None, title=None):
        super().__init__(parent)
        self.ui = Ui_FindDialog()
        self.ui.setupUi(self)

        if title:
            self.ui.lb_dialog_title.setText(title)

        # assign class
        widgets_to_style = {
            "dialog-title": [self.ui.lb_dialog_title],
            "dialog-menu": [self.ui.dlg_menu],
            "dialog-button": [
                self.ui.pb_find_ok, self.ui.pb_find_cancel,
            ],
            "secondary-button": [self.ui.pb_search],
            "table": [self.ui.tbl_find_results],
        }

        Styles.apply(widgets_to_style)
        self.ui.pb_find_cancel.clicked.connect(self.close)