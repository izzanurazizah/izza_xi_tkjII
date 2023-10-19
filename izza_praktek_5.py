# nama : izza nur azizah
# kelas : xi tkj 2
# no absen : 14
# soal : Buat program Python yang mengambil nilai tugas (skala 0-100) dan nilai ujian (skala 0-100) seorang siswa dan menentukan nilai akhirnya. Jika nilai tugas lebih dari 70 dan nilai ujian lebih dari 60, siswa lulus dengan nilai "Lulus". Jika tidak, siswa gagal dengan nilai "Gagal".

nilai_tugas = float(input("masukkan nilai tugas (skala 0-100): "))
nilai_ujian = float(input("masukkan nilai ujian (skala 0-100): "))
if nilai_tugas > 70 and nilai_ujian > 60:
    status = "lulus"
else:
    status = "gagal"

print("nilai tugas:", nilai_tugas)
print("nilai ujian:", nilai_ujian)
print("status:", status)