menu_dimsum = [
    {"kode": "D01", "nama": "Siomay Ayam", "harga": 15000},
    {"kode": "D02", "nama": "Hakau Udang", "harga": 20000},
    {"kode": "D03", "nama": "Xiao Long Bao", "harga": 20000},
    {"kode": "D04", "nama": "Lumpia Kulit Tahu", "harga": 15000},
    {"kode": "D05", "nama": "Bakpao Telur Asin", "harga": 15000},
]


def input_pesanan(menu):

    tampilkan_menu(menu)
    print("\nPetunjuk: Masukkan nomor menu (1-5). Ketik 0 jika selesai.")
    
    daftar_pesanan = []
    
    while True:
        pilihan = int(input("\nPilih nomor menu (1-5, atau 0 selesai): "))
        if pilihan == 0:
            if len(daftar_pesanan) == 0:
                print("Pesanan masih kosong! Silakan pilih minimal 1 menu.")
                continue
            break
            
        if 1 <= pilihan <= len(menu):
            item = menu[pilihan - 1]
            porsi = int(input(f"Jumlah porsi untuk {item['nama']}: "))
            
            sudah_ada = False
            for pesanan in daftar_pesanan:
                if pesanan["kode"] == item["kode"]:
                    pesanan["porsi"] += porsi
                    pesanan["subtotal"] = pesanan["porsi"] * pesanan["harga"]
                    sudah_ada = True
                    break
                    
            if not sudah_ada:
                daftar_pesanan.append({
                    "kode": item["kode"],
                    "nama": item["nama"],
                    "harga": item["harga"],
                    "porsi": porsi,
                    "subtotal": item["harga"] * porsi
                })
            print(f"Berhasil menambahkan {porsi} porsi {item['nama']}.")
        else:
            print("Nomor menu tidak ada! Silakan pilih angka 1 sampai 5.")
            
    return daftar_pesanan



def hitung_total(daftar_pesanan):
    subtotal = 0
    total_porsi = 0
    
    for item in daftar_pesanan:
        subtotal = subtotal + item["subtotal"]
        total_porsi = total_porsi + item["porsi"]
        
    if total_porsi >= 5:
        diskon = int(subtotal * 0.10)
        keterangan_diskon = "Dapat Diskon 10% (Beli Minimal 5 Porsi)"
    else:
        diskon = 0
        keterangan_diskon = "Tidak Dapat Diskon (Kurang dari 5 Porsi)"
        
    total_bayar = subtotal - diskon
    
    return {
        "pesanan": daftar_pesanan,
        "total_porsi": total_porsi,
        "subtotal": subtotal,
        "diskon": diskon,
        "keterangan": keterangan_diskon,
        "total_bayar": total_bayar
    }



def tampilkan_menu(menu):
    print("\n" + "=" * 45)
    print("      DAFTAR MENU DIMSUM BAMBOO HOUSE        ")
    print("=" * 45)
    print(f"| {'No':<3} | {'Nama Menu':<20} | {'Harga':>12} |")
    print("-" * 45)
    for i in range(len(menu)):
        item = menu[i]
        print(f"| {i+1:<3} | {item['nama']:<20} | Rp {item['harga']:>9,d} |")
    print("-" * 45)
    print("*) Promo: Beli minimal 5 porsi dapat Diskon 10%!")


def cetak_struk(hasil, uang_bayar):
    kembalian = uang_bayar - hasil["total_bayar"]
    
    print("\n" + "=" * 45)
    print("             STRUK PEMBAYARAN                ")
    print("          DIMSUM BAMBOO HOUSE                ")
    print("=" * 45)
    print(f" Total Porsi : {hasil['total_porsi']} porsi")
    print("-" * 45)
    print(f" {'Nama Menu':<18} {'Porsi':^7} {'Subtotal':>15}")
    print("-" * 45)
    for item in hasil["pesanan"]:
        print(f" {item['nama']:<18} {item['porsi']:^7} Rp {item['subtotal']:>11,d}")
    print("-" * 45)
    print(f" Subtotal      : Rp {hasil['subtotal']:>18,d}")
    if hasil["diskon"] > 0:
        print(f" Diskon (10%)  : -Rp {hasil['diskon']:>17,d}")
    else:
        print(f" Diskon (0%)   :  Rp {0:>18,d}")
    print("=" * 45)
    print(f" TOTAL BAYAR   : Rp {hasil['total_bayar']:>18,d}")
    print(f" Uang Tunai    : Rp {uang_bayar:>18,d}")
    print(f" Kembalian     : Rp {kembalian:>18,d}")
    print("=" * 45)
    print(f" Status: {hasil['keterangan']}")
    print("         Terima kasih sudah berbelanja!      ")
    print("=" * 45)


