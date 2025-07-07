from odoo import models, fields, api
import requests
from odoo.exceptions import UserError
from odoo.tools.translate import _

class ShopifyInstance(models.Model):
    _name = 'shopify.instance'
    _description = 'Shopify Store Instance'
    _rec_name = 'name'

    name = fields.Char('Instance Name', required=True)
    shop_url = fields.Char('Shopify Shop URL', required=True, help='e.g. https://yourstore.myshopify.com')
    api_key = fields.Char('API Key', required=True)
    password = fields.Char('API Password', required=True)
    shared_secret = fields.Char('Shared Secret', required=True)
    access_token = fields.Char('Access Token', help='OAuth Access Token (if using OAuth)')
    company_id = fields.Many2one('res.company', string='Company', required=True, default=lambda self: self.env.company)
    active = fields.Boolean('Active', default=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('connected', 'Connected'),
        ('error', 'Error'),
    ], string='Status', default='draft')
    last_sync = fields.Datetime('Last Sync')
    note = fields.Text('Notes')

    _sql_constraints = [
        ('shop_url_uniq', 'unique(shop_url, company_id)', 'A Shopify instance with this URL already exists for this company!'),
    ]

    def action_test_connection(self):
        self.ensure_one()
        url = f"{self.shop_url}/admin/api/2024-01/shop.json"
        try:
            response = requests.get(url, auth=(self.api_key, self.password), timeout=10)
            if response.status_code == 200:
                self.state = 'connected'
                self.message_post(body=_('Connection Test Succeeded!'))
                return {
                    'type': 'ir.actions.client',
                    'tag': 'display_notification',
                    'params': {
                        'title': _('Shopify'),
                        'message': _('Connection Test Succeeded!'),
                        'type': 'success',
                        'sticky': False,
                    },
                }
            else:
                self.state = 'error'
                raise UserError(_(f"Connection failed! Status: {response.status_code}\n{response.text}"))
        except Exception as e:
            self.state = 'error'
            raise UserError(_(f"Connection error: {str(e)}")) 