# Muhammad Yusron AL Ghoni Rizqullah
# 202310370311333
# Tugas 2 Modul 2 - Lazy Functional (NIM Ganjil)

data_angka = [
    {"sensor": "S1", "nilai": 0},
    {"sensor": "S2", "nilai": 15},
    {"sensor": "S3", "nilai": -3},
    {"sensor": "S4", "nilai": 20},
    {"sensor": "S5", "nilai": "error"},
    {"sensor": "S6", "nilai": 8},
    {"sensor": "S7", "nilai": None},
    {"sensor": "S8", "nilai": 33},
    {"sensor": "S9", "nilai": 5},
    {"sensor": "S10", "nilai": 73},
    {"sensor": "S11", "nilai": -17},
    {"sensor": "S12", "nilai": 100},
    {"sensor": "S13", "nilai": 60},
    {"sensor": "S14", "nilai": -7},
    {"sensor": "S15", "nilai": 90},
    {"sensor": "S16", "nilai": "invalid"},
    {"sensor": "S17", "nilai": 30},
    {"sensor": "S18", "nilai": -45},
    {"sensor": "S19", "nilai": 88},
    {"sensor": "S20", "nilai": 15}
]

def display_generator_manual(generator, title):
    """
    Fungsi utilitas untuk menampilkan hasil generator secara manual
    sesuai instruksi tugas[cite: 656, 657].
    """
    print(f"\n--- {title} ---")
    while True:
        try:
            item = next(generator)
            print(item)
        except StopIteration:
            print("... Iterator Selesai ...")
            break

# Soal 1: Menghasilkan ID sensor dengan nilai bilangan bulat positif.
# Implementasi: Generator Expression [cite: 362, 652]
print("\n--- Menyelesaikan Soal 1 ---")
gen_sensor_positif = (
    data['sensor'] 
    for data in data_angka 
    if isinstance(data['nilai'], int) and data['nilai'] > 0
)
display_generator_manual(gen_sensor_positif, "ID Sensor dengan Nilai Positif")


# Soal 2: Menghasilkan hasil dari pembagian 1000 / nilai valid.
# Implementasi: Fungsi Generator [cite: 271, 652]
def pembagian_seribu_generator(data_list):
    """
    Generator yang menghasilkan 1000 / nilai untuk setiap data yang valid 
    (bilangan bulat positif).
    """
    print("\n--- Menyelesaikan Soal 2 ---")
    for data in data_list:
        nilai = data['nilai']
        if isinstance(nilai, int) and nilai > 0:
            yield 1000 / nilai

gen_pembagian = pembagian_seribu_generator(data_angka)
display_generator_manual(gen_pembagian, "Hasil Pembagian 1000 / Nilai Valid")


# Soal 3: Menghitung kontribusi tiap sensor valid.
# Implementasi: Fungsi Generator [cite: 271, 652]
def kontribusi_sensor_generator(data_list):
    """
    Generator yang menghitung kontribusi setiap sensor valid terhadap total nilai.
    Hasilnya berupa dictionary.
    """
    print("\n--- Menyelesaikan Soal 3 ---")
    # Langkah 1: Hitung total nilai valid terlebih dahulu
    nilai_valid = [data['nilai'] for data in data_list if isinstance(data['nilai'], int) and data['nilai'] > 0]
    total_nilai_valid = sum(nilai_valid)
    
    if total_nilai_valid == 0:
        print("Tidak ada data valid untuk dihitung kontribusinya.")
        return

    # Langkah 2: Yield kontribusi untuk setiap data valid
    for data in data_list:
        nilai = data['nilai']
        if isinstance(nilai, int) and nilai > 0:
            kontribusi_persen = (nilai / total_nilai_valid) * 100
            yield {
                "sensor": data['sensor'],
                "nilai": nilai,
                "kontribusi": f"{kontribusi_persen:.2f}%"
            }

gen_kontribusi = kontribusi_sensor_generator(data_angka)
display_generator_manual(gen_kontribusi, "Kontribusi Tiap Sensor Valid")