# format string


# contoh generic
# string


nama = "marlene"
str = "hello" + nama 
format_str = f"hello {nama}"
print(format_str)

# angka 
angka = 2005.5
format_str = f"angka = {angka}" 
print(format_str)

# boolean
boolean = True
format_str = f"boolean = {boolean}"
print(format_str)

# bilangan bulat 
angka = 15
format_str = f"bilangan bulat = {angka:d}"
print(format_str)


#bilangan ribuan 
angka = 2000000
fotmat_str = f"ribuan = {angka:,}"
print(format_str)

# bilangan desimal 
angka = 1005.54321
format_str = f"desimal = {angka:.2f}"
print(format_str)

# menampilkan leading zero
angka = 1005.54321
format_str = f"desimal = {angka:010.2f}"
print(format_str)

# menampilkan plus atau minus
angka_minus = -10
angka_plus = 10.1234
format_minus = f"minus =  {angka_minus}"
format_plus = f"plus = {angka_plus:+.3f}"

print(format_minus)
print(format_plus)

# memformat persen 
persentase = 0.045
format_persen = f"persen = {persentase:.2%}"

print(format_persen)

# melakukan operasi aritmatika di dalam placeholder 
harga = 10000
jumlah = 5

format_string = f"harga toal = Rp. {harga * jumlah}"
print(format_string)

# format angka lain (binary, octal, hexadecimal)

angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hexadecimal = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)
