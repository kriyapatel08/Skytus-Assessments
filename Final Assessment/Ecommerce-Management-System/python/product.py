from db_connection import cursor, connection

def add_product():

    name = input("Product Name : ")
    price = float(input("Price : "))
    stock = int(input("Stock : "))

    cursor.execute("""
    INSERT INTO Products(ProductName,Price,Stock)
    VALUES(?,?,?)
    """,(name,price,stock))

    connection.commit()

    print("Product Added")
    
from db_connection import cursor

def view_products():

    cursor.execute("SELECT * FROM Products")

    rows = cursor.fetchall()

    for row in rows:
        print(row)