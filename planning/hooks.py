# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "planning"
app_title = "planning"
app_publisher = "nishta"
app_description = "Project Management System(PMS)"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "vaiju@nishta.in"
app_version = "0.0.1"

# Includes in <head>
# ------------------

# app_include_js = "assets/js/jquery.switchButton.js"
# app_include_css = "assets/css/jquery.switchButton.css"
app_include_css = "assets/css/on_off_button.css"

# include js, css files in header of desk.html
# app_include_css = "/assets/planning/css/planning.css"
# app_include_js = "/assets/planning/js/planning.js"

# include js, css files in header of web template
# web_include_css = "/assets/planning/css/planning.css"
# web_include_js = "/assets/planning/js/planning.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "planning.install.before_install"
# after_install = "planning.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "planning.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }
doc_events = {
    "NNProject": {
        # "after_insert": "planning.planning.doctype.nnproject.nnproject.save_msg",
        "on_update": "planning.planning.doctype.nnproject.nnproject.update_msg",
    },
    "NNMilestone": {
        # "after_insert": "planning.planning.doctype.nnproject.nnproject.save_msg",
        "on_update": "planning.planning.doctype.nnproject.nnproject.update_msg",
    },
    "NNTasklist": {
        # "after_insert": "planning.planning.doctype.nnproject.nnproject.save_msg",
        "on_update": "planning.planning.doctype.nnproject.nnproject.update_msg",
    },
    "NNTask": {
        # "after_insert": "planning.planning.doctype.nnproject.nnproject.save_msg",
        "on_update": "planning.planning.doctype.nnproject.nnproject.update_msg",
    }
}
# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"planning.tasks.all"
# 	],
# 	"daily": [
# 		"planning.tasks.daily"
# 	],
# 	"hourly": [
# 		"planning.tasks.hourly"
# 	],
# 	"weekly": [
# 		"planning.tasks.weekly"
# 	]
# 	"monthly": [
# 		"planning.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "planning.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "planning.event.get_events"
# }

Fixtures = ["NNProject", "NNMilestone", "NNTasklist", "NNTask"]

