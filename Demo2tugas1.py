# Muhammad Yusron AL Ghoni Rizqullah
# 202310370311333
# Tugas 1 Modul 2 - Fungsional Programming

# Data awal (state)
data_akun = {
    'admin': 'admin123',
    'arsipyusron01': 'password333'
}

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

menu_awal = ("1. Login", "2. Register", "3. Keluar")
menu_utama = ("1. Lihat Daftar Arsip", "2. Tambah Arsip Baru", "3. Ubah Data Arsip", "4. Hapus Arsip", "5. Lihat Profil", "6. Keluar (Logout)")

# --- PURE FUNCTIONS ---

def register_pure(akun, profil, arsip, id_baru, password_baru, nama, jabatan, hp):
    """
    Pure function untuk registrasi. Mengembalikan state baru jika berhasil,
    atau state lama dan pesan error jika gagal.
    """
    if id_baru in akun or not id_baru:
        return akun, profil, arsip, "Registrasi gagal: ID sudah digunakan atau kosong."

    # Membuat salinan data untuk menghindari modifikasi state asli
    new_akun = akun.copy()
    new_profil = profil.copy()
    new_arsip = arsip.copy()

    # Menambahkan data baru
    new_akun[id_baru] = password_baru
    new_profil[id_baru] = {'nama': nama, 'jabatan': jabatan, 'hp': hp}
    new_arsip[id_baru] = []
    
    return new_akun, new_profil, new_arsip, "Registrasi berhasil! Silakan login."

def login_pure(akun, profil, id_pengguna, password):
    """
    Pure function untuk login. Mengembalikan ID pengguna jika berhasil,
    atau None jika gagal.
    """
    if id_pengguna in akun and akun[id_pengguna] == password:
        return id_pengguna, f"\nLogin berhasil! Selamat datang, {profil[id_pengguna]['nama']}."
    return None, "\nLogin gagal. ID atau password salah."

def tambah_arsip_pure(list_arsip_user, arsip_baru):
    """
    Pure function untuk menambah arsip. Mengembalikan list arsip baru.
    """
    # Cek duplikasi ID
    if any(arsip['id_arsip'] == arsip_baru['id_arsip'] for arsip in list_arsip_user):
        return list_arsip_user, "ID Arsip sudah ada. Gagal menambahkan."
        
    # Mengembalikan list baru dengan arsip baru ditambahkan
    return list_arsip_user + [arsip_baru], "Arsip baru berhasil ditambahkan!"

def ubah_arsip_pure(list_arsip_user, id_untuk_ubah, data_update):
    """
    Pure function untuk mengubah arsip. Mengembalikan list arsip baru yang telah diubah.
    Ini adalah contoh fungsi deklaratif, fokus pada 'apa' hasilnya.
    """
    # Menggunakan list comprehension untuk membangun list baru
    # Ini lebih deklaratif daripada loop for dengan kondisi if-else
    arsip_baru = [
        # Jika id cocok, gabungkan data lama dengan data update
        {**arsip, **data_update} if arsip['id_arsip'] == id_untuk_ubah else arsip
        for arsip in list_arsip_user
    ]
    
    # Cek apakah ada perubahan
    if arsip_baru == list_arsip_user:
        return list_arsip_user, "ID Arsip tidak ditemukan."
        
    return arsip_baru, "Data arsip berhasil diperbarui."

def hapus_arsip_pure(list_arsip_user, id_untuk_hapus):
    """
    Pure function untuk menghapus arsip. Mengembalikan list arsip baru tanpa data yang dihapus.
    Ini juga contoh fungsi deklaratif.
    """
    # List comprehension untuk memfilter dan mengembalikan list baru
    arsip_baru = [arsip for arsip in list_arsip_user if arsip['id_arsip'] != id_untuk_hapus]
    
    if len(arsip_baru) == len(list_arsip_user):
        return list_arsip_user, "ID Arsip tidak ditemukan."
        
    return arsip_baru, "Arsip berhasil dihapus."

# --- FUNGSI DENGAN EFEK SAMPING (I/O) ---
# Fungsi-fungsi ini bertanggung jawab untuk interaksi dengan pengguna

def lihat_arsip(arsip_milik_pengguna):
    """Fungsi untuk menampilkan arsip. Hanya berisi I/O (print)."""
    print("\n--- Daftar Arsip Anda ---")
    if not arsip_milik_pengguna:
        print("Anda belum memiliki arsip data.")
    else:
        for arsip in arsip_milik_pengguna:
            print(f"ID Arsip : {arsip['id_arsip']}")
            print(f"Nama     : {arsip['nama']}")
            print(f"Tahun    : {arsip['tahun']}")
            print(f"Kategori : {arsip['kategori']}")
            print("-" * 25)

