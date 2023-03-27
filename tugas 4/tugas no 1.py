class Komputer:
    def __init__(self, nama, jenis, harga, merk):
        self.nama = nama
        self.jenis = jenis
        self.harga = harga
        self.merk = merk
    
    def spesifikasi(self):
        pass

class Processor(Komputer):
    def __init__(self, merk, jenis, harga, jumlah_core, kecepatan_processor):
        super().__init__(jenis, 'Processor', harga, merk)
        self.jumlah_core = jumlah_core
        self.kecepatan_processor = kecepatan_processor
    
    def spesifikasi(self):
        return f'Processor {self.jenis} produksi {self.merk}\n'

class RAM(Komputer):
    def __init__(self, merk, jenis, harga, capacity):
        super().__init__(jenis, 'RAM', harga, merk)
        self.capacity = capacity
    
    def spesifikasi(self):
        return f'RAM {self.jenis} produksi {self.merk}\n'

class HDD(Komputer):
    def __init__(self, merk, jenis, harga, capacity, rpm):
        super().__init__(jenis, 'HDD', harga, merk)
        self.capacity = capacity
        self.rpm = rpm
    
    def spesifikasi(self):
        return f'SATA {self.jenis} produksi {self.merk}\n'

class VGA(Komputer):
    def __init__(self, merk, jenis, harga, capacity):
        super().__init__(jenis, 'VGA', harga, merk)
        self.capacity = capacity
    
    def spesifikasi(self):
        return f'VGA {self.jenis} produksi {self.merk}\n'

class PSU(Komputer):
    def __init__(self, merk, jenis, harga, daya):
        super().__init__(jenis, 'PSU', harga, merk)
        self.daya = daya
    
    def spesifikasi(self):
        return f'PSU {self.jenis} produksi {self.merk}\n'

# contoh pembuatan objek
p1 = Processor('Intel', 'Core i7 7740X', 4350000, 4, '4.3GHz')
ram1 = RAM('V-Gen', 'DDR4 SODimm PC19200/2400MHz', 328000, '4GB')
hdd1 = HDD('Seagate', 'HDD 2.5 inch', 295000, '500GB', 7200)
vga1 = VGA('Asus', 'VGA GTX 1050', 250000, '2GB')
psu1 = PSU('Corsair', 'Corsair V550', 250000, '500W')

p2 = Processor('AMD', 'Ryzen 5 3600', 250000, 4, '4.3GHz')
ram2 = RAM('G.SKILL', 'DDR4 2400MHz', 328000, '4GB')
hdd2 = HDD('Seagate', 'HDD 2.5 inch', 295000, '1000GB', 7200)
vga2 = VGA('Asus', '1060Ti', 250000, '8GB')
psu2 = PSU('Corsair', 'Corsair V550', 250000, '500W')

# membuat list komponen-komponen untuk setiap komputer yang dirakit
p1 = Processor('Intel','Core i7 7740X',4350000,4,'4.3GHz')
p2 = Processor('AMD','Ryzen 5 3600',250000,4,'4.3GHz')
ram1 = RAM('V-Gen','DDR4 SODimm PC19200/2400MHz',328000,'4GB')
ram2 = RAM('G.SKILL','DDR4 2400MHz',328000,'4GB')
hdd1 = HDD('Seagate','HDD 2.5 inch',295000,'500GB',7200)
hdd2 = HDD('Seagate','HDD 2.5 inch',295000,'1000GB',7200)
vga1 = VGA('Asus','VGA GTX 1050',250000,'2GB')
vga2 = VGA('Asus','1060Ti',250000,'8GB')
psu1 = PSU('Corsair','Corsair V550',250000,'500W')
psu2 = PSU('Corsair','Corsair V550',250000,'500W')

# membuat list komputer pertama dan kedua
komputer1 = [p1, ram1, hdd1, vga1, psu1]
komputer2 = [p2, ram2, hdd2, vga2, psu2]

# membuat list rakitan komputer
rakit = [komputer1, komputer2]

# menampilkan seluruh komponen pada setiap komputer yang dirakit
for i, komputer in enumerate(rakit):
    print(f"Komputer {i+1}")
    for komponen in komputer:
        if isinstance(komponen, Processor):
            print(f"Processor {komponen.nama} produksi {komponen.merk}")
        elif isinstance(komponen, RAM):
            print(f"RAM {komponen.nama} produksi {komponen.merk}")
        elif isinstance(komponen, HDD):
            print(f"SATA HDD {komponen.nama} produksi {komponen.merk}")
        elif isinstance(komponen, VGA):
            print(f"VGA {komponen.nama} produksi {komponen.merk}")
        elif isinstance(komponen, PSU):
            print(f"PSU {komponen.nama} produksi {komponen.merk}")
    print()