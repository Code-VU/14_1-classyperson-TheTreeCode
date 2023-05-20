class Person:
    name = ''
    age = 0

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