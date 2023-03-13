class Mahasiswa:
    jumlah_mahasiswa = 0  # atribut kelas
    
    def __init__(self, nama, nim, nilai):
        self.__nama = nama  # atribut private
        self._nim = nim  # atribut protected
        self.nilai = nilai  # atribut public
        Mahasiswa.jumlah_mahasiswa += 1
    
    def tampilkan_jumlah(self):
        print("Total mahasiswa:", Mahasiswa.jumlah_mahasiswa)
    
    def tampilkan_profil(self):
        print("Nama:", self.__nama)
        print("NIM:", self._nim)
        print("Nilai:", self.nilai)
    
    def ubah_nama(self, nama_baru):
        self.__nama = nama_baru
    
    def ubah_nim(self, nim_baru):
        self._nim = nim_baru
    
    def ubah_nilai(self, nilai_baru):
        self.nilai = nilai_baru

# membuat objek pertama
mhs1 = Mahasiswa("Shahih", "12345", 80)

# menampilkan profil mahasiswa
mhs1.tampilkan_profil()

# mengubah nama dan nim mahasiswa
mhs1.ubah_nama("Indra")
mhs1.ubah_nim("67890")

# menampilkan profil mahasiswa setelah diubah
mhs1.tampilkan_profil()

# membuat objek kedua
mhs2 = Mahasiswa("Sakti", "67890", 99)

# menampilkan jumlah mahasiswa
mhs2.tampilkan_jumlah()

# menampilkan profil mahasiswa kedua
mhs2.tampilkan_profil()

# mengubah nilai mahasiswa kedua
mhs2.nilai = 95

# menampilkan profil mahasiswa kedua setelah diubah
mhs2.tampilkan_profil()
