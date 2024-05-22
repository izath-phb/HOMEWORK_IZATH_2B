def tampilan():
    print ('selamat datang di program manajemen stok barang!')
    print ('='*50)
    print ('Pilihan:')
    print ('1. Tambah Data Barang')
    print ('2. edit data ')
    print ('3. hapus data barang')
    print ('4. cari data')
    print ('5. tampilkan data barang')
    print ('6. tampilkan jumlah data')
    print ('7. Keluar')
    print ('='*50)

barang_elektronik = []

def tambah():
    nama = str(input('Masukan Nama Barang : '))
    stok = str(input('Masukan Stok Barang : '))
    data_baru = {'nama barang':nama,'stok':stok}
    barang_elektronik.append(data_baru)
    print("Data barang berhasil ditambahkan!")

def edit_data():
    tampilkan_data_barang()
    index = int(input("Masukkan nomor indeks barang yang ingin diedit: "))
    if 0 <= index < len(barang_elektronik):
        nama_barang = input("Masukkan nama barang baru: ")
        stok = int(input("Masukkan jumlah stok baru: "))
        barang_elektronik[index] = {"nama barang": nama_barang, "stok": stok}
        print("Data barang berhasil diedit!")
    else:
        print("Indeks tidak valid!")
    print("Data barang berhasil diedit")

def hapus():
    tampilkan_data_barang()
    if barang_elektronik:
        hapus = int(input('Hapus Data Index Ke : '))
        if 0 <= hapus < len(barang_elektronik):
            del barang_elektronik[hapus]
            print("Data barang berhasil dihapus!")
        else:
            print("Indeks tidak valid!")
    else:
        print("Tidak ada data barang yang bisa dihapus.")

def cari():
    nama_barang = input('Cari Nama Barang: ')
    found = False
    for index, barang in enumerate(barang_elektronik):
        if barang['nama barang'].lower() == nama_barang.lower():
            print(f"Barang ditemukan pada indeks {index}. {barang['nama barang']}, Stok: {barang['stok']}")
            found = True
            break
    if not found:
        print("Barang tidak ditemukan.")

def tampilkan_data_barang():
    if barang_elektronik:
        print("===== Daftar Barang =====")
        for index, barang in enumerate(barang_elektronik):
            print(f"{index}. {barang['nama barang']}, Stok: {barang['stok']}")
    else:
        print("Data barang kosong.")

def tampilkan_jumlah_data():
    print(f"Jumlah Data Tersimpan: {len(barang_elektronik)} Barang")



