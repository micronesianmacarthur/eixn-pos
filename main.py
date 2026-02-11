import sys
from PySide6 import QtWidgets as qtw
from PySide6 import QtCore as qtc

from src.assets.stylesheets.output_qss import get_style
from src.ui.main_app_window_ui import Ui_MainAppWindow

# Import Modular Dialogs
from src.dialogs.cash_counter import CashCounterDialog
from src.dialogs.products import AddProductDialog, EditProductDialog
from src.dialogs.create_customer import CreateCustomerDialog

from src.logic.utils import open_dialog, dialog_connect, window_connect
from src.config.constants import WINDOWS_CONFIG

# Configuration for window connections: (toolbar_button_attr, window_attr, [(button_attr, DialogClass), ...])
WINDOW_CONNECTIONS = [
    ("tb_customers", "customer_manager", [("pb_add", CreateCustomerDialog)]),
    ("tb_inventory", "inventory_manager", [("pb_add", AddProductDialog)]),
    ("tb_inventory", "inventory_manager", [("pb_modify", EditProductDialog)]),
]

# Standalone dialog connections: [(toolbar_button_attr, DialogClass), ...]
STANDALONE_DIALOG_CONNECTIONS = [
    ("tb_cash_count", CashCounterDialog),
]

#======================================= MAIN APP ======================================
class MainWindow(qtw.QMainWindow, Ui_MainAppWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tb_vendors.setText("Suppliers")

        # Dynamically create window instances from config
        for attr_name, cls in WINDOWS_CONFIG:
            instance = cls()
            setattr(self, attr_name, instance)
            self.wd_stacked.addWidget(instance)

        self.wd_stacked.setCurrentWidget(self.home)
        self.current_window = self.home

        # connect signals
        self.tb_exit.clicked.connect(self.close)
        self.act_exit.triggered.connect(self.close)

        # Dynamically connect window signals from config
        for tb_attr, win_attr, dialogs in WINDOW_CONNECTIONS:
            tb_button = getattr(self, tb_attr)
            window = getattr(self, win_attr)
            window_connect(tb_button, self.open_window, window)
            window_connect(getattr(window, "pb_window_close"), self.close_window, window)
            for btn_attr, dlg_cls in dialogs:
                dialog_connect(getattr(window, btn_attr), open_dialog, dlg_cls, self)

        # Connect standalone dialogs
        for tb_attr, dlg_cls in STANDALONE_DIALOG_CONNECTIONS:
            tb_button = getattr(self, tb_attr)
            dialog_connect(tb_button, open_dialog, dlg_cls, self)

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