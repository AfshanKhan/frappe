
from frappe.utils import cint
import frappe

def execute():
	frappe.reload_doctype("Dropbox Settings")
	check_dropbox_enabled = cint(frappe.db.get_value("Dropbox Settings", None, "enabled"))
	if  check_dropbox_enabled == 1:
		frappe.db.set_value("Dropbox Settings", None, 'file_backup', 1)
