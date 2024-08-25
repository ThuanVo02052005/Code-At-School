class Number :
    i = 0 
if __name__ == "__main__":
    n1 = Number()
    n2 = Number()
    n1.i = 2 
    n2.i = 5 
    n1 = n2 
    print(f"giá trị của n1.i : {n1.i}")
    n2.i = 10 
    print(f"giá trị của n1.i : {n1.i}")
    print(f"giá trị của n2.i: {n2.i}")
    n1.i = 20 
    print(f"giá trị của n2.i: {n2.i}")
    print(f"giá trị của n1.i: {n1.i}")

