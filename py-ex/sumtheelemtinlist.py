lst = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = float(input('Enter number '))
    number=numbers/9-numbers/13+numbers/17
    lst.append(number)
print("Sum of elements in given list is :", number)