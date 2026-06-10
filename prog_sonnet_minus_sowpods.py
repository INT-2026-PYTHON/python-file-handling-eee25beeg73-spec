s1=set()
s2=set()
with open("sonnet_words.txt","r") as f1:
    for i in f1:
            i=i.strip()
            s1.add(i)
with open("sowpods.txt","r") as f2:
    for j in f2:
            j=j.strip()
            s2.add(j)
d=set(s1-s2)
print(sorted(d))
