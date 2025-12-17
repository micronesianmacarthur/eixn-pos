import sys
from PySide6 import QtWidgets as qtw
from PySide6 import QtCore as qtc
from PySide6 import QtGui as qtg

from compiled.main_app_window_ui import Ui_MainAppWindow
from compiled.users_list_window_ui import Ui_UsersListWindow
from compiled.customers_list_window_ui import Ui_CustomersListWindow
from compiled.home_window_ui import Ui_HomeWindow
from compiled.new_user_dialog_ui import Ui_NewUserDialog
from compiled.new_customer_dialog_ui import Ui_NewCustomerDialog
from compiled.new_vendor_dialog_ui import Ui_NewVendorDialog
from compiled.vendors_list_window_ui import Ui_VendorsListWindow

# from compiled.sale_screen_ui import Ui_SaleScreen


# class SaleScreen(qtw.QWidget, Ui_SaleScreen):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)

class VendorsListWindow(qtw.QWidget, Ui_VendorsListWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class NewVendorDialog(qtw.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_NewVendorDialog()
        self.ui.setupUi(self)

        self.ui.pb_cancel.clicked.connect(self.reject)
        

class NewCustomerDialog(qtw.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_NewCustomerDialog()
        self.ui.setupUi(self)

        self.ui.pb_cancel.clicked.connect(self.reject)
        
class NewUserDialog(qtw.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_NewUserDialog()
        self.ui.setupUi(self)

        self.ui.pb_cancel.clicked.connect(self.reject)

        self.ui.le_pin.setEchoMode(qtw.QLineEdit.Password)
        self.ui.le_password.setEchoMode(qtw.QLineEdit.Password)
        self.ui.le_password2.setEchoMode(qtw.QLineEdit.Password)
        
        
class HomeWindow(qtw.QWidget, Ui_HomeWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        

class UsersListWindow(qtw.QWidget, Ui_UsersListWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class CustomersListWindow(qtw.QWidget, Ui_CustomersListWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        

class MainApp(qtw.QMainWindow, Ui_MainAppWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.home = HomeWindow()
        self.users_list_window = UsersListWindow()
        self.customers_list_window = CustomersListWindow()
        self.vendors_list_window = VendorsListWindow()

        self.wd_stacked.addWidget(self.home)
        self.wd_stacked.addWidget(self.users_list_window)
        self.wd_stacked.addWidget(self.customers_list_window)
        self.wd_stacked.addWidget(self.vendors_list_window)

        self.current_window = self.home

        self.open_window(self.home)

        # connect menu buttons
        self.tb_exit.clicked.connect(self.close)
        self.act_exit.triggered.connect(self.close)
        #----------- customer listing page ------------------
        self.tb_customers.clicked.connect(
            lambda checked: self.open_window(self.customers_list_window)
        )
        self.customers_list_window.pb_customer_close.clicked.connect(
            lambda checked: self.close_current_window(self.customers_list_window)
        )
        self.customers_list_window.pb_create_customer.clicked.connect(
            lambda checked: self.show_dialog(NewCustomerDialog())
        )
        edit_customer_dialog = NewCustomerDialog()
        edit_customer_dialog.setWindowTitle("Edit Customer Form")
        edit_customer_dialog.ui.lb_page_title.setText("Edit Customer")
        self.customers_list_window.pb_edit_customer.clicked.connect(
            lambda checked: self.show_dialog(edit_customer_dialog)
        )
        #------------ End customer listing page ----------------

        #------------ User listing page ----------------------
        self.act_user_manager.triggered.connect(
            lambda checked: self.open_window(self.users_list_window)
        )
        self.users_list_window.pb_user_close.clicked.connect(
            lambda checked: self.close_current_window(self.users_list_window)
        )
        self.users_list_window.pb_create_user.clicked.connect(
            lambda checked: self.show_dialog(NewUserDialog())
        )
        edit_user_dialog = NewUserDialog()
        edit_user_dialog.setWindowTitle("Edit User Form")
        edit_user_dialog.ui.lb_page_title.setText("Edit User")
        self.users_list_window.pb_edit_user.clicked.connect(
            lambda checked: self.show_dialog(edit_user_dialog)
        )
        #------------ End user listing page -----------------

        #------------ Vendors listing page ------------------
        self.tb_vendors.clicked.connect(
            lambda checked: self.open_window(self.vendors_list_window)
        )
        self.vendors_list_window.pb_page_close.clicked.connect(
            lambda checked: self.close_current_window(self.vendors_list_window)
        )
        self.vendors_list_window.pb_create_vendor.clicked.connect(
            lambda checked: self.show_dialog(NewVendorDialog())
        )
        edit_vendor_dialog = NewVendorDialog()
        edit_vendor_dialog.setWindowTitle("Edit Vendor Form")
        edit_vendor_dialog.ui.lb_page_title.setText("Edit Vendor")
        self.vendors_list_window.pb_edit_vendor.clicked.connect(
            lambda checked: self.show_dialog(edit_vendor_dialog)
        )
        #-------------- End vendors listing -------------------

        
    def open_window(self, window: qtw.QWidget):
        """Closes current window and opens the specified window."""
        # find index of window
        index = self.wd_stacked.indexOf(window)

        # hide current window
        if self.current_window:
            self.current_window.hide()

        # show new window
        window.show()
        self.current_window = window

        self.wd_stacked.setCurrentWidget(window)

    def close_current_window(self, window_to_close: qtw.QWidget):
        """Closes the given window by switching back to home screen."""
        if self.wd_stacked.currentWidget() is window_to_close:
            self.wd_stacked.setCurrentWidget(self.home)

    def show_dialog(self, dialog):
        """Opens given dialog window."""
        self.custom_dialog = dialog
        self.custom_dialog.exec()
        

if __name__ == '__main__':
     app = qtw.QApplication(sys.argv)
     window = MainApp()
     window.show()
     sys.exit(app.exec())