def student_info(name,age,city):
    print("name:",name)
    print("age:",age)
    print("city:",city)
student_info(age=18,city="rajkot",name="Khushi")

#Mixing positional and keyword
def dispaly(a,b,c):
    print("a=",a)
    print("b=",b)
    print("c=",c)
dispaly(4,c=2,b=3)

#create function of simple intrest
def simple_interest(p:float,r:int,t:float):
    si=(p*r*t)/100
    print("simple interest:",si)
simple_interest(p=100000,t=2,r=1.5)
simple_interest(t=1.5,p=20000,r=2)