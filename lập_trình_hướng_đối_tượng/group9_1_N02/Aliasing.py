class Number : 
    i = 0 
class PassObject():
    def f(self, m):
        m.i = 15
if __name__ == "__main__":
    n = Number()
    n.i = 14 
    obj = PassObject()
    obj.f(n)
    print(f"giá trị của n.i : {n.i}")


