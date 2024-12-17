import mysql.connector

def koneksi():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="mahasiswa_db"
    )

conn = koneksi()

def cek_koneksi():
    if conn.is_connected():
        print("Program Terhubung Dengan Database")
    else:
        print("Tidak Terhubung Dengan Database")

def tambah_data(nama, nim, jurusan):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO mahasiswa (nama, nim, jurusan) VALUES (%s, %s, %s)", (nama, nim, jurusan))
    conn.commit()
    cursor.close()

def ubah_data(id, nama, nim, jurusan):
    cursor = conn.cursor()
    cursor.execute("UPDATE mahasiswa SET nama = %s, nim = %s, jurusan = %s WHERE id = %s", (nama, nim, jurusan, id))
    conn.commit()
    cursor.close()

def hapus_data(id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM mahasiswa WHERE id = %s", (id,))
    conn.commit()
    cursor.close()

def lihat_data():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM mahasiswa")
    data = cursor.fetchall()
    if data:
        print("\nData Mahasiswa:")
        print("{:<5} | {:<20} | {:<10} | {:<15}".format("ID", "Nama", "NIM", "Jurusan"))
        print("-" * 55)
        for row in data:
            print("{:<5} | {:<20} | {:<10} | {:<15}".format(row[0], row[1], row[2], row[3]))
    else:
        print("\nTidak ada data mahasiswa.")
    cursor.close()
    return data

print("CRUD DATA MAHASISWA SEDERHANA")
print(f"1. Tambah Data\n2. Ubah Data\n3. Hapus Data\n4. Lihat Data\n5. Exit Program")

while True:
    pilihan = input("Masukkan Pilihan: ")

    if pilihan == '1':
        nama = input("Masukkan Nama: ")
        nim = input("Masukkan NIM: ")
        jurusan = input("Masukkan Jurusan: ")
        try:
            tambah_data(nama, nim, jurusan)
            print("Data berhasil ditambahkan.")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

    elif pilihan == '2':
        data = lihat_data()
        if data:
            try:
                id_terpilih = int(input("Masukkan ID mahasiswa yang ingin diubah: "))
                nama = input("Masukkan Nama baru: ")
                nim = input("Masukkan NIM baru: ")
                jurusan = input("Masukkan Jurusan baru: ")
                ubah_data(id_terpilih, nama, nim, jurusan)
                print("Data berhasil diubah.")
            except ValueError:
                print("ID harus berupa angka.")
            except Exception as e:
                print(f"Terjadi kesalahan: {e}")

    elif pilihan == '3':
        data = lihat_data()
        if data:
            try:
                id_terpilih = int(input("Masukkan ID mahasiswa yang ingin dihapus: "))
                hapus_data(id_terpilih)
                print("Data berhasil dihapus.")
            except ValueError:
                print("ID harus berupa angka.")
            except Exception as e:
                print(f"Terjadi kesalahan: {e}")

    elif pilihan == '4':
        lihat_data()

    elif pilihan == '5':
        print("Keluar dari program.")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih antara 1-5.")
