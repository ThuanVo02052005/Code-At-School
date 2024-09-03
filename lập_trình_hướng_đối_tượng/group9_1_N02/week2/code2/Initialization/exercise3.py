class MyClass: 
    def __init__(self, my_string = None):
        if my_string : 
            print(f"Do you speak English {my_string}")
        else : 
            print("Do you speak English")
    
if __name__ == "__main__":
    obj = MyClass("yes")
