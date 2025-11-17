import frappe

def apply_retainage(doc, method):
    """Apply retainage calculation on Sales Invoice if progress billing."""
    if not getattr(doc, "cm_is_progress_billing", False):
        return
    retainage_pct = getattr(doc, "cm_retainage_percentage", None)
    if not retainage_pct:
        return
    total = 0
    for d in doc.items:
        total += d.amount or 0
    retainage_amount = total * (retainage_pct / 100.0)
    doc.cm_retainage_amount = retainage_amount
    doc.grand_total -= retainage_amount
    doc.outstanding_amount = doc.grand_total
