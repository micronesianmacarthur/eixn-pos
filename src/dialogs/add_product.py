from PySide6 import QtWidgets as qtw
from src.ui.add_product_ui import Ui_AddProductDialog
from src.config.ui_config import Styles
from src.dialogs.categories_dialog import CategoriesDialog

from src.logic.utils import open_dialog

class AddProductDialog(qtw.QDialog, Ui_AddProductDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_AddProductDialog()
        self.ui.setupUi(self)

        # assign class
        widgets_to_style = {
            "group-box bold": [self.ui.grp_general, self.ui.grp_price, self.ui.grp_image],
            "dialog-title": [self.ui.lb_dialog_title],
            "dialog-button": [self.ui.pb_product_save, self.ui.pb_product_cancel],
            "dialog-menu": [self.ui.dlg_menu],
            "small-text": [
                self.ui.created_label, self.ui.updated_label, self.ui.product_id_label,
                self.ui.qty_available_label, self.ui.qty_on_order_label,
                self.ui.lb_created, self.ui.lb_updated, self.ui.lb_product_id,
                self.ui.lb_qty_available, self.ui.lb_qty_on_order,
            ],
            "small-header": [self.ui.lb_information],
            "combobox": [
                self.ui.cb_category, self.ui.cb_supplier, self.ui.cb_stock_type,
            ],
            "spinbox": [
                self.ui.sb_quantity, self.ui.sb_reorder_level,
                self.ui.dbl_cost, self.ui.dbl_price,
            ],
            "secondary-button": [self.ui.pb_browse],
            "new-button": [
                self.ui.pb_supplier_add, self.ui.pb_category_add, self.ui.pb_stock_type_add
            ],
            "display-only": [self.ui.lb_markup_margin, self.ui.lb_suggested_price],
        }

        # connect signals
        Styles.apply(widgets_to_style)
        self.ui.pb_product_cancel.clicked.connect(self.close)
        self.ui.pb_category_add.clicked.connect(lambda: open_dialog(CategoriesDialog, self))
