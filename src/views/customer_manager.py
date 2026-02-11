from PySide6 import QtWidgets as qtw
from src.ui.customer_manager_ui import Ui_CustomerManager
from src.config.ui_config import Styles

class CustomerManager(qtw.QWidget, Ui_CustomerManager):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        styled_widgets= {
            "window-title": [self.lb_window_title],
            "close-button": [self.pb_window_close],
            "primary-button": [
                self.pb_add,
                self.pb_modify,
                self.pb_find,
                self.pb_filter,
                self.pb_new_sale,
                self.pb_delete,
            ],
            "table": [
                self.tbl_customers, self.tbl_customer_items,
                self.tbl_customer_charges,
            ],
        }

        Styles.apply(styled_widgets)
