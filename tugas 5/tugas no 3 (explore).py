class Manusia:
    def __init__(self, tinggi, berat):
        self.tinggi = tinggi
        self.berat = berat

    def hitung_bmi(self):
        bmi = self.berat / (self.tinggi / 100) ** 2
        return bmi

class Pria(Manusia):
    def __init__(self, tinggi, berat):
        super().__init__(tinggi, berat)
        self.berat_ideal = 0

    #magic method str
    def __str__(self):
        return f"Berat ideal pria dengan tinggi {self.tinggi} cm adalah {self.berat_ideal} kg"

    def hitung_berat_ideal(self):
        self.berat_ideal = (self.tinggi - 100)


class Wanita(Manusia):
    def __init__(self, tinggi, berat):
        super().__init__(tinggi, berat)
        self.berat_ideal = 0

    #magic method str
    def __str__(self):
        return f"Berat ideal wanita dengan tinggi {self.tinggi} cm adalah {self.berat_ideal} kg"

    def hitung_berat_ideal(self):
        self.berat_ideal = (self.tinggi - 100)

#membuat objek dari kelas Pria
pria1 = Pria(170, 70)

#membuat objek dari kelas Wanita
wanita1 = Wanita(160, 50)

#menghitung BMI dari masing-masing objek
print("BMI Pria 1:", pria1.hitung_bmi())
print("BMI Wanita 1:", wanita1.hitung_bmi())

#menghitung berat ideal dari masing-masing objek
pria1.hitung_berat_ideal()
wanita1.hitung_berat_ideal()

#berat ideal dari masing-masing objek
print(pria1)
print(wanita1)


def hitung_bmi(self):
    bmi = self.berat / (self.tinggi / 100) ** 2
    if bmi < 18.5:
        print("Berat badan kurang (underweight)")
    elif 18.5 <= bmi <= 24.9:
        print("Berat badan normal")
    elif 25.0 <= bmi <= 29.9:
        print("Berat badan berlebih (overweight)")
    else:
        print("Obesitas")

pria = Pria(170, 70)
pria.hitung_bmi() # output: Berat badan normal