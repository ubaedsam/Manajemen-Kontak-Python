# Berisi fungsi membuka dan menyimpan kontak (tempat penyimpanan data / database)

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