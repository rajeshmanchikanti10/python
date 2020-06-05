

n=int(input("enter the length of list: "));
list1=[];
for i in range(0,n):
    num=int(input("enter the list entry: "));
    list1.append(num);
for i in list1:
    if(i>0):
        print(i,end=" ")
