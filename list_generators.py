numbers = [1,2,3,4,5,6,7,8,9,]

result = []
for number in numbers:
    if number >3 and numbers <6:
        result.append(numbers)
    print(result)

result1 = [number for number in numbers if number >3 and numbers <6]
print(result1)

names = ['leo', 'max', 'kate', 'mag']
names1 = ['LEO', 'MAX', 'KATE', 'MAG']

names2 = [name.upper()for name in names]
print(names2)

names_m = [name for name is names if name[0]== 'm']
print(names)