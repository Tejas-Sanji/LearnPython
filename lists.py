p=input("Enter file name:")
fname=open(p)
l=list()
for line in fname:
    words=line.split()
    for i in words:
        k=0
        for j in l:
            if(j==i):
                k=1
        if k==0:
            l.append(i)
l.sort()
print(l)
        