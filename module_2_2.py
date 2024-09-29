First = int(input("Введите первое число: "))
Second = int(input("Введите второе число: "))
Third = int(input("Введите третье число: "))
if First == Second == Third:
    print(3)
elif First == Second or Second == Third or Third == First:
    print(2)
else:
    print(0)
    
