

def luas_segitiga_siku():
	bidang_datar = 'segitiga siku'
	alas = int(input('masukan alas: '))
	tinggi = int(input('masukan tinggi'))
	luas = int(input('masukan tinggi'))
	return bidang_datar, luas 
	
def luas_persegi ():
	bidang_datar = 'persegi'
	sisi = int(input('masukan sisi:  '))
	luas = sisi * sisi
	return bidang_datar, luas_persegi
	
def luas_lingkaran ():
	bidang_datar = 'lingkaran'
	r = int(input('masukan jari2. '))
	luas =3.14 * (r ** 2)
	return bidang_datar, luas_lingkaran
	
if __name__ == "__main__":
	print("1. luas segitiga siku")
	print("2. luas persegi")
	print("3. luas lingkaran")
	
	pilih_menu = int(input("pilih menu: "))
	if pilih_menu == 1:
		hasil = luas_segitiga_siku()
	elif pilih_menu == 2:
		hasil = luas_persegi()
	elif pilih_menu == 3:
		hasil = luas_persegi()
	else:
		print("menu tidak valid")
		exit()
		
	print ('luas {} adalah {}'.format(hasil[0], hasil[1]))
