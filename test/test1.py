
# from tkinter import Tk, BOTH
# from tkinter.ttk import Frame, Button, Style

# class Example(Frame):
#     def __init__(self, parent):
#        Frame.__init__(self, parent)
#        self.parent = parent
#        self.initUI()
#     def initUI(self):
#        self.parent.title("Quit button")
#        self.style = Style()
#        self.style.theme_use("default")

#        self.pack(fill=BOTH, expand=1)
#        quitButton = Button(self, text="Quit", command=self.quit)
#        quitButton.place(x=100, y=100)

# root = Tk()
# root.geometry("250x150+300+300")
# app = Example(root)
# root.mainloop()
# import tkinter as tk
# from tkinter import messagebox

# def register():
#     messagebox.showinfo("Thông báo", "Bạn đã đăng ký thành công!")

# def cancel():
#     messagebox.showinfo("Thông báo", "Bạn đã hủy đăng ký!")

# # Tạo cửa sổ chính
# root = tk.Tk()
# root.title("Giao diện Đăng ký Học")

# # Tạo nút Đăng ký
# register_button = tk.Button(root, text="Đăng ký", command=register)
# register_button.pack(pady=10)

# # Tạo nút Hủy đăng ký
# cancel_button = tk.Button(root, text="Hủy đăng ký", command=cancel)
# cancel_button.pack(pady=10)

# # Chạy vòng lặp chính
# root.mainloop()
# from tkinter import *
# #Thêm thư viện tkinter
# from tkinter import *

# #Tạo một cửa sổ mới
# window = Tk()

# #Thêm tiêu đề cho cửa sổ
# window.title('Welcome to VniTeach app')

# #Đặt kích thước của cửa sổ
# window.geometry('350x200')

# #Lặp vô tận để hiển thị cửa sổ
# window.mainloop()

# window = Tk()
# window.title("Welcome to VniTeach app")

# #Thêm label có nội dung Hello, font chữ
# lbl = Label(window, text="Hello", font=("Arial Bold", 50))

# #Xác định vị trí của label
# lbl.grid(column=0, row=0)

# window.mainloop()


from tkinter import * 
from PIL import  ImageTk , Image 
anh = Tk()
anh.title('thuan bruno')
anh.geometry('400x400')
anh.attributes('-topmost' , True)
img_import = (Image.open(r'D:\ảnh\ảnh_chế.jpg'))
resize = img_import.resize((300, 300), Image.LANCZOS)
img = ImageTk.PhotoImage(resize)
#tải ảnh về 
logo_import= Image.open("D:\ảnh\ảnh_logo.jpg")
logo = ImageTk.PhotoImage(logo_import)
# Thay đổi logo của cửa sổ
anh.iconphoto(False, logo)
hinh_anh = Button (anh , text = ' ' , font = ('time new roman', 12), image=img)
hinh_anh.place(x = 60 , y = 60)

anh.mainloop()


