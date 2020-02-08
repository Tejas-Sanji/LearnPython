inp=input("Enter file name:")
fname=open(inp)
count=dict()
for line in fname:
    words=line.split()
    if len(words)>0 and words[0]=='From':
        count[words[1]]=count.get(words[1],0)+1
bigmail=None
bigc=None
for k,v in count.items():
    if bigc is None or v>bigc:
        bigmail=k
        bigc=v
print(bigmail,bigc)
