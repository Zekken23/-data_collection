# Muhammad Yusron AL Ghoni Rizqullah
# 202310370311333
# Tugas 1 Modul 3 - Fungsional Programming

# Import 'reduce' dari functools sesuai materi Modul 3
from functools import reduce

# --- Data awal (state) ---
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
# Menu utama dimodifikasi untuk Tugas Modul 3
menu_utama = (
    "1. Lihat Daftar Arsip", 
    "2. Tambah Arsip Baru", 
    "3. Ubah Data Arsip", 
    "4. Hapus Arsip", 
    "5. Lihat Profil",
    "6. Cari Arsip (by Kategori/Tahun)", # Fitur baru Modul 3 (Filter)
    "7. Lihat Statistik Arsip",          # Fitur baru Modul 3 (Reduce & Rekursif)
    "8. Keluar (Logout)"
)

# --- PURE FUNCTIONS (dari Modul 2) ---

def register_pure(akun, profil, arsip, id_baru, password_baru, nama, jabatan, hp):
    """
    Pure function untuk registrasi. Mengembalikan state baru jika berhasil,
    atau state lama dan pesan error jika gagal.
    """
    if id_baru in akun or not id_baru:
        return akun, profil, arsip, "Registrasi gagal: ID sudah digunakan atau kosong."

    new_akun = akun.copy()
    new_profil = profil.copy()
    new_arsip = arsip.copy()

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
    if any(arsip['id_arsip'] == arsip_baru['id_arsip'] for arsip in list_arsip_user):
        return list_arsip_user, "ID Arsip sudah ada. Gagal menambahkan."
        
    return list_arsip_user + [arsip_baru], "Arsip baru berhasil ditambahkan!"

# Penjelasan: Konsep 'list comprehension' (Modul 3) digunakan di sini.
# Alasan: List comprehension adalah cara deklaratif untuk membuat list baru
# berdasarkan list yang ada, yang sangat cocok untuk prinsip immutability.
# Ini lebih ringkas daripada loop 'for' imperatif untuk mengubah data.
def ubah_arsip_pure(list_arsip_user, id_untuk_ubah, data_update):
    """
    Pure function untuk mengubah arsip. Mengembalikan list arsip baru yang telah diubah.
    """
    arsip_baru = [
        {**arsip, **data_update} if arsip['id_arsip'] == id_untuk_ubah else arsip
        for arsip in list_arsip_user
    ]
    
    if arsip_baru == list_arsip_user:
        return list_arsip_user, "ID Arsip tidak ditemukan."
        
    return arsip_baru, "Data arsip berhasil diperbarui."

# Penjelasan: Konsep 'list comprehension' (Modul 3) digunakan di sini.
# Alasan: Sama seperti 'ubah', list comprehension adalah cara fungsional 
# untuk *menyaring* elemen dan membuat list baru tanpa memodifikasi list asli.
def hapus_arsip_pure(list_arsip_user, id_untuk_hapus):
    """
    Pure function untuk menghapus arsip. Mengembalikan list arsip baru tanpa data yang dihapus.
    """
    arsip_baru = [arsip for arsip in list_arsip_user if arsip['id_arsip'] != id_untuk_hapus]
    
    if len(arsip_baru) == len(list_arsip_user):
        return list_arsip_user, "ID Arsip tidak ditemukan."
        
    return arsip_baru, "Arsip berhasil dihapus."

# --- PURE FUNCTIONS (Tambahan Modul 3) ---

def _filter_arsip_helper(arsip, field, value):
    """Helper murni untuk fungsi filter (tanpa lambda)."""
    if field == 'kategori':
        # .lower() untuk case-insensitive search
        return arsip.get('kategori', '').lower() == value.lower()
    elif field == 'tahun':
        try:
            return arsip.get('tahun') == int(value)
        except (ValueError, TypeError):
            return False
    return False

# Penjelasan: Menggunakan 'filter' (Konsep Modul 3).
# Alasan: 'filter' dipilih karena ini adalah cara fungsional/deklaratif untuk
# "menyaring" koleksi data berdasarkan kriteria (fungsi predikat),
# tanpa perlu menulis loop 'for' imperatif.
def filter_arsip_pure(list_arsip_user, field, value):
    """Pure function untuk memfilter arsip menggunakan filter()."""
    
    # 'filter' butuh fungsi dengan 1 argumen. Kita buatkan fungsi (bukan lambda)
    # yang memanggil helper kita.
    def filter_predicate(arsip):
        return _filter_arsip_helper(arsip, field, value)
    
    hasil_filter_objek = filter(filter_predicate, list_arsip_user)
    return list(hasil_filter_objek)

