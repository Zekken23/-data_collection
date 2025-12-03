# Muhammad Yusron AL Ghoni Rizqullah
# 202310370311333

# ----- Arsip Negara ------
# by: Yuson AL Ghoni Rizqullah
# 1. Data akun disimpan dalam dictionary (ID: password)
data_akun = {
    'admin': 'admin123',
    'arsipyusron01': 'password333'
}

# 2. Data profil disimpan dalam nested dictionary (ID: {profil})
data_profil = {
    'admin': {'nama': 'Administrator', 'jabatan': 'Kepala Arsip Nasional', 'hp': '081234567890'},
    'arsipyusron01': {'nama': 'Yusron Al Ghoni R', 'jabatan': 'Pro Arsip 1', 'hp': '087654321098'}
}

data_arsip = {
    'admin': [
        {'id_arsip': 'SK001', 'nama': 'Surat Keputusan Presiden No. 42', 'tahun': 2002, 'kategori': 'Pemerintahan'},
        {'id_arsip': 'PP007', 'nama': 'Peraturan Pemerintah Pengganti UU', 'tahun': 2023, 'kategori': 'Hukum'}
    ],
    'arsipyusron01': [
        {'id_arsip': 'DKM01', 'nama': 'Dokumen Kemerdekaan Asli', 'tahun': 1945, 'kategori': 'Sejarah'}
    ]
}


# 3. Daftar menu aplikasi disimpan dalam bentuk tuple
menu_awal = ("1. Login", "2. Register", "3. Keluar")
menu_utama = ("1. Lihat Daftar Arsip", "2. Tambah Arsip Baru", "3. Ubah Data Arsip", "4. Hapus Arsip", "5. Lihat Profil", "6. Keluar (Logout)")

# --- FUNGSI-FUNGSI APLIKASI ---

def register():
    """Fungsi untuk mendaftarkan pengguna baru."""
    print("\n--- Halaman Registrasi ---")
    while True:
        id_baru = input("Masukkan ID baru: ").lower()
        if id_baru in data_akun:
            print("ID sudah digunakan. Silakan pilih ID lain.")
        elif not id_baru:
             print("ID tidak boleh kosong.")
        else:
            break

    password_baru = input("Masukkan password baru: ")
    # Input data profil
    nama = input("Masukkan Nama Lengkap: ")
    jabatan = input("Masukkan Jabatan: ")
    hp = input("Masukkan No. HP: ")

    # Simpan data baru
    data_akun[id_baru] = password_baru
    data_profil[id_baru] = {'nama': nama, 'jabatan': jabatan, 'hp': hp}
    data_arsip[id_baru] = [] # Buat list arsip kosong untuk pengguna baru

    print("\nRegistrasi berhasil! Silakan login.")

def login():
    """Fungsi untuk login pengguna."""
    print("\n--- Halaman Login ---")
    id_pengguna = input("Masukkan ID: ").lower()
    password = input("Masukkan Password: ")

    # Pengecekan kredensial
    if id_pengguna in data_akun and data_akun[id_pengguna] == password:
        print(f"\nLogin berhasil! Selamat datang, {data_profil[id_pengguna]['nama']}.")
        return id_pengguna # Kembalikan ID pengguna yang berhasil login
    else:
        print("\nLogin gagal. ID atau password salah.")
        return None

def lihat_arsip(id_pengguna):
    """Fungsi untuk menampilkan semua arsip milik pengguna yang login."""
    print("\n--- Daftar Arsip Anda ---")
    arsip_milik_pengguna = data_arsip[id_pengguna]

    if not arsip_milik_pengguna:
        print("Anda belum memiliki arsip data.")
    else:
        for arsip in arsip_milik_pengguna:
            print(f"ID Arsip : {arsip['id_arsip']}")
            print(f"Nama     : {arsip['nama']}")
            print(f"Tahun    : {arsip['tahun']}")
            print(f"Kategori : {arsip['kategori']}")
            print("-" * 25)

def tambah_arsip(id_pengguna):
    """Fungsi untuk menambah data arsip baru."""
    print("\n--- Tambah Arsip Baru ---")
    id_arsip = input("Masukkan ID unik arsip (contoh: SK002): ").upper()

    # Validasi agar ID arsip unik untuk pengguna ini
    for arsip in data_arsip[id_pengguna]:
        if arsip['id_arsip'] == id_arsip:
            print("ID Arsip sudah ada. Gagal menambahkan.")
            return

    nama_arsip = input("Masukkan Nama/Judul Arsip: ")
    while True: # Validasi input tahun harus angka
        try:
            tahun_arsip = int(input("Masukkan Tahun Arsip: "))
            break
        except ValueError:
            print("Input tahun tidak valid. Harap masukkan angka.")

    kategori_arsip = input("Masukkan Kategori Arsip: ")

    arsip_baru = {
        'id_arsip': id_arsip,
        'nama': nama_arsip,
        'tahun': tahun_arsip,
        'kategori': kategori_arsip
    }

    data_arsip[id_pengguna].append(arsip_baru)
    print("Arsip baru berhasil ditambahkan!")

