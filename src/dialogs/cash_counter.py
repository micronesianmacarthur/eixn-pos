from decimal import Decimal
from PySide6 import QtWidgets as qtw
from src.ui.cash_counter_ui import Ui_CashCounter
from src.config.ui_config import Styles
from src.config.constants import CURRENCY_DEFS

from src.logic.cash_logic import calculate_totals, calculate_cash_removal
from src.logic.utils import navigate_stacked_widget


class CashCounterDialog(qtw.QDialog, Ui_CashCounter):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_CashCounter()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(0)

        # source of truth
        self.currency_defs = CURRENCY_DEFS

        # ui style mapping
        widgets_to_style = {
            "dialog-title": [self.ui.lb_dialog_title],
            "bold underlined": [
                self.ui.lb_coins_count,
                self.ui.lb_coins_amount,
                self.ui.lb_coins_remove,
                self.ui.lb_coins_amount_remove,
                self.ui.lb_bills_count,
                self.ui.lb_bills_amount,
                self.ui.lb_bills_remove,
                self.ui.lb_bills_amount_remove,
            ],
            "underlined": [
                self.ui.lb_two_dollars_amt,
                self.ui.lb_hundreds_amt,
                self.ui.lb_two_dollars_amt_remove,
                self.ui.lb_hundreds_amt_remove,
            ],
            "close-total": [
                self.ui.cash_drawer_total,
                self.ui.lb_cash_drawer_total_remove,
            ],
            "dialog-menu": [self.ui.dlg_menu],
            "dialog-button": [
                self.ui.pb_next_page,
                self.ui.pb_previous_page,
                self.ui.pb_cancel,
            ],
            "calculate-button": [self.ui.pb_remove_cash],
            "spinbox": [
                self.ui.dbl_starting_cash,
            ],
        }

        Styles.apply(widgets_to_style)
        self.connect_signals()

    def connect_signals(self):
        self.ui.pb_cancel.clicked.connect(self.close)
        self.ui.pb_next_page.clicked.connect(lambda: self.change_page(1))
        self.ui.pb_previous_page.clicked.connect(lambda: self.change_page(-1))
        self.ui.pb_remove_cash.clicked.connect(self.remove_cash)

        # dynamic signal connection
        for _, key, _ in self.currency_defs:
            line_edit = getattr(self.ui, f"le_{key}")
            line_edit.editingFinished.connect(self.sync_values)

    def sync_values(self):
        currency_counts = {}
        for _, key, _ in self.currency_defs:
            line_edit = getattr(self.ui, f"le_{key}")
            try:
                currency_counts[key] = int(line_edit.text()) if line_edit.text() else 0
            except ValueError:
                currency_counts[key] = 0

        results = calculate_totals(currency_counts, self.currency_defs)

        # update UI labels
        for val, key, cat in self.currency_defs:
            label = getattr(self.ui, f"lb_{key}_amt")
            item_total = currency_counts[key] * val
            label.setText(f"$ {item_total:.02f}")

        self.ui.lb_bills_total.setText(f"$ {results['bills']:.02f}")
        self.ui.lb_coins_total.setText(f"$ {results['coins']:.02f}")
        self.ui.cash_drawer_total.setText(f"$ {results['grand_total']:.02f}")

    def change_page(self, direction: int):
        new_index = navigate_stacked_widget(self.ui.stackedWidget, direction)

        if new_index == 1:
            self.ui.dbl_starting_cash.setFocus()
            self.ui.dbl_starting_cash.selectAll()

    def remove_cash(self):
        try:
            drawer_total = Decimal(
                self.ui.cash_drawer_total.text().replace("$", "").strip()
            )
            starting_cash = Decimal(self.ui.dbl_starting_cash.text())
        except:
            return

        remove_amount = drawer_total - starting_cash
        if remove_amount <= 0:
            return

        available_counts = {}
        for _, key, _ in self.currency_defs:
            drw_le = getattr(self.ui, f"le_{key}")
            available_counts[key] = (
                int(drw_le.text()) if drw_le.text().isnumeric() else 0
            )

        results = calculate_cash_removal(
            remove_amount, available_counts, self.currency_defs
        )

        # update UI
        for _, key, _ in self.currency_defs:
            rem_le = getattr(self.ui, f"le_{key}_remove")
            rem_lb = getattr(self.ui, f"lb_{key}_amt_remove")

            count = results["counts"][key]
            amount = results["amounts"][key]

            rem_le.setText(str(count) if count > 0 else "")
            rem_lb.setText(f"$ {amount:.02f}")

        self.ui.lb_bills_total_remove.setText(
            f"$ {results['category_totals']['bills']:.02f}"
        )
        self.ui.lb_coins_total_remove.setText(
            f"$ {results['category_totals']['coins']:.02f}"
        )
        self.ui.lb_cash_drawer_total_remove.setText(
            f"$ {results['total_removed']:.02f}"
        )
