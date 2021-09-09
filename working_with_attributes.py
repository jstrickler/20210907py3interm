from president import President

p = President(26)

print(p)

print(p.first_name)
print(p.last_name)

a = "first_name"


if hasattr(p, a):
    print(getattr(p, a))

setattr(p, 'first_name', 'Teddy')
print(p)
print(p.first_name, '\n')


for attr_name in sorted(dir(p)):
    if attr_name.startswith('_'):
        continue
    attr_value = getattr(p, attr_name)
    print(f"{attr_name:16} {attr_value}")

def get_by(self):
    return self._bdate.year

setattr(President, 'get_birth_year', get_by)  # monkey-patching
# aka duck-punching

print(p.get_birth_year())

abe = President(16)
print(abe)
print(abe.get_birth_year())












