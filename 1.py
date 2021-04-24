print ("------------- PROGRAM MENGHITUNG BUNGA TABUNGAN -------------")

tabungan = int(input("Masukan jumlah tabungan ="))
lama = int(input("Masukan jumlah lama menabung (bulan) = "))

sukuBunga = (2.5) / 100

for i in range (lama) :
   tabungan += (tabungan * sukuBunga)

print("")

print("Saldo tabungan anda " + str (lama) + " bulan, adalah " + str (round(tabungan)))