class Person:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address

    def display_person_info(self):
        print(f"Name: {self.name}")
        print(f"age: {self.age}")
        print(f"address: {self.address}")