#read file and count how many vowels are present the file

f=open("vowel.txt")
f1=f.read()
print(f1)
print(f.read())
count = 0
for i in f1:
    if i in 'aeiouAEIOU':
        count+=1
print(count)