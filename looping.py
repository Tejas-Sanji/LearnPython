largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        val=int(num)
    except:
        print('Invalid input')
    if largest is None:
        largest=val
    elif largest<val:
        largest=val
    if smallest is None:
        smallest=val
    elif smallest>val:
        smallest=val

print("Maximum is", largest)
print("Minimum is",smallest)