dict_codes = {
    (800, 'Bangladesh'),
    (66, 'Brasil'),
    (77, 'China'),
    (91, 'India')
}

h = {country:code for code, country in dict_codes}

print(h)

def f(**kwargs):
    return kwargs

print(f(**{'1':2}, y=2, **{'4':5}))

