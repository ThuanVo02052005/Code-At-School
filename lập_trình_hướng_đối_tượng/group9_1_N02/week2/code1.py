import math 
# creat classes
# Book.py
class Book : 
    def __init__(self, t , a , p ):
        self.t = t 
        self.a = a 
        self.p = p 
    def showInfo(self):
        print("hiển thị : ", self.t)
        print("hiển thị: ", self.a)
        print("hiển thị: ", self.p)
def showbook():
    myObj = Book("a", "b", 2)
    myObj.showInfo()
#Time.py
class Time : 
    def __init__(self, h = 0 , m = 0 , s = 0 ):
        self.set_time(h , m , s )
    def set_time(self , h , m , s):
        self.setHour(h)
        self.setMinute(m)
        self.setSecond(s)
        return self 
    def setHour(self , h):
        self.hour = h if (h >= 0 and h < 24 ) else 0 
        return self 
    def setMinute(self, m):
        self.minute = m if (m >= 0 and m < 60 ) else 0 
        return self 
    def setSecond(self , s):
        self.second = s if (s >= 0 and s < 60 ) else 0 
        return self
    def getHour(self):
        return self.hour 
    def getMinute(self):
        return self.minute
    def getSecond(self):
        return self.second
    def __str__(self):
        return f"{self.hour:02}:{self.minute:02}:{self.second:02}"
def ShowTime():
    t1 = Time()
    t2 = Time(20 , 3 , 45)
    t1.setHour(7)
    t1.setMinute(32)
    t1.setSecond(23)
    print("t1 is ", t1)
    print("t2 is", t2)
#Recursion.py
class Recursion : 
    def factorial(self, n ):
        self.n = n 
        if (self.n < 0 ):
            print("không thể tính gia thừa")
        elif(self.n == 0 ):
            return 1 
        else: 
            return self.n * self.factorial(n - 1)
def showRecursion(): 
    n = int(input("nhập vào giá trị giai thừa cần tính: "))
    giaithua = Recursion()
    print(f"giá trị {n}! cần tính {giaithua.factorial(n)} ")
#NNColection.py
class NNCollection:
    def __init__(self):
        self.nn_array = [None] * 100
        self.free = 0

    def insert(self, n):
        index = 0
        self.free += 1
        for i in range(self.free - 1, 0, -1):
            if self.nn_array[i - 1] is not None and self.nn_array[i - 1].get_last_name() > n.get_last_name():
                self.nn_array[i] = self.nn_array[i - 1]
                index = i
            else:
                break
        self.nn_array[index] = n

    def find_number(self, l_name):
        for i in range(self.free):
            if self.nn_array[i] is not None and self.nn_array[i].get_last_name() == l_name:
                return self.nn_array[i].get_tel_number()
        return "Name not found"
#NameNumber.py
class NameNumber :
    def __init__(self, name , num ):
        self.lastname = name 
        self.telnumber = num 
    def getLastName(self):
        return self.lastname
    def gettelname(self):
        return self.telnumber

if __name__ == "__main__":
    showbook()
    ShowTime()
    showRecursion()
    
 