# Penjelasan: Menggunakan 'reduce' (Konsep Modul 3).
# Alasan: 'reduce' dipilih untuk "mereduksi"/"melipat" sebuah list arsip 
# menjadi satu nilai tunggal, dalam hal ini sebuah dictionary 
# yang berisi statistik (akumulasi).
def _statistik_kategori_pure(list_arsip_user):
    """Pure function untuk statistik kategori menggunakan reduce."""
    
    # Fungsi helper untuk reduce (2 argumen: akumulator, item)
    def counter(akumulator, arsip):
        kategori = arsip.get('kategori', 'Lainnya')
        # Kita memutasi akumulator; ini umum dalam reduce Python demi efisiensi
        akumulator[kategori] = akumulator.get(kategori, 0) + 1
        return akumulator
    
    if not list_arsip_user:
        return {}
    
    # {} adalah nilai awal (initializer) untuk akumulator
    return reduce(counter, list_arsip_user, {})

# Penjelasan: Menggunakan 'rekursif' (Konsep Modul 3).
# Alasan: 'rekursif' dipilih sebagai alternatif fungsional untuk loop
# dalam menghitung total elemen. Ini memecah masalah 
# (menghitung list) menjadi sub-masalah (1 + hitung sisanya).
def _hitung_arsip_rekursif_pure(list_arsip):
    """Pure function untuk menghitung jumlah arsip secara rekursif."""
    if not list_arsip: 
        return 0 # Base Case
    else:
        # Recursive Case
        return 1 + _hitung_arsip_rekursif_pure(list_arsip[1:]) 

def statistik_arsip_pure(list_arsip_user):
    """Menggabungkan fungsi statistik (reduce & rekursif)."""
    total_arsip = _hitung_arsip_rekursif_pure(list_arsip_user)
    arsip_per_kategori = _statistik_kategori_pure(list_arsip_user)
    return total_arsip, arsip_per_kategori

# --- FUNGSI DENGAN EFEK SAMPING (I/O) ---

def lihat_arsip(arsip_milik_pengguna):
    """Fungsi untuk menampilkan arsip. Hanya berisi I/O (print)."""
    # Fungsi ini tidak perlu murni karena tugasnya hanya I/O (print)
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
    # State arsip lokal untuk sesi user ini
    arsip_user_saat_ini = data_arsip_global.copy()

    while True:
        print("\n--- Menu Utama Pengelolaan Arsip ---")
        for menu in menu_utama:
            print(menu)

        pilihan = input("Pilih menu (1-8): ")

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
            
            # Panggil fungsi murni
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
                # Panggil fungsi murni
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
                # Panggil fungsi murni
                list_arsip_baru, pesan = hapus_arsip_pure(arsip_user_saat_ini[id_pengguna], id_untuk_hapus)
                arsip_user_saat_ini[id_pengguna] = list_arsip_baru # Update state lokal
                print(pesan)
            else:
                print("Penghapusan dibatalkan.")

        elif pilihan == '5':
            print("\n--- Profil Anda ---")
            profil = data_profil[id_pengguna]
            print(f"ID       : {id_pengguna}")
            print(f"Nama     : {profil['nama']}")
            print(f"Jabatan  : {profil['jabatan']}")
            print(f"No. HP   : {profil['hp']}")

        # --- FITUR BARU MODUL 3 ---
        elif pilihan == '6':
            print("\n--- Cari Arsip (Filter) ---")
            print("Cari berdasarkan: 1. Kategori, 2. Tahun")
            pilihan_cari = input("Pilih kriteria (1-2): ")
            
            if pilihan_cari == '1':
                field = 'kategori'
                value = input("Masukkan Kategori yang dicari: ")
            elif pilihan_cari == '2':
                field = 'tahun'
                value = input("Masukkan Tahun yang dicari: ")
            else:
                print("Pilihan tidak valid.")
                continue
                
            if not value:
                print("Input pencarian tidak boleh kosong.")
                continue

            # Panggil fungsi murni 'filter_arsip_pure'
            hasil_filter = filter_arsip_pure(arsip_user_saat_ini[id_pengguna], field, value)
            
            if not hasil_filter:
                print(f"Tidak ada arsip yang cocok dengan {field} '{value}'.")
            else:
                print(f"\n--- Hasil Pencarian untuk {field} '{value}' ---")
                lihat_arsip(hasil_filter) # Gunakan fungsi lihat_arsip yang ada
        
        # --- FITUR BARU MODUL 3 ---
        elif pilihan == '7':
            print("\n--- Statistik Arsip ---")
            # Panggil fungsi murni 'statistik_arsip_pure'
            total_arsip, arsip_per_kategori = statistik_arsip_pure(arsip_user_saat_ini[id_pengguna])
            
            print(f"Total Arsip (dihitung rekursif): {total_arsip}")
            print("\nJumlah Arsip per Kategori (dihitung dgn reduce):")
            if not arsip_per_kategori:
                print("- Belum ada arsip -")
            else:
                for kategori, jumlah in arsip_per_kategori.items():
                    print(f"- {kategori}: {jumlah} arsip")
        
        # --- AKHIR FITUR BARU ---

        elif pilihan == '8': # Diubah dari 6 menjadi 8
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
    # Jalankan fungsi main() untuk memulai program
    main()