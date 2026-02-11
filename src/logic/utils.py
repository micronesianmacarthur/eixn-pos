from PySide6 import QtWidgets as qtw

def open_dialog(dialog_class, parent=None):
    """
    Utility function to instantiate and execute a QDialog.
    """
    dialog = dialog_class(parent=parent)
    return dialog.exec()
