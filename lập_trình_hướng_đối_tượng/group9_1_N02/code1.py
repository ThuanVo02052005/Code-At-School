import math 
class book : 
    def __init__(self, t , a , p ):
        self.t = t 
        self.a = a 
        self.p = p 
    def showInfo(self):
        print("hiển thị : ", self.t)
        print("hiển thị: ", self.a)
        print("hiển thị: ", self.p)
class Recursion: 
    def __init__(self):
        self.n = int(input("nhập vào số n : "))
    def factorial(self):
        if (self.n == 1  ):
            return 1 
        else: 
            return self.n * self.factorial(self.n - 1)
if __name__ == "__main__":

