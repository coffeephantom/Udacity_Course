class Student():
    '''
    A program help to understand the concept of a class and some predefined the class variables.

    '''
    def __init__(self,name,age,major):
        self.Name=name
        self.Age=age
        self.Major=major

    def show_name(self):
        print self.Name

Jack = Student("Jack","24","Computer Science")
Jane = Student("Jane","19","Arts")

print Student.__name__
print Student.__module__
print Student.__doc__





