from PySide6 import QtWidgets as qtw

def open_dialog(dialog_class, parent=None):
    """
    Utility function to instantiate and execute a QDialog.
    """
    dialog = dialog_class(parent=parent)
    return dialog.exec()

def navigate_stacked_widget(stacked_widget: qtw.QStackedWidget, direction: int) -> int:
    """
    Navigates a QStackedWidget by a given direction (e.g., 1 for next, -1 for previous).
    Returns the new index if navigation was successful, otherwise returns the current index.
    """
    new_index = stacked_widget.currentIndex() + direction
    if 0 <= new_index < stacked_widget.count():
        stacked_widget.setCurrentIndex(new_index)
        return new_index
    return stacked_widget.currentIndex()

def dialog_connect(button, function, ui_class, parent=None):
    button.clicked.connect(lambda: function(ui_class, parent))

def window_connect(button, method, window):
    button.clicked.connect(lambda: method(window))
    