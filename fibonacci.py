n=int(input("enter the number of terms required: "))
num1=0;
num2=1;
for i in range(0,n):
    print(num1,end='\t');
    num3=num1+num2;
    num1=num2;
    num2=num3;

