from decimal import Decimal

amount = {
    "penny": Decimal("0.01"),
    "nickel": Decimal("0.05"),
    "dime": Decimal("0.10"),
    "quarter": Decimal("0.25"),
    "one": Decimal("1.00"),
    "five": Decimal("5.00"),
    "ten": Decimal("10.00"),
    "twenty": Decimal("20.00"),
    "fifty": Decimal("50.00"),
}

count = {
    "penny": 13,
    "nickel": 20,
    "dime": 15,
    "quarter": 10,
    "one": 26,
    "five": 0,
    "ten": 2,
    "twenty": 2,
    "fifty": 0,
}

total = Decimal("10")

for dollar in count:
    total += amount[dollar] * count[dollar]

starting_cash = Decimal("25")

remove_amount = total - starting_cash
print(f"{total} - {starting_cash} = $ {remove_amount} cash to remove")

total_removed = 0
print(f"\n$ {remove_amount}")

for c, a in zip(reversed(count), reversed(amount)):
    if count[c] > 0:
        print(f"{c} in drawer: {count[c]}")

        remove_count = int(remove_amount / amount[c])
        actual_remove_count = min(remove_count, count[c])
        amount_removed = actual_remove_count * amount[c]
        total_removed += amount_removed

        print(f"{c} to remove: {remove_count}")
        print(f"{c} removed: {actual_remove_count}")
        print(f"amount_removed: $ {amount_removed}")
        
        remove_amount -= remove_count * amount[c]

        print(f"$ {remove_amount} remaining\n")



