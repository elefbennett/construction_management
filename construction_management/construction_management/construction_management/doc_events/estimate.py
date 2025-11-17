import frappe

def recalculate_totals(doc, method):
    """Recalculate estimate totals based on item rows."""
    direct = 0
    overhead = 0
    profit = 0
    for row in getattr(doc, "items", []):
        direct += row.line_direct_cost or 0
        overhead += row.line_overhead or 0
        profit += row.line_profit or 0
    doc.total_direct_cost = direct
    doc.total_overhead = overhead
    doc.total_profit = profit
    doc.grand_total = direct + overhead + profit
