from typing import  Union
name:str='hello'
age:int=1
isStop:bool=True

class Student:
    pass

stu:Student=Student()

myList:list[int]=[1,2]
myTuple:tuple=(1,2,3)
myDict:dict[str,int]={'111':1}
MyList2:list[Union[int,str]]=[1,'1',2,'2']
var_1=1 #type:int


def greet(name: str, age: int) -> str:
    return f"Hello {name}, you are {age}"


print(greet('```', 1))
print(greet.__annotations__)