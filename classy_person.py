'''
Starter code!
don't forget the use of 'self' and to have the methods:
1. __init__
2. increase_age
3. say_greeting
4. count_to_age
'''
age_counter = 1

class Person:
    name = ''
    age = 0
    age_counter = 1

    def __init__(self, age, name) -> None:
        self.name = name
        self.age = age
    
    def increase_age(self):
        self.age = self.age+1

    def say_greeting(self):
        print(f'Hello world! My name is {self.name}!')

    def count_to_age(self):
        if self.age >= 1:
            for x in range(1,self.age+1): print(x)


# x= Person(35, 'Forest')
