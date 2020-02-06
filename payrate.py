hrs = float(input("Enter Hours:"))
rate = float(input("Enter payrate:"))
if hrs<=40:
	pay=rate*hrs
else:
    pay=40*rate+(hrs-40)*rate*1.5
print(pay)