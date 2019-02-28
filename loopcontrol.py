# a while tells python to exc a block of stsmnt autill a conditon is false
# increment
# an ATM process
# balance=int(input("deposit"))
#
# while balance>0:
#     withdraw=int(input("enter withdraw amount"))
#     balance= balance-withdraw
#     print(balance)
#     if balance ==1 :
#         break
#
# print("sorry you have insufficient amount")
#
# # how to loop through a list a find an item and its positio
# id=[1,2,3,4,5]
# print(id)
# print(len(id))
# x=int(input("enter a value"))
# for io in range(len(id)):
#     if x==id[io]:
#         break
#
# if io<len(id)-1:
#     print(x,'found in position',io+1)
# else:
#     print("x not found in the list")
#
# # how to stop a loop once you encounter a certain letter
# for i in "python":
#     if i=="o":
#         break
#         print("Hapa ndio mwisho: ",i)
#

num=[0,1,2,3,4,5]

while len(num)>0:
    print(num)
    num.pop()