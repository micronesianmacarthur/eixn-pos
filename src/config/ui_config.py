class Styles:
    def __init__(self, styled_widgets:dict):
        self.styled_widgets = styled_widgets

    def set_styles(self):
        for css_class, widgets in self.styled_widgets.items():
            for widget in widgets:
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