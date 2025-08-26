import matplotlib.pyplot as plt
import MyPham as mp

menu_options = {
    1: 'Nạp dữ liệu từ file',
    2: 'Thêm sản phẩm',
    3: 'Hiển thị toàn bộ sản phẩm',
    4: 'Xem chi tiết sản phẩm theo mã',
    5: 'Cập nhật thông tin sản phẩm',
    6: 'Xóa sản phẩm',
    7: 'Tăng giá sản phẩm',
    8: 'Giảm giá sản phẩm',
    9: 'Đếm số lượng sản phẩm',
    10: 'Tính tổng giá trị các sản phẩm',
    11: 'Tính giá trung bình',
    12: 'Hiển thị sản phẩm có giá cao nhất',
    13: 'Sắp xếp theo giá tăng dần',
    14: 'Lưu danh sách ra file',
    15: 'Vẽ biểu đồ giá theo sản phẩm',
    16: 'Vẽ biểu đồ giá trung bình theo loại',
    17: 'Vẽ biểu đồ phần trăm số lượng theo loại',
    'Khác': 'Thoát chương trình'
}

def print_menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])

# Danh sách mỹ phẩm
dsMyPham = []

while True:
    print_menu()
    try:
        choice = int(input("Nhập lựa chọn: "))
    except:
        print("Nhập sai định dạng, vui lòng nhập lại!!!")
        continue

    if choice == 1:
        fr = open('dbmypham_input.db', 'r', encoding='utf-8')
        for line in fr:
            stripLine = line.strip('\n')
            ds = line.strip().split(',')
            code = int(ds[0])
            name = ds[1]
            loai = ds[2]
            gia = float(ds[3])
            sp = mp.MyPham(code, name, loai, float(gia))
            dsMyPham.append(sp)
        fr.close()
    elif choice == 2:
        code = int(input("Mã: "))
        name = input("Tên: ")
        loai = input("Loại: ")
        gia = float(input("Giá: "))
        sp = mp.MyPham(code, name, loai, gia)
        dsMyPham.append(sp)
    elif choice == 3:
        if len(dsMyPham) == 0:
            print("Danh sách rỗng")
        else:
            for item in dsMyPham:
                item.display()
    elif choice == 4:
        if dsMyPham.count == 0:
            print("Danh sách rỗng")
        else:
            code = input("Nhập mã sản phẩm: ")
            for item in dsMyPham:
                if item.code == code:
                    item.display()
    elif choice == 5:
        if dsMyPham.count == 0:
            print("Danh sách rỗng")
        else:
            code = input("Nhập mã cần sửa: ")
            for item in dsMyPham:
                if item.code == code:
                    item.display()
                    item.name = input("Tên mới: ")
                    item.loai = input("Loại mới: ")
                    item.gia = float(input("Giá mới: "))
                    item.display()
    elif choice == 6:
        if dsMyPham.count == 0:
            print("Danh sách rỗng")
        else:
            code = input("Nhập mã cần xóa: ")
            for item in dsMyPham:
                if(item.code == code):
                    item.display()
                    tl = input('Bạn có chắc chắn xóa mỹ phẩm này không Y/N?')
                    if tl == 'Y':
                        dsMyPham.remove(item)
        for item in dsMyPham:
            item.display()
    elif choice == 7:
        if dsMyPham.count == 0:
            print("Danh sách rỗng")
        else:
            code = input("Mã sản phẩm cần tăng giá: ")
            for item in dsMyPham:
                if item.code == code:
                    inc = float(input("Nhập số tiền tăng: "))
                    item.tangGia(inc)
                    item.display()
    elif choice == 8:
        code = input("Mã sản phẩm cần giảm giá: ")
        for item in dsMyPham:
            if item.code == code:
                dec = float(input("Nhập số tiền giảm: "))
                item.giamGia(dec)
                item.display()
    elif choice == 9:
        print("Tổng số sản phẩm:", len(dsMyPham))
    elif choice == 10:
        total = sum([item.gia for item in dsMyPham])
        print("Tổng giá trị:", total)
    elif choice == 11:
        avg = sum([item.gia for item in dsMyPham]) / len(dsMyPham) if dsMyPham else 0
        print("Giá trung bình:", avg)
    elif choice == 12:
        if dsMyPham.count == 0:
            print("Danh sách rỗng")
        else:
            for item in dsMyPham:
                max_price = item.gia
                break
            for item in dsMyPham:
                if(item.gia > max_price):
                    max_price = item.gia
        print("Sản phẩm có giá cao nhất:",max_price)
    elif choice == 13:
        dsMyPham.sort(key=lambda x: x.gia)
        print("Đã sắp xếp theo giá tăng dần")
    elif choice == 14:
        fw = open("dbmypham_output.db", "w", encoding="utf-8")
        for item in dsMyPham:
            fw.write(f"{item.code},{item.name},{item.loai},{item.gia},{item.hansd},{item.thuonghieu}\n")
        fw.close()
        print("✅ Đã lưu file dbmypham_output.db")


    elif choice == 15:
        # Vẽ biểu đồ giá theo sản phẩm
        labels = [item.name for item in dsMyPham]
        prices = [item.gia for item in dsMyPham]
        plt.bar(labels, prices, color='skyblue')
        plt.xticks(rotation=45, ha='right')
        plt.title("Biểu đồ giá theo sản phẩm")
        plt.ylabel("Giá (VND)")
        plt.show()

    elif choice == 16:
        # Vẽ giá trung bình theo loại
        loai_dict = {}
        for item in dsMyPham:
            loai_dict.setdefault(item.loai, []).append(item.gia)
        loais = list(loai_dict.keys())
        avg_prices = [sum(g)/len(g) for g in loai_dict.values()]
        plt.bar(loais, avg_prices, color='orange')
        plt.title("Giá trung bình theo loại sản phẩm")
        plt.ylabel("Giá trung bình (VND)")
        plt.show()

    elif choice == 17:
        # Vẽ phần trăm số lượng sản phẩm theo loại
        category_count = {}
        for item in dsMyPham:
            category_count[item.loai] = category_count.get(item.loai, 0) + 1
        labels = category_count.keys()
        values = category_count.values()
        plt.pie(values, labels=labels, autopct='%1.1f%%')
        plt.title("Tỉ lệ % số lượng sản phẩm theo loại")
        plt.show()

    else:
        print("BYE BYE")
        break
