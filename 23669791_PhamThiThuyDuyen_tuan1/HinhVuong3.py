'''
Lưu trữ danh sách các hình vuông từ file input.db
Lưu danh sách các hình chữ nhật xuống file output.db theo định dạng
canh-chuvi-dientich
Lưu ý: Trong các file mỗi hàng là thông tin một hình
'''
import HinhVuong as hV 
#Tải dữ liệu từ file vào dsHinhVuong
fr = open('input.db',mode = 'r',encoding='utf-8')
dsHinhVuong = []
for line in fr:
    stripLine = line.strip('\n')
    ds = stripLine.split(',')
    c = float(ds[0])
    hv = hV.HinhVuong(c)
    dsHinhVuong.append(hv)
fr.close()
# Ghi dữ liệu từ dsHinhVuong xuống file
fw = open('output.db',mode='w',encoding='utf-8')
for item in dsHinhVuong:
    fw.write(f'{item.canh}-{item.perimeter()}-{item.area()}\n')
fw.close()
'''
(*) Sinh viên tự thực hành
Viết chương trình menu
1- Đọc dữ liệu từ file input.db
2- Thêm mới hình chữ nhật
3- Hiển thị danh sách hình chữ nhật
4- Lưu danh sách hình chữ nhật xuống file demo4output.db
Others- Thoát
'''
import HinhVuong as hV 
menu ={
1:'Đọc dữ liệu từ file input.db'   ,
2:'Thêm mới hình chữ nhật',
3:'Hiển thị danh sách hình chữ nhật',
4:'Lưu danh sách hình chữ nhật xuống file demo4output.db',
'Others':'Thoát'
}
def print_menu():
    for key in menu.keys():
        print(key,'--',menu[key])
while(True):
    print_menu()
    Chon = ''
    try:
        Chon = int(input('Nhập tùy chon: '))
    except:
        print('Nhập sai định dạng,vui lòng nhập lại!!!')
        continue
    
    if Chon == 1:
        fr = open('input.db',mode = 'r',encoding='utf-8')
        dsHinhVuong = []
        for line in fr:
            stripLine = line.splip('\n')
            ds = stripLine.split(',')
            c = float(ds[0])
            hv = hV.HinhVuong(c)
            dsHinhVuong.append(hv)
        fr.close()
    if Chon == 2:
        c = float(input('Nhập độ dài cạnh: '))
        hv = hV.HinhVuong(c)
        dsHinhVuong.append(hv)
    if Chon == 3:
        if dsHinhVuong.count == 0:
            print('Danh sách rỗng')
        else:
            for item in dsHinhVuong:
                item.display()
    if Chon == 4:
        fw = open('outputdemo4.db',mode='w',encoding='utf-8')
        for item in dsHinhVuong:
            fw.write(f'{item.canh}-{item.perimeter()}-{item.area()}\n')
        fw.close()
    else:
        print('Thoát.')
        break
