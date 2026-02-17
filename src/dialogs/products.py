from PySide6 import QtWidgets as qtw
from PySide6.QtGui import QPixmap

from src.ui.add_product_ui import Ui_AddProductDialog
from src.config.ui_config import Styles
from src.dialogs.categories_dialog import CategoriesDialog
from src.dialogs.stock_types_dialog import StockTypesDialog
from src.dialogs.image_browser import ImageBrowser

from src.logic.utils import open_dialog, dialog_connect

import os
from PIL import Image
from io import BytesIO


class AddProductDialog(qtw.QDialog, Ui_AddProductDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_AddProductDialog()
        self.ui.setupUi(self)
        self.image_browser = ImageBrowser(self)

        self.image_label = qtw.QLabel(self.ui.frame_product_image)
        self.image_label.setGeometry(25, 25, 100, 100)
        self.image_label.setScaledContents(True)
        self.image_label.hide()

        # assign class
        widgets_to_style = {
            "group-box bold": [
                self.ui.grp_general,
                self.ui.grp_price,
                self.ui.grp_image,
            ],
            "dialog-title": [self.ui.lb_dialog_title],
            "dialog-button": [self.ui.pb_product_save, self.ui.pb_product_cancel],
            "dialog-menu": [self.ui.dlg_menu],
            "small-text": [
                self.ui.created_label,
                self.ui.updated_label,
                self.ui.product_id_label,
                self.ui.qty_available_label,
                self.ui.qty_on_order_label,
                self.ui.lb_created,
                self.ui.lb_updated,
                self.ui.lb_product_id,
                self.ui.lb_qty_available,
                self.ui.lb_qty_on_order,
            ],
            "small-header": [self.ui.lb_information],
            "combobox": [
                self.ui.cb_category,
                self.ui.cb_supplier,
                self.ui.cb_stock_type,
            ],
            "spinbox": [
                self.ui.sb_quantity,
                self.ui.sb_reorder_level,
                self.ui.dbl_cost,
                self.ui.dbl_price,
            ],
            "secondary-button": [self.ui.pb_browse],
            "new-button": [
                self.ui.pb_supplier_add,
                self.ui.pb_category_add,
                self.ui.pb_stock_type_add,
            ],
            "display-only": [self.ui.lb_markup_margin, self.ui.lb_suggested_price],
        }

        # connect signals
        self.apply_widget_styles(widgets_to_style)
        self.ui.pb_product_cancel.clicked.connect(self.close)
        dialog_connect(self.ui.pb_category_add, open_dialog, CategoriesDialog, self)
        dialog_connect(self.ui.pb_stock_type_add, open_dialog, StockTypesDialog, self)
        self.ui.pb_browse.clicked.connect(
            lambda: self.image_browser.browse_image(self.ui.le_select_image)
        )

        self.ui.le_select_image.textChanged.connect(self.update_image_display)

    def apply_widget_styles(self, widgets_dict):
        Styles.apply(widgets_dict)

    def update_image_display(self):
        path = self.ui.le_select_image.text()
        if os.path.isfile(path) and path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            img = Image.open(path)
            img = img.resize((100, 100), Image.Resampling.LANCZOS)
            buffer = BytesIO()
            img.save(buffer, format='PNG')
            pixmap = QPixmap()
            pixmap.loadFromData(buffer.getvalue())
            self.image_label.setPixmap(pixmap)
            self.image_label.show()
            self.ui.lb_no_image.hide()
        else:
            self.image_label.clear()
            self.image_label.hide()
            self.ui.lb_no_image.show()


class EditProductDialog(AddProductDialog):
    def __init__(self, parent=None, product_id=None):
        super().__init__(parent)
        self.product_id = product_id
        # Customize for editing
        self.ui.lb_dialog_title.setText("Edit Product")
        self.ui.pb_product_save.setText("Save")
        # Add logic to load existing product data using product_id
        if product_id:
            self.load_product_data(product_id)

    def load_product_data(self, product_id):
        # Implement loading logic from database or source
        # Example: Fetch product details and populate fields
        self.ui.lb_product_id.setText(product_id)

    # Override save method if needed
    def save_product(self):
        # Update instead of add
        pass
