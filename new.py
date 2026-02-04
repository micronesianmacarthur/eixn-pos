from decimal import Decimal, DecimalException
import sys
from PySide6 import QtWidgets as qtw
from PySide6 import QtCore as qtc
from PySide6 import QtGui as qtg

from assets.stylesheets.output_css import get_style

from ui.main_app_window_ui import Ui_MainAppWindow
from ui.home_window_ui import Ui_HomeWindow
from ui.customer_manager_ui import Ui_CustomerManager

# import dialogs
from ui.cash_counter_ui import Ui_CashCounter

# import config setup
from src.config.ui_config import Styles


#======================================= MAIN WINDOWS ===================================
class CustomerManager(qtw.QWidget, Ui_CustomerManager):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        styled_widgets= {
            "window-title": [self.lb_window_title],
            "close-button": [self.pb_window_close],
            "inline-button-text": [
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

        Styles(styled_widgets).set_styles()


class HomeWindow(qtw.QWidget, Ui_HomeWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.lb_welcome.setProperty("class", "welcome-text")


#======================================= DIALOGS ======================================
class CashCounterDialog(qtw.QDialog, Ui_CashCounter):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_CashCounter()
        self.ui.setupUi(self)      

        self.ui.stackedWidget.setCurrentIndex(0)

        # currency map
        self.currency_map = {
            "coins": [
                (self.ui.le_pennies, self.ui.lb_pennies_amt, Decimal("0.01")),
                (self.ui.le_nickels, self.ui.lb_nickels_amt, Decimal("0.05")),
                (self.ui.le_dimes, self.ui.lb_dimes_amt, Decimal("0.10")),
                (self.ui.le_quarters, self.ui.lb_quarters_amt, Decimal("0.25")),
                (self.ui.le_half_dollars, self.ui.lb_half_dollars_amt, Decimal("0.50")),
                (self.ui.le_dollars, self.ui.lb_dollars_amt, Decimal("1.00")),
                (self.ui.le_two_dollars, self.ui.lb_two_dollars_amt, Decimal("2.00")),
            ],
            "bills": [
                (self.ui.le_ones, self.ui.lb_ones_amt, Decimal("1.00")),
                (self.ui.le_twos, self.ui.lb_twos_amt, Decimal("2.00")),
                (self.ui.le_fives, self.ui.lb_fives_amt, Decimal("5.00")),
                (self.ui.le_tens, self.ui.lb_tens_amt, Decimal("10.00")),
                (self.ui.le_twenties, self.ui.lb_twenties_amt, Decimal("20.00")),
                (self.ui.le_fifties, self.ui.lb_fifties_amt, Decimal("50.00")),
                (self.ui.le_hundreds, self.ui.lb_hundreds_amt, Decimal("100.00")),
            ]
        }

        self.currency_map_remove = {
            "coins": [
                (self.ui.le_pennies_remove, self.ui.lb_pennies_amt_remove, Decimal("0.01")),
                (self.ui.le_nickels_remove, self.ui.lb_nickels_amt_remove, Decimal("0.05")),
                (self.ui.le_dimes_remove, self.ui.lb_dimes_amt_remove, Decimal("0.10")),
                (self.ui.le_quarters_remove, self.ui.lb_quarters_amt_remove, Decimal("0.25")),
                (self.ui.le_half_dollars_remove, self.ui.lb_half_dollars_amt_remove, Decimal("0.50")),
                (self.ui.le_dollar_remove, self.ui.lb_dollar_amt_remove, Decimal("1.00")),
                (self.ui.le_two_dollars_remove, self.ui.lb_two_dollars_amt_remove, Decimal("2.00")),
            ],
            "bills": [
                (self.ui.le_ones_remove, self.ui.lb_ones_amt_remove, Decimal("1.00")),
                (self.ui.le_twos_remove, self.ui.lb_twos_amt_remove, Decimal("2.00")),
                (self.ui.le_fives_remove, self.ui.lb_fives_amt_remove, Decimal("5.00")),
                (self.ui.le_tens_remove, self.ui.lb_tens_amt_remove, Decimal("10.00")),
                (self.ui.le_twenties_remove, self.ui.lb_twenties_amt_remove, Decimal("20.00")),
                (self.ui.le_fifties_remove, self.ui.lb_fifties_amt_remove, Decimal("50.00")),
                (self.ui.le_hundreds_remove, self.ui.lb_hundreds_amt_remove, Decimal("100.00")),
            ]
        }

        styled_widgets = {
            "dialog-title": [self.ui.lb_dialog_title],
            "bold underlined": [
                self.ui.lb_coins_count, self.ui.lb_coins_amount,
                self.ui.lb_bills_count, self.ui.lb_bills_amount,
                self.ui.lb_coins_remove, self.ui.lb_coins_amount_remove,
                self.ui.lb_bills_remove, self.ui.lb_bills_amount_remove,
            ],
            "underlined": [
                self.ui.lb_two_dollars_amt, self.ui.lb_hundreds_amt,
                self.ui.lb_two_dollars_amt_remove, self.ui.lb_hundreds_amt_remove,
            ],
            "close-total": [self.ui.cash_drawer_total, self.ui.lb_cash_drawer_total_remove],
            "primary-button": [
                self.ui.pb_next_page, self.ui.pb_previous_page,
                self.ui.pb_cancel
            ],
            "calculate-button": [self.ui.pb_remove_cash],
        }

        Styles(styled_widgets).set_styles()
        self.connect_signals()
        self.ui.pb_remove_cash.clicked.connect(self.remove_cash)

    def connect_signals(self):
        """Connect UI element signals to their respective slots with lambda."""
        self.ui.pb_cancel.clicked.connect(self.close)
        self.ui.pb_next_page.clicked.connect(lambda: self.change_page(1))
        self.ui.pb_previous_page.clicked.connect(lambda: self.change_page(-1))
        # self.ui.pb_remove_cash.clicked.connect(self.calculate_remove_cash)

        # connect LineEdits using map
        for category in self.currency_map.values():
            for line_edit, label, value in category:
                line_edit.editingFinished.connect(
                    lambda le=line_edit, lb=label, val=value: self.sync_values()
                )


    def sync_values(self):
        """Syncs the values for category total and grand total."""
        grand_total = Decimal("0.00")

        for category, items in self.currency_map.items():
            category_total = Decimal("0.00")

            for line_edit, label, value in items:
                try:
                    count = int(line_edit.text()) if line_edit.text() else 0
                except ValueError:
                    count = 0

                line_item_total = count * value
                category_total += line_item_total
                label.setText(f"$ {line_item_total:.02f}")

            # update specific category total label
            target_label = self.ui.lb_coins_total if category == "coins" else self.ui.lb_bills_total
            target_label.setText(f"$ {category_total:.02f}")
            grand_total += category_total

        # update grand total label
        self.ui.cash_drawer_total.setText(f"$ {grand_total:.02f}")

    def change_page(self, direction: int):
        """Changes the current stackedWidget page according to direction."""
        current_index = self.ui.stackedWidget.currentIndex()
        new_index = current_index + direction
        
        if 0 <= new_index < self.ui.stackedWidget.count():
            self.ui.stackedWidget.setCurrentIndex(new_index)

    # def calculate_remove_cash(self):
    #     try:
    #         grand_total = Decimal(self.ui.cash_drawer_total.text().replace("$ ", "").strip())
    #         starting_cash = Decimal(self.ui.dbl_starting_cash.text())
    #     except (ValueError, DecimalException):
    #         return

    #     amount_to_remove = grand_total - starting_cash

    #     if amount_to_remove <= 0:
    #         return

    #     categories = ["bills", "coins"]
    #     total_removed_calc = Decimal("0.00")

    #     for category in categories:
    #         drawer_items = self.currency_map[category]
    #         remove_items = self.currency_map_remove[category]

    #         for (src_le, _, value), (rem_le, rem_lb, _) in zip(drawer_items, remove_items):
    #             try:
    #                 available_count = int(src_le.text()) if src_le.text() else 0
    #             except ValueError:
    #                 available_count = 0

    #             if amount_to_remove >= value and available_count > 0:
    #                 needed_count = int(amount_to_remove / value)
    #                 actual_to_take = min(needed_count, available_count)
                    
    #                 amount_to_remove -= (actual_to_take * value)
    #                 total_removed_calc += (actual_to_take * value)

    #                 rem_le.setText(str(actual_to_take))
    #                 rem_lb.setText(f"$ {actual_to_take * value:.02f}")
    #             else:
    #                 rem_le.setText("")
    #                 rem_lb.setText("$ 0.00")

    #             print(f"{src_le.objectName()}: needed_count: {needed_count}, available_count: {available_count}, actual to take: {actual_to_take}, total_removed: {total_removed_calc}")

    #     self.ui.lb_cash_drawer_total_remove.setText(f"$ {total_removed_calc:.02f}")

    def remove_cash(self):
        grand_total = Decimal(self.ui.cash_drawer_total.text().replace("$", "").strip())
        starting_cash = Decimal(self.ui.dbl_starting_cash.text())

        remove_amount = grand_total - starting_cash
        total_removed = Decimal("0")

        categories = ["bills", "coins"]
        
        if remove_amount > 0:
            for category in categories:
                drawer_items = self.currency_map[category]
                remove_items = self.currency_map_remove[category]
                
                for (drw_le, drw_lb, drw_val), (rem_le, rem_lb, rem_val) in zip(reversed(drawer_items), reversed(remove_items)):
                    if drw_le.text().isnumeric():
                        need_to_remove = int(remove_amount / drw_val)
                        actual_to_remove = min(need_to_remove, int(drw_le.text()))
                        amount_removed = Decimal(f"{actual_to_remove * drw_val:.02f}")
                        total_removed += amount_removed
                        remove_amount -= amount_removed

                        if actual_to_remove <=0:
                            rem_le.setText("")
                        else:
                            rem_le.setText(str(actual_to_remove))

                        rem_lb.setText(str(amount_removed))
                        
            self.ui.lb_cash_drawer_total_remove.setText(str(total_removed))
                
        else:
            return
                    

        

#======================================= MAIN APP ======================================
class MainWindow(qtw.QMainWindow, Ui_MainAppWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.home = HomeWindow()
        customer_manager = CustomerManager()

        self.wd_stacked.addWidget(self.home)
        self.wd_stacked.addWidget(customer_manager)
        self.wd_stacked.setCurrentWidget(self.home)

        self.current_window = self.home

        # connect signal
        self.tb_customers.clicked.connect(
            lambda checked: self.open_window(customer_manager)
        )
        customer_manager.pb_window_close.clicked.connect(
            lambda checked: self.close_window(customer_manager)
        )
        # cash count
        self.tb_cash_count.clicked.connect(
            lambda checked: self.open_dialog(CashCounterDialog())
        )

    def open_window(self, window:qtw.QWidget):
        self.wd_stacked.setCurrentWidget(window)
        self.current_window = window

    def close_window(self, window: qtw.QWidget):
        self.wd_stacked.setCurrentWidget(self.home)
        self.current_window = self.home

    def open_dialog(self, dialog: qtw.QDialog):
        self.dialog = dialog
        self.dialog.exec()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    # apply styles
    app.setStyleSheet(get_style())
    window = MainWindow()
    window.show()
    sys.exit(app.exec())