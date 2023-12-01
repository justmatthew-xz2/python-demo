def ssconvert(ss):
    ss = int(ss)

    d = ss // 86400
    h = ss // 3600 - d*24
    m = ss // 60 - d*24*60 - h*60
    s = ss - d*24*60*60 - h*60*60 - m*60
    print(f'{ss} giây = {d} ngày {h} giờ {m} phút {s} giây')
    print('')


def ssinput():
    global ss

    ss = str(input('Nhập số giây cần quy đổi (ghi /"exit/" để thoát) >>> '))

    if ss == "exit":
        return False
    else:
        while ss.isdigit() is not True:
            print("! Bạn chỉ được nhập số từ 0 trở lên !")
            ss = str(input('Nhập số giây cần quy đổi (ghi /"exit/" để thoát) >>> '))

            if ss == 'exit':
                return False

        ssconvert(ss)
        return True


while True:
    if ssinput() is False:
        break
