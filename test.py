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
from ui.user_form_dialog_ui import Ui_UserFormDialog
from ui.customer_form_dialog_ui import Ui_CustomerFormDialog
from ui.vender_form_dialog_ui import Ui_VendorFormDialog

class HomeWindow(qtw.QWidget, home_window_ui.Ui_HomeWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.lb_welcome.setProperty("class", "welcome-text")


class UserFormDialog(qtw.QDialog, Ui_UserFormDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_UserFormDialog()
        self.ui.setupUi(self)

        self.charge_options = {
            0: [self.ui.lb_system_limit, self.ui.chk_system_limit],
            1: [self.ui.lb_custom_limit, self.ui.le_custom_limit],
            2: [self.ui.lb_disable_limit, self.ui.chk_disable_limit],
        }

        # set default value
        self.ui.cb_charge_account.setCurrentText("Disabled")
        self.ui.cb_status.setCurrentText("Active")
        self.ui.chk_system_limit.setText("$50.00")
        self.disable_charge_options()
        
        self.ui.lb_form_title.setProperty("class", "dialog-title")
        self.ui.lb_username.setProperty("class", "inline-label")
        self.ui.le_username.setProperty("class", "inline-lineEdit")
        self.ui.lb_first_name.setProperty("class", "inline-label")
        self.ui.le_first_name.setProperty("class", "inline-lineEdit")
        self.ui.lb_last_name.setProperty("class", "inline-label")
        self.ui.le_last_name.setProperty("class", "inline-lineEdit")
        self.ui.lb_phone.setProperty("class", "inline-label")
        self.ui.le_phone.setProperty("class", "inline-lineEdit")
        self.ui.lb_email.setProperty("class", "inline-label")
        self.ui.le_email.setProperty("class", "inline-lineEdit")
        self.ui.lb_address.setProperty("class", "inline-label")
        self.ui.le_address.setProperty("class", "inline-lineEdit")

        self.ui.lb_role.setProperty("class", "inline-label")
        self.ui.cb_role.setProperty("class", "inline-combobox")
        self.ui.lb_status.setProperty("class", "inline-label")
        self.ui.cb_status.setProperty("class", "inline-combobox")
        self.ui.lb_charge_account.setProperty("class", "inline-label")
        self.ui.cb_charge_account.setProperty("class", "inline-combobox")
        self.ui.lb_system_limit.setProperty("class", "checkbox-label")
        self.ui.chk_system_limit.setProperty("class", "inline-checkbox")
        self.ui.lb_custom_limit.setProperty("class", "inline-label")
        self.ui.le_custom_limit.setProperty("class", "inline-lineEdit")
        self.ui.chk_disable_limit.setProperty("class", "inline-checkbox")
        self.ui.lb_pin.setProperty("class", "inline-label")
        self.ui.le_pin.setProperty("class", "inline-lineEdit")
        self.ui.lb_password.setProperty("class", "inline-label")
        self.ui.le_password.setProperty("class", "inline-lineEdit")
        self.ui.lb_password_2.setProperty("class", "inline-label")
        self.ui.le_password_2.setProperty("class", "inline-lineEdit")

        self.ui.pb_save_user.setProperty("class", "create-button")
        self.ui.pb_close_form.setProperty("class", "close-button")


        self.ui.le_pin.setEchoMode(qtw.QLineEdit.Password)
        self.ui.le_password.setEchoMode(qtw.QLineEdit.Password)
        self.ui.le_password_2.setEchoMode(qtw.QLineEdit.Password)
    
        # connect signals
        self.ui.pb_close_form.clicked.connect(self.close)
        self.ui.cb_charge_account.currentTextChanged.connect(lambda checked: self.update_charge_options())
        self.ui.chk_system_limit.toggled.connect(lambda checked: self.update_charge_options(0))
        self.ui.chk_disable_limit.toggled.connect(lambda checked: self.update_charge_options(2))

    # custom methods
    def disable_charge_options(self):
        for key, value in self.charge_options.items():
            for widget in value:
                widget.setDisabled(True)

    def update_charge_options(self, sender_key=None):
        is_checked = False
        if sender_key is not None:
            sender = self.charge_options[sender_key][1]
            for key, value in self.charge_options.items():
                if sender.isChecked():
                    # disable the others
                    if sender_key == key:
                        pass
                    else:
                        for widget in value:
                            widget.setDisabled(True)
                else:
                    for widget in value:
                        widget.setDisabled(False)
        else:
            for key, value in self.charge_options.items():
                for widget in value:
                    if self.ui.cb_charge_account.currentText() == "Disabled":
                        widget.setDisabled(True)
                    else:
                        widget.setDisabled(False)


class CustomerFormDialog(qtw.QDialog,Ui_CustomerFormDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_CustomerFormDialog()
        self.ui.setupUi(self)

        # set variable
        self.charge_options = {
            0: [self.ui.lb_system_limit, self.ui.chk_system_limit],
            1: [self.ui.lb_custom_limit, self.ui.le_custom_limit],
            2: [self.ui.lb_disable_limit, self.ui.chk_disable_limit],
        }

        # set default value
        self.ui.le_custom_limit.setPlaceholderText("0.00")
        self.disable_charge_options()

        # assign class property
        self.ui.lb_form_title.setProperty("class", "dialog-title")
        self.ui.pb_save_customer.setProperty("class", "create-button")
        self.ui.pb_close_form.setProperty("class", "close-button")
        self.ui.lb_first_name.setProperty("class", "inline-label")
        self.ui.le_first_name.setProperty("class", "inline-lineEdit")
        self.ui.lb_last_name.setProperty("class", "inline-label")
        self.ui.le_last_name.setProperty("class", "inline-lineEdit")
        self.ui.lb_company.setProperty("class", "inline-label")
        self.ui.le_company.setProperty("class", "inline-lineEdit")
        self.ui.lb_phone.setProperty("class", "inline-label")
        self.ui.le_phone.setProperty("class", "inline-lineEdit")
        self.ui.lb_email.setProperty("class", "inline-label")
        self.ui.le_email.setProperty("class", "inline-lineEdit")
        self.ui.lb_address.setProperty("class", "inline-label")
        self.ui.le_address.setProperty("class", "inline-lineEdit")
        self.ui.lb_charge_account.setProperty("class", "inline-label")
        self.ui.cb_charge_account.setProperty("class", "inline-combobox")
        self.ui.lb_system_limit.setProperty("class", "checkbox-label")
        self.ui.chk_system_limit.setProperty("class", "inline-checkbox")
        self.ui.lb_custom_limit.setProperty("class", "inline-label")
        self.ui.le_custom_limit.setProperty("class", "inline-lineEdit")
        self.ui.lb_disable_limit.setProperty("class", "checkbox-label")
        self.ui.chk_disable_limit.setProperty("class", "inline-checkbox")

        # connect signal
        self.ui.pb_close_form.clicked.connect(self.close)
        # disable custom limit when system limit is checked
        self.ui.chk_system_limit.toggled.connect(lambda checked: self.update_charge_options(0))
        self.ui.chk_disable_limit.toggled.connect(lambda checked: self.update_charge_options(2))
        self.ui.cb_charge_account.currentTextChanged.connect(lambda checked: self.update_charge_options())

    def disable_charge_options(self):
        for key, value in self.charge_options.items():
            for widget in value:
                widget.setDisabled(True)

    def update_charge_options(self, sender_key=None):
        is_checked = False
        if sender_key is not None:
            sender = self.charge_options[sender_key][1]
            for key, value in self.charge_options.items():
                if sender.isChecked():
                    # disable the others
                    if sender_key == key:
                        pass
                    else:
                        for widget in value:
                            widget.setDisabled(True)
                else:
                    for widget in value:
                        widget.setDisabled(False)
        else:
            for key, value in self.charge_options.items():
                for widget in value:
                    if self.ui.cb_charge_account.currentText() == "Disabled":
                        widget.setDisabled(True)
                    else:
                        widget.setDisabled(False)

        # if self.ui.chk_system_limit.isChecked():
        #     self.system_limit_enabled()
        # else:
        #     self.system_limit_disabled()

class VendorFormDialog(qtw.QDialog, Ui_VendorFormDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_VendorFormDialog()
        self.ui.setupUi(self)

        # assign class
        self.ui.lb_form_title.setProperty("class", "dialog-title")
        self.ui.lb_company_name.setProperty("class", "inline-label")
        self.ui.le_company_name.setProperty("class", "inline-lineEdit")
        self.ui.lb_phone.setProperty("class", "inline-label")
        self.ui.le_phone.setProperty("class", "inline-lineEdit")
        self.ui.lb_email.setProperty("class", "inline-label")
        self.ui.le_email.setProperty("class", "inline-lineEdit")
        self.ui.lb_address.setProperty("class", "inline-label")
        self.ui.le_address.setProperty("class", "inline-lineEdit")
        self.ui.pb_save_vendor.setProperty("class", "create-button")
        self.ui.pb_close.setProperty("class", "close-button")

        # connect signal
        self.ui.pb_close.clicked.connect(self.close)


class CustomerManager(qtw.QWidget, customer_manager_window_ui.Ui_CustomerManagerWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # set default
        self.pb_make_payment.setText("Receive Payment")
        
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

        # set default
        self.pb_make_payment.setText("Receive Payment")

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

        # set default value
        self.pb_make_payment.setText("Make Payment")
        
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
        # create customer dialog
        self.customer_manager.pb_create_customer.clicked.connect(
            lambda checked: self.show_dialog(CustomerFormDialog())
        )
        # edit customer dialog
        edit_customer_dialog = CustomerFormDialog()
        edit_customer_dialog.setWindowTitle("Edit Customer Form")
        edit_customer_dialog.ui.lb_form_title.setText("Edit Customer")
        self.customer_manager.pb_edit_customer.clicked.connect(
            lambda checked: self.show_dialog(edit_customer_dialog)
        )

        #------------ End customer window -------------------

        #------------ User manager window --------------------
        self.act_user_manager.triggered.connect(
            lambda checked: self.open_window(self.user_manager)
        )
        self.user_manager.pb_close_page.clicked.connect(
            lambda checked: self.close_current_window(self.user_manager)
        )
        # create user dialog
        self.user_manager.pb_create_user.clicked.connect(
            lambda checked: self.show_dialog(UserFormDialog())
        )
        # edit user form
        edit_user_dialog = UserFormDialog()
        edit_user_dialog.setWindowTitle("Edit User Form")
        edit_user_dialog.ui.lb_form_title.setText("Edit User")
        self.user_manager.pb_edit_user.clicked.connect(
            lambda checked: self.show_dialog(edit_user_dialog)
        )
        #------------ End user window ------------------------

        #------------ Vendor manager window --------------------
        self.tb_vendors.clicked.connect(
            lambda checked: self.open_window(self.vendor_manager)
        )
        self.vendor_manager.pb_close_page.clicked.connect(
            lambda checked: self.close_current_window(self.vendor_manager)
        )
        # create vendor dialog
        self.vendor_manager.pb_create_vendor.clicked.connect(
            lambda checked: self.show_dialog(VendorFormDialog())
        )
        # edit vendor dialog
        edit_vendor_dialog = VendorFormDialog()
        edit_vendor_dialog.setWindowTitle("Edit Vendor Form")
        edit_vendor_dialog.ui.lb_form_title.setText("Edit Vendor")
        self.vendor_manager.pb_edit_vendor.clicked.connect(
            lambda checked: self.show_dialog(edit_vendor_dialog)
        )
        #------------ End vendor window ------------------------


    def open_window(self, window: qtw.QWidget):
        self.wd_stacked.setCurrentWidget(window)
        self.current_window = window

    def close_current_window(self, window: qtw.QWidget):
        if self.current_window == window:
            self.wd_stacked.setCurrentWidget(self.home)

    def show_dialog(self, dialog):
        """Opens given dialog window"""
        self.custom_dialog = dialog
        self.custom_dialog.exec()

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)

    # apply styles
    app.setStyleSheet(get_style())

    window = MainAppWindow()
    window.show()
    sys.exit(app.exec())