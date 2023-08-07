class Person:
    name = "John Smith"
    age = 30
    gender = "male"
    address = "123 Main St"
    phone_number = "555-555-5555"
    email = "johnsmith@example.com"
    is_employed = True


x = input().lower()
y = x.split()
for i in y:
    print(hasattr(Person, i))