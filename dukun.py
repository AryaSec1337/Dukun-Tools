#Author : AryaSec
def ngedukun(chipertext):
    soal_dukun = ""
    lawak_bingits = chipertext.split('-')
    for parah in lawak_bingits:
        if parah:
            length = len(parah) - 9
            character = chr(length ^ 0x50)
            soal_dukun += character
    soal_dukun = soal_dukun[::-1]
    return soal_dukun

chipertext = input("Masukan soal dukun: ")
print("Hasil : ")
print(ngedukun(chipertext))
