class Number :
    n1 = 2 
    n2 = 5 
    def Hoandoi(self):
        self.n1 = self.n2
        self.n2 = 10 
        self.n1 = 20 
    def Hienthi(self):
        print(f"giá trị n1 :{self.n1}")
        print(f"giá trị n2: {self.n2}")
giatri = Number()
giatri.Hoandoi()
giatri.Hienthi()

