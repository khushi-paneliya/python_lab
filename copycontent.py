src=open("student.txt","r")
data=src.read()
src.close()

dst=open("atmiya.txt","w")
dst.write(data)
dst.close()
print("file copied successfully!")