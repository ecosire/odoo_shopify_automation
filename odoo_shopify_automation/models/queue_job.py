from odoo import models, fields, api

class ShopifyQueueJob(models.Model):
    _name = 'shopify.queue.job'
    _description = 'Shopify Import/Export Queue Job'
    _order = 'create_date desc'

    name = fields.Char('Job Name')
    job_type = fields.Selection([
        ('import_product', 'Import Product'),
        ('export_product', 'Export Product'),
        ('import_order', 'Import Order'),
        ('export_order', 'Export Order'),
        ('import_customer', 'Import Customer'),
        ('export_customer', 'Export Customer'),
        ('other', 'Other'),
    ], string='Job Type', required=True)
    instance_id = fields.Many2one('shopify.instance', string='Shopify Instance', required=True)
    related_model = fields.Char('Related Model')
    related_record_id = fields.Integer('Related Record ID')
    status = fields.Selection([
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('failed', 'Failed'),
        ('cancelled', 'Cancelled'),
    ], string='Status', default='pending')
    error_message = fields.Text('Error Message')
    create_date = fields.Datetime('Created On', readonly=True)
    write_date = fields.Datetime('Last Updated', readonly=True)
    note = fields.Text('Notes') 