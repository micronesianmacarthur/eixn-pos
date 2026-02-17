from PySide6 import QtWidgets as qtw
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPainter, QIcon
from src.config.ui_config import Styles


class ImageBrowser:
    def __init__(self, parent=None):
        self.file_dialog = qtw.QFileDialog(parent)
        self.apply_widget_styles = self._apply_widget_styles

    def _apply_widget_styles(self, widgets_dict):
        Styles.apply(widgets_dict)

    def recolor_icon(self, widget, color):
        icon = widget.icon()
        if icon.isNull():
            return
        pixmap = icon.pixmap(16, 16)
        painter = QPainter(pixmap)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(pixmap.rect(), color)
        painter.end()
        widget.setIcon(QIcon(pixmap))

    def browse_image(self, line_edit):
        self.file_dialog.setWindowTitle("Select Image")
        self.file_dialog.setNameFilter("Images (*.png *.jpg *.jpeg *.bmp)")

        # Find QFileDialog internal widgets for styling
        file_type_combo = self.file_dialog.findChild(qtw.QComboBox, "fileTypeCombo")
        look_in_combo = self.file_dialog.findChild(qtw.QComboBox, "lookInCombo")
        file_name_edit = self.file_dialog.findChild(qtw.QLineEdit, "fileNameEdit")
        button_box = self.file_dialog.findChild(qtw.QDialogButtonBox, "buttonBox")

        # Find toolbar buttons and recolor their icons
        toolbar_buttons = [
            self.file_dialog.findChild(qtw.QToolButton, name)
            for name in [
                "backButton",
                "forwardButton",
                "toParentButton",
                "newFolderButton",
                "listModeButton",
                "detailModeButton",
            ]
        ]
        for button in toolbar_buttons:
            if button and button.icon():
                self.recolor_icon(button, QColor(Qt.green))

        # Find buttons by text since they lack object names
        open_button = None
        cancel_button = None
        if button_box:
            buttons = button_box.findChildren(qtw.QPushButton)
            open_button = next((b for b in buttons if b.text() == "&Open"), None)
            cancel_button = next((b for b in buttons if b.text() == "Cancel"), None)
            if open_button:
                open_button.setObjectName("openButton")
            if cancel_button:
                cancel_button.setObjectName("cancelButton")

        open_button.setFixedHeight(25)
        cancel_button.setFixedHeight(25)
        file_name_edit.setFixedHeight(25)
        file_type_combo.setFixedHeight(25)
        look_in_combo.setFixedHeight(25)

        # Apply styles similar to dialog widgets
        file_widgets_to_style = {
            "combobox": (
                [file_type_combo, look_in_combo]
                if file_type_combo and look_in_combo
                else []
            ),
            "lineedit": [file_name_edit] if file_name_edit else [],
            "close-button": [cancel_button],
            "new-button": [open_button],
        }
        self.apply_widget_styles(file_widgets_to_style)

        if self.file_dialog.exec():
            file_path = self.file_dialog.selectedFiles()[0]
            line_edit.setText(file_path)

        # # Debug: Inspect widgets (remove after testing)
        # for widget in self.file_dialog.findChildren(qtw.QWidget):
        #     print(widget.objectName(), type(widget).__name__)

        # # Inspect buttonBox children
        # if button_box:
        #     for button in button_box.findChildren(qtw.QPushButton):
        #         print(f"Button: {button.objectName() or 'Unnamed'} - Text: '{button.text()}'")
