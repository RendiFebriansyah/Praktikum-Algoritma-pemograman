print("=======  TOKO BERKAH JAYA =======")
print("======= SELAMAT BERBELANJA =======")

pembeli = input("Masukkan Nama Pembeli: ")
print ("Nama Anda :", pembeli)
pembeli = input("Masukkan Alamat Pembeli: ")
print ("Alamat Anda :", pembeli)
pembeli = input("Masukkan No Telp Pembeli: ")
print ("No Telp Anda :", pembeli)

harga = []
barang = []
total_harga = 0
while True:
    print("""
    ========== daftar_barang ==========
     | No |    Nama Barang   | Harga |
    -----------------------------------
     | 1  | Downny           | 37000 |
     | 2  | Baygon           | 43000 |
     | 3  | Mamy Poko        | 59000 |
     | 4  | Susu Ovaltine    | 70000 |
     | 5  | Beras            | 70000 |
    -----------------------------------
    """)

    kode = int(input("Masukkan angka barang  : "))
    if kode == 1:
        jumlah1 = int(input("Masukkan jumlah barang : "))
        total_harga += 23000 * jumlah1
        harga.append(23000)
        
    elif kode == 2:
        jumlah2 = int(input("Masukkan jumlah barang : "))
        total_harga += 43000 * jumlah2
        harga.append(43000)
        
    elif kode == 3:
        jumlah3 = int(input("Masukkan jumlah barang : "))
        total_harga += 59000 * jumlah3 
        harga.append(59000)
        
    elif kode == 4:
        jumlah4 = int(input("Masukkan jumlah barang : "))
        total_harga += 70000 * jumlah4
        harga.append(70000)
        
    elif kode == 5:
        jumlah5 = int(input("Masukkan jumlah barang : "))
        total_harga += 70000 * jumlah5   
        harga.append(70000)
        
    
    else:
     print("Pilihan yang anda masukan salah!")

    beli_barang_lain = input("Beli barang lain ?\nTekan (YES/NO) : ")
    if beli_barang_lain == "No" :
        print("")

    print(f"""
Barang : {barang}
harga  : Rp.{harga}
jumlah total harga: Rp.{total_harga}
""")

    bayar=total_harga

    print("\nTotal harus Dibayar: Rp",total_harga)
    uang=int(input("Uang Tunai Pembeli: Rp "))
    kembalian=int(uang-total_harga)
    print("Kembalian :",kembalian)

