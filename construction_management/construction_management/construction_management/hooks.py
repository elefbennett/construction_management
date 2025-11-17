from . import __version__ as app_version

app_name = "construction_management"
app_title = "Construction Management"
app_publisher = "Bennett CnD"
app_description = "Construction management tools for ERPNext"
app_email = "admin@example.com"
app_license = "MIT"

after_install = "construction_management.install.after_install"

# Document event hooks
# Key: DocType, value: events dictionary mapping event name to dotted path



doc_events = {
    "CM Time Entry": {
        "validate": "construction_management.doc_events.time_entry.validate_time_entry",
        "on_submit": "construction_management.doc_events.time_entry.on_submit_time_entry",
    },
    "Sales Invoice": {
        "validate": "construction_management.doc_events.invoice.apply_retainage",
    },
    "CM Estimate": {
        "validate": "construction_management.doc_events.estimate.recalculate_totals",
    },
}

# No fixtures defined yet; custom fields are created via install.py
fixtures = []
