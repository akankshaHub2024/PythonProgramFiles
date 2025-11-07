l1=[1,2,3,4,5,4,4,4,4]
mul=1
for i in l1:
    mul=mul*i
print(mul)
import operator
from functools import reduce
print(reduce(operator.mul,l1))
print(reduce(operator.add,l1))
print(reduce(operator.sub,l1))
list2=[[1,2],[1,2],[1]]
from  itertools import chain
multi1=reduce(operator.mul,chain.from_iterable(list2))
print(multi1)
print(sum(chain.from_iterable(list2)))
print(l1.count(4))
