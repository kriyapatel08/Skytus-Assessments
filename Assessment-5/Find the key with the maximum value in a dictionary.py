#Find the key with the maximum value in a dictionary.
Dict = {
    "Kriya": 85,
    "Riya": 92,
    "Aman": 78
}
max_key = max(Dict, key=Dict.get)
print("Key with the maximum value:", max_key)
