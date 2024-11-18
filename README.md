# HW16_MAKTAB119
# Inventory Management System  

## Overview  

The Inventory Management System is designed to efficiently manage a variety of items, both physical and digital. It allows users to add new items, update stock levels, and generate comprehensive reports. The system is built using object-oriented programming principles, leveraging inheritance and polymorphism, and integrates with a PostgreSQL database for persistent storage.  

## Features  

- **Item Management**: Create, update, and delete items in the inventory.  
- **Item Types**: Support for both physical items (with weight and dimensions) and digital items (with file size and download link).  
- **Polymorphism**: Unified stock update process for all item types.  
- **Logging System**: Track changes in stock with a detailed logging mechanism.  
- **PostgreSQL Integration**: Store item details in a relational database.  

## Class Structure  

### Base Class: `Item`  

- **Attributes**:  
  - `id`: Unique identifier for the item.  
  - `name`: Name of the item.  
  - `quantity`: Current stock quantity.  
  - `price`: Price of the item.  

### Subclasses  

1. **PhysicalItem** (inherits from `Item`)  
   - **Additional Attributes**:  
     - `weight`: Weight of the item.  
     - `dimensions`: Dimensions of the item.  

2. **DigitalItem** (inherits from `Item`)  
   - **Additional Attributes**:  
     - `file_size`: Size of the digital file.  
     - `download_link`: URL for downloading the item.  

### Methods  

- `update_stock(amount)`: Update the stock quantity of the item.  
- `get_info()`: Retrieve detailed information about the item.  

## Database Schema  

The PostgreSQL database includes a table named `inventory` with the following columns:  

- `id`: Serial primary key.  
- `name`: VARCHAR.  
- `quantity`: INTEGER.  
- `price`: DECIMAL.  
- `type`: VARCHAR (indicates whether the item is physical or digital).  
- Additional columns specific to item types (e.g., `weight`, `dimensions`, `file_size`, `download_link`).  

## Queries  

The following SQL queries are implemented for managing the inventory:  

1. **Insert a new item**:  
   ```sql  
   INSERT INTO inventory (name, quantity, price, type, weight, dimensions) VALUES ('Item Name', 10, 19.99, 'Physical', 1.5, '10x5x3');
