# Odoo Shopify Automation

Advanced Shopify-Odoo Connector by ECOSIRE (PRIVATE) LIMITED

## Overview

This module provides comprehensive, real-time, and automated integration between Odoo and Shopify. It supports bidirectional synchronization of products, orders, and customers with advanced queue management and logging capabilities.

## Features

### Core Functionality
- **Multi-Store Support**: Connect multiple Shopify stores to a single Odoo instance
- **Multi-Company Support**: Full support for Odoo's multi-company architecture
- **Real-time Synchronization**: Webhook-based real-time updates from Shopify
- **Automated Scheduling**: Configurable cron jobs for regular synchronization
- **Queue Management**: Robust job queue system for handling large data volumes
- **Comprehensive Logging**: Detailed logging for troubleshooting and audit trails

### Data Synchronization
- **Products**: Import/export products with variants, images, and inventory
- **Orders**: Complete order synchronization with line items and customer data
- **Customers**: Customer profile synchronization with address management

### User Experience
- **Dashboard**: Real-time KPI dashboard with sync status
- **Smart Buttons**: Quick access to related data from any record
- **Manual Sync Wizard**: On-demand synchronization with progress tracking
- **Connection Testing**: Built-in connection validation for Shopify instances

## Installation

### Prerequisites
- Odoo 17.0 or 18.0
- Python 3.8+
- Required Python packages (see requirements.txt)

### Installation Steps
1. Copy the module to your Odoo addons directory
2. Install required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Update the addons list in Odoo
4. Install the "Odoo Shopify Automation" module
5. Configure your Shopify instances

## Configuration

### Shopify Instance Setup
1. Go to **Shopify Automation > Configuration > Shopify Instances**
2. Create a new instance with your Shopify store details:
   - **Instance Name**: A descriptive name for your store
   - **Shop URL**: Your Shopify store URL (e.g., https://yourstore.myshopify.com)
   - **API Key**: Your Shopify API key
   - **API Password**: Your Shopify API password
   - **Shared Secret**: Your Shopify webhook shared secret
3. Test the connection using the "Test Connection" button

### Scheduled Synchronization
The module includes pre-configured cron jobs:
- **Product Import**: Every 30 minutes
- **Order Import**: Every 15 minutes
- **Customer Import**: Every 60 minutes
- **Queue Processing**: Every 5 minutes

You can modify these schedules in **Configuration > Scheduled Jobs**.

## Usage

### Manual Synchronization
1. Go to **Shopify Automation > Synchronization**
2. Select the data type you want to sync (Products, Orders, Customers)
3. Use the "Manual Sync" wizard to perform on-demand synchronization

### Monitoring
- **Dashboard**: View real-time KPIs and sync status
- **Queue Jobs**: Monitor pending and completed synchronization jobs
- **Logs**: Review detailed logs for troubleshooting

### Webhooks
The module automatically sets up webhook endpoints for real-time updates:
- `/shopify/webhook/product` - Product updates
- `/shopify/webhook/order` - Order updates
- `/shopify/webhook/customer` - Customer updates

## API Compatibility

This module uses the Shopify Admin API 2024-01, ensuring compatibility with the latest Shopify features and requirements.

## Support

For support and questions, please contact ECOSIRE (PRIVATE) LIMITED.

## License

This module is licensed under LGPL-3.

## Version History

- **18.0.1.0.0**: Initial release with full Odoo 18 compatibility
- Updated to Shopify API 2024-01
- Enhanced error handling and logging
- Improved user interface and dashboard
