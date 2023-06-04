class Robot:

    jumlah_turn = 0

    def __init__(self, nama, health, damage):
        self.nama = nama
        self.health = health
        self.damage = damage
        
    def lakukan_aksi(self,nama):
        if nama == "Antares": 
            if self.jumlah_turn % 3 == 0:
                damage = self.damage * 1.5  
            else:
                damage = self.damage

        elif nama == "Alphasetia":
            if self.jumlah_turn % 2 == 0:
                self.health += 4000  
                print(f'Robot lawan ({nama}) menambah darah sebanyak 4000 HP')
            damage = self.damage

        elif nama == "Lecalicus":
            if self.jumlah_turn % 4 == 0:
                self.health += 7000
                print(f'Robot lawan ({nama}) menambah darah sebanyak 7000 HP')
                damage = self.damage * 2        
            else:
                damage = self.damage

        else:
            damage = self.damage
        return damage
    
    def terima_aksi(self,damage, status,nama):
        self.health -= damage
        if status == 1:
            print(f'Robotmu ({nama}) menyerang sebanyak {int(damage)} DMG')
        elif status == 2:
            print(f'Robot lawan ({nama}) menyerang sebanyak {int(damage)} DMG')

class Antares(Robot):
    def __init__(self, nama, health, damage):
        super().__init__(nama, health, damage)
        
class Alphasetia(Robot):
    def __init__(self, nama, health, damage):
        super().__init__(nama, health, damage)

class Lecalicus(Robot):
    def __init__(self, nama, health, damage):
        super().__init__(nama, health, damage)
        
def pertarungan(p1,p2):
    while True:
        if p1.health <= 0:
            print("robotmu kalah setelah",p1.jumlah_turn,"turn")
            break
        if p2.health <= 0:
            print("robotmu menang setelah",p1.jumlah_turn,"turn")
            break
            
        p1.jumlah_turn +=1
        p2.jumlah_turn +=1
        print("Turn saat ini : ", p1.jumlah_turn)
        print("Robotmu (",p1.nama,"-",p1.health,"HP),robot lawan (",p2.nama,"-",p2.health,"HP)")
        
        a = int(input(f'Pilih tangan robotmu ({p1.nama}): '))
        b = int(input(f'Pilih tangan robot lawan ({p2.nama}): '))
        if (a < 4 and a > 0) and (b < 4 and b > 0):
            if (a == 1 and b == 3) or (a == 2 and b == 1) or (a == 3 and b == 2):
                aksi1 = p1.lakukan_aksi(p1.nama)
                p2.terima_aksi(aksi1, 1,p1.nama)
            elif (a == 3 and b == 1) or (a == 1 and b == 2) or (a == 2 and b == 3):
                aksi2 = p2.lakukan_aksi(p2.nama)
                p1.terima_aksi(aksi2, 2, p2.nama)
            elif (a == 1 and b == 1) or (a == 2 and b == 2) or (a == 3 and b == 3):
                print("Draw Try Again!!!!!!") 
        else:
            print("tangan robotmu tidak ada")
        
print("Selamat datang di pertandingan robot Yamako")
while True:
    robotmu = int(input("Pilih robotmu (1=Antares, 2=Alphasetia, 3=Lecalicus):"))
    robot_lawan = int(input("Pilih robot lawan (1=Antares, 2=Alphasetia, 3=Lecalicus):"))
    if (robotmu < 4 and robotmu > 0) and (robot_lawan < 4 and robot_lawan > 0):
        if robotmu == 1:
            p1 = Antares("Antares",50000,5000)
        elif robotmu == 2:
            p1 = Alphasetia("Alphasetia",40000,6000)
        elif robotmu == 3:
            p1 = Lecalicus("Lecalicus",45000,5500)
        if robot_lawan == 1:
            p2 = Antares("Antares",50000,5000)
        elif robot_lawan == 2:
            p2 = Alphasetia("Alphasetia",40000,6000)
        elif robot_lawan == 3:
            p2 = Lecalicus("Lecalicus",45000,5500)
        break
    else:
        print("robot tidak tersedia")
        
print("Pilih 1 untuk batu, 2 untuk kertas, dan 3 untuk gunting")
pertarungan(p1,p2)
