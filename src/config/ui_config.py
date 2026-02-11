from PySide6 import QtWidgets as qtw

class Styles:
    @staticmethod
    def apply(styled_widgets: dict):
        """
        Static method to apply CSS classes to a dictionary of widgets.
        Format: {"class-name": [widget1, widget2, ...]}
        """
        for css_class, widgets in styled_widgets.items():
            for widget in widgets:
                if widget:
                    widget.setProperty("class", css_class)
                    widget.style().polish(widget)

class Totals:
    def __init__(self, map:dict, coin_total:qtw.QLabel, bill_total:qtw.QLabel, grand_total_label:qtw.QLabel):
        self.map = map
        self.coin_total = coin_total
        self.bill_total = bill_total
        self.grand_total_label = grand_total_label

    def set_totals(self):
        pass