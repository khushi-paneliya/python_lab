n=int(input("Enter a number of lines :"))
i=1
while i<=n:
    print("*" * i)
    i=i+1
\
\
for i in range (1,4):
    print("*" * i)

\
\
n=5
for i in range(5,0,-1):
    for j in range (i,0,-1):
          print(j ,end="")
    print()
\
\
n=5
for i in range(1,n+1):
    for j in range (1,i+1):
        print(j , end="")
    print()
\
\
n=5
for i in range (1,n+1):
    for j in range(i):
        print(chr(65+j),end="")
    print()