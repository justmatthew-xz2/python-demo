ss = int(input("Nhập số giây cần đổi >>>"))

d = ss // 86400
h = ss // 3600 - d*24
m = ss // 60 - h*60 - d*24*60
s = ss - d*24*60 - h*60*60 - m*60

print(f" {ss} giây = {d} ngày {h} giờ {m} phút {s} giây")
