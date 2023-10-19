# nama : izza nur azizah
# kelas : xi tkj 2
# no absen : 14
# soal : Buat program Python yang mengambil estimasi waktu selesai proyek dan tanggal target selesai. Jika estimasi waktu selesai lebih awal atau sama dengan tanggal target, program harus mencetak "Tepat waktu," jika tidak, program harus mencetak "Terlambat."

estimasi_selesai = input("masukkan estimasi waktu selesai proyek (tahun-bulan-tanggal): ")
tanggal_target_selesai = input("masukkan tanggaltarget selesai (tahun-bulan-tanggal): ")

if estimasi_selesai <= tanggal_target_selesai:
    print("tepat waktu")
else:
    print("terlambat")
    