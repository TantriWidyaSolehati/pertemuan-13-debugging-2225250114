def status_lulus(nilai):
	if nilai >= 60:
		return "Lulus"
	return "Tidak lulus"


print("Nilai 59 :", status_lulus(59))
print("Nilai 60 :", status_lulus(60))
print("Nilai 61 :", status_lulus(61))
