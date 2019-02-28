tasklist= [23,"jane",["leesso 23",560,{"cureency":"kes"}],987,(76,"john")]

# determin type of tasklist
print(type(tasklist))

# print "kes"
kesl=tasklist[2]
kesl1=kesl[2]
print(kesl1["cureency"])

# print 560
print(tasklist[2][1])

# use fxn to find len of tasklist
print(len(tasklist))

# change 987 to 789 using inbuit fxn
print(str(tasklist[3]))
print(type(str(tasklist[3])))
revern=(str(tasklist[3])[::-1])
print(revern)

# change name = "john to jane"
changename=tasklist[-1]
print("we cannot change an element in :",changename,"because is a :",type(changename))
# we cannot change an element
# you will get an error:















































































































































































