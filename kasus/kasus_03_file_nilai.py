with open("nilai.txt", "r") as file:
	nilai = [int(baris.strip()) for baris in file if baris.strip()]

if nilai:
	print("Rata-rata:", sum(nilai) / len(nilai))
else:
	print("Tidak ada nilai untuk dihitung.")
