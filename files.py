fname=input('Enter file name:')
fil=open(fname)
for line in fil:
    print(line.upper().rstrip())