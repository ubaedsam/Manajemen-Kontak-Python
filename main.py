# Progam Manajemen Kontak
import kontak

# Program utama
def main():
    kontak_kantor = kontak.Kontak() # Tempat penyimpanan data di tabel
    kontak_keluarga = kontak.Kontak()

    while True:
        print("\nMenu Kontak")
        print("1. Melihat Semua Kontak")
        print("2. Menambahkan Kontak Baru")
        print("3. Menghapus Kontak")
        print("4. Mengubah Kontak")
        print("5. Keluar dari Kontak")

        pilihan = input("Masukkan pilihan menu kontak (1,2,3,4 atau 5): ")

        if pilihan == '1':
            kontak_keluarga.melihat_kontak()

        elif pilihan == '2':
            kontak_keluarga.menambah_kontak()

        elif pilihan == '3':
            kontak_keluarga.menghapus_kontak()

        elif pilihan == '4':
            kontak_keluarga.mengubah_kontak()

        elif pilihan == '5':
            kontak_keluarga.keluar_kontak()
            print("Perubahan telah disimpan. Program selesai.")
            break

        else:
            print("Anda memasukkan pilihan yang salah!")

if __name__ == "__main__":
    main()