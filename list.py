# alist can store any other data type
emptystring= ["brian","mike",8,True]
daysoftheweek=["monday","tueday","wed","thue","frid","sat","sun"]

print(len(daysoftheweek))

# list indexing
wedq=daysoftheweek[2]
print(type(wedq))
print(daysoftheweek[3:4])

details=["michael maina","29","mmaina@gmail","karen"]

print(details[-3:3])

numbers=[0,1,1,1,2,3,4,5,6,7,8,9,10]
print(numbers[-3:-1])

daysoftheweek.append(numbers)
print(daysoftheweek[-1])
daysoftheweek.extend(numbers)
print(daysoftheweek)

# rept=numbers*4
reve=numbers[::-1]
print(reve[2:5])
print(max(reve))