from PySide6 import QtWidgets as qtw
from src.ui.categories_dialog_ui import Ui_CreateCategoryDialog
from src.config.ui_config import Styles


class CategoriesDialog(qtw.QDialog, Ui_CreateCategoryDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_CreateCategoryDialog()
        self.ui.setupUi(self)

        # assign class
        widgets_to_style = {
            "dialog-title": [self.ui.lb_dialog_title],
            "section-header": [self.ui.lb_section_header],
            "new-button": [self.ui.pb_category_save],
            "dialog-button": [
                self.ui.pb_category_modify,
                self.ui.pb_category_delete,
                self.ui.pb_category_cancel,
            ],
            "table": [self.ui.tbl_categories],
            "dialog-menu": [self.ui.dlg_menu],
        }

        # connect signals
        Styles.apply(widgets_to_style)
        self.ui.pb_category_cancel.clicked.connect(self.close)
