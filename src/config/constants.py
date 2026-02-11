from decimal import Decimal

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
