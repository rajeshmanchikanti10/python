import sys
if __name__ == '__main__':
    list1=[]
    minvalue=sys.float_info.max
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if(minvalue>score):
            minvalue=score
        list1.append([name,score])
    print(minvalue)
    for i in list1:
        if(abs(i[1]-min)==0):
            print(i[0],end="\n")
    print(list1)
