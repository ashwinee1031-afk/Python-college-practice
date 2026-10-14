#list of 10 numbers and display sum of last 4 digits
#remove the items from the list located at 2nd and 5th position
#print the difference of highest and smallest no of list
#append new element in the list which is half of the item of 3rd position in the list

list=[1,2,3,4,5,6,7,8,9,10]
print("Sum of last 4 digits",sum(list[-4::]))

print(list.pop(1))
print(list.pop(4))
print(list)

m1=max(list)
m2=min(list)
print(m1-m2)

a = list[3]/2
list.append(a)
print(list)



