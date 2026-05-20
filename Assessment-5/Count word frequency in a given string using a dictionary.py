# Count word frequency in a given string using a dictionary.
string = ("My name is Kriya. I am a 20 years old. I am currently pursuing B.Tech. ")
word_frequency = {}
for word in string.split():
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1
print(word_frequency)
