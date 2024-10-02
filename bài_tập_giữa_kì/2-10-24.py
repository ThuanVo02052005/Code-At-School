import os

# Tạo folder nếu chưa có
folder_name = 'bai_tap_cuoi_ky'
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Đường dẫn tới file
file_path = os.path.join(folder_name, 'login.txt')

# Mở file để ghi
with open(file_path, 'w') as file:
    file.write('username: password\n')  # Ghi dòng chữ vào file

# File sẽ tự động đóng khi ra khỏi khối with
# Mở file để đọc
with open(file_path, 'r') as file:
    content = file.read()  # Đọc nội dung file

# Hiển thị nội dung ra màn hình
print(content)
