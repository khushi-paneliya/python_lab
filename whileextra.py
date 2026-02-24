i=1
while i<=5:
    print(i)
    i=i+1  

num=int(input("Enter a number :"))
i=1
s=0
while i<=num :
    s=s+i
    i=i+1
print("sum is :",s)  

print("odd no:")
i=1
while i <= 20:
    if i%2!=0:
        print(i)
    i=i+1
        

num=4
i=1
while i<=10:
    print(num,"X",i,"=",num*i)
    i=i+1 

i=5
while i>=1:
    print(i)
    i=i-1

num=[10,30,50,90,100]
max_no=num[0]
i=1
while i<len(num):
    if num[i]>max_no:
        max_no=num[i]
    i=i+1
print("largest no is :",max_no)    

print("Even no:")
i=1
while i<=20:
    if i%2==0:
        print(i)
    i=i+1