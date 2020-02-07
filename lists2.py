inp=input('Enter name of file')
fname=open(inp)
count=0
for lines in fname:
    words=lines.split()
    if len(words)>0:
    	if words[0]=='From':
        	print(words[1])
        	count=count+1
print('There were',count,'lines in the file with From as the first word')