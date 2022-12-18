data_angka = [1, 5, 1, 3, 1, 5, 6, 7, 3, 3, 8, 4, 0, 1, 4]
print(f"data angka = \n{data_angka}")


# count data
jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)


print(f"jumlah angka 4 = {jumlah_data_4}")
print(f"jumlah angka 3 = {jumlah_data_3}")


# ambil posisi data (index)

data = ["Ucup", "Otong", "Dudung", "Ujang"]

print(f"data = {data}")

index_dudung = data.index("Dudung")
index_ujang = data.index("Ujang")
print(f"index si Dudung = {index_dudung}")
print(f"index si Ujang = {index_ujang}")

# data.index("usep") error


# mengurutkan list
print(f"data angka sebelum sort = \n{data_angka}")
data_angka.sort()
print(f"data angka sort = \n{data_angka}")

print(f"data = {data}")
data.sort()
print(f"data sort  = {data} ")


# balik listnya
data_angka.reverse()
data.reverse()
print(f"data di reverse = \n{data_angka} \n{data}")
