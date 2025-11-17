import frappe

def validate_time_entry(doc, method):
    """Ensure mandatory fields and basic validation for CM Time Entry."""
    if not doc.cost_code:
        frappe.throw("Cost Code is required.")
    if not doc.project:
        frappe.throw("Project is required.")
    if (doc.hours or 0) <= 0:
        frappe.throw("Hours must be greater than zero.")

def on_submit_time_entry(doc, method):
    """Update project budget actuals when a time entry is submitted."""
    if not doc.project or not doc.cost_code:
        return
    budgets = frappe.get_all(
        "CM Project Budget",
        filters={"project": doc.project},
        limit=1,
        pluck="name",
    )
    if not budgets:
        return
    budget_doc = frappe.get_doc("CM Project Budget", budgets[0])
    # Find or create the budget line
    line = None
    for l in budget_doc.lines:
        if l.cost_code == doc.cost_code:
            line = l
            break
    if not line:
        line = budget_doc.append("lines", {})
        line.cost_code = doc.cost_code
        line.description = doc.cost_code
    line.qty_actual = (line.qty_actual or 0) + (doc.hours or 0)
    line.cost_actual = (line.cost_actual or 0) + (doc.amount or 0)
    budget_doc.save()
