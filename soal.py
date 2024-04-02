nama_peserta_BUMN = str(input('masukan nama peserta : '))
umur = int(input('masukan umur : '))
pendidikan = str(input('masukan pendidikan : '))
kesehatan = str(input('masukan sehat / tidak sehat : '))
nilai = int(input('transkip nilai : '))

min_pendidikan = ['SMA', 'SMK','D3']
if umur <= 30 and pendidikan in min_pendidikan and kesehatan == "Sehat" and nilai >= 80:
    print("SELAMAT ANDA LOLOS ")
else :
    print("ANDA TIDAK LOLOS ")