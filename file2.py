f=input("Enter file name:")
fname=open(f)
s=0
count=0
for line in fname:
    if(line.startswith('X-DSPAM-Confidence:')):
        count=count+1
        loc=line.find('0')
        stri=line[loc:]
        s=s+float(stri)
print('Average spam confidence:',s/count)