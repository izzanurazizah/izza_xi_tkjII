# nama : izza nur azizah
# kelas : xi tkj 2
# no absen : 14
# soal : memeinta input status persiapan proyek (siap atau tunda)
status_persiapan = input("masukkan status persiapan proyek (siap/tunda):").strip().lower()
# menentukan proyek apakah bisa diluncurkan
if status_persiapan == "siap":
    print("proyek diluncurkan.")
elif status_persiapan == "tunda":
    print("proyek ditunda.")
else:
    print("status persiapan tidak valid. masukkan 'siap' atau ' tunda' ")