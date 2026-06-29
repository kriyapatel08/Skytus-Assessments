CREATE DATABASE EcommerceDB;
GO

USE EcommerceDB;
GO

DROP TABLE IF EXISTS Orders;
GO

DROP TABLE IF EXISTS Products;
GO

DROP TABLE IF EXISTS Customers;
GO

CREATE TABLE Customers(
    CustomerID INT IDENTITY(1,1) PRIMARY KEY,
    CustomerName VARCHAR(100),
    Email VARCHAR(100),
    Phone VARCHAR(20),
    Address VARCHAR(200)
);

DROP TABLE IF EXISTS Products;
GO

CREATE TABLE Products(
    ProductID INT IDENTITY(1,1) PRIMARY KEY,
    ProductName VARCHAR(100),
    Price DECIMAL(10,2),
    Stock INT
);

CREATE TABLE Orders(
    OrderID INT IDENTITY(1,1) PRIMARY KEY,
    CustomerID INT,
    ProductID INT,
    Quantity INT,
    TotalAmount DECIMAL(10,2),

    FOREIGN KEY(CustomerID)
        REFERENCES Customers(CustomerID),

    FOREIGN KEY(ProductID)
        REFERENCES Products(ProductID)
);

USE EcommerceDB;

SELECT * FROM Customers;
SELECT * FROM Products;
SELECT * FROM Orders;