import os
os.system('cls')
database={
 'python':'khoi dau',
 'html':'tiep theo'
}
#-----------------
def show_menu():
    print('**************************')
    print('Chuong trinh note V.0.0.1')
    print('**************************')
    print('1.Them du lieu')
    print('2.Xoa')
    print('3.Tim')
    print('4.Xem tat ca')
    print('An 0 de thoat')
#------------------------------
def add():
 data=input('Du lieu moi:')
 note=input('Ghi chu:')
 database[data]=note
 print('Da them du lieu.(●ˇ∀ˇ●)');
def find():
    data=input('+Nhap du lieu can tim: ')
    if data in database:
        print('Tim thay: [%s: %s]' % (data,database[data]))
    else:
        print('Khong tim thay du lieu: [%s]' % data)
def delete():
    data=input('Du lieu gi: ')
    if data in database:
        del database[data]
        print('Du lieu [%s] da bi xoa'%data)
    else:
        print('Khong tim thay du lieu: [%s]'%data)
def view_all():
    for data,note in database.items():
     print('[%s: %s]'%(data,note));
#menu
show_menu()
#--------------
choice=int(input('Hay nhap lua chon: '))
while choice !=0:
    if choice==0:
        break
    elif choice==1:
        add(); 
        choice=int(input('Hay nhap lua chon: '))     
    elif choice==2:
        delete();
        choice=int(input('Hay nhap lua chon: '))
    elif choice==3:
        find();
        choice=int(input('Hay nhap lua chon: '))
    elif choice==4:
        view_all();  
        choice=int(input('Hay nhap lua chon: '))  
    else:
        print('Khong co lua chon nay!!!')
        choice=int(input('Hay nhap lua chon: '))
print('Cam on da dung []~(0▽0)~*')