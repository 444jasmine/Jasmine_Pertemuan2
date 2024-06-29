class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def cetak_info(self):
        print("Nama:", self.nama)
        print("Umur:", self.umur)

nama = input("Masukkan nama: ")
umur = int(input("Masukkan umur: "))
orang = Manusia(nama, umur)
orang.cetak_info()
