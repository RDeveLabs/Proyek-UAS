from data import InputData
from proses import Proses
from view import view

def main():
    try:
        a = int(input("Masukkan angka pertama: "))
        b = int(input("Masukkan angka kedua: "))
        data = InputData(a, b)
        proses = Proses(data)
        tampilan = view(proses)
        print(tampilan.tampilkan_tabel())
    except ValueError:
        return "Input harus berupa angka bulat."
    
if __name__ == "__main__":
    main()