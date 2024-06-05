def check_ganjil_genap():
    try:
        # Input angka pengguna
        number = int(input("Pilih satu angka dalam rentang 1 sampai 25: "))
        
        # Memastikan angka berada dalam rentang yang benar
        if number < 1 or number > 25:
            print("Angka salah, pastikan angka dalam rentang 1 sampai 25.")
        else:
            # Ternary operator untuk menentukan ganjil atau genap
            result = "genap" if number % 2 == 0 else "ganjil"
            print(f"Angka {number} adalah {result}.")
    except ValueError:
        print("Harap masukkan karakter angka yang valid.")

# Menjalankan fungsi
check_ganjil_genap()
