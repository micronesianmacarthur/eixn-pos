import sys
from PySide6 import QtWidgets as qtw
from PySide6 import QtCore as qtc

from src.assets.stylesheets.output_qss import get_style
from src.ui.main_app_window_ui import Ui_MainAppWindow

# Import Modular Views
from src.views.home_window import HomeWindow
from src.views.customer_manager import CustomerManager
from src.views.inventory_manager import InventoryManager

# Import Modular Dialogs
from src.dialogs.cash_counter import CashCounterDialog
from src.dialogs.add_product import AddProductDialog
from src.dialogs.create_customer import CreateCustomerDialog

from src.logic.utils import open_dialog

#======================================= MAIN APP ======================================
class MainWindow(qtw.QMainWindow, Ui_MainAppWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tb_vendors.setText("Suppliers")

        self.home = HomeWindow()
        self.customer_manager = CustomerManager()
        self.inventory_manager = InventoryManager()

        self.wd_stacked.addWidget(self.home)
        self.wd_stacked.addWidget(self.customer_manager)
        self.wd_stacked.addWidget(self.inventory_manager)
        self.wd_stacked.setCurrentWidget(self.home)

        self.current_window = self.home

        # connect signals
        self.tb_exit.clicked.connect(self.close)
        self.act_exit.triggered.connect(self.close)

        #================= customer window =======================
        self.tb_customers.clicked.connect(
            lambda checked: self.open_window(self.customer_manager)
        )
        self.customer_manager.pb_window_close.clicked.connect(
            lambda checked: self.close_window(self.customer_manager)
        )
        self.customer_manager.pb_add.clicked.connect(
            lambda checked: open_dialog(CreateCustomerDialog, self)
        )

        #================= inventory window =======================
        self.tb_inventory.clicked.connect(
            lambda checked: self.open_window(self.inventory_manager)
        )
        self.inventory_manager.pb_window_close.clicked.connect(
            lambda checked: self.close_window(self.inventory_manager)
        )
        self.inventory_manager.pb_add.clicked.connect(
            lambda checked: open_dialog(AddProductDialog, self)
        )

        #================= cash count =======================
        self.tb_cash_count.clicked.connect(
            lambda checked: open_dialog(CashCounterDialog, self)
        )

    def open_window(self, window:qtw.QWidget):
        self.wd_stacked.setCurrentWidget(window)
        self.current_window = window

    def close_window(self, window: qtw.QWidget):
        self.wd_stacked.setCurrentWidget(self.home)
        self.current_window = self.home


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    # apply styles
    app.setStyleSheet(get_style())
    window = MainWindow()
    window.show()
    sys.exit(app.exec())