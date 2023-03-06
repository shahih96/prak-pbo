class mahasiswa:
    def __init__(self, nama, pekerjaan, tahun_lahir, gender):
        self.nama = nama
        self.pekerjaan = pekerjaan
        self.tahun_lahir = tahun_lahir
        self.gender = gender
        
    def kegiatan(self, kegiatan):
        print(kegiatan)
        
    def hitung_usia(self):
        return 2023 - self.tahun_lahir
    
    def info(self):
        print("Nama: {}".format(self.nama))
        print("Pekerjaan: {}".format(self.pekerjaan))
        print("Tahun Lahir: {}".format(self.tahun_lahir))
        print("Gender: {}".format(self.gender))
        print("Usia: {}".format(self.hitung_usia()))

mahasiswa1 = mahasiswa("Shahih", "Mahasiswa", 2003, "Laki-laki")
mahasiswa1.info()
mahasiswa1.kegiatan("Belajar")
