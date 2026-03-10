
#Slicing in array
"""
from array import array
arr=array('i',[10,20,30,40,50])
print(arr[1:4])#1 to 3 
print(arr[:3])#start to index 2
print(arr[2:])#2 to end
print(arr[:])# entire array

"""
"""
# with step
from array import array
arr=array('i',[10,20,30,40,50,60,70,80])
print(arr[::2])#every second element
print(arr[1::2])#every second starting form index 1
print(arr[::3])#every third element 
"""
"""
#Negative slicing
from array import array 
arr=array('i',[10,20,30,40,50,])
print(arr[-4:-1])
print(arr[-3:])
print(arr[:-2])

#Reverse array 

from array import array
arr=array('i',[10,20,30,40,50])
print(arr[::-1])
"""
#modifying slicing

from array import array
arr=array('i',[10,20,30,40,50])
arr[1:4]=array('i',[25,35,45])
print(arr)


from array import array
arr=array('i',[10,20,30,40,50])
arr[1:3]=array('i',[25,35,45])
print(arr)