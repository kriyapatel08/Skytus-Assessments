# #Write a program to read a file and display its contents
file = open("sample.txt", "r")

content = file.read()
print(content)

file.close()

#Write a program to count the number of lines in a file.
file = open("sample.txt", "r")

count = 0

for line in file:
    count += 1

print("Number of lines:", count)

file.close()

#Write a program to count how many times each word appears in a file.
file = open("sample.txt", "r")

text = file.read().lower()
words = text.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for word, count in word_count.items():
    print(word, ":", count)

file.close()

#Write a program to write 5 user-entered sentences to a file.
file = open("sentences.txt", "w")

for i in range(5):
    sentence = input("Enter sentence: ")
    file.write(sentence + "\n")

file.close()

print("Data saved successfully.")

#Write a program to append a list of strings to an existing file.
file = open("sample.txt", "a")

data = [
    "Python is easy.",
    "File handling is useful.",
    "Practice daily."
]

for line in data:
    file.write(line + "\n")

file.close()

print("Data appended successfully.")

#Write a program to read a file and print only lines containing a specific word.
word = input("Enter word to search: ")

file = open("sample.txt", "r")

for line in file:
    if word.lower() in line.lower():
        print(line.strip())

file.close()

# Write a program to replace a specific word in a file and save changes.
old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")

file = open("sample.txt", "r")
content = file.read()
file.close()

content = content.replace(old_word, new_word)

file = open("sample.txt", "w")
file.write(content)
file.close()

print("Word replaced successfully.")
    
# #Write a program to merge the contents of two text files into a third file.
file1 = open("file1.txt", "r")
file2 = open("file2.txt", "r")

content1 = file1.read()
content2 = file2.read()

file3 = open("merged.txt", "w")

file3.write(content1)
file3.write("\n")
file3.write(content2)

file1.close()
file2.close()
file3.close()

print("Files merged successfully.")

 #Write a program to read a CSV file and display its content in a formatted way.   

import csv

file = open("students.csv", "r")

reader = csv.reader(file)

for row in reader:
    print(row)

file.close()

#Write a program to back up a file by copying its contents into another file. 
source = open("sample.txt", "r")

content = source.read()

source.close()

backup = open("backup.txt", "w")

backup.write(content)

backup.close()

print("Backup created successfully.")