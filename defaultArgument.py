def greet(name,msg="Good morning"):
    print("Hello",name+",",msg)
greet("Khushi")
greet("siddh","Good Evening")

#power function
def power(num,exp=2):
    return num**exp
print(power(5))
print(power(3,3))
print(power(2,5))

#multiple defalt arguments
def student_info(name,age=18,course="BCA"):
    print("Name:",name)
    print("Age:",age)
    print("Course:",course)
student_info("rutu")
student_info("seema",20)
student_info("Khushi",18,"B.SC.IT")