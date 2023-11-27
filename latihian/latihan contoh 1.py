def luas_segitiga_siku(x):
	bidang_datar = 'segitiga siku'
	
	alas = int(input('masukan alas: '))
	tinggi = int(input('masukan tinggi: '))
	luas = 0.5 * alas * tinggi
	
	return bidang_datar,luas

def luas_persesegi():
	bidang_datar = 'persegi'
	sisi =int(input('masukan sisi: '))
	luas = sisi * sisi
	
	return bidang_datar,luas


if __name__ == "__main__":
	print("1. luas segitiga siku")
	print("2. luaspersegi")
	print("3. luas lingkaran")
	
	pilih_menu = int(input("pilih menu"))

	if pilih_menu == 1:
		luas_segitiga_siku()
	elif pilih_menu == 2:
		hasil = luas_persegi()
	elif pilih_menu == 3:
		luas_persegi
		break
	print('luas {} adalah {}'.format(hasil[0],hasil[1]))
