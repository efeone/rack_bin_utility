from . import __version__ as app_version

app_name = "rack_bin_utility"
app_title = "Rack Bin Utility"
app_publisher = "efeone"
app_description = "Frappe application to maintain Products or any  other related things in an ordered maner"
app_email = "info@efeone.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/rack_bin_utility/css/rack_bin_utility.css"
# app_include_js = "/assets/rack_bin_utility/js/rack_bin_utility.js"

# include js, css files in header of web template
# web_include_css = "/assets/rack_bin_utility/css/rack_bin_utility.css"
# web_include_js = "/assets/rack_bin_utility/js/rack_bin_utility.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "rack_bin_utility/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "rack_bin_utility.utils.jinja_methods",
#	"filters": "rack_bin_utility.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "rack_bin_utility.install.before_install"
# after_install = "rack_bin_utility.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "rack_bin_utility.uninstall.before_uninstall"
# after_uninstall = "rack_bin_utility.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "rack_bin_utility.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"rack_bin_utility.tasks.all"
#	],
#	"daily": [
#		"rack_bin_utility.tasks.daily"
#	],
#	"hourly": [
#		"rack_bin_utility.tasks.hourly"
#	],
#	"weekly": [
#		"rack_bin_utility.tasks.weekly"
#	],
#	"monthly": [
#		"rack_bin_utility.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "rack_bin_utility.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "rack_bin_utility.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "rack_bin_utility.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["rack_bin_utility.utils.before_request"]
# after_request = ["rack_bin_utility.utils.after_request"]

# Job Events
# ----------
# before_job = ["rack_bin_utility.utils.before_job"]
# after_job = ["rack_bin_utility.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"rack_bin_utility.auth.validate"
# ]
