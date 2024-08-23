class Number :
    n1 = 2 
    n2 = 5 
    def hoandoi(self):
        self.n1 = self.n2
        self.n2 = 10 
    def hienthi(self):
        print(f"giá trị của n1 sau hoán đổi : {self.n1}")
        print(f"giá trị của n2 sau hoán đổi : {self.n2}")


giatri = Number()
giatri.hoandoi()
giatri.hienthi()