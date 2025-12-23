import sys
from PySide6 import QtWidgets as qtw
from PySide6 import QtCore as qtc
from PySide6 import QtGui as qtg

from assets.stylesheets.output_css import get_style


from main import MainApp
# from ui.main_app_window_ui import Ui_MainAppWindow
# from ui.home_window_ui import Ui_HomeWindow
from ui import (main_app_window_ui, home_window_ui, customer_manager_window_ui, user_manager_window_ui,
    vendor_manager_window_ui)
from ui.user_form_dialog_ui import Ui_CreateUserDialog

class HomeWindow(qtw.QWidget, home_window_ui.Ui_HomeWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.lb_welcome.setProperty("class", "welcome-text")


class CustomerManager(qtw.QWidget, customer_manager_window_ui.Ui_CustomerManagerWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # assign class
        self.lb_page_title.setProperty("class", "page-title")
        self.pb_close_page.setProperty("class", "close-button")
        self.le_search_customer.setProperty("class", "line-search-input")
        self.pb_create_customer.setProperty("class", "create-button")
        self.wd_detail_labels.setProperty("class", "wd_detail_view")
        self.lb_customer_table.setProperty("class", "section-title")
        self.lb_transaction_list.setProperty("class", "section-title")
        self.tbl_customers.setProperty("class", "table")
        self.ls_transactions.setProperty("class", "list")

    
class UserManagerWindow(qtw.QWidget, user_manager_window_ui.Ui_UserManagerWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.lb_page_title.setProperty("class", "page-title")
        self.pb_close_page.setProperty("class", "close-button")
        self.le_search_user.setProperty("class", "line-search-input")
        self.pb_create_user.setProperty("class", "create-button")
        self.tbl_users.setProperty("class", "table")
        self.ls_transactions.setProperty("class", "list")
        self.wd_detail_labels.setProperty("class", "wd_detail_view")
        self.lb_user_table.setProperty("class", "section-title")
        self.lb_transaction_list.setProperty("class", "section-title")


class VendorManagerWindow(qtw.QWidget, vendor_manager_window_ui.Ui_VendorManagerWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.lb_page_title.setProperty("class", "page-title")
        self.pb_close_page.setProperty("class", "close-button")
        self.le_search_vendor.setProperty("class", "line-search-input")
        self.pb_create_vendor.setProperty("class", "create-button")
        self.tbl_vendors.setProperty("class", "table")
        self.lb_vendor_table.setProperty("class", "section-title")
        self.ls_transactions.setProperty("class", "list")
        self.lb_transaction_list.setProperty("class", "section-title")
        self.wd_detail_labels.setProperty("class", "wd_detail_view")


class MainAppWindow(qtw.QMainWindow, main_app_window_ui.Ui_MainAppWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.tb_exit.clicked.connect(self.close)
        self.act_exit.triggered.connect(self.close)

        self.home = HomeWindow()
        self.customer_manager = CustomerManager()
        self.user_manager = UserManagerWindow()
        self.vendor_manager = VendorManagerWindow()
        self.current_window = self.home

        self.wd_stacked.addWidget(self.home)
        self.wd_stacked.addWidget(self.customer_manager)
        self.wd_stacked.addWidget(self.user_manager)
        self.wd_stacked.addWidget(self.vendor_manager)

        self.wd_stacked.setCurrentWidget(self.home)
        

        #------------ customer manager window ---------------
        self.tb_customers.clicked.connect(
            lambda checked: self.open_window(self.customer_manager)
        )
        self.customer_manager.pb_close_page.clicked.connect(
            lambda checked: self.close_current_window(self.customer_manager)
        )
        #------------ End customer window -------------------

        #------------ User manager window --------------------
        self.act_user_manager.triggered.connect(
            lambda checked: self.open_window(self.user_manager)
        )
        self.user_manager.pb_close_page.clicked.connect(
            lambda checked: self.close_current_window(self.user_manager)
        )
        #------------ End user window ------------------------

        #------------ Vendor manager window --------------------
        self.tb_vendors.clicked.connect(
            lambda checked: self.open_window(self.vendor_manager)
        )
        self.vendor_manager.pb_close_page.clicked.connect(
            lambda checked: self.close_current_window(self.vendor_manager)
        )
        #------------ End vendor window ------------------------


    def open_window(self, window: qtw.QWidget):
        self.wd_stacked.setCurrentWidget(window)
        self.current_window = window

    def close_current_window(self, window: qtw.QWidget):
        if self.current_window == window:
            self.wd_stacked.setCurrentWidget(self.home)

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)

    # apply styles
    app.setStyleSheet(get_style())

    window = MainAppWindow()
    window.show()
    sys.exit(app.exec())