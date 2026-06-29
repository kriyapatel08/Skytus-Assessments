from customer import *
from product import *
from order import *
from report import *

while True:

    print("\n===== E-Commerce Management System =====")

    print("1. Add Customer")
    print("2. View Customers")
    print("3. Add Product")
    print("4. View Products")
    print("5. Place Order")
    print("6. Order Report")
    print("7. Exit")

    choice = input("Enter Choice : ")

    if choice == '1':
        add_customer()

    elif choice == '2':
        view_customers()

    elif choice == '3':
        add_product()

    elif choice == '4':
        view_products()

    elif choice == '5':
        place_order()

    elif choice == '6':
        order_report()

    elif choice == '7':
        break

    else:
        print("Invalid Choice")