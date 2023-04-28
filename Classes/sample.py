"""
1. Class is user defined blueprint of an object constructor
2. object is an instance of particular class
3. class keyword is used to create a class
4. Class attributes can be accessed by using directly with (class_name.variables )
5. It can be accessed by using object
6. Assigning a class to variable is called object instantiation
7. if any change of any attribute using class_name will completely change in entire class
8. if the changes made using object then it will to the object instance itself

"""
def sum():
    return 10 + 10

def mul():
    return 10*10
def sub():
    return 10-10

class Sample:
    name = "riya"

if __name__ == '_main':
    print("Hello Finished....")





print(Sample.name)  # directly accessing using class_name
obj = Sample()
print(obj.name)  # object calling
Sample.name = "Revanth"
print("using class_name:", Sample.name)
print("Change after class_name using object", obj)