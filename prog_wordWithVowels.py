file=input("enter the name of the file:")
l=[]
n=0
v={'a','e','i','o','u'}
with open(file,"r") as f:
    for i in f:
        s=set()
        i=i.strip()
        s.update(i)
        if ( v & s)==v :
                l.append(i)
                n=n+1
print("words having all five vowels:")
for i in l:
    print(i)
print("total number of word with all vowels:",n)
