# Progam Manajemen Kontak

class Kontak:
    def __init__(self):
        self.kontak = []

    def melihat_kontak(self):
        # Melihat semua kontak
        if self.kontak:
            for num, item in enumerate(self.kontak, start=1):
                print(f'\n{num}. {item["nama"]} ({item["HP"]}, {item["email"]})')
        else:
            print("Kontak masih kosong!")
            return 1

    def menambah_kontak(self):
        # Menambahkan kontak
        nama = input("Masukkan nama kontak yang baru: ")
        HP = input("Masukkan nomor HP kontak yang baru: ")
        email = input("Masukkan email kontak yang baru: ")
        kontak_baru = {'nama': nama, 'HP': HP, 'email': email}
        self.kontak.append(kontak_baru)
        print("Kontak baru berhasil ditambahkan!")

    def menghapus_kontak(self):
        # Menghapus kontak
        if self.melihat_kontak() == 1:
            return
        else:
            i_hapus = int(input("Masukkan nomor kontak yang akan dihapus: "))
            if 1 <= i_hapus <= len(self.kontak):
                del self.kontak[i_hapus - 1]
                print("Kontak yang dimaksud sudah dihapus")
            else:
                print("Nomor kontak tidak valid!")

    def mengubah_kontak(self):
        # Mengubah kontak
        if self.melihat_kontak() == 1:
            return
        else:
            i_ubah = int(input("Masukkan nomor kontak yang akan diubah: "))
            if 1 <= i_ubah <= len(self.kontak):
                kontak_terpilih = self.kontak[i_ubah - 1]
                print(f'Mengubah kontak: {kontak_terpilih["nama"]} ({kontak_terpilih["HP"]}, {kontak_terpilih["email"]})')

                nama_baru = input(f"Masukkan nama baru (kosongkan jika tidak ingin mengubah): ") or kontak_terpilih["nama"]
                HP_baru = input(f"Masukkan nomor HP baru (kosongkan jika tidak ingin mengubah): ") or kontak_terpilih["HP"]
                email_baru = input(f"Masukkan email baru (kosongkan jika tidak ingin mengubah): ") or kontak_terpilih["email"]

                self.kontak[i_ubah - 1] = {'nama': nama_baru, 'HP': HP_baru, 'email': email_baru}
                print("Kontak berhasil diubah!")
            else:
                print("Nomor kontak tidak valid!")

# Program utama (Tempat penyimpanan data / database)
kontak_kantor = Kontak()
kontak_keluarga = Kontak()

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
        # Keluar dari kontak
        print("Program selesai. Terima kasih!")
        break

    else:
        print("Anda memasukkan pilihan yang salah!")
