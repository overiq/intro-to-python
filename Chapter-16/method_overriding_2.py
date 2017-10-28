class A:
    def explore(self):
        print("explore() method from class A")

class B(A):
    def explore(self):
        super().explore()  # calling the parent class explore() method
        print("explore() method from class B")


b_obj = B()
b_obj.explore()