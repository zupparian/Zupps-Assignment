def check_ganjil_genap():
    try:
        # Input angka pengguna
        number = int(input("Pilih satu angka dalam rentang 1 sampai 25: "))
        
        # Memastikan angka masih berada dalam rentang 1-25
        if number < 1 or number > 25:
            print("Pastikan angka dalam rentang 1 sampai 25.")
        else:
            # Memeriksa apakah angka tersebut genap atau ganjil
            if number % 2 == 0:
                print(f"Angka {number} adalah genap.")
            else:
                print(f"Angka {number} adalah ganjil.")
    except ValueError:
        print("Harap masukkan karakter angka yang valid.")

# Menjalankan fungsi
check_ganjil_genap()