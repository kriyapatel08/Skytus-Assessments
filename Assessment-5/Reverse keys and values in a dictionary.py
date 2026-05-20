#Reverse keys and values in a dictionary.
Dict = {
    "Kriya": 85,    
    "Riya": 92,
    "Aman": 78
}
reversed_dict = {value: key for key, value in Dict.items()}
print("Reversed dictionary:", reversed_dict)