print("======== PROGRAM FILE HANDLING ==========")
def tulis_biodata(nama_file):
    nama = input("Nama: ")
    umur = input("Umur: ")
    alamat = input("Alamat: ")
    email = input("Email: ")
    dosen_wali = input("Dosen Wali: ")

    with open(nama_file, "w") as file:
        file.write(f"Nama: {nama}\n")
        file.write(f"Umur: {umur}\n")
        file.write(f"Alamat: {alamat}\n")
        file.write(f"Email: {email}\n")
        file.write(f"Dosen Wali: {dosen_wali}\n")

    print(f"Biodata telah berhasil disimpan di file {nama_file}.")

def baca_biodata(nama_file):
    try:
        with open(nama_file, "r") as file:
            biodata = file.read()
            print("Isi Biodata:")
            print(biodata)
    except FileNotFoundError:
        print(f"Biodata pada file {nama_file} belum tersedia.")

# Program Utama
while True:
    print("\nMenu:")
    print("1. Menulis Biodata")
    print("2. Membaca Biodata")
    print("3. Menutup Program")

    pilihan = input("Pilih menu (1/2/3): ")

    if pilihan == "1":
        nama_file = input("Masukkan nama file untuk menyimpan biodata: ")
        tulis_biodata(nama_file)
    elif pilihan == "2":
        nama_file = input("Masukkan nama file untuk membaca biodata: ")
        baca_biodata(nama_file)
    elif pilihan == "3":
        print("Program ditutup.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih menu 1, 2, atau 3.")
