from db_connection import connection, cursor

def add_customer():
    name = input("Name : ")
    email = input("Email : ")
    phone = input("Phone : ")
    address = input("Address : ")

    cursor.execute("""
        INSERT INTO Customers
        (CustomerName, Email, Phone, Address)
        VALUES (?, ?, ?, ?)
    """, (name, email, phone, address))

    connection.commit()

    print("Customer Added Successfully")


def view_customers():
    cursor.execute("SELECT * FROM Customers")

    rows = cursor.fetchall()

    for row in rows:
        print(row)