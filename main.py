# arbitrary Arguments ( *args )

# arbitrary Arguments adalah istilah untuk menyebut jumlah
# argument yang tidak bisa ditentukan atau berubah-ubah

def sapa_teman(nama1,nama2,nama3):
    print("Hallo", nama1)
    print("Hallo", nama2)
    print("Hallo", nama3)

sapa_teman("Alex", "Nisa", "Sari")
# sapa_teman("Andri", "jono", "Eko", "Sena")

def sapa_kawan(*args):
    print(args)
    print(type(args))

sapa_kawan("Ando", "bundo", "redo", "sodo", "kodo")

def hello_bro(*nama):
    for i in nama:
        print("Hallo", i)

hello_bro("Andri", "Ujang", "Joni", "Faisal", "Gebby")

def my_function(*kids):
    print("the Youngest child is " + kids[3])

my_function("Angela", "John", "Jordi", "Alfred")

def jumlah(*args):
    hasil = 0
    for i in args:
        hasil += i
    return hasil

print(jumlah(5,7))
print(jumlah(10,20,30,40))
print(jumlah(25,26,27,28,29,30))
print(jumlah(10,10,10,10,10))

def perkalian(*args):
    hasil = 1
    for i in args:
        hasil *= i
    return hasil

print(perkalian(5,7))
print(perkalian(10,20,30,40))
print(perkalian(25,26,27,28,29,30))
print(perkalian(10,10,10,10,10))

def pengurangan(*args):
    hasil = 0
    for i in args:
        hasil -= i
    return hasil

print(pengurangan(7,5))
print(pengurangan(100,20,30,40))
print(pengurangan(250,26,27,28,29,30))
print(pengurangan(100,10,10,10,10))

def pembagian(*args):
    hasil = 1
    for i in args:
        hasil /= i
    return hasil

print(pembagian(10,100))
print(pembagian(100,20,30,40))
print(pembagian(250,26,27,28,29,30))
print(pembagian(100,10,10,10,10))