# def large(x):
#     x.sort()
#     largest=x[-1]
#     return largest
#
# x=int(input("enter first no "))
# y=int(input("enter second no "))
# z=int(input("enter third no "))
#
# var=[x,y,z]
#
# print("the largest {}".format(large(var)))



def findthelargest(x,y,z):
    if x>y or x>z:
     return x
    elif y>x or y>z:
        return y
    elif z>y or z>x:
        return z
    else:
        print(z)

x=int(input("enter first no "))
y=int(input("enter second no "))
z=int(input("enter third no "))

# call the fxn
largestno=findthelargest(x,y,z)

print(largestno)