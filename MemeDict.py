meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "LMAO": "ketawa tak ter kontrol sampai gemetar",
            "ROFL": "ketawa sampai mengelinding di lantai",
            "SMH": "ekspresi menggelng kepala",
            "WTH": "ekspresi kaget",
            "OTW": "pengetahuan di jalan ke lokasi",
            "BRB": "pengetahuan akan pergi dan kembali nanti"
            }
word = input("masukan kata gaul: ")
if word.upper() in meme_dict.keys():
    # Apa yang harus kita lakukan jika kata itu ditemukan?
    print (meme_dict[word.upper()])
else:
    # Apa yang harus kita lakukan jika kata itu tidak ditemukan?
    print ("gak ada kata itu di dict ini")
