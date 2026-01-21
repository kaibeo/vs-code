# Nhập số nguyên n từ bàn phím
n = int(input("Nhập số nguyên n: "))

# Kiểm tra chia hết cho 3 và 5
if n % 3 == 0 and n % 5 == 0:
    print(n, "chia hết cho cả 3 và 5")
else:
    print(n, "không chia hết cho cả 3 và 5")
