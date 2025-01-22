# Progam Manajemen Kontak

def membuka_kontak(path='kontak.txt'):
    try:
        with open(path, mode='r') as file:
            kontak = file.readlines()
    except FileNotFoundError:
        kontak = [] # Jika terjadi error
    return kontak


def menyimpan_kontak(path='kontak.txt', isi=[]):
    with open(path, mode='w') as file:
        file.writelines(isi)


class Kontak:
    def __init__(self, path='kontak.txt'):
        self.path = path
        self.kontak = membuka_kontak(self.path)

    def melihat_kontak(self):
        # Melihat semua kontak
        if self.kontak:
            for num, item in enumerate(self.kontak, start=1):
                print(f'{num}. {item.strip()}')
        else:
            print("Kontak masih kosong!")
            return 1

    def menambah_kontak(self):
        # Menambahkan kontak
        nama = input("Masukkan nama kontak yang baru: ")
        HP = input("Masukkan nomor HP kontak yang baru: ")
        email = input("Masukkan email kontak yang baru: ")
        kontak_baru = f'{nama} ({HP}, {email})\n'
        self.kontak.append(kontak_baru)
        print("Kontak baru berhasil ditambahkan!")

    def menghapus_kontak(self):
        # Menghapus kontak
        if self.melihat_kontak() == 1:
            return
        else:
            try:
                i_hapus = int(input("Masukkan nomor kontak yang akan dihapus: "))
                if 1 <= i_hapus <= len(self.kontak):
                    del self.kontak[i_hapus - 1]
                    print("Kontak yang dimaksud sudah dihapus")
                else:
                    print("Nomor kontak tidak valid!")
            except ValueError:
                print("Input yang anda masukkan salah!")

    def mengubah_kontak(self):
        # Mengubah kontak
        if self.melihat_kontak() == 1:
            return
        else:
            try:
                i_ubah = int(input("Masukkan nomor kontak yang akan diubah: "))
                if 1 <= i_ubah <= len(self.kontak):
                    kontak_terpilih = self.kontak[i_ubah - 1].strip()
                    print(f'Mengubah kontak: {kontak_terpilih}')

                    nama, sisa = kontak_terpilih.split(' (')
                    HP, email = sisa[:-1].split(', ')

                    nama_baru = input(f"Masukkan nama baru (kosongkan jika tidak ingin mengubah): ") or nama
                    HP_baru = input(f"Masukkan nomor HP baru (kosongkan jika tidak ingin mengubah): ") or HP
                    email_baru = input(f"Masukkan email baru (kosongkan jika tidak ingin mengubah): ") or email

                    self.kontak[i_ubah - 1] = f'{nama_baru} ({HP_baru}, {email_baru})\n'
                    print("Kontak berhasil diubah!")
                else:
                    print("Nomor kontak tidak valid!")
            except (ValueError, IndexError):
                print("Input yang anda masukkan salah!")

    def keluar_kontak(self):
        # Menyimpan perubahan ke file
        menyimpan_kontak(self.path, self.kontak)


# Program utama
kontak_kantor = Kontak() # Tempat penyimpanan data / database
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
        kontak_keluarga.keluar_kontak()
        print("Perubahan telah disimpan. Program selesai.")
        break

    else:
        print("Anda memasukkan pilihan yang salah!")
