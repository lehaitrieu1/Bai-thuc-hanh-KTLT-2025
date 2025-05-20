print("sinh vien: Le Hai Trieu")
print("Mssv: 235752020710021")
def read_entire_file(file_path):
#Định nghĩa một hàm có tên là read_entire_file, nhận vào tham số file_path là đường dẫn đến tệp cần đọc.
    try:
    #Bắt đầu một khối try-except để xử lý lỗi (nếu có lỗi khi đọc tệp).
        with open(file_path, 'r', encoding='utf-8') as file:
        
