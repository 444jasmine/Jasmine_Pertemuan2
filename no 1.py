class Persegi:
    def __init__(self, sisi):
        self.sisi = sisi

    def hitung_luas(self):
        return self.sisi ** 2

    def hitung_keliling(self):
        return 4 * self.sisi

# Contoh penggunaan
sisi_persegi = float(input("Masukkan panjang sisi persegi: "))
persegi = Persegi(sisi_persegi)
print("Luas persegi:", persegi.hitung_luas())
print("Keliling persegi:", persegi.hitung_keliling())
