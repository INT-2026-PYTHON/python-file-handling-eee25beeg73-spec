file=input("enter name of file:")
s=[]
n=0
with open(file,"r") as f:
    for i in f:
        i=i.strip()
        if i==i[::-1]:
            s.append(i)
            n +=1
print("palindrome:")
for i in s:
    print(i)
print("total numer of palindrome:",n)
