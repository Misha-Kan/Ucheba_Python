
print("Словари")
my_dict = {"Dasha_M": 1988, "Misha_M": 1990}
print(my_dict)
print(my_dict["Misha_M"])
my_dict["Lisa_K"] = 1992
#print(my_dict)
print(my_dict["Lisa_K"])
my_dict.update({"Olga_K": 1962, "Misha_K": 1965})
print(my_dict)
print(my_dict.pop(("Lisa_K")))
print(my_dict.get("Piter_L"))
print(my_dict)
print("Множества")
my_set = {1, 4, 7, 8, 2, 4, 8, 1}
print(my_set)
my_set.update([1, 4, 9, 3, (1, 2, 3), "Line"])
print(my_set)
my_set.discard((1, 2, 3))
print(my_set)








