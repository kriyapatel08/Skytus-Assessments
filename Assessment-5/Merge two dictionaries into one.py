#Merge two dictionaries into one.
dict_1 = {
    "Aeni": 85,
    "Kriya": 92,
    "Charlie": 78,
}
dict_2 = {
    "Raini": 85,
    "Mili": 92,
    "Nirali": 78,
}
#merge two dictionaries.
merge_dict = dict_1 | dict_2
print(merge_dict)

