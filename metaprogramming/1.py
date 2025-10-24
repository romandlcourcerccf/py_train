# class MYClass:
#     pass

# some_obj = MYClass()

# print(type(some_obj))
# print(type(MYClass))
# print(type)

MYClass = type('MYClass', (object,), {'x':42, 'my_method': lambda self: print("hello")})

o = MYClass()

print(o.my_method())
print(o.x)

MYList = type("MYList", (list, ), {'add_twice': lambda self, item: self.extend([item, item])})


ml = MYList()

ml.append(10)
print(ml)
ml.add_twice(20)

print(ml)

class ValidateMeta(type):
    required_fields = []

    def __new__(cls, name, bases, attrs):
        missing_fields = set(cls.required_fields) - set(attrs.keys())
        if missing_fields:
            raise ValueError(f"Missing required fields: {', '.join(missing_fields)}")

        for field, field_type in cls.field_types.items():
            if not isinstance(attrs.get(field), field_type):
                raise TypeError(f"Field '{field}' must be of type {field_type}")

        return super().__new__(cls, name, bases, attrs)

class User(metaclass=ValidateMeta):
    required_fields = ["name", "email"]
    field_types = {"name": str, "email": str}

    def __init__(self, name, email):
        self.name = name
        self.email = email

invalid_user1 = User("Alice", 123)  # Type mismatch for email
invalid_user2 = User(name="Bob")     # Missing required field: email