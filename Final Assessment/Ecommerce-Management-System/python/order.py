from db_connection import cursor, connection

def place_order():

    customer = int(input("Customer ID : "))
    product = int(input("Product ID : "))
    qty = int(input("Quantity : "))

    cursor.execute(
        "SELECT Price,Stock FROM Products WHERE ProductID=?",
        (product,)
    )

    item = cursor.fetchone()

    if item is None:
        print("Product Not Found")
        return

    price = item.Price
    stock = item.Stock

    if qty > stock:
        print("Not Enough Stock")
        return

    total = price * qty

    cursor.execute("""
    INSERT INTO Orders
    (CustomerID,ProductID,Quantity,TotalAmount)
    VALUES(?,?,?,?)
    """,(customer,product,qty,total))

    cursor.execute("""
    UPDATE Products
    SET Stock=Stock-?
    WHERE ProductID=?
    """,(qty,product))

    connection.commit()

    print("Order Placed Successfully")