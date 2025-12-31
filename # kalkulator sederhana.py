# kalkulator sederhana

def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "error! ngga bisa bagi nol kocak"
    else: 
        return a / b
    
#selamat datang pemai
print("=" * 40)
print(" kalkulator orang keren")
print("=" * 40)

while True:
    print("\nPilih operasi dulu woi")
    print("1. Tambah (+)")
    print("2. Kuranng (-)")
    print("3. Kali (*)")
    print("4. Bagi (/)")
    print("5. Keluar")

    pilihan = input("\nMaukin nomer pilihan (1-5): ")

    if pilihan == '5':
        print("Jago banget gua bikin ni kalkuator")

    if pilihan in ['1', '2', '3', '4',]:
        try:
            angka1 = float(input("masukin angka pertama: "))
            angka2 = float(input("masukin angka kedua: "))
        except ValueError: 
            print("ERROR KOCAK MASUKIN ANGKA YANG BENER")
            continue

        if pilihan == '1':
            hasil = tambah(angka1, angka2)
            operasi = "+"
        elif pilihan == '2':
            hasil = kurang(angka1, angka2)
            operasi = "-"
        elif pilihan == '3':
            hasil = kali(angka1, angka2)
            operasi = "*"
        elif pilihan == '4':
            hasil = bagi(angka1, angka2)
            operasi = "/"

        print(f"\nHasil: {angka1} {operasi} {angka2} = {hasil}")
    else:
        print("Pilihan gak valid kocak")