def ssinput():
    global ss

    ss = str(input('Nhập số giây cần quy đổi (ghi /"exit/" để thoát?) >>> '))
    while ss.isdigit() is not True:
        print("! Bạn chỉ được nhập số !")
        ss = str(
            input('Nhập số giây cần quy đổi (ghi /"exit/" để thoát) >>> '))
        ssconvert(ss)
        return False


def ssconvert(ss):
    ss = int(ss)
    global options

    d = ss // 86400
    h = ss // 3600 - d*24
    m = ss // 60 - d*24*60 - h*60
    s = ss - d*24*60*60 - h*60*60 - m*60
    print(f'{ss} giây = {d} ngày {h} giờ {m} phút {s} giây')
    print('')
    ssinput()


""" def go():
    global options

    options = str(input('Bạn muốn tiếp tục? (Y/N): ')).lower()
    try:
        if options in ['y', 'n']:
            if options == 'y':
                return True
            elif options == 'n':
                return False
        else:
            return False
    except:
        return False """


def ssinput():
    global ss

    ss = str(input('Nhập số giây cần quy đổi (ghi /"exit/" để thoát) >>> '))
    if ss == "exit":
        return True
    else:
        while ss.isdigit() is not True:
            print("! Bạn chỉ được nhập số !")
            ss = str(
                input('Nhập số giây cần quy đổi (ghi /"exit/" để thoát) >>> '))
            if ss == "exit":
                return True
        ssconvert(ss)
        return False


def ssconvert(ss):
    ss = int(ss)
    global options

    d = ss // 86400
    h = ss // 3600 - d*24
    m = ss // 60 - d*24*60 - h*60
    s = ss - d*24*60*60 - h*60*60 - m*60
    print(f'{ss} giây = {d} ngày {h} giờ {m} phút {s} giây')
    print('')
    ssinput()


""" def go():
    global options

    options = str(input('Bạn muốn tiếp tục? (Y/N): ')).lower()
    try:
        if options in ['y', 'n']:
            if options == 'y':
                return True
            elif options == 'n':
                return False
        else:
            return False
    except:
        return False """


while True:
    ssinput()
    if ss == "exit":
        break
