from PySide6 import QtWidgets as qtw
from src.ui.create_customer_dialog_ui import Ui_CreateCustomerDialog
from src.config.ui_config import Styles
from src.logic.utils import load_countries, load_states_for_country


class CreateCustomerDialog(qtw.QDialog, Ui_CreateCustomerDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_CreateCustomerDialog()
        self.ui.setupUi(self)

        # set defaults
        self.ui.chk_allow_account_charge.setChecked(False)
        # assign class
        widgets_to_style = {
            "group-box bold": [self.ui.grp_bill_to, self.ui.grp_account],
            "dialog-title": [self.ui.lb_dialog_title],
            "dialog-button": [self.ui.pb_customer_save, self.ui.pb_customer_cancel],
            "dialog-menu": [self.ui.dlg_menu],
            "small-text": [
                self.ui.lb_created_label,
                self.ui.lb_updated_label,
                self.ui.lb_customer_id_label,
                self.ui.lb_charge_balance_label,
                self.ui.lb_store_credit_label,
                self.ui.lb_created,
                self.ui.lb_updated,
                self.ui.lb_customer_id,
                self.ui.lb_charge_balance,
                self.ui.lb_store_credit,
            ],
            "small-header": [self.ui.lb_information],
            "combobox": [
                self.ui.cb_country,
                self.ui.cb_state,
            ],
            "spinbox": [
                self.ui.sb_zip_code,
                self.ui.dbl_custom_charge_limit,
            ],
            "display-only": [self.ui.lb_system_charge_limit],
            "checkbox": [
                self.ui.chk_allow_account_charge,
                self.ui.chk_disable_charge_limit,
            ],
        }

        Styles.apply(widgets_to_style)

        # Load countries into combo box
        self.ui.pb_customer_cancel.clicked.connect(self.close)
        self.ui.cb_country.addItems(load_countries())
        self.ui.cb_state.addItems(
            load_states_for_country(self.ui.cb_country.currentText())
        )
        self.ui.cb_state.setCurrentText("Pohnpei")
        self.ui.cb_country.currentTextChanged.connect(self.on_country_changed)
        self.ui.chk_allow_account_charge.stateChanged.connect(
            self.toggle_charge_widgets
        )
        self.ui.chk_disable_charge_limit.stateChanged.connect(
            self.toggle_charge_widgets
        )
        self.toggle_charge_widgets()

    def on_country_changed(self):
        country = self.ui.cb_country.currentText()
        states = load_states_for_country(country)
        self.ui.cb_state.clear()
        self.ui.cb_state.addItems(states)

    def toggle_charge_widgets(self):
        enabled = self.ui.chk_allow_account_charge.isChecked()
        disable_widgets = [
            self.ui.lb_system_charge_limit_label,
            self.ui.lb_system_charge_limit,
            self.ui.system_charge_limit_dollar_label,
            self.ui.lb_custom_charge_limit_label,
            self.ui.dbl_custom_charge_limit,
            self.ui.custom_charge_limit_dollar_label,
        ]
        widgets_to_toggle = [
            self.ui.lb_system_charge_limit_label,
            self.ui.lb_system_charge_limit,
            self.ui.lb_custom_charge_limit_label,
            self.ui.dbl_custom_charge_limit,
            self.ui.chk_disable_charge_limit,
            self.ui.system_charge_limit_dollar_label,
            self.ui.custom_charge_limit_dollar_label,
        ]
        for widget in widgets_to_toggle:
            widget_enabled = enabled and not (
                widget in disable_widgets
                and self.ui.chk_disable_charge_limit.isChecked()
            )
            widget.setEnabled(widget_enabled)
