#Check if a key exists in a dictionary.
student = {
    "name": "Kriya",
    "age": 20,
    "course": "B.Tech"
}

key = input("Enter key to check: ")

if key in student:
    print("Key exists")
else:
    print("Key does not exist")