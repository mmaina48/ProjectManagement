
lst = []
num = int(input('How many numbers: '))

for n in range(num):
        numbers = int(input('Enter number '))
        lst.append(numbers)

print(lst)
print(len(lst))
print(lst[::len(lst)-1])

# use a method