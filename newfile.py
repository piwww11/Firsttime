print("=== Program Catatan Harian ===")

running = True

while running:
    print("\nMenu : ")
    print("1. Tulis catatan")
    print("2. Lihat catatan")
    print("3. Hapus catatan tertentu")
    print("4. Hapus semua catatan")
    print("5. Keluar")
    
    pilihan = input("Pilih menu (1/2/3/4/5): ")

    # ==================== TULIS CATATAN ====================
    if pilihan == "1":
        print("\n=== Tulis Catatan ===")
        catatan = input("Tulis catatan kamu: ")

        with open("catatan.txt", "a") as file:
            file.write(catatan + "\n")

        print("Catatan berhasil disimpan!")

    # ==================== LIHAT CATATAN ====================
    elif pilihan == "2":
        print("\n=== Isi Catatan Kamu ===")

        try:
            with open("catatan.txt", "r") as file:
                isi = file.read()

            if isi.strip() == "":
                print("Belum ada catatan.")
            else:
                print(isi)

        except FileNotFoundError:
            print("Belum ada file catatan. Tulis catatan dulu.")

    # ==================== HAPUS CATATAN TERTENTU ====================
    elif pilihan == "3":
        print("\n=== Hapus Catatan Tertentu ===")

        try:
            with open("catatan.txt", "r") as file:
                catatan = file.readlines()

            if not catatan:
                print("Belum ada catatan yang bisa dihapus!")
                continue

            # Tampilkan semua catatan
            print("Daftar Catatan:")
            for i, isi in enumerate(catatan, start=1):
                print(f"{i}. {isi.strip()}")

            # Input nomor catatan
            nomor = int(input("\nMasukkan nomor catatan yang mau dihapus: "))

            if nomor < 1 or nomor > len(catatan):
                print("Nomor catatan tidak valid!")
                continue

            # Hapus catatan
            catatan.pop(nomor - 1)

            # Tulis ulang file
            with open("catatan.txt", "w") as file:
                file.writelines(catatan)

            print("Catatan berhasil dihapus!")

        except FileNotFoundError:
            print("Belum ada file catatan!")

    # ==================== HAPUS SEMUA CATATAN ====================
    elif pilihan == "4":
        with open("catatan.txt", "w") as file:
            file.write("")

        print("Semua catatan berhasil dihapus!")

    # ==================== KELUAR ====================
    elif pilihan == "5":
        print("Keluar dari program...")
        running = False

    else:
        print("Pilihan tidak valid. Coba lagi!")