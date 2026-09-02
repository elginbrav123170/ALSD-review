nama = "Elgin Brav Ekazatia"
nilai_tugas = 100
nilai_uts = 100
nilai_uas = 100

def nilai_akhir(*data):
    nama, nilai_tugas, nilai_uts, nilai_uas = data
    nilai_akhir = 0.3 * nilai_tugas + 0.3 * nilai
    print(f"| {'Nama':11} :", nama, type(nama))
    print(f"| {'Nilai Akhir':12}: {nilai_akhir:.2f}", type(nilai_akhir))