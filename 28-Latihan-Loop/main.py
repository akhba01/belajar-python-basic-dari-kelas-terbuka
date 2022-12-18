#Latihan perulangan membuat segitiga

sisi = 10

# 1. Menggunakan for
# dummy variable
print("awal dari for")
count = 1
for i in range(4):
    print("*"*count)
    count +=1

print("akhir dari for ") 
# 2. Menggunakan while

print("awal while")
count = 1
while True :
    print("*"*count)
    count+=1

    if count > sisi:
        break

print("akhier while")


# 3. hanya ganjil saja
print("awal while")
count = 1
while True :
    # akan kembali ke atas jika ganjil
    if count % 2 == 0 :
        count += 1
        continue

    # akan print jika genap
    print("*"*count)
    count+=1

    # akan break jika count melebihi sisi
    if count > sisi:
        break

print("akhier while")

# 4. hanya ganjil saja
print("awal while")
count = 1
spasi = int(sisi/2)
print(spasi)
while True :
    # akan kembali ke atas jika ganjil
    if count % 2 == 1 :
        print(" "*spasi,"+"*count)
        spasi -= 1
        count += 1
    else:
        # akan kembali ke  atas jika ganjil
        count += 1
        continue
    
    # akan break jika count melebihi sisi
    if count > sisi:
        break

print("akhier while")

# 5. ketupat 
  # membuat variabel untuk menentukan tinggi pola rombus
tinggi = 5

# looping untuk mencetak setiap baris pola rombus
for i in range(tinggi):
  # mencetak spasi pada setiap baris
  for j in range(tinggi-i-1):
    print(" ", end="")
  
  # mencetak bintang pada setiap baris
  for j in range(i+1):
    print("* ", end="")
  
  # pindah ke baris berikutnya
  print() 
