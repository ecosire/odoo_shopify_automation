{
    'name': 'Odoo Shopify Connector with Automations',
    'version': '18.0.1.0.0',
    'summary': 'Advanced Shopify-Odoo Connector by ECOSIRE (PRIVATE) LIMITED',
    'description': '''
Comprehensive, real-time, and automated integration between Odoo and Shopify. 

🔗 **Core Features:**
• Multi-store Shopify integration with connection testing
• Bidirectional product synchronization (Odoo ↔ Shopify)
• Automated order import/export with customer auto-creation
• Real-time customer data synchronization
• Product variant handling and mapping

⚙️ **Automation & Scheduling:**
• Automated cron jobs (products: 30min, orders: 15min, customers: 60min)
• Queue management system with background processing
• Manual sync wizard for on-demand operations
• Real-time webhooks for instant updates

📊 **Monitoring & Analytics:**
• Comprehensive dashboard with sync status overview
• Detailed logging and error tracking
• Performance metrics and success rate monitoring
• Queue job monitoring and management

🔒 **Security & Access Control:**
• Role-based access permissions
• Multi-company support with data isolation
• Secure API credential management
• Data validation and integrity checks

🛠️ **Technical Features:**
• Support for Odoo 17.0 and 18.0
• Webhook endpoints for real-time updates
• Extensible architecture for custom integrations
• Robust error handling and recovery

Perfect for e-commerce businesses requiring seamless integration between Odoo ERP and Shopify e-commerce platforms.

Developed by ECOSIRE (PRIVATE) LIMITED.
    ''',
    'author': 'ECOSIRE (PRIVATE) LIMITED',
    'website': 'https://www.ecosire.com/',
    'category': 'Connector',
    'depends': ['base', 'sale_management', 'stock', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_cron_data.xml',
        'views/menu.xml',
        'views/shopify_instance_view.xml',
        'views/shopify_product_view.xml',
        'views/shopify_order_view.xml',
        'views/shopify_customer_view.xml',
        'views/shopify_queue_job_view.xml',
        'views/shopify_log_view.xml',
        'views/dashboard_view.xml',
        'views/shopify_cron_view.xml',
        'wizard/manual_sync_wizard_view.xml',
    ],
    'images': [
        'static/description/cover.png',
        'static/description/Screen 1.png',
        'static/description/Screen 2.png',
        'static/description/Screen 3.png',
        'static/description/Screen 4.png',
        'static/description/Screen 5.png',
        'static/description/Screen 6.png',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
    'assets': {},
    'support': 'https://www.ecosire.com/',
    'maintainer': 'ECOSIRE (PRIVATE) LIMITED',
    'price': 0.0,
    'currency': 'EUR',
} 