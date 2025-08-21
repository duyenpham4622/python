'''
Cài đặt lớp hình chữ vuông theo thiết kế
Có 1 fields (thuộc tính): cạnh
Có các phương thức: 
- tính diện tích (area)
- tính chu vi (perimeter)
- hiện thị cơ bản (display)
Phạm vi khai báo class HinhVuong được tính từ phím tab sau class HinhVuong
'''
class HinhVuong:
    '''
Hàm (method) khởi tạo (constructor)
Đây là method (phương thức) đặc biệt phải có khi khai báo class
Mục đích: Để nạp những giá trị ban đầu cho các thể hiện (cụ thể)
của đối tượng khi chạy chương trình
'''
    def __init__(self,canh):
        self.canh = canh
        
    def area(self):
        result = self.canh ** 2
        return result
    def perimeter(self):
        result = self.canh * 4
        return result
    def display(self):
        print(f'Cạnh: {self.canh}, Chu vi: {self.perimeter():.2f}, Diện tich: {self.area():.2f}\n')
        