import tabulate as tabel

from proses import Proses

class view:
    def __init__(self, proses: Proses):
        self.proses = proses

    def tampilkan_tabel(self):
        hasil = self.proses.bagi()
        table = [["Angka pertama", self.proses.data.a],["Angka kedua", self.proses.data.b],["Hasil Pembagian", hasil]]
        return tabel.tabulate(table, headers=["Deskripsi", "Nilai"], tablefmt="grid")