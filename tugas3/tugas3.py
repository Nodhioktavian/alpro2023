

if __name__ == "__main__" :
	input_str = input("masukkan diameter tabung: ")
	diameter =float(input_str)
	input_str =input("masukkan tinggi tabung: ")
	t = float(input_str)
	pi = 22.0/7.0
	r =diameter/2
	print("volume tabung dengan diameter {} dan tinggi {} adalah: {}" .format(diameter, t, pi*r**2*t))
