class sStudent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, I am {self.name} and I am {self.age} years old. I am a student.")
        self.subject = "Math"
