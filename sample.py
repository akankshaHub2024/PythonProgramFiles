#Numeric DT
a=10
b=20.190
c=5+2j
print(c.real,c.imag)
print(type(c))
#Sequenc DT
l1=[1,2,3,4,5,6]
l1[0]=65
print(l1)
t1=(1,2,3)
print(t1)
r1=range(4,50,4)
print(list(r1))
d1={"name":"akanksha","surname":"konda"}
print(d1["name"])
s1={1,2,3,"Hello",3}
# s1[0]=4
print(s1)
f1=frozenset(l1)
l1[0]=89
print(f1)
b1=5<8
print(b1)
binary1=bytes(b"Hello")
print(binary1,type(binary1))
binary2=bytearray(b"Hello")
m=memoryview(binary2)
m[0]=65
print(binary2,type(binary2),m)


