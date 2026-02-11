from PySide6 import QtWidgets as qtw
from src.ui.inventory_manager_ui import Ui_InventoryManager
from src.config.ui_config import Styles

class InventoryManager(qtw.QWidget, Ui_InventoryManager):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # assign class
        widgets_to_style = {
            "window-title": [self.lb_window_title],
            "close-button": [self.pb_window_close],
            "table": [
                self.tbl_products, self.tbl_product_stock,
                self.tbl_product_sales, self.tbl_product_receiving
            ],
            "primary-button": [
                self.pb_add,
                self.pb_modify,
                self.pb_find,
                self.pb_filter,
                self.pb_receive,
                self.pb_use_in_sale,
                self.pb_delete,
            ],
        }

        # apply styles
        Styles.apply(widgets_to_style)
