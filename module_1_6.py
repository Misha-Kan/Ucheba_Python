#Dict: {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
#Existing value: 2002
#Not existing value: None
#Deleted value: 1999
#Modified dictionary: {'Vasya': 1975, 'Kamila': 1981, 'Artem': 1915, 'Masha': 2002}

#Set: {1, 'Яблоко', 42.314}
#Modified set: {'Яблоко', 42.314, 13, (5, 6, 1.6)}
print("Словари")
my_dict = {"Dasha_M": 1988, "Misha_M": 1990}
print(my_dict)
print(my_dict["Misha_M"])
my_dict["Lisa_K"] = 1992
#print(my_dict)
print(my_dict["Lisa_K"])
my_dict.update({"Olga_K": 1962, "Misha_K": 1965})
print(my_dict)
del my_dict["Lisa_K"]
#print(my_dict)
print(my_dict.get("Lisa_K", "Клиент не найден"))
print(my_dict)
print("Множества")
my_set = {1, 4, 7, 8, 2, 4, 8, 1}
print(my_set)
my_set.update([1, 4, 9, 3, (1, 2, 3), "Line"])
print(my_set)
my_set.discard((1, 2, 3))
print(my_set)








