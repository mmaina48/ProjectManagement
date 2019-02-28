id=["Yes","yes","YES",""]

x=(input("enter yes :"))
for io in range(len(id)):
    if x==id[io]:
        break

if io<len(id)-1:
    print('Yes')
else:
    print("NO")



if x=="Yes":
    print("yes")



# for loops nested with if and lop control Break
# for i in [4,5,6]:
#     if i==[2]:
#         break
#     print((i))