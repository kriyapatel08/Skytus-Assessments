#Join a list of words into a single string with - between them
words = input("Enter a list of words separated by spaces: ").split()
joined_string = '-'.join(words)
print("Joined string:", joined_string)
