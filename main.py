# Menampilkan semua data kontak
def melihat_kontak():
    # melihat semua kontak
    if kontak:
        for num, item in enumerate(kontak, start=1):
            print(f'\n{num}. {item["nama"]} ({item["HP"]}, {item["email"]})')
    else:
        print("Kontak masih kosong!")
        return 1

# Menambah data kontak
def menambah_kontak():
    # menambahkan kontak
    nama = input("Masukkan nama kontak yang baru: ")
    HP = input("Masukkan nomor HP kontak yang baru: ")
    email = input("Masukkan email kontak yang baru: ")
    kontak_baru = {'nama': nama, 'HP': HP, 'email': email}
    kontak.append(kontak_baru)
    print("Kontak baru berhasil ditambahkan!")

# Menghapus data kontak
def menghapus_kontak():
    # menghapus kontak

    # if kontak:
    #     for num, item in enumerate(kontak, start=1):
    #         print(f'\n{num}. {item["nama"]} ({item["HP"]}, {item["email"]})')
    # else:
    #     print("Kontak masih kosong!")
    #     continue

    if melihat_kontak() == 1:
        return
    else:
        i_hapus = int(input("Masukkan nomor kontak yang akan dihapus: "))
        if 1 <= i_hapus <= len(kontak):
            del kontak[i_hapus - 1]
            print("Kontak yang dimaksud sudah dihapus")
        else:
            print("Nomor kontak tidak valid!")

kontak1 = {'nama' : "Andi", 'HP': '109989303', 'email': 'Andi@python.com'}
kontak2 = {'nama' : "Ani", 'HP': '933953335', 'email': 'Ani@python.com'}
kontak = [kontak1, kontak2] # sebagai database/tempat penyimpanan data

while True:
    print("\nMenu Kontak")
    print("1. Melihat Semua Kontak")
    print("2. Menambahkan Kontak Baru")
    print("3. Menghapus Kontak")
    print("4. Mengubah Kontak")
    print("5. Keluar dari Kontak")

    pilihan = input("Masukkan pilihan menu kontak (1,2,3,4 atau 5): ")

    if pilihan == '1':
        melihat_kontak() #memanggil fungsi

    elif pilihan == '2':
        menambah_kontak() #memanggil fungsi

    elif pilihan == '3':
        menghapus_kontak() #memanggil fungsi

    elif pilihan == '4':
        # mengubah kontak
        if kontak:
            for num, item in enumerate(kontak, start=1):
                print(f'\n{num}. {item["nama"]} ({item["HP"]}, {item["email"]})')
        else:
            print("Kontak masih kosong!")
            continue

        i_ubah = int(input("Masukkan nomor kontak yang akan diubah: "))
        if 1 <= i_ubah <= len(kontak):
            kontak_terpilih = kontak[i_ubah-1]
            print(f'Mengubah kontak: {kontak_terpilih["nama"]} ({kontak_terpilih["HP"]}, {kontak_terpilih["email"]})')

            nama_baru = input(f"Masukkan nama baru (kosongkan jika tidak ingin mengubah): ") or kontak_terpilih["nama"]
            HP_baru = input(f"Masukkan nomor HP baru (kosongkan jika tidak ingin mengubah): ") or kontak_terpilih["HP"]
            email_baru = input(f"Masukkan email baru (kosongkan jika tidak ingin mengubah): ") or kontak_terpilih["email"]

            kontak[i_ubah-1] = {'nama': nama_baru, 'HP': HP_baru, 'email': email_baru}
            print("Kontak berhasil diubah!")
        else:
            print("Nomor kontak tidak valid!")

    elif pilihan == '5':
        # keluar dari kontak
        break
    else:
        print("Anda memasukkan pilihan yang salah!")
