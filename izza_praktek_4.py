# nama : izza nur azizah
# kelas : xi tkj 2
# no absen : 14
# soal : Buat program Python yang mengambil total belanjaan dan status anggota (biasa atau premium). Berikan diskon berdasarkan aturan berikut:
# • Anggota premium: Jika total belanjaan lebih dari 500.000, berikan diskon 15%. Jika tidak, berikan diskon 10%.
# • Anggota biasa: Jika total belanjaan lebih dari 300.000, berikan diskon 7%. Jika tidak, berikan diskon 0%.

total_belanjaan = float(input("masukkan total belanjaan: "))
status_anggota = input("masukkan status anggota (biasa/premium): ").lower()
diskon = 0
if status_anggota == "premium":
    if total_belanjaan > 500000:
        diskon = 0.15 # 15% diskon untuk anggota premium dengan total belanjaan > 500.000
    else: 
        diskon = 0.10 # 10% diskon untuk anggota premium dengan totol belanjaan <= 500.000
elif status_anggota == "biasa":
    if total_belanjaan > 300000:
        diskon = 0.07 #7% diskon untuk anggota biasa dengan total belanjaan > 300,.000
jumlah_bayar = total_belanjaan - (total_belanjaan * diskon)
print("total belanjaan: Rp", total_belanjaan)
print("status_anggota:", status_anggota)
print("diskon yang diterapkan", diskon *100, "%")
print("jumlah yang harus dibayar: Rp", jumlah_bayar)
