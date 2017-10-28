class A:
    def explore(self):
        print("explore() method called")

class B:
    def search(self):
        print("search() method called")

class C:
    def discover(self):
        print("discover() method called")

class D(A, B, C):
    def test(self):
        print("test() method called")


d_obj = D()
d_obj.explore()
d_obj.search()
d_obj.discover()
d_obj.test()