def ubah_arsip(id_pengguna):
    """Fungsi untuk mengubah data arsip yang ada."""
    lihat_arsip(id_pengguna)
    if not data_arsip[id_pengguna]:
        return

    print("\n--- Ubah Data Arsip ---")
    id_untuk_ubah = input("Masukkan ID Arsip yang akan diubah: ").upper()

    arsip_ditemukan = None
    for arsip in data_arsip[id_pengguna]:
        if arsip['id_arsip'] == id_untuk_ubah:
            arsip_ditemukan = arsip
            break

    if arsip_ditemukan:
        print(f"Data lama: {arsip_ditemukan['nama']} ({arsip_ditemukan['tahun']})")
        nama_baru = input("Masukkan nama arsip baru (kosongkan jika tidak ingin diubah): ")
        tahun_baru_str = input("Masukkan tahun baru (kosongkan jika tidak ingin diubah): ")
        kategori_baru = input("Masukkan kategori baru (kosongkan jika tidak ingin diubah): ")

        if nama_baru:
            arsip_ditemukan['nama'] = nama_baru
        if tahun_baru_str:
            while True:
                try:
                    arsip_ditemukan['tahun'] = int(tahun_baru_str)
                    break
                except ValueError:
                    print("Input tahun tidak valid.")
                    tahun_baru_str = input("Masukkan tahun baru (angka): ")
        if kategori_baru:
            arsip_ditemukan['kategori'] = kategori_baru

        print("Data arsip berhasil diperbarui.")
    else:
        print("ID Arsip tidak ditemukan.")

def hapus_arsip(id_pengguna):
    """Fungsi untuk menghapus data arsip."""
    lihat_arsip(id_pengguna)
    if not data_arsip[id_pengguna]:
        return

    print("\n--- Hapus Data Arsip ---")
    id_untuk_hapus = input("Masukkan ID Arsip yang akan dihapus: ").upper()

    arsip_dihapus = None
    for i, arsip in enumerate(data_arsip[id_pengguna]):
        if arsip['id_arsip'] == id_untuk_hapus:
            konfirmasi = input(f"Anda yakin ingin menghapus arsip '{arsip['nama']}'? (y/n): ").lower()
            if konfirmasi == 'y':
                arsip_dihapus = data_arsip[id_pengguna].pop(i)
            break

    if arsip_dihapus:
        print("Arsip berhasil dihapus.")
    else:
        print("Penghapusan dibatalkan atau ID Arsip tidak ditemukan.")

def lihat_profil(id_pengguna):
    """Fungsi untuk menampilkan profil pengguna yang sedang login."""
    print("\n--- Profil Anda ---")
    profil = data_profil[id_pengguna]
    print(f"ID       : {id_pengguna}")
    print(f"Nama     : {profil['nama']}")
    print(f"Jabatan  : {profil['jabatan']}")
    print(f"No. HP   : {profil['hp']}")

def jalankan_menu_utama(id_pengguna):
    """Menjalankan loop menu setelah pengguna berhasil login."""
    while True:
        print("\n--- Menu Utama Pengelolaan Arsip ---")
        # Menggunakan slicing untuk menampilkan menu
        for menu in menu_utama[:]:
            print(menu)

        pilihan = input("Pilih menu (1-6): ")

        if pilihan == '1':
            lihat_arsip(id_pengguna)
        elif pilihan == '2':
            tambah_arsip(id_pengguna)
        elif pilihan == '3':
            ubah_arsip(id_pengguna)
        elif pilihan == '4':
            hapus_arsip(id_pengguna)
        elif pilihan == '5':
            lihat_profil(id_pengguna)
        elif pilihan == '6':
            print("Anda telah logout.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# --- PROGRAM UTAMA ---
def main():
    """Fungsi utama untuk menjalankan aplikasi."""
    while True:
        print("\n========================================")
        print("  Sistem Manajemen Arsip Negara Digital ")
        print("========================================")

        # Menggunakan slicing untuk menampilkan menu awal
        for menu in menu_awal[:]:
            print(menu)

        pilihan = input("Pilih menu (1-3): ")

        if pilihan == '1':
            id_pengguna_login = login()
            if id_pengguna_login:
                # Jika login berhasil, jalankan menu utama
                jalankan_menu_utama(id_pengguna_login)
        elif pilihan == '2':
            register()
        elif pilihan == '3':
            print("Terima kasih telah menggunakan sistem. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan angka 1-3.")

if __name__ == "__main__":
    main()