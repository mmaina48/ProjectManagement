
# try:
#     x=int(input("1st number"))
#     y=int(input("2nd number"))
#     z=x/y
#     print("answer is",z)
#
# except(ValueError,ZeroDivisionError,KeyboardInterrupt):
#     print("Error occuser kindly check the no. you enterd")

# Arguments in except

# try:
#     def square(var):
#         print(int(var)**2)
#         return
# except ValueError as Argument:
#     print("hii sio number: ",Argument)
#8
# square("10")

# Raising an exception
try:
    marks=int(input("weka marks"))
    if marks<0 or marks>100:
        raise Exception(marks)
    print("markes within range=",marks)

except Exception as e:
    print("Error. Invalid marks",e)
