import os
import csv
import pandas as pd
from tabulate import tabulate
import random
import time
from datetime import datetime, timedelta

# Tentukan lebar terminal
lebar_terminal = 160

def cls():  # agar tampilan terminal rapi
    os.system("cls" if os.name == "nt" else "clear")

def garis(x):  # untuk garis sebagai pembatas logo
    print(x * lebar_terminal)

def skip():
    input("Tekan tombol enter untuk melanjutkan >>> ")

def center(text, width=lebar_terminal):  # fungsi untuk meletakkan teks di tengah
    return "\n".join([line.center(width) for line in text.splitlines()])

def Agrismart():  # logo
    logo = """
    █████╗  ██████╗  ██████╗ ██╗███████╗███╗   ███╗ █████╗ ██████╗ ████████╗
    ██╔══██╗██╔════╝ ██╔══██╗██║██╔════╝████╗ ████║██╔══██╗██╔══██╗╚══██╔══╝
    ███████║██║  ███╗██████╔╝██║███████╗██╔████╔██║███████║██████╔╝   ██║   
    ██╔══██║██║   ██║██╔══██╗██║╚════██║██║╚██╔╝██║██╔══██║██╔══██╗   ██║   
    ██║  ██║╚██████╔╝██║  ██║██║███████║██║ ╚═╝ ██║██║  ██║██║  ██║   ██║   
    ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   
    """
    print(center(logo))

def terimakasih():
    thanks = """
    ████████╗███████╗██████╗ ██╗███╗   ███╗ █████╗ ██╗  ██╗ █████╗ ███████╗██╗██╗  ██╗
    ╚══██╔══╝██╔════╝██╔══██╗██║████╗ ████║██╔══██╗██║ ██╔╝██╔══██╗██╔════╝██║██║  ██║
       ██║   █████╗  ██████╔╝██║██╔████╔██║███████║█████╔╝ ███████║███████╗██║███████║
       ██║   ██╔══╝  ██╔══██╗██║██║╚██╔╝██║██╔══██║██╔═██╗ ██╔══██║╚════██║██║██╔══██║
       ██║   ███████╗██║  ██║██║██║ ╚═╝ ██║██║  ██║██║  ██╗██║  ██║███████║██║██║  ██║
       ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═╝
    """
    print(center(thanks))

def tampilkan_peraturan():
    cls()
    garis("=")
    Agrismart()
    garis("=")
    peraturan = """
    Peraturan AgriSmart:
    
    1. Pendaftaran dan Keanggotaan
    - Setiap konsumen wajib mendaftar sebagai anggota sebelum memulai transaksi dan menggunakan layanan kami.
    - Informasi pribadi dan data yang diberikan saat pendaftaran harus akurat dan diperbarui secara berkala.

    2. Pemilihan Paket Layanan
    - Konsumen dapat memilih paket layanan yang sesuai dengan kebutuhan pengelolaan tanaman, mulai dari penyediaan bibit, perawatan, hingga pemanenan.
    - Setiap paket memiliki deskripsi layanan yang jelas, termasuk durasi, biaya, dan jenis tanaman yang dikelola.

    3. Pembayaran dan Biaya
    - Pembayaran untuk setiap layanan dilakukan di awal proses sesuai dengan ketentuan yang telah disepakati.
    - Konsumen wajib membayar tepat waktu sesuai dengan metode pembayaran yang tersedia. Keterlambatan pembayaran akan dikenakan denda sesuai kebijakan yang berlaku.
    - Biaya tambahan dapat dikenakan jika ada perubahan pada jenis layanan atau permintaan khusus selama masa pengelolaan tanaman.

    4. Pengiriman dan Ketersediaan Produk
    - Penyediaan bibit dan produk pertanian lainnya akan dikirimkan sesuai jadwal yang telah ditentukan dalam kontrak layanan.
    - Konsumen akan diberitahu jika ada keterlambatan pengiriman atau ketidaksesuaian stok produk.
    - Konsumen harus memeriksa produk saat penerimaan dan melaporkan kerusakan atau ketidaksesuaian dalam waktu 48 jam setelah penerimaan.

    5. Perawatan Tanaman
    - Layanan perawatan tanaman termasuk penyiraman, pemupukan, dan perlindungan dari hama akan dilakukan sesuai dengan jadwal yang disepakati.
    - Konsumen yang melakukan perawatan tanaman secara mandiri di luar layanan yang diberikan harus mengikuti panduan yang disediakan oleh kami untuk menjaga kualitas tanaman.
    - Kerusakan tanaman yang disebabkan oleh kelalaian konsumen di luar layanan yang disediakan tidak menjadi tanggung jawab perusahaan.

    6. Pengembalian dan Penukaran
    - Pengembalian atau penukaran bibit atau produk pertanian hanya dapat dilakukan jika produk tidak sesuai dengan spesifikasi yang telah disepakati atau jika terjadi kerusakan saat pengiriman.
    - Permintaan pengembalian atau penukaran harus diajukan dalam waktu 7 hari setelah penerimaan produk.

    7. Garansi dan Jaminan Kualitas
    - Kami memberikan garansi kualitas terhadap bibit dan produk pertanian yang kami sediakan selama jangka waktu tertentu sesuai dengan jenis tanaman.
    - Konsumen wajib mengikuti instruksi perawatan agar garansi tetap berlaku. Jika ditemukan kelalaian dalam perawatan, garansi dapat dibatalkan.

    8. Tanggung Jawab Konsumen
    - Konsumen bertanggung jawab untuk mematuhi aturan yang berlaku terkait pengelolaan tanaman di wilayah mereka, termasuk peraturan tentang lingkungan dan penggunaan bahan kimia.
    - Setiap kerusakan atau kerugian yang terjadi akibat ketidakpatuhan terhadap aturan tersebut menjadi tanggung jawab konsumen.

    9. Pembatalan dan Penghentian Layanan
    - Konsumen dapat membatalkan layanan dengan memberikan pemberitahuan kepada admin setidaknya 7 hari sebelum jadwal layanan dimulai.
    - Pembatalan setelah layanan dimulai dapat dikenakan biaya pembatalan sebesar persentase tertentu dari total biaya layanan.
    - Kami berhak menghentikan layanan kepada konsumen yang melanggar peraturan atau tidak mematuhi kewajiban pembayaran.

    10. Penyelesaian Sengketa
    - Jika terjadi perselisihan terkait layanan yang diberikan, konsumen dan pihak penyedia layanan berkomitmen untuk menyelesaikan secara musyawarah.
    - Jika musyawarah tidak mencapai kesepakatan, maka sengketa akan diselesaikan melalui jalur hukum sesuai dengan hukum yang berlaku di wilayah operasional bisnis.
    """
    print(peraturan)
    skip()

