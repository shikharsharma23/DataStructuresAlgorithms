class test:
    def __init__(self,a,b):
        self.a = a
        self.b = b



a = [2,3,4]
b = a

b.append(5)

print(a)
print(b)


obj1 = test(2,3)

obj2 = obj1

obj2.a = 5

print(obj1.a)
print(obj2.a)

## both for lists assignment and object assignment within a global scope, we see it is pass by reference

b = obj1.a
b = 7
print(b)
print(obj1.a)

print(type(obj1.a))
print(type(obj1))

## for primitives / values being assigned to other variables, a subpart of some structure, then it is pass by value

a = [1,2,3]



