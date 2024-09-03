class Main : 
    def myMethod():
        print("I just got executed!")
class Number1 : 
    x = 5 
class Number2:
    x = 5 
    def showInfo(self):
        print(f"{self.x}")
def Now():
    myojb1 = Number2()
    myojb1.showInfo()
    myojb2 = Number2()
    myojb2.showInfo()
if __name__ == "__main__":
    Main.myMethod()
    Main.myMethod()
    Main.myMethod()
    myObj = Number1()
    print(myObj.x)
    Now()

  
