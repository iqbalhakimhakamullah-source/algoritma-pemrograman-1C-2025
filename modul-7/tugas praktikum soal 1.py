buku_kontak = {}

def tampilkan_menu():
    """Tampilkan menu utama"""
    print("\n=== BUKU KONTAK ===")
    print("1. Tampilkan Semua Kontak")
    print("2. Cari Kontak")
    print("3. Tambah Kontak")
    print("4. Update Email")
    print("5. Hapus Kontak")
    print("6. Keluar")

def tampilkan_semua_kontak():
    """Menampilkan semua kontak"""
    print("\n=== DAFTAR KONTAK ===")
    
    if len(buku_kontak) == 0:
        print("Belum ada kontak.")
    else:
        for nama, data in buku_kontak.items():
            print(f"\nNama  : {nama}")
            print(f"Nomor : {data[0]}")
            print(f"Email : {data[1]}")

def cari_kontak():
    """Mencari kontak berdasarkan nama"""
    print("\n=== CARI KONTAK ===")
    nama = input("Nama: ")
    
    if nama in buku_kontak:
        print(f"\nNama  : {nama}")
        print(f"Nomor : {buku_kontak[nama][0]}")
        print(f"Email : {buku_kontak[nama][1]}")
    else:
        print(f"Kontak '{nama}' tidak ditemukan.")

def tambah_kontak():
    """Menambah kontak baru"""
    print("\n=== TAMBAH KONTAK ===")
    nama = input("Nama  : ")
    
    if nama in buku_kontak:
        print(f"Kontak '{nama}' sudah ada.")
    else:
        nomor = input("Nomor : ")
        email = input("Email : ")
        buku_kontak[nama] = [nomor, email]
        print(f"Kontak '{nama}' berhasil ditambahkan.")
        

def update_email():
    """Memperbarui email kontak"""
    print("\n=== UPDATE EMAIL ===")
    nama = input("Nama: ")
    
    if nama in buku_kontak:
        print(f"Email saat ini: {buku_kontak[nama][1]}")
        email_baru = input("Email baru   : ")
        buku_kontak[nama][1] = email_baru
        print(f"Email '{nama}' berhasil diupdate.")
    else:
        print(f"Kontak '{nama}' tidak ditemukan.")

def hapus_kontak():
    """Menghapus kontak"""
    print("\n=== HAPUS KONTAK ===")
    nama = input("Nama: ")
    
    if nama in buku_kontak:
        konfirmasi = input(f"Hapus '{nama}'? (y/n): ")
        if konfirmasi.lower() == 'y':
            del buku_kontak[nama]
            print(f"Kontak '{nama}' berhasil dihapus.")
        else:
            print("Penghapusan dibatalkan.")
    else:
        print(f"Kontak '{nama}' tidak ditemukan.")

# PROGRAM UTAMA
def main():
    """Fungsi utama"""
    print("Selamat datang di Buku Kontak!")
    
    while True:
        tampilkan_menu()
        pilihan = input("\nPilih menu (1-6): ")
        
        if pilihan == "1":
            tampilkan_semua_kontak()
        elif pilihan == "2":
            cari_kontak()
        elif pilihan == "3":
            tambah_kontak()
        elif pilihan == "4":
            update_email()
        elif pilihan == "5":
            hapus_kontak()
        elif pilihan == "6":
            print("\nTerima kasih!")
            break
        else:
            print("Pilihan tidak valid!")

# Jalankan program
if __name__ == "__main__":
    main()