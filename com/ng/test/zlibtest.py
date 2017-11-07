import zlib
s = b'witch which has which witches wrist watch'
print(len(s))
t = zlib.compress(s)
print(t);

s1=zlib.decompress(t)
t1=zlib.crc32(s)
print(type(s1))
print(type(t1));
print(3**(1/3))