from decimal import Decimal
import sys
from PySide6 import QtWidgets as qtw
from PySide6 import QtCore as qtc
from PySide6 import QtGui as qtg

from assets.stylesheets.output_qss import get_style

from ui.main_app_window_ui import Ui_MainAppWindow
from ui.home_window_ui import Ui_HomeWindow
from ui.customer_manager_ui import Ui_CustomerManager
from ui.inventory_manager_ui import Ui_InventoryManager

# import dialogs
from ui.cash_counter_ui import Ui_CashCounter
from ui.add_product_ui import Ui_AddProductDialog
from ui.categories_dialog_ui import Ui_CreateCategoryDialog
from ui.create_customer_dialog_ui import Ui_CreateCustomerDialog

# import config setup
from src.config.ui_config import Styles


#======================================= MAIN WINDOWS ===================================
# customer manager
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

        Styles(styled_widgets).set_styles()


class HomeWindow(qtw.QWidget, Ui_HomeWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.lb_welcome.setProperty("class", "welcome-text")


# inventory manager
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

        # connect signals

        Styles(widgets_to_style).set_styles()



#======================================= DIALOGS ======================================
class CashCounterDialog(qtw.QDialog, Ui_CashCounter):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_CashCounter()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(0)

        # source of truth
        # format: (value, keyName, category)
        self.currency_defs = [
            (Decimal("100.00"), "hundreds", "bills"),
            (Decimal("50.00"), "fifties", "bills"),
            (Decimal("20.00"), "twenties", "bills"),
            (Decimal("10.00"), "tens", "bills"),
            (Decimal("5.00"), "fives", "bills"),
            (Decimal("2.00"), "twos", "bills"),
            (Decimal("1.00"), "ones", "bills"),
            (Decimal("2.00"), "two_dollars", "coins"),
            (Decimal("1.00"), "dollars", "coins"),
            (Decimal("0.50"), "half_dollars", "coins"),
            (Decimal("0.25"), "quarters", "coins"),
            (Decimal("0.10"), "dimes", "coins"),
            (Decimal("0.05"), "nickels", "coins"),
            (Decimal("0.01"), "pennies", "coins"),
        ]

        # ui style mapping
        widgets_to_style = {
            "dialog-title": [self.ui.lb_dialog_title],
            "bold underlined": [
                self.ui.lb_coins_count, self.ui.lb_coins_amount,
                self.ui.lb_coins_remove, self.ui.lb_coins_amount_remove,
                self.ui.lb_bills_count, self.ui.lb_bills_amount,
                self.ui.lb_bills_remove, self.ui.lb_bills_amount_remove,
            ],
            "underlined": [
                self.ui.lb_two_dollars_amt, self.ui.lb_hundreds_amt,
                self.ui.lb_two_dollars_amt_remove, self.ui.lb_hundreds_amt_remove,
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
            ]
        }

        Styles(widgets_to_style).set_styles()
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
        totals = {"bills": Decimal("0"), "coins": Decimal("0")}

        for val, key, cat in self.currency_defs:
            line_edit = getattr(self.ui, f"le_{key}")
            label = getattr(self.ui, f"lb_{key}_amt")

            try:
                count = int(line_edit.text()) if line_edit.text() else 0
            except ValueError:
                count = 0

            item_total = count * val
            totals[cat] += item_total
            label.setText(f"$ {item_total:.02f}")

        # update category total
        self.ui.lb_bills_total.setText(f"$ {totals['bills']:.02f}")
        self.ui.lb_coins_total.setText(f"$ {totals['coins']:.02f}")
        self.ui.cash_drawer_total.setText(f"$ {totals['bills'] + totals['coins']:.02f}")

    def change_page(self, direction:int):
        new_index = self.ui.stackedWidget.currentIndex() + direction
        if 0 <= new_index < self.ui.stackedWidget.count():
            self.ui.stackedWidget.setCurrentIndex(new_index)
            
            if new_index == 1:
                self.ui.dbl_starting_cash.setFocus()
                self.ui.dbl_starting_cash.selectAll()

    def remove_cash(self):
        try:
            drawer_total = Decimal(self.ui.cash_drawer_total.text().replace("$", "").strip())
            starting_cash = Decimal(self.ui.dbl_starting_cash.text())
        except: return

        remove_amount = drawer_total - starting_cash
        if remove_amount <= 0: return

        category_removed = {"bills": Decimal("0"), "coins": Decimal("0")}
        total_removed = Decimal("0")

        for val, key, cat in self.currency_defs:
            drw_le = getattr(self.ui, f"le_{key}")
            rem_le = getattr(self.ui, f"le_{key}_remove")
            rem_lb = getattr(self.ui, f"lb_{key}_amt_remove")

            available_count = int(drw_le.text()) if drw_le.text().isnumeric() else 0

            # Greedy calculation
            count_taken = min(int(remove_amount / val), available_count)
            amount_taken = count_taken * val

            remove_amount -= amount_taken
            total_removed += amount_taken
            category_removed[cat] += amount_taken

            rem_le.setText(str(count_taken) if count_taken > 0 else "")
            rem_lb.setText(f"$ {amount_taken:.02f}")

        # update ui
        self.ui.lb_bills_total_remove.setText(f"$ {category_removed['bills']:.02f}")
        self.ui.lb_coins_total_remove.setText(f"$ {category_removed['coins']:.02f}")
        self.ui.lb_cash_drawer_total_remove.setText(f"$ {total_removed:.02f}")    


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
        Styles(widgets_to_style).set_styles()
        self.ui.pb_product_cancel.clicked.connect(self.close)
        self.ui.pb_category_add.clicked.connect(lambda: self.open_second_dialog(CategoriesDialog))

    def open_second_dialog(self, dialog_class):
        second_dialog = dialog_class(parent=self)
        second_dialog.exec()


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
                self.ui.pb_category_modify, self.ui.pb_category_delete, self.ui.pb_category_cancel
            ],
            "table": [self.ui.tbl_categories],
            "dialog-menu": [self.ui.dlg_menu],
        }

        # connect signals
        Styles(widgets_to_style).set_styles()
        self.ui.pb_category_cancel.clicked.connect(self.close)

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

        Styles(widgets_to_style).set_styles()


#======================================= MAIN APP ======================================
class MainWindow(qtw.QMainWindow, Ui_MainAppWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tb_vendors.setText("Suppliers")

        self.home = HomeWindow()
        customer_manager = CustomerManager()
        inventory_manager = InventoryManager()

        self.wd_stacked.addWidget(self.home)
        self.wd_stacked.addWidget(customer_manager)
        self.wd_stacked.addWidget(inventory_manager)
        self.wd_stacked.setCurrentWidget(self.home)

        self.current_window = self.home

        # connect signal
        self.tb_exit.clicked.connect(self.close)
        self.act_exit.triggered.connect(self.close)

        #================= customer window =======================
        self.tb_customers.clicked.connect(
            lambda checked: self.open_window(customer_manager)
        )
        customer_manager.pb_window_close.clicked.connect(
            lambda checked: self.close_window(customer_manager)
        )
        customer_manager.pb_add.clicked.connect(
            lambda checked: self.open_dialog(CreateCustomerDialog())
        )

        #================= inventory window =======================
        self.tb_inventory.clicked.connect(
            lambda checked: self.open_window(inventory_manager)
        )
        inventory_manager.pb_window_close.clicked.connect(
            lambda checked: self.close_window(inventory_manager)
        )
        inventory_manager.pb_add.clicked.connect(
            lambda checked: self.open_dialog(AddProductDialog())
        )

        #================= category dialog ========================
        

        #================= cash count =======================
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