# Latihan Perhitungan Konversi satuan temperature

# program konversi celcius ke satuan lain

print("\nPROGRAM KONVERSI TEMPERATURE\n")

celcius = float(input('Masukkan suhu dalam celcius : '))
print("suhu adalah ", celcius, " Celcius" )

# reamur 
reamur = (4/5) * celcius
print("suhu dalam reamur adalah ", reamur, " Reamur" )

# Fahrenheit
fahrenheit =  ((9/5) * celcius) + 32
print("suhu dalam fahrenheit ", fahrenheit, " Fahrenheit" )


#Kelvin
kelvin = celcius  + 273
print("suhu dalam Kelvin ", kelvin, " Kelvin" )
