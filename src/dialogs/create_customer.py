from PySide6 import QtWidgets as qtw
from src.ui.create_customer_dialog_ui import Ui_CreateCustomerDialog
from src.config.ui_config import Styles

class CreateCustomerDialog(qtw.QDialog, Ui_CreateCustomerDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_CreateCustomerDialog()
        self.ui.setupUi(self)

        # assign class
        widgets_to_style = {
            "group-box bold": [self.ui.grp_bill_to, self.ui.grp_account],
            "dialog-title": [self.ui.lb_dialog_title],
            "dialog-button": [self.ui.pb_customer_save, self.ui.pb_customer_cancel],
            "dialog-menu": [self.ui.dlg_menu],
            "small-text": [
                self.ui.lb_created_label, self.ui.lb_updated_label, self.ui.lb_customer_id_label,
                self.ui.lb_charge_balance_label, self.ui.lb_store_credit_label,
                self.ui.lb_created, self.ui.lb_updated, self.ui.lb_customer_id,
                self.ui.lb_charge_balance, self.ui.lb_store_credit,
            ],
            "small-header": [self.ui.lb_information],
            "combobox": [
                self.ui.cb_country,
            ],
            "spinbox": [
                self.ui.sb_zip_code, self.ui.dbl_custom_charge_limit,
            ],
            "display-only": [self.ui.lb_system_charge_limit],
        }

        Styles.apply(widgets_to_style)
