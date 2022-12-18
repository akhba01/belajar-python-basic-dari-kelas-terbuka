# Membandingkan nilai
#  Setiap hasil dari operasi komparasi adalah boolean
# >,<,<=,>=,==,!=, is, is not

a = 4
b = 2

# lebih besar dari >
print('======= lebih besar dari > =======')
hasil = a > 3
print(a, '>', 3, '=', hasil)
hasil = b > 3
print(b, '>', 3, '=', hasil)
hasil = b > a
print(b, '>', a, '=', hasil)
hasil = b > 2
print(b, '>', 2, '=', hasil)

# kurang dari < 
print('======= lebih besar dari < =======')
hasil = a < 5
print(a, '<', 5, '=', hasil)
hasil = b < 5
print(b, '<', 5, '=', hasil)
hasil = b < a
print(b, '<', a, '=', hasil)
hasil = b < 2
print(b, '<', 2, '=', hasil)

# lebih dari sama dengan >=
print('======= lebih besar dari sama dengan >= =======')
hasil = a >= 4
print(a, '>=', 4, '=', hasil)
hasil = b >= 4
print(b, '>=', 4, '=', hasil)
hasil = b >= a
print(b, '>=', a, '=', hasil)
hasil = b >= 2
print(b, '>=', 2, '=', hasil)

# Kurang dari sama dengan <=
print('======= lebih besar dari sama dengan <= =======')
hasil = a <= 4
print(a, '<=', 4, '=', hasil)
hasil = b <= 4
print(b, '<=', 4, '=', hasil)
hasil = b <= a
print(b, '<=', a, '=', hasil)
hasil = b <= 2
print(b, '<=', 2, '=', hasil)

# sama dengan ==
print('======= lebih besar dari sama dengan == =======')
hasil = a == 4
print(a, '==', 4, '=', hasil)
hasil = b == 4
print(b, '==', 4, '=', hasil)
hasil = b == a
print(b, '==', a, '=', hasil)
hasil = b == 2
print(b, '==', 2, '=', hasil)


# Tidak sama dengan !=
print('======= lebih besar dari sama dengan != =======')
hasil = a != 4
print(a, '!=', 4, '=', hasil)
hasil = b != 4
print(b, '!=', 4, '=', hasil)
hasil = b != a
print(b, '!=', a, '=', hasil)
hasil = b != 2
print(b, '!=', 2, '=', hasil)

# 'is' sebagai komparasi object identity
print('======= object identity (is) =======')
x = 5 # ini adalah assigment membuat object
y = 5 # ini adalah assigment membuat object
print('nilai x =', x,', id=', id(x)),
print('nilai y =', y,', id=', id(y)) 
hasil = x is y
print('x is y =', hasil)

x = 5 # ini adalah assigment membuat object
y = 6 # ini adalah assigment membuat object
print('nilai x =', x,', id=', id(x)),
print('nilai y =', y,', id=', id(y)) 
hasil = x is y
print('x is y =', hasil)