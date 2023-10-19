# nama : izza nur azizah
# kelas : xi tkj 2
# no absen : 14
# soal : meminta input durasi peminjaman buku dalam hari
durasi_peminjaman = int(input("masukkan durasi peminjaman uku dalam hari: "))
# menentukan jenis pinjaman berdasarkan durasi
if durasi_peminjaman <= 7:
    jenis_pinjaman = "pminjaman pendek"
elif 7 < durasi_peminjaman <= 30:
    jenis_pinjaman = "pinjaman menengah"
else:
    jenis_pinjaman = "pinjaman panjang"
# menampilkan jenis pinjaman
print(f"durasi pinjaman: {durasi_peminjaman} hari")
print(f"jenis pinjaman: {jenis_pinjaman}")