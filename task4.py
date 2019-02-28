num = int(input('Weka Number'))
modulles = num % 2

if num%2==0 and num%4!=0:
    print("this no is even :",num)
elif num%2 !=0:
    print("this no is an odd number", num)
elif num %4==0:
    print("the no. is a multiple of 4")
else:
    print("invalid input !!!please use interger")


