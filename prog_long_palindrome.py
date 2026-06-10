file=input("enter the file to open:")
s=[]
m=0
with open(file,"r") as f:
    for i in f:
        i=i.strip()
        if i==i[::-1]:
            l=len(i)
            if l>m:
                m=l
                s=[i]
            elif l==m:
                s.append(i)

print("largest palindrome length:",m)
print("words:")
for j in s:
    print(j)