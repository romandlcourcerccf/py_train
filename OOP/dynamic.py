class Rec:
    """ """


john = {
    "name": "John Doe",
    "position": "Python Developer",
    "department": "Engineering",
    "salary": 80000,
    "hire_date": "2020-01-01",
    "is_manager": False,
}


john_record = Rec()

for field, val in john.items():
    setattr(john_record, field, val)


print(john_record.position)