def jalankan_pengujian():
    skenario = [
        {
            "nomor": 1,
            "nama": "Skenario 1: Beli 3 Porsi (Kurang dari 5 porsi -> Diskon 0%)",
            "bayar": 50000,
            "pesanan": [
                {"kode": "D01", "nama": "Siomay Ayam", "harga": 15000, "porsi": 2, "subtotal": 30000},
                {"kode": "D02", "nama": "Hakau Udang", "harga": 20000, "porsi": 1, "subtotal": 20000},
            ]
        },
        {
            "nomor": 2,
            "nama": "Skenario 2: Beli Tepat 5 Porsi (Tepat batas -> Diskon 10%)",
            "bayar": 100000,
            "pesanan": [
                {"kode": "D01", "nama": "Siomay Ayam", "harga": 15000, "porsi": 3, "subtotal": 45000},
                {"kode": "D02", "nama": "Hakau Udang", "harga": 20000, "porsi": 2, "subtotal": 40000},
            ]
        },
        {
            "nomor": 3,
            "nama": "Skenario 3: Beli 8 Porsi (Lebih dari 5 porsi -> Diskon 10%)",
            "bayar": 150000,
            "pesanan": [
                {"kode": "D01", "nama": "Siomay Ayam", "harga": 15000, "porsi": 4, "subtotal": 60000},
                {"kode": "D03", "nama": "Xiao Long Bao", "harga": 20000, "porsi": 4, "subtotal": 80000},
            ]
        }
    ]
    
    print("\n" + "=" * 55)
    print("      MENJALANKAN 3 SKENARIO PENGUJIAN OTOMATIS       ")
    print("=" * 55)
    
    for s in skenario:
        print(f"\n>>> {s['nama']}")
        hasil = hitung_total(s["pesanan"])
        cetak_struk(hasil, s["bayar"])
        
    print("\n" + "=" * 55)
    print("  KESIMPULAN: SELURUH PENGUJIAN TELAH SELESAI DIJALANKAN ")
    print("=" * 55)


def main():
    print("=" * 45)
    print("   PROGRAM KASIR DIMSUM BAMBOO HOUSE         ")
    print("=" * 45)
    
    while True:
        print("\nPILIHAN MENU:")
        print("1. Jalankan Pengujian Otomatis (3 Skenario)")
        print("2. Pesan Dimsum (Manual)")
        print("3. Keluar")
        
        pilihan = int(input("Pilih menu (1-3): "))
        
        if pilihan == 1:
            jalankan_pengujian()
        elif pilihan == 2:
            pesanan = input_pesanan(menu_dimsum)
            hasil = hitung_total(pesanan)
            
            print(f"\nTotal Porsi : {hasil['total_porsi']} porsi")
            print(f"Subtotal    : Rp {hasil['subtotal']:,}")
            print(f"Diskon      : Rp {hasil['diskon']:,} ({hasil['keterangan']})")
            print(f"Total Bayar : Rp {hasil['total_bayar']:,}")
            
            uang = int(input("Masukkan Uang Pembayaran: Rp "))
            while uang < hasil["total_bayar"]:
                kurang = hasil["total_bayar"] - uang
                print(f"Uang kurang Rp {kurang:,}!")
                uang = int(input("Masukkan Uang Pembayaran yang cukup: Rp "))
                
            cetak_struk(hasil, uang)
        elif pilihan == 3:
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid! Masukkan angka 1 sampai 3.")


if __name__ == "__main__":
    main()