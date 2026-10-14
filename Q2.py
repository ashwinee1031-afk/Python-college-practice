file = open("readfile.txt")
f1 = file.readlines()
print(f1)
count = 0 
for i in f1:
    count +=1
print("Total number of lines",count)
print("2nd line is - ",f1[1])
print("4th line is -",f1[3])       
