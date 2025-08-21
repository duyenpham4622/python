'''
Chương trình menu
1- Thêm mới hình vuông
2- Hiển thị danh sách hình vuông
3- Tính tổng diện tích các hình vuông
4- Hiển thị các hình vuông có chu vi nhỏ nhất
Others- Thoát
'''
import HinhVuong as HV
menu_option = {
    1:'Thêm mới hình vuông',
    2:'Hiển thị danh sách hình vuông',
    3:'Tính tổng diện tích các hình vuông',
    4:'Hiển thị các hình vuông có chu vi nhỏ nhất',
    'Orthers':'Thoát'
}
def print_menu():
    for key in menu_option.keys():
        print(key,'--',menu_option[key])
        
#Khai báo biến lưu trữ hình vuông
dsHV = []
while(True):
    print_menu()
    Chon = ''
    try:
        Chon = int(input('Nhập tùy chon: '))
    except:
        print('Nhập sai định dạng,vui lòng nhập lại!!!')
        continue
    
    if Chon == 1:
        c = float(input('Nhập độ dài cạnh: '))
        hv = HV.HinhVuong(c)
        dsHV.append(hv)
    elif Chon == 2:
        for item in dsHV:
            item.display()
    elif Chon == 3:
        DienTich = 0.0
        for item in dsHV:
            DienTich = DienTich + item.area()
        print(f'Tổng diện tích là: {DienTich}')
    elif Chon == 4:
        if dsHV.count == 0:
            print('Danh sách rỗng')
        else:
            chuvi = dsHV[0].perimeter()
            for item in dsHV:
                if chuvi > item.perimeter():
                    chuvi = item.perimeter()
            for item in dsHV:
                if item.perimeter() == chuvi:
                    item.display()
    else:
        print('Thoát.')
        break