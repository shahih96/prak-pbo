#Muhammad Shahih Indra Sakti
#121140184

username="informatika"
password="12345678"

percobaan=0
while percobaan<3:
    input_uname = input("Masukkan username: ")
    input_passw = input("Masukkan password: ")

    if input_uname == username and input_passw == password:
        print("Berhasil login")
        break
    else:
        percobaan=percobaan+1
        print("Username atau password salah")

if percobaan == 3:
    print("Akun diblokir")