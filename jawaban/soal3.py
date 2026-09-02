def hitung_rata2(list_nilai):
    RataRata = []
    for i in range(len(list_nilai)):
        if list_nilai[i] >= 0 and list_nilai[i] <= 100:
            print(f"Nilai ke-{i+1}: {list_nilai[i]}")
            RataRata.append(list_nilai[i])
        else:
            continue
    print(f"Rata-rata: {sum(RataRata) / len(RataRata)}")
nilai_mhs = [80, 75, 90, 100, 88]
hitung_rata2(nilai_mhs)