# Variabel untuk menyimpan status login dan peran pengguna
is_logged_in = False
role = None  # Menyimpan apakah pengguna adalah 'admin' atau 'user'
username = None  # Menyimpan username untuk digunakan di fungsi lain

def login():  # membuat fungsi login
    global is_logged_in, role, username  # gunakan variabel global untuk peran pengguna dan username
    print(center("===================== Login ====================="))
    username_input = input("Masukkan Username : ").strip()
    password = input("Masukkan Password : ").strip()
    
    # Cek apakah username dan password adalah admin
    if username_input == "admin" and password == "admin":
        print(center("Login berhasil sebagai Admin"))
        is_logged_in = True
        role = "admin"
        return

    if not os.path.exists("data.csv"):  # cek apakah data ada di file csv
        print(center("Username atau Password salah"))
        return
    
    # Membaca file CSV untuk login pengguna biasa
    try:
        with open("data.csv", "r") as file:  # membuka file data.csv
            reader = csv.reader(file)
            next(reader)  # melewati header username,password
            for x in reader:
                if x[0] == username_input and x[1] == password:  # verifikasi username dan password
                    print(center("Login berhasil"))
                    is_logged_in = True  # login berhasil
                    role = "user"  # set peran sebagai user
                    username = username_input  # simpan username
                    return
    except Exception as e:
        print(center(f"Terjadi kesalahan saat membaca file: {e}"))
    
    print(center("Username atau Password salah"))

