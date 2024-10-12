class Debitur:
    def __init__(self, nama, ktp, limitPinjam):  # Konstruktor
        self.nama = nama  # nama debitur (nasabah)
        # ktp nasabah bersifat private (ditandai dengan 2 underscore(__))
        self.__ktp = ktp
        # batas max pinjam bersifat protected (ditandai dengan 1 underscore(_))
        self._limitPinjam = limitPinjam

    def get_ktp(self):
        return self.__ktp  # Mengembalikan nilai ktp, menggunakan get untuk menjaga privasi ktp


class Pinjaman:
    def __init__(self, nama, jumlah, bunga, bulan):  # konstruktor
        self.nama = nama  # nama debitur
        self.jumlah = jumlah  # jumlah yang dipinjam
        self.bunga = bunga  # bunga yang didapat
        self.bulan = bulan  # jangka waktu pinjaman (dalam bulan)

    # Menghitung angsuran bulanan dan total angsuran dengan rumus yang telah ditentukan berdasarkan jumlah pinjaman, bunga, dan waktu (bulan).
    def hitungAngsuran(self):
        angsuranUtama = self.jumlah * self.bunga // 100
        angsuranBulanan = angsuranUtama // self.bulan
        totalAngsur = angsuranUtama + (angsuranBulanan * self.bulan)
        return angsuranBulanan, totalAngsur


class SistemPinjaman:
    def __init__(self):  # konstruktor
        self.debitur = []  # semua objek debitur disimpan di list ini
        self.pinjaman = []  # semua objek pinjaman disimpan di list ini

    def nambahDebitur(self, nama, ktp, limitPinjam):  # nambah debitur sesuai ktp
        if any(d.get_ktp() == ktp for d in self.debitur):
            # jika ktp sudah digunakan akan muncul error
            print("ERROR: KTP sudah terdaftar !!!")
            return
        self.debitur.append(Debitur(nama, ktp, limitPinjam))
        # jika ktp belum pernah terdaftar, maka pendaftaran berhasil
        print(f"Debitur (Nasabah) atas nama : {nama} berhasil ditambahkan")

    def nampilinDebitur(self):  # menampilkan nasabah
        for d in self.debitur:
            print(
                f"Nama: {d.nama}, KTP: {d.get_ktp()}, Limit Pinjaman: {d._limitPinjam}")

    def cariDebitur(self, nama):  # mencari nasabah sesuai nama yang diinputkan
        hasil = [d for d in self.debitur if d.nama.lower() == nama.lower()]
        if hasil:
            for d in hasil:
                print(
                    f"Nama: {d.nama}, KTP: {d.get_ktp()}, Limit Pinjaman: {d._limitPinjam}")
        else:
            # jika nama yang diinput tidak ada dalam list (data), maka akan menampilkan error
            print("ERROR: Debitur (Nasabah) tidak ditemukan")

    def nambahPinjaman(self, nama, jumlah, bunga, bulan):  # menambah pinjaman
        debitur = next(
            (d for d in self.debitur if d.nama.lower() == nama.lower()), None)
        if not debitur:
            # nama tidak ada harus input di bagian menu 1 submenu 3
            print("ERROR: Nama tidak ada !!!")
            return
        if jumlah > debitur._limitPinjam:
            # pinjaman melebihi limit (nabung dulu aja jangan menuhin gengsi)
            print("ERROR: Pinjaman melebihi limit, GAYA SESUAI LIMIT !!!")
            return
        self.pinjaman.append(Pinjaman(nama, jumlah, bunga, bulan))
        print(f"Pinjaman untuk nasabah : {nama} berhasil ditambahkan")

    def nampilinPinjaman(self):  # menampilkan pinjaman
        for p in self.pinjaman:
            angsuranBulanan, totalAngsur = p.hitungAngsuran()
            print(
                f"Nama: {p.nama}, Pinjaman: {p.jumlah}, Bunga: {p.bunga}%, Bulan: {p.bulan}")
            print(
                f"Angsuran/bln: {angsuranBulanan}, Total Angsuran: {totalAngsur}")


def main():  # fungsi utama
    sistem = SistemPinjaman()  # memanggil class sistem pinjaman

    while True:
        print("=====MENU BANK PLECIT | Hutangmu Rejekiku=====")  # judul program
        print("\n1. Kelola Debitur (Nasabah)")
        print("2. Kelola Pinjaman")
        print("3. Keluar")
        Menu = input("Pilih menu [1-2], 3 Keluar. : ")  # user input [1-3]

        if Menu == '1':
            print("\n1. Tampilkan Debitur (Nasabah)")
            print("2. Cari Debitur (Nasabah)")
            print("3. Tambah Debitur (Nasabah)")
            subMenu = input("Pilih menu [1-3]: ")  # user input [1-3]

            if subMenu == '1':
                sistem.nampilinDebitur()
            elif subMenu == '2':
                nama = input("Masukkan nama debitur: ")
                sistem.cariDebitur(nama)
            elif subMenu == '3':
                nama = input("Nama: ")
                ktp = input("KTP: ")
                limit = int(input("Limit Pinjaman: "))
                sistem.nambahDebitur(nama, ktp, limit)

        elif Menu == '2':
            print("\n1. Tambah Pinjaman")
            print("2. Tampilkan Pinjaman")
            subMenu = input("Pilih sub-menu: ")

            if subMenu == '1':
                nama = input("Nama Debitur: ")
                jumlah = int(input("Jumlah Pinjaman: "))
                bunga = int(input("Bunga (%): "))
                bulan = int(input("Jangka Waktu (bulan): "))
                sistem.nambahPinjaman(nama, jumlah, bunga, bulan)
            elif subMenu == '2':
                sistem.nampilinPinjaman()

        elif Menu == '3':
            print("Terimakasih telah berhutang kepada jasa kami | Hutangmu Rejekiku")
            break


main()
