# Method Resolution Order (MRO)

# Linear
```
class A:
    def show(self):
        print("A")

class B:
    def show(self):
        print("B")

class C(A,B):
    pass

c = C()

c.show() // A - C-> A -> B -> object
```

# Diamond
```
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B,C):
    pass

d = D()
d.show() // B - D -> B -> C -> A -> object

```

# Tasks
1 Add a middleware to authenticate user request before delivering data
2 Brand name
3 Navigation - Home, Contact
4 Body - It should deliver with respect to page. hint - different content for Home and different content for contact 
5 Year and copyright info