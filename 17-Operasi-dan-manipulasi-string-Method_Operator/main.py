# Operator dalma bentuk methods

# merubah case dari string

# merubah ke upper case

salam = "bro!"
print("normal = " + salam )
salam = salam.upper()

# merubah semua ke lowe case
alay = "aKu KeCe AbieZZZzZZ"
print("normal = " + alay)
alay = alay.lower()
print("lower = " + alay)

## pengecekan dengan isX method

#contoh pengecekan lowe case
salam = "sist"
apakah_lower = salam.islower()
print(salam + "is lower =" + str(apakah_lower))
apakah_upper = salam.isupper() #hasilnya bool
print(salam + "is upper =" + str(apakah_upper))


# isalpha() <-- untuk mengecek semuanya huruf
# isalnum() <-- huruf dan angka
# isdecimal() <-- angka
# isspace() <--- spasi, tab, newline \n
# istitle() <--- semua kaa dimulai dengan huruf besar


judul = "It Is Okay Not To Be Orkay"
cek_judul = judul.istitle() #hasilnya bool

print(judul + " is title = " + str(cek_judul))

## ngecek komponen startswith() endwith() <=== 
cek_start = "Sangjangnim Oppa".startswith("Sangjangnim") 
print("start = " + str(cek_start))

cek_end = "Sangjangnim Oppak".endswith("Oppak")
print("end = " + str(cek_end))


## penggabungan komponen join() split()
pisah = ['aku', 'sayang', 'kamu']
gabung = ','.join(pisah)
print(pisah)
print(gabung)

gabungan = " ".join(pisah)
print(gabungan)

gabungan = ' ehm '.join(pisah)
print(gabungan)


gabugan = 'akuehmsayangehmkamu'
print(gabungan.split('ehm'))

# alokasi karakter rjust(), ljust() center()
print(5*"="+"data"+"="*5)


kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")


tengah = "tengah".center(20,":")
print("'"+tengah+"'")

# kebalikannya -> strip()
tengah = tengah.strip(":") # menghilangkan tanga?
print("'"+tengah+"'")
