class MyClass : 
    my_string = "năm hai đại học"
    def __init__(self):
        self.you_string = "năm ba đại học "
    def showInfo(self):
        print(f"{MyClass.my_string}")
        print(f"{self.you_string}")
if __name__ == "__main__":
    obj = MyClass()
    obj.showInfo()
# sự khác biệt : 
# khởi tạo tại điểm định nghĩa : 
# biến này được khởi tạo ngay sau khi tạo lớp 
# biến là mặc định và không thay đổi được trừ khi thay đỏi thủ công 
# biến này thuộc về lớp 
# khai báo sử dụng constructor 
# khi khai báo 1 đối tượng biến này sẽ dcd tham chiếu đến 
# mỗi đối tượng sẽ có 1 giá trị 
