import sys
import os

# Add the project root to sys.path to resolve 'src' imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from PySide6 import QtWidgets as qtw
from src.assets.stylesheets.output_qss import get_style

# Import the dialog you want to test
from src.dialogs.cash_counter import CashCounterDialog
from src.dialogs.products import AddProductDialog, EditProductDialog
from src.dialogs.create_customer import CreateCustomerDialog
from src.dialogs.categories_dialog import CategoriesDialog
from src.dialogs.find import FindDialog
from src.dialogs.stock_types_dialog import StockTypesDialog

def test_dialog():
    app = qtw.QApplication(sys.argv)
    
    # Apply global styles so the dialog looks correct
    app.setStyleSheet(get_style())
    
    # Instantiate the dialog
    # dialog = FindDialog()
    dialog = AddProductDialog()
    # dialog = CashCounterDialog()
    # dialog = CreateCustomerDialog()
    # dialog = CategoriesDialog()
    # dialog = EditProductDialog(product_id="12335654")
    # dialog = StockTypesDialog()
    
    # Show it and exit
    dialog.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    test_dialog()
