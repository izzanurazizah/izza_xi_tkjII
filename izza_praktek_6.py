# nama : izza nur azizah
# kelas : xi tkj 2
# no absen : 14
# soal : Buat program Python yang mengambil data penjualan bulanan produk dan menentukan kategori produk berdasarkan penjualan:
# • Jika penjualan lebih dari 1000 unit, kategorikan sebagai "Produk Terlaris." 
# • Jika penjualan antara 500 hingga 1000 unit, kategorikan sebagai "Produk Populer." 
# • Jika penjualan kurang dari 500 unit, kategorikan sebagai "Produk Biasa."

# mengambil data penjualan bulanan produk dari pengguna 
penjualan = int(input("masukkan jumlah penjualan bulanan produk: "))

# menentukan katagori produk berdasarkan penjualan
if penjualan > 1000:
    kategori = "produk terlaris"
elif 500 <= penjualan <= 1000:
    kategori = "produk populer"
else:
    katagori = "produk biasa"

# mencetak hasil
print("jumlah penjualan bulanan: ", penjualan, "unit")
print("kategori produk: ",{katagori})
