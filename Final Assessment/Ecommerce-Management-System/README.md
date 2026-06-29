# 🛒 E-commerce Management System

## 📌 Overview
A simple console-based E-commerce Management System developed using **Python** and **SQL Server (SSMS)**. It allows users to manage customers, products, and orders with data stored in a SQL Server database.

## 🚀 Features
- Add Customer
- View Customers
- Add Product
- View Products
- Place Order
- View Order Report

## 🛠 Technologies Used
- Python 3.x
- SQL Server (SSMS)
- pyodbc
- Visual Studio Code

## 📂 Project Structure
```
Ecommerce-Management-System/
│── database/
│   └── ecommerce.sql
│── python/
│   ├── db_connection.py
│   ├── customer.py
│   ├── product.py
│   ├── order.py
│   ├── report.py
│   └── main.py
│── README.md
│── requirements.txt
```

## ⚙ Installation
1. Install Python.
2. Install SQL Server (SSMS).
3. Install the required package:
```bash
pip install pyodbc
```
4. Create the `EcommerceDB` database and execute `ecommerce.sql`.
5. Update the SQL Server name in `db_connection.py`.
6. Run:
```bash
python main.py
```

## 📋 Menu
```
1. Add Customer
2. View Customers
3. Add Product
4. View Products
5. Place Order
6. Order Report
7. Exit
```
