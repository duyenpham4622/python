class MyPham:
    def __init__(self, code, name, loai, gia):
        self.code = code
        self.name = name
        self.loai = loai
        self.gia = gia

    def display(self):
        print(f"Mã: {self.code}, Tên: {self.name}, Loại: {self.loai}, Giá: {self.gia}")

    def tangGia(self, amount):
        if amount > 0:
            self.gia += amount

    def giamGia(self, amount):
        if 0 < amount <= self.gia * 0.2:   # giảm tối đa 20%
            self.gia -= amount
    def display(self):
        print(f'code: {self.code}, name: {self.name}, age: {self.loai}, salary: {self.gia},income: {self.income()}\n')
