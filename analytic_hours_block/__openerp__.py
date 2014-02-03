# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Vincent Renaville, ported by Joel Grand-Guillaume
#    Copyright 2010-2012 Camptocamp SA
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

{
    "name": "Project Hours Blocks Management",
    "description": """
Project Hours Blocks Management
===============================

This module allows you to handle hours blocks,
to follow for example the user support contracts.
This means, you sell a product of type "hours block"
then you input the spent hours on the hours block and
you can track and follow how much has been used.

 """,
    "version": "1.3",
    "author": "Camptocamp",
    "license": 'AGPL-3',
    "category": "Generic Modules/Projects & Services",
    "website": "http://www.camptocamp.com",
    "depends": [
        "account",
        "hr_timesheet_invoice",
        "analytic"
        ],
    "data": [
        "hours_block_view.xml",
        "hours_block_data.xml",
        "hours_block_menu.xml",
        "report.xml",
        "security/hours_block_security.xml",
        "security/ir.model.access.csv",
        ],
    "active": False,
    "installable": True
}