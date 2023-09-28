# Sistem Penilaian Akhir Mahasiswa
# Fungsi yang digunakan untuk menghitung nilai akhir satu mahasiswa
def hitung_nilai_akhir(uts, uas):
    return (uts + uas) / 2

# menghitung nilai akhir semua mahasiswa
def hitung_nilai_akhir_semua(data_mahasiswa):
    data_nilai_akhir = {}
    for nama, nilai in data_mahasiswa.items():
        uts, uas = nilai
        nilai_akhir = hitung_nilai_akhir(uts, uas)
        data_nilai_akhir[nama] = nilai_akhir
    return data_nilai_akhir

# menampilkan nilai akhir
def tampilkan_nilai_akhir(data_nilai_akhir):
    print("Hasil Nilai Akhir Mahasiswa:")
    for nama, nilai_akhir in data_nilai_akhir.items():
        print("Nama: {}\tNilai Akhir: {:.2f}".format(nama, nilai_akhir))

def main():
    data_mahasiswa = {
        "Mahasiswa 1": (80, 90),  # Contoh data nilai mahasiswa 1
        "Mahasiswa 2": (75, 85),  # Contoh data nilai mahasiswa 2
    }

    data_nilai_akhir = hitung_nilai_akhir_semua(data_mahasiswa)
    tampilkan_nilai_akhir(data_nilai_akhir)

if __name__ == "__main__":
    main()



