#Write a program to read a file and display its contents
# Open the file in read mode
file_path = 'LICENSE.txt'  # Replace with your file path
try:
    with open(file_path, 'r') as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("An error occurred:", e)
    