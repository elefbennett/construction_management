import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def after_install():
    """Run after app installation to create custom fields on core DocTypes."""
    custom_fields = {
        "Sales Invoice": [
            dict(
                fieldname="cm_project",
                label="Project",
                fieldtype="Link",
                options="Project",
                insert_after="customer",
            ),
            dict(
                fieldname="cm_is_progress_billing",
                label="Is Progress Billing",
                fieldtype="Check",
                insert_after="cm_project",
            ),
            dict(
                fieldname="cm_retainage_percentage",
                label="Retainage %",
                fieldtype="Percent",
                insert_after="cm_is_progress_billing",
            ),
            dict(
                fieldname="cm_retainage_amount",
                label="Retainage Amount",
                fieldtype="Currency",
                insert_after="cm_retainage_percentage",
                read_only=1,
            ),
        ]
    }
    create_custom_fields(custom_fields, update=True)
