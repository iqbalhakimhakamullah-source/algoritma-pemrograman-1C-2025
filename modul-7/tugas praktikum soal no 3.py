kupon_tersedia = {
    "DISKON10": 10,
    "DISKON20": 20,
    "DISKON15": 15,
    "PROMO30": 30,
    "HEMAT25": 25,
    "SPESIAL50": 50,
}


def tampilkan_menu():
    """Menampilkan menu utama"""
    print("\nSistem Validasi Kupon Diskon")
    print("1. Tampilkan Semua Kupon")
    print("2. Proses Transaksi")
    print("3. Cek Kupon")
    print("4. Keluar")


def tampilkan_semua_kupon():
    """Menampilkan semua kupon yang masih tersedia"""
    print("\nDaftar Kupon:")
    if not kupon_tersedia:
        print("(Tidak ada kupon)")
    else:
        for kode, diskon in kupon_tersedia.items():
            print(f"{kode}: {diskon}%")


def cek_kupon_spesifik():
    """Mengecek kupon tertentu"""
    kode = input("Masukkan kode kupon: ").strip().upper()
    if kode in kupon_tersedia:
        print(f"Kupon '{kode}' VALID — Diskon: {kupon_tersedia[kode]}%")
    else:
        print(f"Kupon '{kode}' TIDAK VALID atau sudah dipakai.")


def proses_transaksi():
    """Memproses transaksi dengan kupon"""
    try:
        total_belanja = float(input("Total belanja (Rp): ").strip())
    except ValueError:
        print("Input tidak valid. Masukkan angka untuk total belanja.")
        return

    if total_belanja < 0:
        print("Total belanja tidak boleh negatif.")
        return

    gunakan = input("Gunakan kupon? (y/n): ").strip().lower()
    if gunakan != 'y':
        print(f"Total Bayar: Rp {total_belanja:,.0f}")
        return

    if not kupon_tersedia:
        print("Tidak ada kupon yang tersedia.")
        print(f"Total Bayar: Rp {total_belanja:,.0f}")
        return

    print("Kupon tersedia:")
    print(', '.join(kupon_tersedia.keys()))
    kode = input("Masukkan kode kupon: ").strip().upper()

    if kode not in kupon_tersedia:
        print(f"Kupon '{kode}' TIDAK VALID atau sudah dipakai.")
        print(f"Total Bayar: Rp {total_belanja:,.0f}")
        return

    persen = kupon_tersedia[kode]
    besar_diskon = total_belanja * persen / 100
    total_bayar = total_belanja - besar_diskon

    print(f"Kupon '{kode}' dipakai — Diskon {persen}%")
    print(f"Total Belanja : Rp {total_belanja:,.0f}")
    print(f"Diskon        : Rp {besar_diskon:,.0f}")
    print(f"Total Bayar   : Rp {total_bayar:,.0f}")

    del kupon_tersedia[kode]
    print(f"Kupon '{kode}' telah dihapus.")


def main():
    print("\nSelamat datang")
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-4): ").strip()
        if pilihan == '1':
            tampilkan_semua_kupon()
        elif pilihan == '2':
            proses_transaksi()
        elif pilihan == '3':
            cek_kupon_spesifik()
        elif pilihan == '4':
            print("Terima kasih.")
            break
        else:
            print("Pilihan tidak valid. Pilih 1-4.")


if __name__ == '__main__':
    main()
