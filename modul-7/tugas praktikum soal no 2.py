inventaris = {}

def tampilkan_menu():
    """Tampilkan menu utama"""
    print("\n=== INVENTARIS GUDANG ===")
    print("1. Tampilkan Semua Barang")
    print("2. Cari Barang")
    print("3. Tambah Barang")
    print("4. Update Stok")
    print("5. Hapus Barang")
    print("6. Keluar")

def tampilkan_semua_barang():
    """Menampilkan semua barang"""
    print("\n=== DAFTAR BARANG ===")
    
    if len(inventaris) == 0:
        print("Belum ada barang di gudang.")
    else:
        for id_barang, data in inventaris.items():
            print(f"\nID     : {id_barang}")
            print(f"Nama   : {data[0]}")
            print(f"Harga  : Rp {data[1]:,}")
            print(f"Stok   : {data[2]} unit")

def cari_barang():
    """Mencari barang berdasarkan ID"""
    print("\n=== CARI BARANG ===")
    id_barang = input("ID Barang: ")
    
    if id_barang in inventaris:
        print(f"\nID     : {id_barang}")
        print(f"Nama   : {inventaris[id_barang][0]}")
        print(f"Harga  : Rp {inventaris[id_barang][1]:,}")
        print(f"Stok   : {inventaris[id_barang][2]} unit")
    else:
        print(f"Barang dengan ID '{id_barang}' tidak ditemukan.")

def tambah_barang():
    """Menambah barang baru"""
    print("\n=== TAMBAH BARANG ===")
    id_barang = input("ID Barang : ")
    
    if id_barang in inventaris:
        print(f"Barang dengan ID '{id_barang}' sudah ada.")
    else:
        nama = input("Nama Barang : ")
        harga = int(input("Harga       : "))
        stok = int(input("Stok        : "))
        
        inventaris[id_barang] = [nama, harga, stok]
        print(f"Barang '{nama}' berhasil ditambahkan.")

def update_stok():
    """Memperbarui stok barang"""
    print("\n=== UPDATE STOK ===")
    id_barang = input("ID Barang: ")
    
    if id_barang in inventaris:
        print(f"Nama Barang : {inventaris[id_barang][0]}")
        print(f"Stok saat ini: {inventaris[id_barang][2]} unit")
        
        print("\nPilih operasi:")
        print("1. Tambah stok")
        print("2. Kurangi stok")
        operasi = input("Pilihan (1/2): ")
        
        jumlah = int(input("Jumlah: "))
        
        if operasi == "1":
            # Tambah stok
            inventaris[id_barang][2] += jumlah
            print(f"Stok berhasil ditambah. Stok sekarang: {inventaris[id_barang][2]} unit")
        elif operasi == "2":
            # Kurangi stok
            stok_sekarang = inventaris[id_barang][2]
            stok_baru = stok_sekarang - jumlah
            
            # Validasi: stok tidak boleh negatif
            if stok_baru < 0:
                print(f"Gagal! Stok tidak boleh negatif.")
                print(f"Stok tersedia hanya {stok_sekarang} unit.")
                return
            else:
                inventaris[id_barang][2] = stok_baru
                print(f"Stok berhasil dikurangi. Stok sekarang: {inventaris[id_barang][2]} unit")
        else:
            print("Pilihan tidak valid!")
    else:
        print(f"Barang dengan ID '{id_barang}' tidak ditemukan.")

def hapus_barang():
    """Menghapus barang"""
    print("\n=== HAPUS BARANG ===")
    id_barang = input("ID Barang: ")
    
    if id_barang in inventaris:
        nama_barang = inventaris[id_barang][0]
        konfirmasi = input(f"Hapus '{nama_barang}'? (y/n): ")
        
        if konfirmasi.lower() == 'y':
            del inventaris[id_barang]
            print(f"Barang '{nama_barang}' berhasil dihapus.")
        else:
            print("Penghapusan dibatalkan.")
    else:
        print(f"Barang dengan ID '{id_barang}' tidak ditemukan.")

# PROGRAM UTAMA
def main():
    """Fungsi utama"""
    print("Selamat datang di Sistem Inventaris Gudang!")
    
    while True:
        tampilkan_menu()
        pilihan = input("\nPilih menu (1-6): ")
        
        if pilihan == "1":
            tampilkan_semua_barang()
        elif pilihan == "2":
            cari_barang()
        elif pilihan == "3":
            tambah_barang()
        elif pilihan == "4":
            update_stok()
        elif pilihan == "5":
            hapus_barang()
        elif pilihan == "6":
            print("\nTerima kasih!")
            break
        else:
            print("Pilihan tidak valid!")

# Jalankan program
if __name__ == "__main__":
    main()