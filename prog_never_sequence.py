file=input("enter the file to open:")
s=set()
d=set()
r=set()
with open(file,"r") as f:
    for i in f:  
        i=i.strip()
        s.update(i)
        for j in range(len(i)-1):
            if i[j]==i[j+1]:
                d.add(i[j])
r=sorted(s-d)
print("letter that never appear back to back are:")
print(r)