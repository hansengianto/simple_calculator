print("""==============================================
SIMPLE CALCULATOR V0.1
Created By Hansen Gianto
Language : Python 3.9
Os : Windows 10
==============================================
* = Kali
/ = Bagi
+ = Tambah
- = Kurang
==============================================""")

operasi = str(input("Silahkan Pilih Operasi Yang Ingin Dipakai : ")) 
angka1 = int(input("Silahkan Masukan Angka Pertama : "))
angka2 = int(input("Silahkan Masukan Angka Kedua : "))

if operasi == "*":
	print("\nHasil Dari Hitungan Diatas Adalah : " + str(angka1 * angka2))

elif operasi == "/":
	print("\nHasil Dari Hitungan Diatas Adalah : " + str(angka1 / angka2))

elif operasi == "+":
	print("\nHasil Dari Hitungan Diatas Adalah : " + str(angka1 + angka2))

elif operasi == "-":
	print("\nHasil Dari Hitungan Diatas Adalah : " + str(angka1 - angka2))

else:
	print("Maaf, Silahkan Masukan Data Dengan Benar.")