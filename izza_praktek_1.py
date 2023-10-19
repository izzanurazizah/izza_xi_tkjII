# nama: izza nur azizah
# kelas : xi tkj 2
# absen : 14
# soal : Buat program Python yang mengambil total belanjaan pelanggan dan memberikan diskon berdasarkan aturan berikut

total_belanjaan = float(input("total_belanjaan anda: "))
if total_belanjaan > 500000:
    diskon = total_belanjaan*0.10
elif total_belanjaan >= 300000:
    diskon = total_belanjaan *0.05    
else:
    diskon = 0
total_pembayaran = total_belanjaan - diskon
print("total pembayaran setelah diskon: {total_pembayaran}")