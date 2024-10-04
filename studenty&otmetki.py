grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# находим средние оценки
grad_mid = [sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]),
            sum(grades[2])/len(grades[2]), sum(grades[3])/len(grades[3]), sum(grades[4])/len(grades[4])]

print(grad_mid)

#сортировка студентов
stud_sort = sorted(students)
print(stud_sort)

#создание запакованного словаря
dict_z = zip(stud_sort, grad_mid)

#распаковка словаря
dict_fin = dict(zip(stud_sort, grad_mid))
print(dict_fin)

