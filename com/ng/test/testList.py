params = {"server": "mpilgrim", "database": "master", "uid": "sa", "pwd": "secret"}
keys = params.keys()
print('-----keys------');
print(type(keys))
print(keys)
values = params.values()
print('-----values------');

print(type(values))
print(values)
items = params.items()
print('-----items------');

print(type(items))
print(items)
ks = [k for k, v in params.items()]
print('-----ks------');

print(type(ks))
print(ks)

vs = [v for k, v in params.items()]
print('-----vs------');

print(type(vs))
print(vs)

ss = ["%s=%s" % (k, v) for k, v in params.items()]
print('-----ss------');

print(type(ss))
print(ss)
