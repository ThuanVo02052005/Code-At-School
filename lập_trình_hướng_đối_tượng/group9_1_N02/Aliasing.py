class Number : 
    i = 0 
def f(m):
    m.i = 15 
if __name__ =="__main__":
    n = Number()
    n.i = 14 
    f(n)
    print(f"giá trị của n.i: {n.i}")

