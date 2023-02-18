import json

def tambah_kontak(nama, nomor, buku_telepon):
    buku_telepon[nama] = nomor
    print("Kontak berhasil ditambahkan.")

def hapus_kontak(nama, buku_telepon):
    if nama in buku_telepon:
        del buku_telepon[nama]
        print("Kontak berhasil dihapus.")
    else:
        print("Kontak tidak ditemukan.")

def cek_kontak(nama, buku_telepon):
    if nama in buku_telepon:
        print("Nomor telepon", nama, "adalah", buku_telepon[nama])
    else:
        print("Kontak tidak ditemukan.")

def update_kontak(nama, nomor, buku_telepon):
    if nama in buku_telepon:
        buku_telepon[nama] = nomor
        print("Kontak berhasil diperbarui.")
    else:
        print("Kontak tidak ditemukan.")

def buka_file(nama_file):
    try:
        with open(nama_file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("File tidak ditemukan.")
        return {}

def simpan_file(nama_file, buku_telepon):
    with open(nama_file, 'w') as f:
        json.dump(buku_telepon, f)

if __name__ == '__main__':
    nama_file = "buku_telepon.json"
    buku_telepon = buka_file(nama_file)

    while True:
        print("\n=== Buku Telepon ===")
        print("1. Tambah kontak")
        print("2. Hapus kontak")
        print("3. Cek kontak")
        print("4. Update kontak")
        print("5. Tampilkan semua kontak")
        print("6. Keluar")

        pilihan = input("Masukkan pilihan (1-6): ")

        if pilihan == '1':
            nama = input("Masukkan nama: ")
            nomor = input("Masukkan nomor telepon: ")
            tambah_kontak(nama, nomor, buku_telepon)
            simpan_file(nama_file, buku_telepon)

        elif pilihan == '2':
            nama = input("Masukkan nama: ")
            hapus_kontak(nama, buku_telepon)
            simpan_file(nama_file, buku_telepon)

        elif pilihan == '3':
            nama = input("Masukkan nama: ")
            cek_kontak(nama, buku_telepon)

        elif pilihan == '4':
            nama = input("Masukkan nama: ")
            nomor = input("Masukkan nomor telepon baru: ")
            update_kontak(nama, nomor, buku_telepon)
            simpan_file(nama_file, buku_telepon)

        elif pilihan == '5':
            if buku_telepon:
                print("Daftar kontak:")
                for nama, nomor in buku_telepon.items():
                    print(nama, ":", nomor)
            else:
                print("Buku telepon kosong.")

        elif pilihan == '6':
            break

        else:
            print("Pilihan tidak valid.")
