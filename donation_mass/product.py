# -*- encoding: utf-8 -*-
##############################################################################
#
#    Donation Mass module for Odoo
#    Copyright (C) 2014-2015 Barroux Abbey (www.barroux.org)
#    Copyright (C) 2014-2015 Akretion France (www.akretion.com)
#    @author: Alexis de Lattre <alexis.delattre@akretion.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.onchange('mass')
    def mass_change(self):
        super(ProductTemplate, self).mass_change()
        if self.mass:
            self.donation = True


class ProductProduct(models.Model):
    _inherit = 'product.product'

    @api.onchange('mass')
    def mass_change(self):
        super(ProductProduct, self).mass_change()
        if self.mass:
            self.donation = True
