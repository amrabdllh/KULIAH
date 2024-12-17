import streamlit as st
import mysql.connector

# Koneksi ke database
def get_connection():
    return mysql.connector.connect(
        host="localhost",  # Sesuaikan dengan konfigurasi MySQL Anda
        user="root",
        password="",
        database="mahasiswa_db"
    )

# Fungsi untuk menambahkan data
def add_mahasiswa(nama, nim, jurusan):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO mahasiswa (nama, nim, jurusan) VALUES (%s, %s, %s)", (nama, nim, jurusan))
    conn.commit()
    cursor.close()
    conn.close()

# Fungsi untuk membaca data
def get_mahasiswa():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM mahasiswa")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data

# Fungsi untuk mengupdate data
def update_mahasiswa(id, nama, nim, jurusan):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE mahasiswa SET nama = %s, nim = %s, jurusan = %s WHERE id = %s",
        (nama, nim, jurusan, id)
    )
    conn.commit()
    cursor.close()
    conn.close()

# Fungsi untuk menghapus data
def delete_mahasiswa(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM mahasiswa WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()

# Streamlit UI
st.title("CRUD Data Mahasiswa")

menu = ["Create", "Read", "Update", "Delete"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Create":
    st.subheader("Tambah Data Mahasiswa")
    with st.form("form_tambah", clear_on_submit=True):
        nama = st.text_input("Nama")
        nim = st.text_input("NIM")
        jurusan = st.text_input("Jurusan")
        submit = st.form_submit_button("Tambah")
        if submit:
            add_mahasiswa(nama, nim, jurusan)
            st.success(f"Data mahasiswa {nama} berhasil ditambahkan!")

elif choice == "Read":
    st.subheader("Data Mahasiswa")
    data = get_mahasiswa()
    if data:
        for row in data:
            st.write(f"**ID:** {row[0]}")
            st.write(f"**Nama:** {row[1]}")
            st.write(f"**NIM:** {row[2]}")
            st.write(f"**Jurusan:** {row[3]}")
            st.write("---")
    else:
        st.warning("Belum ada data mahasiswa.")

elif choice == "Update":
    st.subheader("Update Data Mahasiswa")
    data = get_mahasiswa()
    id_list = [row[0] for row in data]
    selected_id = st.selectbox("Pilih ID", id_list)
    if selected_id:
        selected_data = [row for row in data if row[0] == selected_id][0]
        nama, nim, jurusan = st.text_input("Nama", selected_data[1]), st.text_input("NIM", selected_data[2]), st.text_input("Jurusan", selected_data[3])
        if st.button("Update"):
            update_mahasiswa(selected_id, nama, nim, jurusan)
            st.success("Data berhasil diperbarui!")

elif choice == "Delete":
    st.subheader("Hapus Data Mahasiswa")
    data = get_mahasiswa()
    id_list = [row[0] for row in data]
    selected_id = st.selectbox("Pilih ID", id_list)
    if selected_id and st.button("Hapus"):
        delete_mahasiswa(selected_id)
        st.success("Data berhasil dihapus!")
