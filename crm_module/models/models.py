# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
class IniciativasCrm(models.Model):
	_inherit = "crm.lead"

	@api.one
	def create_customer(self):
		contact_obj = self.env['res.partner']
		contact_values = {
			'company_type': 'person',
			'name': self.name,
			'street': self.street,
			'city': self.city,
			'state_id': self.state_id.id,
			'zip': self.zip,
			'country_id': self.country_id.id,
			'email': self.email_from,
			'function': self.function,	
			'phone': self.phone,
			'mobile': self.mobile,
			'website': self.website,
			'customer': True,
			'type': 'contact',
		}
		contact_id = contact_obj.create(contact_values)