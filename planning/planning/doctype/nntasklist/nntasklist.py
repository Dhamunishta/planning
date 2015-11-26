# -*- coding: utf-8 -*-
# Copyright (c) 2015, nishta and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class NNTasklist(Document):
	pass
	
	def autoname(self):
		no_rows = frappe.db.count("NNTasklist")
		tasklist = self.tasklist +"-"+str(no_rows)
		self.tasklist = tasklist
		self.name = tasklist