from db_connection import cursor

def order_report():

    cursor.execute("""

    SELECT

    Orders.OrderID,

    Customers.CustomerName,

    Products.ProductName,

    Orders.Quantity,

    Orders.TotalAmount

    FROM Orders

    JOIN Customers

    ON Orders.CustomerID=Customers.CustomerID

    JOIN Products

    ON Orders.ProductID=Products.ProductID

    """)

    rows = cursor.fetchall()

    print("\nOrder Report\n")

    for row in rows:
        print(row)