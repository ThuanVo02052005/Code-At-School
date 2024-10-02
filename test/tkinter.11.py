# #thêm thư viện tkinter 
# from tkinter import * 
# #tạo 1 cứ sổ giao diện
# win = Tk()
# #đặt tên cho nó 
# win.title("thuan bruno")
# #tạo ra giao diện hộp thoại 
# win.geometry('500x300')
# # sửa đổi màu nền 
# win['bg'] = 'white'
# #hiển thị lên trên cử sổ khác 
# win.attributes('-topmost', True)
# # tạo label 
# name = Label(win , text = "hello em", font =('time new Roman', 14), bg = 'yellow', fg = 'red')
# name.place(x= 50 , y = 30)
# #hàm để thực hiện chức năng sau khi click vào 
# def anvao():
#     name1 = Label(win , text = "bạn đã click vào ", font =('Arial', 14), bg = 'yellow', fg = 'red')
#     name1.place(x= 50  , y = 300)
#     but1 = Button(win , text="click to click", bg = 'yellow', fg = 'red', width = 10 , height = 2, command= anvao)
#     but1.place(x = 50 , y = 320)
# #tạo 1 nút 
# but = Button(win , text="click to click", bg = 'yellow', fg = 'red', width = 30 , height = 10, command= anvao)
# but.place(x = 50 , y = 100)
# #tạo entry nhập liệu với tkinter 
# from tkinter import *
# topgod = Tk()
# topgod.geometry('400x300')
# topgod.title('thuận thật đẹp trai')
# topgod.attributes('-topmost', True)
# entry = Entry(topgod , width = 5 , font =('time new Roman', 14))
# entry.place(x = 5, y = 10)
# entry.focus()
# topgod.mainloop()
# win.mainloop()
# from tkinter import * 
# now =Tk()
# now.geometry('400x300')
# now.title('thuan fan MU')
# now['bg'] = 'white'
# a = Label(now , text = 'fan MU' , font = ('time new Roman' , 14) , bg = 'white', fg = 'black')
# a.place(x = 20 , y = 20 )
# def nhapvao():
#     entry = Entry(now , width = 7 , font = ('time new Roman', 16))
#     entry.place(x = 50 , y = 70)
# but = Button(now , text = 'click fan MU', font = ('arial', 12), bg = 'yellow' , fg = 'pink',width = 20 , height = 20, command = nhapvao )
# but.place(x = 40 , y = 60 )
# now.mainloop()
# from tkinter import * 
# min = Tk()
# min.title('võ hữu thuận ')
# min.geometry('500x400')
# min['bg'] = 'white'
# min.attributes('-topmost', True)
# a1 = Label(min , text = 'số thứ nhất:', font = ('time new Roman', 13))
# a1.place(x = 10 , y = 10 )
# a2 = Label(min , text = 'số thứ nhất:', font = ('time new Roman', 13))
# a2.place(x = 10 , y = 50)
# c1= Entry(min ,width= 20 , font = ('time new roman ', 12) )
# c1.place(x = 100, y = 10 ) 
# c1.focus()
# c2 = Entry(min ,width= 20 , font = ('time new roman ', 12) )
# c2.place(x = 120, y = 50 ) 
# c2.focus()
# def hienthi():
#     a = Label(min , text = float(c1.get()) + float(c2.get()), font = ('time new Roman', 16))
#     a.place(x = 150, y = 80 )
#     now = Tk()
#     now.title('AI')
#     now.geometry('300x400')
#     now.attributes('-topmost', True)
#     def hienthi2():

#         a = Label(now, text = 'tôi rất tiếc vì điều đó', font = ('time new Roman', 16))
#         a.place(x = 20, y = 140)

    
#     a3 = Label(now , text = 'bạn đag cảm thấy như thế nào:', font = ('time new Roman', 15))
#     a3.place(x = 20 , y = 20)
#     c3= Entry(now ,width= 20 , font = ('time new roman ', 15) )
#     c3.place(x = 20, y = 60) 
#     b1 = Button(now, text = 'Ok' , font = ('time new roman', 12), width = 10, command = hienthi2)
#     b1.place(x = 20 , y = 100)
    
#     now.mainloop()

# b = Button(min, text = 'tổng 2 số : ' , font = ('time new roman', 12), width = 10, command = hienthi)
# b.place(x = 10 , y = 80)


# min.mainloop()

# from tkinter import * 
# sinhvien = Tk()
# sinhvien.geometry('700x700')
# sinhvien.title('Phenikaa university')
# sinhvien.attributes('-topmost', False)
# def taikhoan():
#     sinhvien.withdraw() 
#     taikhoan = Tk()
#     taikhoan.geometry('500x500')
#     taikhoan.title('Phenikaa University')
#     taikhoan.attributes('-topmost', True)
#     def hienthi3():
#        a3 = Label(taikhoan , text = b.get(), font = ('time new roman', 12))
#        a3.place(x = 120, y = 10)
#        a4 = Label(taikhoan , text = b.get(), font = ('time new roman', 12))
#        a4.place(x = 120, y = 40)  
#     def themsinhvien():
#         a3 = Label(taikhoan , text = 'ho va ten', font = ('time new roman', 12))
#         a3.place(x = 100, y = 100)
#         b2= Entry(taikhoan,width= 20 , font = ('time new roman ', 12))
#         b2.place(x = 200, y = 100 ) 
#         b2.focus()
#         a4 = Label(taikhoan , text = 'maSV:', font = ('time new roman', 12))
#         a4.place(x = 100, y = 140) 
#         b3= Entry(taikhoan,width= 20 , font = ('time new roman ', 12))
#         b3.place(x = 200, y = 140 ) 
#         a5 = Label(taikhoan , text = 'diachi:', font = ('time new roman', 12))
#         a5.place(x = 100, y = 160) 
#         b4= Entry(taikhoan,width= 20 , font = ('time new roman ', 12))
#         b4.place(x = 200, y = 160) 

#     c2= Button(taikhoan, text = 'hienthi' , font = ('time new roman', 12), width = 10, bg = 'blue', fg = 'white', command = hienthi3)
#     c2.place(x = 10 , y = 10)
#     c2.focus()
#     c2= Button(taikhoan, text = 'them' , font = ('time new roman', 12), width = 10, bg = 'red', fg = 'white', command = themsinhvien)
#     c2.place(x = 10 , y = 60)
#     c2.focus()
#     taikhoan.mainloop()
# a = Label(sinhvien , text = 'Đăng Nhập', font = ('time new roman', 20), fg = 'blue')
# a.place(x = 300, y = 20)
# a1 = Label(sinhvien , text = 'nhập tài khoản hoặc email: ', font = ('time new roman', 12))
# a1.place(x = 100, y = 80)
# a2 = Label(sinhvien , text = 'nhập mật khẩu: ', font = ('time new roman', 12))
# a2.place(x = 100, y = 120)
# b= Entry(sinhvien,width= 30 , font = ('time new roman ', 12))
# b.place(x = 300, y = 80 ) 
# b.focus()
# b1= Entry(sinhvien,width= 30 , font = ('time new roman ', 12))
# b1.place(x = 300, y = 120)
# b1.focus()
# c= Button(sinhvien, text = 'Đăng Nhập' , font = ('time new roman', 12), width = 10, bg = 'blue', fg = 'white' , command= taikhoan)
# c.place(x = 100 , y = 200)

# sinhvien.mainloop()
