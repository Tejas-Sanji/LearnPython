inp=input('enter file name')
handle=open(inp)
count=dict()
for line in handle:
    words=line.split()
    if len(words)>0 and words[0]=='From':
        time=words[5]
        time=time.split(':')
        count[time[0]]=count.get(time[0],0)+1
count=sorted(count.items())
for x,y in count:
    print(x,y)