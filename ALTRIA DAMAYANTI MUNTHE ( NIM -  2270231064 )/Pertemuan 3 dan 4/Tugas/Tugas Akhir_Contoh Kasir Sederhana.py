
print("Nama: Altria Damayanti Munthe ")
print("NIM: 2270231064 ")
print("Tugas Akhir: Contoh Kasir Sederhana ")





jenis1="" 
jenis2="" 
print("===Program Kasir Sederhana===")
Nama=input("Masukkan Nama Pelanggan: ")
Alamat=input("Masukkan Alamat: ")
NoHP=input("Masukkan NoHP pelanggan: ")
Tanggal=input("Tanggal pembelian: ") 
print("Nama Pelanggan: ",Nama)
print("Alamat P: ",Alamat)
print("NoHP: ",NoHP)
print("Tanggal Pembelian: ",Tanggal) 
print("") 
print("Produk Pakaian") 
def pilihan(i): 
 switcher={ 
 1: '----Kemeja = Rp.135.000----',
 2: '----Kaos = Rp.65.000----',
 3: '----Jaket = Rp.200.000----',
 4: '----Baju Tidur = Rp.75.000----',
 5: '----Dress Brukat = Rp.300.000----',
 } 
 return switcher.get(i,"Masukkan Pilihan Yang Benar!") 
print("1. Kemeja") 
print("2. Kaos") 
print("3. Jaket") 
print("4. Baju Tidur")
print("5. Dress Brukat")
nomor=int(input("Masukkan Pilihan: ")) 
3 
c=pilihan(nomor) 
print(c) 
jumlah1=int(input("Banyak unit yang dibeli: ")) 
if nomor==1: 
 a=jumlah1*135000 
 print("Sub-Total= Rp. ",a) 
 jenis1=("Kemeja") 
if nomor==2: 
 a=jumlah1*65000 
 print("Sub-Total= Rp. ",a) 
 jenis1=("Kaos") 
if nomor==3: 
 a=jumlah1*200000 
 print("Sub-Total= Rp. ",a) 
 jenis1=("Jaket") 
if nomor==4: 
 a=jumlah1*75000 
 print("Sub-Total= Rp. ",a) 
 jenis1=("Baju Tidur")
if nomor==5: 
 a=jumlah1*300000 
 print("Sub-Total= Rp. ",a) 
 jenis1=("Dress Brukat") 
def pilihan (i): 
 switcher={ 
 1: '----celana panjang = Rp.150.000----',
 2: '----Celana Pendek = Rp.85.000----',
 3: '----Jeans = Rp.325.000----',
 4: '----Sarung = Rp.100.000----',
 } 
 return switcher.get(i,"Masukkan Pilihan Yang Benar!") 
print("\nProduk Celana") 
print("1. Celana Panjang") 
print("2. Celana Pendek")
print("3. Jeans") 
print("4. Sarung") 
nomor=int(input("Masukkan Pilihan: ")) 
c=pilihan(nomor) 
print(c) 
jumlah2=int(input("Banyak unit yang dibeli: "))
if nomor==1: 
 b=jumlah2*150000
print("Sub-Total= Rp. ",b) 
jenis2=("Celana Panjang") 
if nomor==2:
 b=jumlah2*85000 
print("Sub-Total= Rp. ",b) 
jenis2=("Celana Pendek") 
if nomor==3:
 b=jumlah2*325000 
print("Sub-Total= Rp. ",b) 
jenis2=("Jeans") 
if nomor==4: 
 b=jumlah2*100000 
print("Sub-Total= Rp. ",b) 
jenis2=("Sarung") 
print("total Belanja= Rp.",a+b) 
uang=int(input("\nUang Tunai: Rp.")) 
akhir=int(uang-(a+b)) 
print("|\n==============================|") 
print("|========== S T R U K ==========|")
print("|================================|") 
print ("=== Nama :",Nama)
print ("=== Alamat :",Alamat)
print ("=== NoHP :",NoHP)
print ("=== Tanggal :",Tanggal)
print ("=== Beli :",jumlah1,jenis1) 
print ("=== ",jumlah2,jenis2) 
print ("=== Tagihan :Rp.",a+b) 
print ("=== Bayar :Rp.",uang) 
print ("=== Kembalian :Rp.",akhir) 
print ("|==========TERIMAKASIH===========|") 
print ("=telah berbelanja di toko kami=") 