def register():  # membuat fungsi register
    print(center("===================== Register ====================="))
    username_input = input("Masukkan Username : ").strip()
    password = input("Masukkan Password : ").strip()
    
    if not username_input or not password:
        print(center("Username dan Password tidak boleh kosong"))
        return
    
    if not os.path.exists("data.csv"):  # cek jika data.csv belum ada membuat file baru dengan header
        with open("data.csv", "w", newline="") as file:
            write = csv.writer(file)
            write.writerow(["username", "password"])  # sebagai header
    
    try:
        with open("data.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)
            for x in reader:
                if x[0] == username_input:  # cek username di file data.csv
                    print(center("Username sudah ada"))
                    return
        
        with open("data.csv", "a", newline="") as file:  # menyimpan inputan akun baru ke dalam file csv
            write = csv.writer(file)
            write.writerow([username_input, password])
        print(center("Registrasi berhasil"))
    except Exception as e:
        print(center(f"Terjadi kesalahan saat menyimpan data: {e}"))

def lihat_data_pengguna():
    try:
        # Membaca data pengguna dari file CSV
        data_pengguna = pd.read_csv('data.csv')
        
        # Menampilkan data pengguna dalam format tabel
        print(center(tabulate(data_pengguna, headers='keys', tablefmt='psql', showindex=False)))
    except FileNotFoundError:
        print("File tidak ditemukan. Pastikan path file CSV sudah benar.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

daftar_pengguna = []  # Inisialisasi daftar pengguna

def load_pengguna():
    global daftar_pengguna
    daftar_pengguna = []
    if os.path.exists("data.csv"):
        with open("data.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)  # Melewati header
            for row in reader:
                daftar_pengguna.append(row[0])  # Menambahkan username ke daftar

def hapus_pengguna():
    global daftar_pengguna  # Pastikan untuk menggunakan daftar pengguna global
    username_input = input("Masukkan username pengguna yang ingin dihapus: ").strip()
    
    if username_input in daftar_pengguna:  # Cek apakah username ada di daftar
        daftar_pengguna.remove(username_input)  # Hapus username dari daftar
        print(center(f"Pengguna '{username_input}' telah dihapus."))
        
        # Simpan perubahan ke file data.csv
        with open("data.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["username", "password"])  # Tulis header
            for user in daftar_pengguna:
                writer.writerow([user, ""])  # Tulis username, password bisa dikosongkan atau diisi sesuai kebutuhan
    else:
        print(center(f"Pengguna '{username_input}' tidak ditemukan."))

load_pengguna()

def catat_pemesanan(username, tipe_pesanan, jumlah, status="Belum Dibayar", total_harga=None):
    try:
        # Cek apakah file rekap_pemesanan.csv sudah ada 
        if not os.path.exists("rekap_pemesanan.csv"):
            # Jika file belum ada, buat file baru dan tulis header 
            with open("rekap_pemesanan.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["username", "tipe_pesanan", "jumlah", "status", "harga", "tanggal_pemesanan", "tanggal_pembayaran"])  # Tambahkan kolom tanggal_pemesanan

        # Tambahkan pemesanan ke file rekap_pemesanan.csv 
        with open("rekap_pemesanan.csv", "a", newline="") as file:
            writer = csv.writer(file)
            tanggal_pemesanan = datetime.now().strftime('%Y-%m-%d')  # Ambil tanggal saat ini
            if status == "Lunas":
                tanggal_pembayaran = datetime.now().strftime('%Y-%m-%d')  # Ambil tanggal saat ini 
            else:
                tanggal_pembayaran = ""  # Kosongkan jika belum lunas
            writer.writerow([username, tipe_pesanan, jumlah, status, total_harga, tanggal_pemesanan, tanggal_pembayaran])  # Simpan tanggal_pemesanan

    except Exception as e:
        print(f"Terjadi kesalahan saat mencatat pemesanan: {e}")

def rekap_pemesanan(): 
    try: 
        data_pemesanan = pd.read_csv('rekap_pemesanan.csv') 
        data_pemesanan.columns = data_pemesanan.columns.str.strip() 
        # Tentukan kolom yang ingin ditampilkan, tanpa 'tanggal_pembayaran'
        required_columns = ['username', 'tipe_pesanan', 'jumlah', 'status', 'harga', 'tanggal_pemesanan']  

        for col in required_columns: 
            if col not in data_pemesanan.columns: 
                print(f"Kolom '{col}' tidak ditemukan dalam data pemesanan.") 
                return 

        print("Data pemesanan:") 
        data_pemesanan['harga'] = data_pemesanan['harga'].fillna('-') 

        # Format harga dengan pemisah ribuan
        data_pemesanan['harga'] = data_pemesanan['harga'].apply(lambda x: f'Rp{int(x):,}' if isinstance(x, (int, float)) else x)

        # Menangani status pembayaran yang kosong 
        data_pemesanan['status'] = data_pemesanan['status'].fillna('Belum Dibayar') 

        # Tampilkan tabel tanpa kolom 'tanggal_pembayaran'
        print(center(tabulate(data_pemesanan[required_columns], headers='keys', tablefmt='psql', showindex=False)))

    except FileNotFoundError: 
        print("File tidak ditemukan.") 
    except pd.errors.EmptyDataError: 
        print("File CSV kosong.") 
    except pd.errors.ParserError: 
        print("Terjadi kesalahan saat membaca file CSV.") 
    except Exception as e: 
        print(f"Terjadi kesalahan: {e}") 

# Menu untuk admin
def menu_admin():
    while True:
        cls()
        garis("=")
        Agrismart()
        garis("=")
        print(center("Selamat datang Admin"))
        print(center("1. Lihat Data Pengguna"))
        print(center("2. Lihat Rekap Pemesanan"))
        print(center("3. Hapus Pengguna"))
        print(center("4. Exit"))
        inputan = input(">>> ").strip()
        
        cls()

        if inputan == "1":
            lihat_data_pengguna()
        elif inputan == "2":
            rekap_pemesanan() 
        elif inputan == "3":
            hapus_pengguna()
        elif inputan == "4":
            cls()
            terimakasih()
            break
        else:
            print(center("Pilihan tidak tersedia"))
        skip()

def kelola_lahan():
    global username
    
    # Informasi Biaya Pengelolaan Lahan per Hektar
    biaya_per_hektar = {
        "Pembajakan dan Persiapan Lahan per hektar": 1250000,
        "Pemupukan Awal dan Penyemprotan Pestisida per hektar": 1500000,
        "Penyiraman, Pemupukan Tambahan, Perlindungan Hama per hektar": 2000000,
        "Tenaga Kerja untuk Penanaman, Perawatan, Pemanenan per hektar": 3000000,
        "Penyiraman dan Pemupukan Tambahan per hektar": 1500000,
        "Biaya Pemanenan per hektar": 2000000
    }
    
    total_biaya_per_hektar = 12250000  # Total biaya per hektar di Jember

    while True:
        try:
            # Menampilkan rincian biaya
            print(center("===================== Kelola Lahan ====================="))
            print(center("\n===================== Rincian Biaya Pengelolaan Lahan ====================="))
            for rincian, biaya in biaya_per_hektar.items():
                print(center(f"{rincian}: Rp{biaya:,.0f} per hektar"))
            # Meminta input dari user tentang luas lahan
            luas_lahan = float(input("Masukkan luas lahan yang ingin dikelola (dalam hektar): ").strip())
            if luas_lahan <= 0:
                print(center("Luas lahan harus lebih besar dari 0. Silakan coba lagi."))
                continue

            # Menghitung total biaya berdasarkan luas lahan
            total_biaya = total_biaya_per_hektar * luas_lahan


            print(center(f"\nTotal Estimasi Biaya Pengelolaan untuk {luas_lahan} hektar: Rp{total_biaya:,.0f}"))
            
            # Mencatat pemesanan
            catat_pemesanan(username, "Kelola Lahan", luas_lahan, "Belum Dibayar", total_biaya)
            break
        except ValueError:
            print(center("Input tidak valid. Harap masukkan angka yang benar."))
    

def kelola_tanaman():
    global username
    while True:
        print(center("===================== Kelola Tanaman ====================="))
        print(center("Pilih tanaman yang ingin ditanam:"))
        print(center("1. Padi"))
        print(center("2. Jagung"))
        print(center("3. Tembakau"))
        print(center("4. Kembali"))
        pilihan_tanaman_user = input(">>> ")   
        
        cls()

        if pilihan_tanaman_user == "1":
            harga_per_kg = 75000
            print(center("Informasi tentang Padi:"))
            print(center("Cuaca: Memerlukan iklim tropis dan subtropis. Suhu ideal: 24°C - 30°C. Kelembapan tinggi (sekitar 70-90%)."))
            print(center("Curah Hujan: Padi membutuhkan curah hujan yang cukup, sekitar 1000-2000 mm per tahun."))
            print(center("Ketersediaan Air: Padi membutuhkan tanah yang selalu tergenang air, terutama pada fase pertumbuhan vegetatif dan pembentukan bulir."))
            print(center("pH Tanah: Optimal pada pH 5.5 - 7."))
            print(center("Ketersediaan Nutrisi: Nitrogen (N), fosfor (P), dan kalium (K) dalam jumlah yang cukup diperlukan, terutama untuk pembentukan daun dan bulir."))
            print(center("Tekstur Tanah: Tanah lempung berpasir atau tanah liat yang mampu menahan air."))
            print(center("Harga bibit padi: Rp75.000 per kg"))
            print(center("Kebutuhan bibit: 25 kg per hektar"))
            while True:
                jumlah_kg_input = input("Masukkan jumlah kg bibit padi yang ingin dipesan: ")
                if jumlah_kg_input.isdigit() and int(jumlah_kg_input) > 0:
                    jumlah_kg = int(jumlah_kg_input)
                    total_harga = jumlah_kg * harga_per_kg
                    catat_pemesanan(username, "Padi", jumlah_kg, "Belum Dibayar", total_harga)
                    print(center("Pemesanan berhasil"))  
                    
                    break
                else:
                    print(center("Input tidak valid. Silakan masukkan angka.")) 
        elif pilihan_tanaman_user == "2":
            harga_per_kg = 60000
            print(center("Informasi tentang Jagung:"))
            print(center("Cuaca: Suhu ideal untuk pertumbuhan: 24°C - 30°C. Tidak toleran terhadap cuaca terlalu lembap atau terlalu dingin."))
            print(center("Curah Hujan: Kebutuhan air sekitar 500-800 mm selama musim tanam, dengan curah hujan merata."))
            print(center("pH Tanah: Optimal pada pH 5.8 - 7."))
            print(center("Ketersediaan Nutrisi: Nitrogen sangat penting, diikuti oleh fosfor dan kalium. Pemupukan tambahan mikronutrien seperti seng (Zn) sering diperlukan di beberapa lahan."))
            print(center("Tekstur Tanah: Tanah lempung berpasir atau lempung yang memiliki drainase baik, tapi mampu menyimpan kelembapan."))
            print(center("Harga bibit jagung: Rp60.000 per kg"))
            print(center("Kebutuhan bibit: 20 kg per hektar"))
            while True:
                jumlah_kg_input = input("Masukkan jumlah kg bibit jagung yang ingin dipesan: ")
                if jumlah_kg_input.isdigit() and int(jumlah_kg_input) > 0:
                    jumlah_kg = int(jumlah_kg_input)
                    total_harga = jumlah_kg * harga_per_kg
                    catat_pemesanan(username, "Jagung", jumlah_kg, "Belum Dibayar", total_harga)
                    print(center("Pemesanan berhasil"))  
                    
                    break
                else:
                    print(center("Input tidak valid. Silakan masukkan angka.")) 

        elif pilihan_tanaman_user == "3":
            harga_per_gram = 1500
            print(center("Informasi tentang Tembakau:"))
            print(center("Cuaca: Suhu optimal: 20°C - 30°C. Memerlukan iklim yang hangat dan kering selama periode pertumbuhan, serta cukup sinar matahari."))
            print(center("Curah Hujan: Kebutuhan air lebih rendah, sekitar 400-600 mm per tahun. Kelembapan tinggi tidak disukai, terutama pada fase pematangan daun."))
            print(center("pH Tanah: Optimal pada pH 5.5 - 6.5."))
            print(center("Ketersediaan Nutrisi: Nitrogen, kalium, dan kalsium penting untuk kualitas daun tembakau. Kelebihan nitrogen bisa mengurangi kualitas tembakau, terutama untuk aroma dan cita rasanya."))
            print(center("Tekstur Tanah: Tanah ringan, seperti tanah berpasir atau lempung berpasir, dengan drain ase yang baik untuk menghindari kelembapan berlebih."))
            print(center("Harga bibit tembakau: Rp1.500 per gram"))
            print(center("Biaya persemaian Rp400.000 per hektar, mencakup biaya pupuk, media tanam, dan tenaga kerja untuk proses persemaian."))
            print(center("Kebutuhan bibit per hektar 75 gram per hektar"))
            while True:
                jumlah_gram_input = input("Masukkan jumlah gram bibit tembakau yang ingin dipesan: ")
                if jumlah_gram_input.isdigit() and int(jumlah_gram_input) > 0:
                    jumlah_gram = int(jumlah_gram_input)
                    total_harga = jumlah_gram * harga_per_gram
                    catat_pemesanan(username, "Tembakau", jumlah_gram, "Belum Dibayar", total_harga)
                    print(center("Pemesanan berhasil"))   
                    
                    break
                else:
                    print(center("Input tidak valid. Silakan masukkan angka."))

        elif pilihan_tanaman_user == "4":
            break
        
        else:
            print(center("Pilihan tidak valid"))

def kelola_pupuk(): 
    global username

    while True: 
        print(center("===================== Kelola Pupuk & Pestisida =====================")) 
        print(center("1. Pupuk")) 
        print(center("2. Pestisida")) 
        print(center("3. Kembali")) 
        pilihan = input(">>> ").strip() 

        if pilihan == "1":
            pupuk()
        elif pilihan == "2": 
            kelola_pestisida()  # Panggil fungsi untuk kelola pestisida
        elif pilihan == "3":
            break
        else: 
            print(center("Pilihan tidak valid."))
    

def pupuk():
    pupuk = [ 
        {"nama": "Pupuk Urea (Subsidi)", "harga": 2500, "tanaman": "Padi, jagung, tembakau", "manfaat": "Mengandung nitrogen tinggi yang mempercepat pertumbuhan tanaman"}, 
        {"nama": "Pupuk NPK Phonska (Subsidi)", "harga": 2700, "tanaman": "Padi, jagung, tembakau", "manfaat": "Meningkatkan sistem perakaran dan jumlah anakan pada tanaman"}, 
        {"nama": "Pupuk ZA (Subsidi)", "harga": 1800, "tanaman": "Padi, jagung, tembakau", "manfaat": "Menambah kandungan sulfur dan nitrogen yang baik untuk kesuburan tanaman"}, 
        {"nama": "Pupuk Organik Granul (Subsidi)", "harga": 900, "tanaman": "Padi, jagung", "manfaat": "Menambah kesuburan tanah secara alami"}, 
    ] 

    print(center("Pilihan Pupuk:")) 
    for i, p in enumerate(pupuk, 1): 
        print(center(f"{i}. {p['nama']} - Harga: Rp {p['harga']} per kg")) 
        print(center(f"   Tanaman: {p['tanaman']}")) 
        print(center(f"   Manfaat: {p['manfaat']}")) 

    pilihan_pupuk = input("Masukkan nomor pilihan pupuk yang ingin dipesan: ").strip() 
    if pilihan_pupuk.isdigit() and 1 <= int(pilihan_pupuk) <= len(pupuk): 
        try:
            jumlah = int(input("Masukkan jumlah (dalam kg, harus angka bulat): ").strip())
            if jumlah <= 0:
                print(center("Jumlah harus lebih besar dari 0."))
                

            nama_pupuk = pupuk[int(pilihan_pupuk) - 1]["nama"] 
            harga_pupuk = pupuk[int(pilihan_pupuk) - 1]["harga"] 
            total_harga = harga_pupuk * jumlah 
            print(center(f"Anda telah memesan {jumlah} kg {nama_pupuk} dengan total harga Rp {total_harga:,.0f}.")) 

            # Mencatat pemesanan
            catat_pemesanan(username, f"Pesanan Pupuk: {nama_pupuk} ({jumlah} kg)", jumlah, "Belum Dibayar", total_harga)
            
        except ValueError:
            print(center("Input tidak valid. Harap masukkan angka bulat."))
    skip()
    cls()


def kelola_pestisida(): 
    pestisida = [ 
        {"nama": "Pestisida Fungisida Dithane M-45", "harga": 90000, "tanaman": "Padi, tembakau", "manfaat": "Mencegah penyakit jamur pada daun"}, 
        {"nama": "Pestisida Insektisida Marshal 200EC", "harga": 110000, "tanaman": "Padi, jagung, tembakau", "manfaat": "Mengendalikan hama ulat dan serangga pada tanaman"}, 
    ] 

    print(center("Pilihan Pestisida:")) 
    for i, p in enumerate(pestisida, 1): 
        print(center(f"{i}. {p['nama']} - Harga: Rp {p['harga']} per 500 gram")) 
        print(center(f"   Tanaman: {p['tanaman']}")) 
        print(center(f"   Manfaat: {p['manfaat']}")) 

    pilihan_pestisida = input("Masukkan nomor pilihan pestisida yang ingin dipesan: ").strip() 
    if pilihan_pestisida.isdigit() and 1 <= int(pilihan_pestisida) <= len(pestisida): 
        try:
            jumlah = int(input("Masukkan jumlah paket (per paket 500 gram, harus angka bulat): ").strip())
            if jumlah <= 0:
                print(center("Jumlah harus lebih besar dari 0."))
                return

            nama_pestisida = pestisida[int(pilihan_pestisida) - 1]["nama"] 
            harga_pestisida = pestisida[int(pilihan_pestisida) - 1]["harga"] 
            total_harga = harga_pestisida * jumlah 
            print(center(f"Anda telah memesan {jumlah} paket {nama_pestisida} dengan total harga Rp {total_harga:,.0f}.")) 

            # Mencatat pemesanan
            catat_pemesanan(username, f"Pesanan Pestisida: {nama_pestisida} ({jumlah} paket)", jumlah, "Belum Dibayar", total_harga)
        except ValueError:
            print(center("Input tidak valid. Harap masukkan angka bulat."))
    else: 
        print(center("Pilihan tidak valid.")) 
    skip()
    cls()


def kelola_peralatan():
    global username
    print(center("===================== Kelola Peralatan ====================="))
    
    while True:
        print(center("Pilih jenis tanaman yang ingin dikelola dengan peralatan:"))
        print(center("1. Padi"))
        print(center("2. Jagung"))
        print(center("3. Tembakau"))
        print(center("4. Kembali"))
        pilihan_tanaman = input(">>> ").strip()

        if pilihan_tanaman == "1":
            jenis_tanaman = "Padi"
            harga_peralatan = {
                "Traktor untuk Bajak Tanah (Sewa)": 1800000,
                "Alat Tanam Padi (Transplanter)": 1300000,
                "Pompa Air": 900000,
                "Alat Pemupukan dan Penyemprotan (Sprayer)": 450000,
                "Alat Pemanenan (Padi Harvester)": 2800000
            }
            total_biaya = 7250000

        elif pilihan_tanaman == "2":
            jenis_tanaman = "Jagung"
            harga_peralatan = {
                "Traktor untuk Bajak Tanah (Sewa)": 1500000,
                "Alat Tanam Jagung (Seeder)": 1100000,
                "Pompa Air": 800000,
                "Alat Pemupukan dan Penyemprotan (Sprayer)": 400000,
                "Alat Pemanenan (Jagung Harvester)": 2500000
            }
            total_biaya = 6300000

        elif pilihan_tanaman == "3":
            jenis_tanaman = "Tembakau"
            harga_peralatan = {
                "Traktor untuk Bajak Tanah (Sewa)": 1700000,
                "Alat Tanam Tembakau (Tanam Manual atau Seeder Manual)": 900000,
                "Pompa Air": 1000000,
                "Alat Pemupukan dan Penyemprotan (Sprayer)": 450000,
                "Alat Pemanenan (Tembakau Harvester atau Manual)": 2000000
            }
            total_biaya = 6050000

        elif pilihan_tanaman == "4":
            break

        else:
            print(center("Pilihan tidak valid. Silakan coba lagi."))
            continue

        print(center(f"\n===================== Paket Peralatan untuk Tanaman {jenis_tanaman} ====================="))
        for peralatan, harga in harga_peralatan.items():
            print(center(f"{peralatan}: Rp{harga:,.0f} per hektar"))

        try:
            luas_lahan = float(input("\nMasukkan luas lahan yang ingin dikelola (dalam hektar): ").strip())
            if luas_lahan <= 0:
                print(center("Luas lahan harus lebih besar dari 0. Silakan coba lagi."))
                continue

            total_biaya_lahan = total_biaya * luas_lahan
            print(center(f"\nTotal Biaya untuk {jenis_tanaman} di {luas_lahan} hektar: Rp{total_biaya_lahan:,.0f}"))

            # Mencatat pemesanan
            catat_pemesanan(username, f"Peralatan Tanaman {jenis_tanaman}", luas_lahan, "Belum Dibayar", total_biaya_lahan)
            break

        except ValueError:
            print(center("Input tidak valid. Silakan masukkan angka yang benar."))

def kelola_transaksi(): 
    global username 
    try: 
        # Membaca data pemesanan dari file CSV 
        data_pemesanan = pd.read_csv('rekap_pemesanan.csv') 

        # Filter pemesanan berdasarkan username yang sedang login 
        pemesanan_user = data_pemesanan[data_pemesanan['username'] == username] 

        if pemesanan_user.empty: 
            print(center("Anda belum melakukan pemesanan.")) 
            skip() 
            return 

        # Menampilkan rekap pemesanan dalam format tabel yang lebih rapi 
        print(center("===================== Rekap Pemesanan Anda =====================")) 

        # Format harga dengan pemisah ribuan 
        pemesanan_user['harga'] = pemesanan_user['harga'].apply(lambda x: f"Rp {x:,.0f}") 

        # Menampilkan tabel dengan tabulate, mengatur lebar kolom jika diperlukan 
        print(center(tabulate(pemesanan_user, headers='keys', tablefmt='psql', showindex=False, numalign="right"))) 

        # Cek apakah ada pesanan yang belum dibayar 
        if 'Belum Dibayar' in pemesanan_user['status'].values: 
            print(center("\nBeberapa pemesanan Anda belum dibayar. Silakan lanjutkan ke proses pembayaran.")) 

            total_harga = pemesanan_user[pemesanan_user['status'] == 'Belum Dibayar']['harga'].apply(lambda x: int(x.replace('Rp ', '').replace(',', ''))).sum() 
            print(center(f"Total pembayaran yang harus dilunasi: Rp{total_harga:,.0f}")) 

            # Memilih metode pembayaran 
            metode_pembayaran = pilih_metode_pembayaran() 
            if metode_pembayaran: 
                # Memproses pembayaran 
                if proses_pembayaran(total_harga, metode_pembayaran): 
                    # Update status menjadi 'Lunas' setelah pembayaran 
                    data_pemesanan.loc[(data_pemesanan['username'] == username) & (data_pemesanan['status'] == 'Belum Dibayar'), 'status'] = 'Lunas' 
                    
                    # Pastikan kolom 'tanggal_pembayaran' bertipe object
                    data_pemesanan['tanggal_pembayaran'] = data_pemesanan['tanggal_pembayaran'].astype(object)
                    
                    # Mencatat tanggal pembayaran
                    data_pemesanan.loc[(data_pemesanan['username'] == username) & (data_pemesanan['status'] == 'Lunas'), 'tanggal_pembayaran'] = datetime.now().strftime('%Y-%m-%d')
                    
                    data_pemesanan.to_csv('rekap_pemesanan.csv', index=False) 
                    print(center("\nPembayaran berhasil! Semua pesanan Anda telah lunas.\n")) 
                else: 
                    print(center("Pembayaran gagal. Silakan coba lagi.")) 
        else: 
            print(center("\nSemua pesanan Anda telah lunas.\n")) 

    except FileNotFoundError: 
        print(center("File pemesanan tidak ditemukan.")) 
    except pd.errors.EmptyDataError: 
        print(center("File pemesanan kosong.")) 
    except Exception as e: 
        print(center(f"Terjadi kesalahan: {e}")) 
    
    skip()

def pilih_metode_pembayaran():
    print(center("===================== Pilih Metode Pembayaran ====================="))
    print(center("1. M-Banking"))
    print(center("2. DANA"))
    print(center("3. ShopeePay"))
    print(center("4. Kembali"))

    pilihan = input("Masukkan pilihan metode pembayaran (1/2/3/4): ").strip()
    if pilihan == "1":
        return "M-Banking"
    elif pilihan == "2":
        return "DANA"
    elif pilihan == "3":
        return "ShopeePay"
    elif pilihan == "4":
        return None
    else:
        print(center("Pilihan tidak valid."))
        return None

def proses_pembayaran(total_harga, metode): 
    print(center(f"\n===================== Proses Pembayaran via {metode} =====================")) 
    print(center(f"Nominal yang harus dibayar: Rp{total_harga:,.0f}")) 

    # Simulasi pembayaran dengan nomor acak sebagai bukti pembayaran 
    kode_pembayaran = random.randint(100000, 999999) 
    print(center(f"Kode Pembayaran: {kode_pembayaran}")) 

    # Konfirmasi pembayaran 
    konfirmasi = input(center(f"Apakah Anda sudah melakukan pembayaran via {metode}? (y/n): ")).strip().lower() 
    if konfirmasi == "y": 
        print(center("Pembayaran sedang diproses...")) 
        time.sleep(2)  # Simulasi waktu proses pembayaran 
        return True 
    else: 
        return False 

def cek_perkembangan_tanaman(debug=False):
    try:
        # Membaca data pemesanan dari file CSV
        data_pemesanan = pd.read_csv('rekap_pemesanan.csv')

        # Mencari pemesanan berdasarkan username yang sedang login
        pemesanan_user = data_pemesanan[data_pemesanan['username'] == username]

        if pemesanan_user.empty:
            print(center("Anda belum melakukan pemesanan."))
            skip()
            return

        # Mengecek apakah ada pemesanan dengan status "Lunas"
        lunas_pemesanan = pemesanan_user[pemesanan_user['status'] == "Lunas"]
        if lunas_pemesanan.empty:
            print(center("Perkembangan tanaman hanya dapat dicek setelah pembayaran lunas."))
            skip()
            return

        # Menampilkan notifikasi perkembangan tanaman setelah H+2 pembayaran
        print(center("===================== Cek Perkembangan Tanaman ====================="))
        print(center("Notifikasi perkembangan tanaman Anda:"))

        for index, row in lunas_pemesanan.iterrows():
            if 'tanggal_pembayaran' in row and 'tipe_pesanan' in row:
                tanggal_pembayaran = row['tanggal_pembayaran']
                tipe_pesanan = row['tipe_pesanan']

                # Debugging: Tampilkan isi tipe_pesanan jika debug diaktifkan
                if debug:
                    print(center(f"Debug: Tipe pesanan untuk index {index}: {tipe_pesanan}"))

                # Memastikan tipe_pesanan memiliki format yang benar
                if isinstance(tipe_pesanan, str):
                    # Cek jika tipe_pesanan mengandung ":"
                    if ':' in tipe_pesanan:
                        jenis_tanaman = tipe_pesanan.split(":")[1].strip()  # Menentukan jenis tanaman dari tipe pesanan
                    else:
                        # Jika tidak ada ":", kita bisa menggunakan tipe_pesanan sebagai jenis_tanaman
                        jenis_tanaman = tipe_pesanan.strip()

                    # Menghitung tanggal mulai pertumbuhan
                    tanggal_pembayaran = datetime.strptime(tanggal_pembayaran, '%Y-%m-%d')
                    tanggal_mulai = tanggal_pembayaran + timedelta(days=2)  # H+2 pembayaran

                    # Menghitung hari-hari yang telah berlalu
                    hari_sejak_mulai = (datetime.now() - tanggal_mulai).days

                    # Menentukan fase pertumbuhan berdasarkan jenis tanaman
                    if jenis_tanaman.lower() == "padi":
                        if hari_sejak_mulai < 0:
                            print(center("Fase Persemaian belum dimulai."))
                        elif hari_sejak_mulai < 30:
                            print(center("Fase Persemaian."))
                        elif hari_sejak_mulai < 60:
                            print(center("Fase Vegetatif."))
                        elif hari_sejak_mulai < 100:
                            print(center("Fase Reproduktif."))
                        else:
                            print(center("Fase Pematangan."))

                    elif jenis_tanaman.lower() == "jagung":
                        if hari_sejak_mulai < 0:
                            print(center("Fase Perkecambahan belum dimulai."))
                        elif hari_sejak_mulai < 7:
                            print(center("Fase Perkecambahan."))
                        elif hari_sejak_mulai < 50:
                            print(center("Fase Vegetatif."))
                        elif hari_sejak_mulai < 80:
                            print(center("Fase Generatif (Bunga dan Polinasi)."))
                        else:
                            print(center("Fase Pematangan."))

                    elif jenis_tanaman.lower() == "tembakau":
                        if hari_sejak_mulai < 0:
                            print(center("Fase Persemaian belum dimulai."))
                        elif hari_sejak_mulai < 30:
                            print(center("Fase Persemaian."))
                        elif hari_sejak_mulai < 60:
                            print(center("Fase Vegetatif."))
                        elif hari_sejak_mulai < 90:
                            print(center("Fase Pembungaan."))
                        else:
                            print(center("Fase Pematangan."))

                else:
                    print(center(f"Format tipe pesanan tidak valid untuk pemesanan dengan index {index}. Pastikan formatnya benar."))
            else:
                print(center ("Data pemesanan tidak lengkap."))

    except FileNotFoundError:
        print(center("File tidak ditemukan. Pastikan path file CSV sudah benar."))
    except pd.errors.EmptyDataError:
        print(center("File tidak ditemukan. Pastikan ada data pemesanan."))
    except Exception as e:
        print(center(f"Terjadi kesalahan: {e}"))

    skip()

# Menu untuk memilih peran admin atau user
def pilih_peran():
    global role  # Gunakan variabel global
    while True:
        cls()
        garis("=")
        Agrismart()
        garis("=")
        print(center("Pilih peran Anda:"))
        print(center("1. Admin"))
        print(center("2. User"))
        print(center("3. Exit"))
        inputan = input(">>> ").strip()
        
        cls()

        if inputan == "1":
            role = "admin"
            login()  # Admin harus login
            if is_logged_in and role == "admin":  # Periksa apakah berhasil login sebagai admin
                menu_admin()
            break
        elif inputan == "2":
            role = "user"
            fiturlogin()  # Panggil fungsi login untuk user
            break
        elif inputan == "3":
            cls()
            terimakasih()
            break
        else:
            print(center("Pilihan tidak tersedia"))
        skip()

# Menu login atau register
# Menu login atau register
def fiturlogin():
    global is_logged_in  # gunakan variabel global untuk cek login
    
    while True:  # pemilihan menu
        cls()
        garis("=")
        Agrismart()
        garis("=")
        
        if not is_logged_in:  # Jika belum login, hanya tampilkan menu login dan register
            print(center("Selamat datang di AgriSmart"))
            print(center("1. Login".ljust(30)))  # Padding untuk meratakan
            print(center("2. Register".ljust(30)))
            print(center("3. Exit".ljust(30)))
            inputan = input(">>> ").strip()
            
            cls()

            if inputan == "1":
                login()
            elif inputan == "2":
                register()
            elif inputan == "3":
                cls()
                terimakasih()
                break
            else:
                print(center("Pilihan tidak tersedia"))
            skip()
        
        else:  # Jika sudah login, tampilkan semua menu kelola
            print(center("Selamat datang di AgriSmart"))
            print(center("1. Kelola Lahan".ljust(30)))
            print(center("2. Kelola Tanaman".ljust(30)))
            print(center("3. Kelola Peralatan".ljust(30)))
            print(center("4. Kelola Pupuk dan Pestisida".ljust(30)))
            print(center("5. Kelola Transaksi".ljust(30)))
            print(center("6. Cek Perkembangan Tanaman".ljust(30)))  # Opsi baru untuk cek perkembangan tanaman
            print(center("7. Exit".ljust(30)))
            inputan = input(">>> ").strip()
            
            cls()

            if inputan == "1":
                kelola_lahan()
            elif inputan == "2":
                kelola_tanaman()
            elif inputan == "3":
                kelola_peralatan()
            elif inputan == "4":
                kelola_pupuk()
            elif inputan == "5":
                kelola_transaksi()
            elif inputan == "6":
                cek_perkembangan_tanaman()  # Panggil fungsi cek perkembangan tanaman
            elif inputan == "7":
                cls()
                terimakasih()
                break
            else:
                print(center("Pilihan tidak tersedia"))
            skip()

tampilkan_peraturan()
pilih_peran()
