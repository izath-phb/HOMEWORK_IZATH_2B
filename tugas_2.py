import stok_barang as tugas_2
while True:
    tugas_2.tampilan()
    pilihan = int(input('Masukan Pilihan : '))

    if pilihan == 1:
        tugas_2.tambah()

    if pilihan == 2:
        tugas_2.edit_data()
    
    if pilihan == 3:
        tugas_2.hapus()

    if pilihan == 4:
        tugas_2.cari()    

    if pilihan == 5:
        tugas_2.tampilkan_data_barang()  

    if pilihan == 6:
        tugas_2.tampilkan_jumlah_data()

    if pilihan == 7:
        print('='*50)
        print('Terimakasih Telah Mencoba')
        print('='*50)
        exit()

