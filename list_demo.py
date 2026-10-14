#empty list
my_list=[]
print(my_list)

#to access the list using index
numbers=[1,2,3]
print(numbers[0])
print(numbers[-2])

#append the list
colors=["red","blue"]
colors.append("green")
print("After adding at last",colors)

#insert at specific position
#colors.append()

#functions
#1. length
numbers=[1,2,3,4,5]
print("No of items in the list",len(numbers))

#2.sum
print("sum of the list numbers",sum(numbers))

#3.sorting
print("List in ascending order",sorted(numbers))
print("List in descending order",sorted(numbers,reverse=True))