def jalankan_menu_utama(id_pengguna, data_arsip_global):
    """Menjalankan loop menu, mengelola state arsip khusus untuk user yang login."""
    arsip_user_saat_ini = data_arsip_global.copy()

    while True:
        print("\n--- Menu Utama Pengelolaan Arsip ---")
        for menu in menu_utama:
            print(menu)

        pilihan = input("Pilih menu (1-6): ")

        if pilihan == '1':
            lihat_arsip(arsip_user_saat_ini[id_pengguna])
        
        elif pilihan == '2':
            print("\n--- Tambah Arsip Baru ---")
            id_arsip = input("Masukkan ID unik arsip: ").upper()
            nama_arsip = input("Masukkan Nama/Judul Arsip: ")
            
            tahun_arsip_str = input("Masukkan Tahun Arsip: ")
            try:
                tahun_arsip = int(tahun_arsip_str)
            except ValueError:
                print("Input tahun tidak valid. Gagal menambahkan.")
                continue

            kategori_arsip = input("Masukkan Kategori Arsip: ")
            
            arsip_baru_data = {'id_arsip': id_arsip, 'nama': nama_arsip, 'tahun': tahun_arsip, 'kategori': kategori_arsip}
            
            list_arsip_baru, pesan = tambah_arsip_pure(arsip_user_saat_ini[id_pengguna], arsip_baru_data)
            arsip_user_saat_ini[id_pengguna] = list_arsip_baru # Update state lokal
            print(pesan)

        elif pilihan == '3':
            lihat_arsip(arsip_user_saat_ini[id_pengguna])
            if not arsip_user_saat_ini[id_pengguna]: continue
            
            id_untuk_ubah = input("Masukkan ID Arsip yang akan diubah: ").upper()
            
            nama_baru = input("Masukkan nama arsip baru (kosongkan jika tidak ingin diubah): ")
            tahun_baru_str = input("Masukkan tahun baru (kosongkan jika tidak ingin diubah): ")
            kategori_baru = input("Masukkan kategori baru (kosongkan jika tidak ingin diubah): ")
            
            data_update = {}
            if nama_baru: data_update['nama'] = nama_baru
            if kategori_baru: data_update['kategori'] = kategori_baru
            if tahun_baru_str:
                try:
                    data_update['tahun'] = int(tahun_baru_str)
                except ValueError:
                    print("Input tahun tidak valid. Perubahan tahun dibatalkan.")

            if data_update:
                list_arsip_baru, pesan = ubah_arsip_pure(arsip_user_saat_ini[id_pengguna], id_untuk_ubah, data_update)
                arsip_user_saat_ini[id_pengguna] = list_arsip_baru # Update state lokal
                print(pesan)
            else:
                print("Tidak ada data yang diubah.")

        elif pilihan == '4':
            lihat_arsip(arsip_user_saat_ini[id_pengguna])
            if not arsip_user_saat_ini[id_pengguna]: continue
            
            id_untuk_hapus = input("Masukkan ID Arsip yang akan dihapus: ").upper()
            konfirmasi = input(f"Anda yakin ingin menghapus arsip dengan ID '{id_untuk_hapus}'? (y/n): ").lower()
            if konfirmasi == 'y':
                list_arsip_baru, pesan = hapus_arsip_pure(arsip_user_saat_ini[id_pengguna], id_untuk_hapus)
                arsip_user_saat_ini[id_pengguna] = list_arsip_baru # Update state lokal
                print(pesan)
            else:
                print("Penghapusan dibatalkan.")

        elif pilihan == '5':
            # Fungsi ini hanya membaca, jadi tidak perlu versi pure yang kompleks
            print("\n--- Profil Anda ---")
            profil = data_profil[id_pengguna]
            print(f"ID       : {id_pengguna}")
            print(f"Nama     : {profil['nama']}")
            print(f"Jabatan  : {profil['jabatan']}")
            print(f"No. HP   : {profil['hp']}")

        elif pilihan == '6':
            print("Anda telah logout.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
    
    # Mengembalikan state arsip yang mungkin telah berubah setelah logout
    return arsip_user_saat_ini

# --- PROGRAM UTAMA ---
def main():
    """Fungsi utama untuk menjalankan aplikasi."""
    # State utama aplikasi
    current_data_akun = data_akun
    current_data_profil = data_profil
    current_data_arsip = data_arsip

    while True:
        print("\n========================================")
        print("  Sistem Manajemen Arsip Negara Digital ")
        print("========================================")
        for menu in menu_awal:
            print(menu)

        pilihan = input("Pilih menu (1-3): ")

        if pilihan == '1':
            id_pengguna_input = input("Masukkan ID: ").lower()
            password_input = input("Masukkan Password: ")
            
            id_pengguna_login, pesan = login_pure(current_data_akun, current_data_profil, id_pengguna_input, password_input)
            print(pesan)

            if id_pengguna_login:
                # Jalankan menu utama dan terima kembali state arsip yang mungkin sudah diubah
                updated_data_arsip = jalankan_menu_utama(id_pengguna_login, current_data_arsip)
                current_data_arsip = updated_data_arsip # Update state global

        elif pilihan == '2':
            print("\n--- Halaman Registrasi ---")
            id_baru = input("Masukkan ID baru: ").lower()
            password_baru = input("Masukkan password baru: ")
            nama = input("Masukkan Nama Lengkap: ")
            jabatan = input("Masukkan Jabatan: ")
            hp = input("Masukkan No. HP: ")

            # Panggil fungsi murni dan update state
            new_akun, new_profil, new_arsip, pesan = register_pure(
                current_data_akun, current_data_profil, current_data_arsip,
                id_baru, password_baru, nama, jabatan, hp
            )
            current_data_akun = new_akun
            current_data_profil = new_profil
            current_data_arsip = new_arsip
            print(pesan)
        
        elif pilihan == '3':
            print("Terima kasih telah menggunakan sistem. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan angka 1-3.")

if __name__ == "__main__":
    main()