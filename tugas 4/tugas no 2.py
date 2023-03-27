import random

class Robot:
    jumlah_turn = 0

    def __init__(self, nama, health, damage):
        self.nama = nama
        self.health = health
        self.damage = damage

    def lakukan_aksi(self):
        if self.jumlah_turn % self.aksi_interval == 0 and self.jumlah_turn != 0:
            self.tambah_darah()
            self.damage_temp = self.damage * self.damage_multiplier
        else:
            self.damage_temp = self.damage

        print(f"{self.nama} menyerang sebanyak {self.damage_temp} DMG")
        return self.damage_temp

    def terima_aksi(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.nama} kalah")
            return False
        else:
            return True

class Antares(Robot):
    base_health = 50000
    base_attack = 5000
    aksi_interval = 3
    damage_multiplier = 1.5
    damage_temp = base_attack

    def tambah_darah(self):
        self.health += 0

class Alphasetia(Robot):
    base_health = 40000
    base_attack = 6000
    aksi_interval = 2
    damage_multiplier = 1
    damage_temp = base_attack

    def tambah_darah(self):
        self.health += 4000

class Lecalicus(Robot):
    base_health = 45000
    base_attack = 5500
    aksi_interval = 4
    damage_multiplier = 2
    damage_temp = base_attack

    def tambah_darah(self):
        self.health += 7000


def main():
    print("Selamat datang di pertandingan robot Yamako")
    pilihan_robotmu = int(input("Pilih robotmu (1 = Antares, 2 = Alphasetia, 3 = Lecalicus): "))
    pilihan_lawan = int(input("Pilih robot lawan (1 = Antares, 2 = Alphasetia, 3 = Lecalicus): "))
    robotmu = None
    lawan = None

    if pilihan_robotmu == 1:
        robotmu = Antares("Antares", Antares.base_health, Antares.base_attack)
    elif pilihan_robotmu == 2:
        robotmu = Alphasetia("Alphasetia", Alphasetia.base_health, Alphasetia.base_attack)
    elif pilihan_robotmu == 3:
        robotmu = Lecalicus("Lecalicus", Lecalicus.base_health, Lecalicus.base_attack)

    if pilihan_lawan == 1:
        lawan = Antares("Antares", Antares.base_health, Antares.base_attack)
    elif pilihan_lawan == 2:
        lawan = Alphasetia("Alphasetia", Alphasetia.base_health, Alphasetia.base_attack)
    elif pilihan_lawan == 3:
        lawan = Lecalicus("Lecalicus", Lecalicus.base_health, Lecalicus.base_attack)

    tangan_robotmu = int(input("Pilih tangan robotmu (" + robotmu.nama + "): "))
    tangan_lawan = random.randint(1, 3)
    print(f"Pilih tangan robot lawan ({lawan.nama}): {tangan_lawan}")

    while robotmu.health > 0 and lawan.health > 0:
        if tangan_robotmu == tangan_lawan:
            print("Seri!")
        elif tangan_robotmu == 1 and tangan_lawan == 2:
            lawan.health -= robotmu.damage
            print(f"{robotmu.nama} menang dan menyerang sebanyak {robotmu.damage} DMG")
        if lawan.health > 0:
            lawan.lakukan_aksi(robotmu)
        elif tangan_robotmu == 2 and tangan_lawan == 3:
            lawan.health -= robotmu.damage
            print(f"{robotmu.nama} menang dan menyerang sebanyak {robotmu.damage} DMG")
        if lawan.health > 0:
            lawan.lakukan_aksi(robotmu)
        elif tangan_robotmu == 3 and tangan_lawan == 1:
            lawan.health -= robotmu.damage
            print(f"{robotmu.nama} menang dan menyerang sebanyak {robotmu.damage} DMG")
        if lawan.health > 0:
            lawan.lakukan_aksi(robotmu)
        else:
            robotmu.health -= lawan.damage
            print(f"{lawan.nama} menang dan menyerang sebanyak {lawan.damage} DMG")
        if robotmu.health > 0:
            robotmu.lakukan_aksi(lawan)


    # increment jumlah_turn setiap turn
    robotmu.jumlah_turn += 1
    lawan.jumlah_turn += 1

    # check apakah sudah saatnya Alphasetia dan Lecalicus melakukan aksi khusus
    if isinstance(robotmu, Alphasetia) and robotmu.jumlah_turn % 2 == 0:
        robotmu.tambah_darah(4000)
        print(f"{robotmu.nama} menambah darah sebanyak 4000 HP")

    if isinstance(robotmu, Lecalicus) and robotmu.jumlah_turn % 4 == 0:
        robotmu.tambah_darah(7000)
        robotmu.damage *= 2
        print(f"{robotmu.nama} menambah darah sebanyak 7000 HP dan menaikkan damage menjadi {robotmu.damage} DMG")

    if isinstance(lawan, Alphasetia) and lawan.jumlah_turn % 2 == 0:
        lawan.tambah_darah(4000)
        print(f"{lawan.nama} menambah darah sebanyak 4000 HP")

    if isinstance(lawan, Lecalicus) and lawan.jumlah_turn % 4 == 0:
        lawan.tambah_darah(7000)
        lawan.damage *= 2
        print(f"{lawan.nama} menambah darah sebanyak 7000 HP dan menaikkan damage menjadi {lawan.damage} DMG")

    # check apakah permainan telah berakhir
    if robotmu.health <= 0:
        print(f"{robotmu.nama} kalah dan keluar dari pertandingan!")
        print(f"Selamat kepada {lawan.nama} yang memenangkan pertandingan!")
        break

    if lawan.health <= 0:
        print(f"{lawan.nama} kalah dan keluar dari pertandingan!")
        print(f"Selamat kepada {robotmu.nama} yang memenangkan pertandingan!")
        break

# input tangan_robotmu dan tangan_lawan untuk turn selanjutnya
tangan_robotmu = int(input(f"\nTurn saat ini: {robotmu.jumlah_turn}\nRobotmu ({robotmu.nama} - {robotmu.health} HP), robot lawan ({lawan.nama} - {lawan.health} HP)\nPilih tangan robotmu ({robotmu.nama}): "))
print(f"Pilih tangan robot lawan ({lawan.nama}): {tangan_lawan}")


# Lakukan aksi berdasarkan hasil dari permainan
if tangan_robotmu == tangan_lawan:
    print("Hasil imbang!")
elif (tangan_robotmu == 1 and tangan_lawan == 3) or (tangan_robotmu == 2 and tangan_lawan == 1) or (tangan_robotmu == 3 and tangan_lawan == 2):
    print(f"Robotmu ({robotmu.nama}) menang!")
    lawan.health -= robotmu.damage
    robotmu.jumlah_turn += 1
    robotmu.lakukan_aksi(lawan)
else:
    print(f"Robot lawan ({lawan.nama}) menang!")
    robotmu.health -= lawan.damage
    lawan.jumlah_turn += 1
    lawan.lakukan_aksi(robotmu)

# Periksa kondisi kesehatan robot setelah melakukan aksi
if robotmu.health <= 0:
    print(f"\n{robotmu.nama} kalah!")
    break
elif lawan.health <= 0:
    print(f"\n{lawan.nama} kalah!")
    break

#output
if robotmu.health > 0:
    print(f"\nSelamat, {robotmu.nama} menang!")
else:
    print(f"\nSayang sekali, {robotmu.nama} kalah!")