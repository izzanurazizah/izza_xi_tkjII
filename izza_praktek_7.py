# nama : izza nur azizah
# kelas : xi tkj 2
# no absen : 14
# soal : meminta input informasi pembaruan misalnya  "Y" atau "N"9
pembaruan = input("apakah terdapat pembaruan yang memerlukan restart (Y/N)? ").strip().lower()
# memeriksa apakah pembaruan memerlukan restart
if pembaruan == "Y":
    print("sistem perlu di-restart.")
elif pembaruan == "N": 
    print("sistem tidak perlu di-restart.")
else:
    print("input tidak valid. silahkan masukkan 'Y' atau 'N' untuk mengindikasikan pembaruan")