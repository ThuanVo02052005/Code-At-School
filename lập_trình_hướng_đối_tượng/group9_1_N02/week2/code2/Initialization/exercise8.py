class MyClass : 
    area = 0 
    def __init__(self):
        self.pi = int(input("nhập vào số pi "))
    def phuongThuc1(self):
        MyClass.phuongThuc2(self)
        self.phuongThuc2()
    def phuongThuc2(self):
        self.area = self.pi * self.pi 
        print(f"{self.area}")
if __name__ == "__main__":
    obj = MyClass()
    obj.phuongThuc1()
