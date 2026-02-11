from PySide6 import QtWidgets as qtw
from src.ui.home_window_ui import Ui_HomeWindow

class HomeWindow(qtw.QWidget, Ui_HomeWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.lb_welcome.setProperty("class", "welcome-text")
