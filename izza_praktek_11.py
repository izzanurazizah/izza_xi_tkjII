# nama : izza nur azizah
# kelas : xi tkj 2
# no absen : 14
# soal : meminta input nilai performa karyawan (1-5)
performa = float(input("masukkan nial performa karyawan (1-5): "))
#meminta input gaji tahunan karyawan
gaji_tahunan = float(input("masukkan gaji tahunan karyawan: "))
# menghitung bonus tahunan menggunakan percabangan ternary
bonus = (0.20 * gaji_tahunan) if performa == 5 else \
        (0.10 * gaji_tahunan) if performa == 4 else \
        (0.05 * gaji_tahunan) if performa == 3 else \
        (0.02 * gaji_tahunan) if performa == 2 else 0

# menampilkan bonus tahunan
# print(f"bonus tahunan: {bonus:.2f} IDR")        