from decimal import Decimal
from src.views.home_window import HomeWindow
from src.views.customer_manager import CustomerManager
from src.views.inventory_manager import InventoryManager
from src.dialogs.products import AddProductDialog
from src.dialogs.create_customer import CreateCustomerDialog

CURRENCY_DEFS = [
    (Decimal("100.00"), "hundreds", "bills"),
    (Decimal("50.00"), "fifties", "bills"),
    (Decimal("20.00"), "twenties", "bills"),
    (Decimal("10.00"), "tens", "bills"),
    (Decimal("5.00"), "fives", "bills"),
    (Decimal("2.00"), "twos", "bills"),
    (Decimal("1.00"), "ones", "bills"),
    (Decimal("2.00"), "two_dollars", "coins"),
    (Decimal("1.00"), "dollars", "coins"),
    (Decimal("0.50"), "half_dollars", "coins"),
    (Decimal("0.25"), "quarters", "coins"),
    (Decimal("0.10"), "dimes", "coins"),
    (Decimal("0.05"), "nickels", "coins"),
    (Decimal("0.01"), "pennies", "coins"),
]

# Configuration for windows: (attribute_name, Class)
WINDOWS_CONFIG = [
    ("home", HomeWindow),
    ("customer_manager", CustomerManager),
    ("inventory_manager", InventoryManager),
]
