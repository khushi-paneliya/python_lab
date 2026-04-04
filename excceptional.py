"""try:
    number1=int(input("Enter a number :"))
    number2=int(input("Enter anoyher number :"))
    result=number1 / number2
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("Please enter a valid number!")
else:
    print("Divistion successful! Result is : ",result)
finally:
    print("This block always runs")"""

try:
    my_list=[1,2,3]
    print(my_list[1])
except IndexError:
    print("Index is out of range!!")
else:
    print("Element found successful! ")
finally:
    print("program finished")

