import sys
from PySide6 import QtWidgets as qtw
from PySide6 import QtCore as qtc
from PySide6 import QtGui as qtg

from assets.stylesheets.output_css import get_style

from ui.main_app_window_ui import Ui_MainAppWindow
from ui.home_window_ui import Ui_HomeWindow
from ui.customer_manager_ui import Ui_CustomerManager


class CustomerManager(qtw.QWidget, Ui_CustomerManager):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # assign class
        self.lb_window_title.setProperty("class", "page-title")
        self.pb_window_close.setProperty("class", "close-button")
        self.pb_add.setProperty("class", "inline-button-text")
        self.pb_modify.setProperty("class", "inline-button-text")
        self.pb_find.setProperty("class", "inline-button-text")
        self.pb_filter.setProperty("class", "inline-button-text")
        self.pb_new_sale.setProperty("class", "inline-button-text")
        self.pb_delete.setProperty("class", "inline-button-text")


class HomeWindow(qtw.QWidget, Ui_HomeWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.lb_welcome.setProperty("class", "welcome-text")


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