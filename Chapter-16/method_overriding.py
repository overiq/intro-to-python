class A:
    def explore(self):
        print("explore() method from class A")

class B(A):
    def explore(self):
        print("explore() method from class B")


b_obj = B()
a_obj = A()

b_obj.explore() # child class object is used to call overridden method, so child class version of the object will be called
a_obj.explore()