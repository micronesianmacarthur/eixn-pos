from decimal import Decimal
from typing import List, Tuple, Dict

def calculate_totals(currency_counts: Dict[str, int], currency_defs: List[Tuple[Decimal, str, str]]) -> Dict[str, Decimal]:
    """
    Calculates category totals and grand total based on currency counts.
    Returns a dictionary with 'bills', 'coins', and 'grand_total'.
    """
    totals = {"bills": Decimal("0"), "coins": Decimal("0")}
    
    for val, key, cat in currency_defs:
        count = currency_counts.get(key, 0)
        totals[cat] += count * val
        
    totals["grand_total"] = totals["bills"] + totals["coins"]
    return totals

def calculate_cash_removal(remove_amount: Decimal, available_counts: Dict[str, int], currency_defs: List[Tuple[Decimal, str, str]]) -> Dict[str, any]:
    """
    Performs a greedy calculation to determine how much of each denomination to remove.
    Returns a dictionary mapping currency keys to counts taken and category/grand totals.
    """
    results = {
        "counts": {},
        "amounts": {},
        "category_totals": {"bills": Decimal("0"), "coins": Decimal("0")},
        "total_removed": Decimal("0")
    }
    
    remaining_to_remove = remove_amount
    
    for val, key, cat in currency_defs:
        available = available_counts.get(key, 0)
        
        # Greedy calculation
        count_taken = min(int(remaining_to_remove / val), available)
        amount_taken = count_taken * val
        
        remaining_to_remove -= amount_taken
        results["total_removed"] += amount_taken
        results["category_totals"][cat] += amount_taken
        results["counts"][key] = count_taken
        results["amounts"][key] = amount_taken
        
    return results
