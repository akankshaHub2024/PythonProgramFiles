a1=[10,20,30,40,50]
print(sum(a1))
count=0
for i in a1:
    count+=i
print(count)
sumval=sum([i for i in a1])
print(sumval)
a2=[[1,2],[3,4],[5,6]]
suminner=sum([sum(z) for z in a2])
innersum=list(([sum(z) for z in a2]))

print(suminner)
print(innersum)
t1=(1,2,3,4)
print(sum(t1))

from itertools import chain
a2=[[1,2],[3,4],[5]]
total=sum(chain.from_iterable(a2))
print(total)

