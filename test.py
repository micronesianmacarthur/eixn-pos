import sys
from PySide6 import QtWidgets as qtw
from PySide6 import QtCore as qtc
from PySide6 import QtGui as qtg

from assets.stylesheets.output_css import get_style


from main import MainApp
# from ui.main_app_window_ui import Ui_MainAppWindow
# from ui.home_window_ui import Ui_HomeWindow
from ui import main_app_window_ui, home_window_ui, customer_manager_window_ui


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
        self.lb_customer_win_title.setProperty("class", "page-title")
        self.pb_customer_win_close.setProperty("class", "close-button")
        self.pb_search_customer.setProperty("class", "line-search-button")
        self.le_search_customer.setProperty("class", "line-search-input")
        self.pb_create_customer.setProperty("class", "create-button")
        self.wd_detail_view.setProperty("class", "wd_detail_view")

class MainAppWindow(qtw.QMainWindow, main_app_window_ui.Ui_MainAppWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.tb_exit.clicked.connect(self.close)
        self.act_exit.triggered.connect(self.close)

        self.home = HomeWindow()
        self.customer_manager = CustomerManager()
        self.current_window = self.home

        self.wd_stacked.addWidget(self.home)
        self.wd_stacked.addWidget(self.customer_manager)

        self.wd_stacked.setCurrentWidget(self.home)
        self.tb_customers.clicked.connect(
            lambda checked: self.open_window(self.customer_manager)
        )

        #------------ customer manager window ---------------
        self.customer_manager.pb_customer_win_close.clicked.connect(
            lambda checked: self.close_current_window(self.customer_manager)
        )
        #------------ End customer window -------------------


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