import time



#DIVIDER TAMPILAN MENU UTAMA CONVERTER
"""MENU CONVERTER"""
def menu() :
    while True:
            print("======== KONVERTER SUHU ========")
            print("1.Celcius")
            print("2.Reamur")
            print("3.Fahrenheit")
            print("4.Kelvin")
            print("5.Keluar Converter")
            pilihan = input("Masukkan Pilihan Anda: ").lower()
            if pilihan not in [
                "1", "celcius", "1.celcius",
                "2", "reamur", "2.reamur",
                "3", "fahrenheit", "3.fahrenheit",
                "4", "kelvin", "4.kelvin",
                "5", "keluar", "keluar converter", "5.keluar converter"
            ]:
                print("Pilihan Tidak Valid")
                continue
            else:
                if pilihan in [
                    "5", "keluar", "keluar converter", "5.keluar converter"
                ]:
                    print("Terima kasih telah menggunakan converter kami:D")
                    time.sleep(2)
                    break
                elif pilihan in [
                    "1", "celcius", "1.celcius"
                ]:
                    menu_celcius()
                elif pilihan in [
                    "2", "reamur", "2.reamur"
                ]:
                    menu_reamur()
                elif pilihan in [
                    "3", "fahrenheit", "3.fahrenheit"
                ]:
                    menu_fahrenheit()
                elif pilihan in [
                    "4", "kelvin", "4.kelvin"
                ]:
                    menu_kelvin()


#DIVIDER TAMPILAN MENU CELCIUS
def menu_celcius():
    while True:
        print("======== KONVERSI CELCIUS ========")
        print("1.Celcius Ke Reamur")
        print("2.Celcius Ke Fahrenheit")
        print("3.Celcius Ke Kelvin")
        print("4.Kembali Ke Tampilan Menu Utama")
        pilihan_celcius = input("Masukkan Pilihan Anda: ").lower()
        if pilihan_celcius not in [
            "1", "celcius ke reamur", "1.celcius ke reamur",
            "2", "celcius ke fahrenheit", "2.celcius ke fahrenheit",
            "3", "celcius ke kelvin", "3.celcius ke kelvin",
            "4", "kembali", "kembali ke menu utama", "kembali ke tampilan menu utama", "4.kembali ke tampilan menu utama"
        ]:
            print("Harap Memilih Dengan Benar!!")
            continue
        else:
            if pilihan_celcius in [
                "4", "kembali", "kembali ke menu utama", "kembali ke tampilan menu utama", "4.kembali ke tampilan menu utama"
            ]:
                print("Kembali Ke Menu tampilan..")
                time.sleep(1)
                break
            elif pilihan_celcius in [
                "1", "celcius ke reamur", "1.celcius ke reamur"
            ]:
                proses_celcius_reamur()
            elif pilihan_celcius in [
                "2", "celcius ke fahrenheit", "2.celcius ke fahrenheit"
            ]:
                proses_celcius_fahrenheit()
            elif pilihan_celcius in [
                "3", "celcius ke kelvin", "3.celcius ke kelvin"
            ]:
                proses_celcius_kelvin()

#DIVIDER TAMPILAN MENU REAMUR
def menu_reamur():
    while True:
        print("======== KONVERSI REAMUR ========")
        print("1.Reamur Ke Celcius")
        print("2.Reamur Ke Fahrenheit")
        print("3.Reamur Ke Kelvin")
        print("4.Kembali Ke Tampilan Menu Utama")
        pilihan_reamur = input("Masukkan Pilihan Anda: ").lower()
        if pilihan_reamur not in [
            "1", "reamur ke celcius", "1.reamur ke celcius",
            "2", "reamur ke fahrenheit", "2.reamur ke fahrenheit",
            "3", "reamur ke kelvin", "3.reamur ke kelvin",
            "4", "kembali", "kembali ke menu utama", "kembali ke tampilan menu utama", "4.kembali ke tampilan menu utama"
        ]:
            print("Harap Memilih Dengan Benar!!")
            continue
        else:
            if pilihan_reamur in [
                "4", "kembali", "kembali ke menu utama", "kembali ke tampilan menu utama", "4.kembali ke tampilan menu utama"
            ]:
                print("Kembali Ke Menu Tampilan..")
                time.sleep(1)
                break
            elif pilihan_reamur in [
                "1", "reamur ke celcius", "1.reamur ke celcius"
            ]:
                proses_reamur_celcius()
            elif pilihan_reamur in [
                "2", "reamur ke fahrenheit", "2.reamur ke fahrenheit"
            ]:
                proses_reamur_fahrenheit()
            elif pilihan_reamur in [
                "3", "reamur ke kelvin", "3.reamur ke kelvin"
            ]:
                proses_reamur_kelvin()

#DIVIDER TAMPILAN MENU FAHRENHEIT
def menu_fahrenheit():
    while True:
        print("======== KONVERSI FAHRENHEIT ========")
        print("1.Fahrenheit Ke Celcius")
        print("2.Fahrenheit Ke Reamur")
        print("3.Fahrenheit Ke Kelvin")
        print("4.Kembali Ke Tampilan Menu Utama")
        pilihan_fahrenheit = input("Masukkan Pilihan Anda: ").lower()
        if pilihan_fahrenheit not in [
            "1", "fahrenheit ke celcius", "1.fahrenheit ke celcius",
            "2", "fahrenheit ke reamur", "2.fahrenheit ke reamur",
            "3", "fahrenheit ke kelvin", "3.fahrenheit ke kelvin",
            "4", "kembali", "kembali ke menu utama", "kembali ke tampilan menu utama", "4.kembali ke tampilan menu utama"
        ]:
            print("Harap memilih dengan benar!!")
            continue
        else:
            if pilihan_fahrenheit in [
                "4", "kembali", "kembali ke menu utama", "kembali ke tampilan menu utama", "4.kembali ke tampilan menu utama"
            ]:
                print("Kembali Ke Menu Tampilan..")
                time.sleep(1)
                break
            elif pilihan_fahrenheit in [
                "1", "fahrenheit ke celcius", "1.fahrenheit ke celcius"
            ]:
                proses_fahrenheit_celcius()
            elif pilihan_fahrenheit in [
                "2", "fahrenheit ke reamur", "2.fahrenheit ke reamur"
            ]:
                proses_fahrenheit_reamur()
            elif pilihan_fahrenheit in [
                "3", "fahrenheit ke kelvin", "3.fahrenheit ke kelvin"
            ]:
                proses_fahrenheit_kelvin()

#DIVIDER TAMPILAN MENU KELVIN
def menu_kelvin():
    while True:
        print("======== KONVERSI KELVIN ========")
        print("1.Kelvin Ke Celcius")
        print("2.Kelvin Ke Reamur")
        print("3.Kelvin Ke Fahrenheit")
        print("4.Kembali Ke Tampilan Menu Utama")
        pilihan_kelvin = input("Masukkan Pilihan Anda: ").lower()
        if pilihan_kelvin not in [
            "1", "kelvin ke celcius", "1.kelvin ke celcius",
            "2", "kelvin ke reamur", "2.kelvin ke reamur",
            "3", "kelvin ke fahrenheit", "3.kelvin ke fahrenheit",
            "4", "kembali", "kembali ke menu utama", "kembali ke tampilan menu utama", "4.kembali ke tampilan menu utama"
        ]:
            print("Harap Memilih Dengan Benar!!")
            continue
        else:
            if pilihan_kelvin in [
                "4", "kembali", "kembali ke menu utama", "kembali ke tampilan menu utama", "4.kembali ke tampilan menu utama"
            ]:
                print("Kembali Ke Tampilan Menu..")
                time.sleep(1)
                break
            else:
                if pilihan_kelvin in [
                    "1", "kelvin ke celcius", "1.kelvin ke celcius"
                ]:
                    proses_kelvin_celcius()
                elif pilihan_kelvin in [
                    "2", "kelvin ke reamur", "2.kelvin ke reamur"
                ]:
                    proses_kelvin_reamur()
                elif pilihan_kelvin in [
                    "3", "kelvin ke fahrenheit", "3.kelvin ke fahrenheit"
                ]:
                    proses_kelvin_fahrenheit()


#DIVIDER CELCIUS

"""INPUT SUHU/TEMPERATURE CELCIUS"""
def input_suhu_celcius() :
    try:
        suhu_celcius = float(input("Masukkan Suhu Celcius: "))
        return suhu_celcius
    except ValueError:
        print("Harus Masukkan Angka!!")
        return None


"""CELCIUS TO REAMUR"""
def celcius_reamur(suhu_celcius) :
    return (4 / 5 ) * suhu_celcius

"""CELCIUS TO FAHRENHEIT"""
def celcius_fahrenheit(suhu_celcius):
    return (9 / 5 * suhu_celcius) + 32

"""CELCIUS TO KELVIN"""
def celcius_kelvin(suhu_celcius):
    return suhu_celcius + 273.15


#DIVIDER REAMUR

"""INPUT SUHU REAMUR"""
def input_suhu_reamur() :
    try:
        suhu_reamur = float(input("Masukkan Suhu Reamur: "))
        return suhu_reamur
    except ValueError:
        print("Harus Masukkan Angka!!")
        return None

"""REAMUR TO CELCIUS"""
def reamur_celcius(suhu_reamur) :
    return (5 / 4) * suhu_reamur

"""REAMUR TO FAHRENHEIT"""
def reamur_fahrenheit(suhu_reamur) :
    return (9 / 4 * suhu_reamur) + 32

"""REAMUR TO KELVIN"""
def reamur_kelvin(suhu_reamur) :
    return (5 / 4 * suhu_reamur) + 273.15


#DIVIDER FAHRENHEIT

"""INPUT SUHU FAHRENHEIT"""
def input_suhu_fahrenheit() :
    try:
        suhu_fahrenheit = float(input("Masukkan Suhu Fahrenheit: "))
        return suhu_fahrenheit
    except ValueError:
        print("Harus Masukkan Angka!!")
        return None

"""FAHRENHEIT TO CELCIUS"""
def fahrenheit_celcius(suhu_fahrenheit) :
    return (5 / 9) * (suhu_fahrenheit - 32)

"""FAHRENHEIT TO REAMUR"""
def fahrenheit_reamur(suhu_fahrenheit) :
    return (4 / 9) * (suhu_fahrenheit - 32)

"""FAHRENHEIT TO KELVIN"""
def fahrenheit_kelvin(suhu_fahrenheit):
    hasil_celcius = fahrenheit_celcius(suhu_fahrenheit)
    return hasil_celcius + 273.15


#DIVIDER KELVIN

"""INPUT SUHU KELVIN"""
def input_suhu_kelvin():
    try:
        suhu_kelvin = float(input("Masukkan Suhu Kelvin: "))
        if suhu_kelvin < 0:
            print("Suhu Kelvin Tidak Boleh kurang Dari Nol!!")
            return None
        return suhu_kelvin
    except ValueError:
        print("Harus Masukkan Angka!!")
        return None

"""KELVIN TO CELCIUS"""
def kelvin_celcius(suhu_kelvin) :
    return suhu_kelvin - 273.15

"""KELVIN TO REAMUR"""
def kelvin_reamur(suhu_kelvin) :
    return (4 / 5) * (suhu_kelvin - 273.15)

"""KELVIN TO FAHRENHEIT"""
def kelvin_fahrenheit(suhu_kelvin) :
    hasil_celcius1 = kelvin_celcius(suhu_kelvin)
    return (9 / 5 * hasil_celcius1) + 32


#DIVIDER OUTPUT CELCIUS

"""OUTPUT HASIL CELCIUS"""

def output_celcius_reamur(suhu_celcius):
    hasil_celcius_to_reamur = celcius_reamur(suhu_celcius)
    print(f"Hasil Celcius Ke Reamur Adalah: {hasil_celcius_to_reamur:,.2f}")

def output_celcius_fahrenheit(suhu_celcius):
    hasil_celcius_to_fahrenheit = celcius_fahrenheit(suhu_celcius)
    print(f"Hasil Celcius Ke Fahrenheit Adalah: {hasil_celcius_to_fahrenheit:,.2f}")

def output_celcius_kelvin(suhu_celcius):
    hasil_celcius_to_kelvin = celcius_kelvin(suhu_celcius)
    print(f"Hasil Celcius Ke Kelvin Adalah: {hasil_celcius_to_kelvin:,.2f}")

#DIVIDER OUTPUT REAMUR

"""OUTPUT HASIL REAMUR"""

def output_reamur_celcius(suhu_reamur):
    hasil_reamur_to_celcius = reamur_celcius(suhu_reamur)
    print(f"Hasil Reamur Ke Celcius Adalah: {hasil_reamur_to_celcius:,.2f}")

def output_reamur_fahrenheit(suhu_reamur):
    hasil_reamur_to_fahrenheit = reamur_fahrenheit(suhu_reamur)
    print(f"Hasil Reamur Ke Fahrenheit Adalah: {hasil_reamur_to_fahrenheit:,.2f}")

def output_reamur_kelvin(suhu_reamur):
    hasil_reamur_to_kelvin = reamur_kelvin(suhu_reamur)
    print(f"Hasil Reamur Ke Kelvin Adalah: {hasil_reamur_to_kelvin:,.2f}")

#DIVIDER OUTPUT FAHRENHEIT
"""OUTPUT HASIL FAHRENHEIT"""

def output_fahrenheit_celcius(suhu_fahrenheit) :
    hasil_fahrenheit_to_celcius = fahrenheit_celcius(suhu_fahrenheit)
    print(f"Hasil Fahrenheit Ke Celcius Adalah: {hasil_fahrenheit_to_celcius:,.2f}")

def output_fahrenheit_reamur(suhu_fahrenheit):
    hasil_fahrenheit_to_reamur = fahrenheit_reamur(suhu_fahrenheit)
    print(f"Hasil Fahrenheit Ke Reamur Adalah: {hasil_fahrenheit_to_reamur:,.2f}")

def output_fahrenheit_kelvin(suhu_fahrenheit):
    hasil_fahrenheit_to_kelvin = fahrenheit_kelvin(suhu_fahrenheit)
    print(f"Hasil Fahrenheit Ke Kelvin Adalah: {hasil_fahrenheit_to_kelvin:,.2f}")

#DIVIDER OUTPUT KELVIN
"""OUTPUT HASIL KELVIN"""


def output_kelvin_celcius(suhu_kelvin):
    hasil_kelvin_to_celcius = kelvin_celcius(suhu_kelvin)
    print(f"Hasil Kelvin Ke Celcius Adalah: {hasil_kelvin_to_celcius:,.2f}")

def output_kelvin_reamur(suhu_kelvin):
    hasil_kelvin_to_reamur = kelvin_reamur(suhu_kelvin)
    print(f"Hasil Kelvin Ke Reamur Adalah: {hasil_kelvin_to_reamur:,.2f}")

def output_kelvin_fahrenheit(suhu_kelvin):
    hasil_kelvin_to_fahrenheit = kelvin_fahrenheit(suhu_kelvin)
    print(f"Hasil Kelvin Ke Fahrenheit Adalah: {hasil_kelvin_to_fahrenheit:,.2f}")

#DIVIDER PROCESS CELCIUS

"""CELCIUS PROCESS"""

def proses_celcius_reamur():
    celcius = input_suhu_celcius()
    if celcius is None:
        return
    output_celcius_reamur(celcius)

def proses_celcius_fahrenheit():
    celcius = input_suhu_celcius()
    if celcius is None:
        return
    output_celcius_fahrenheit(celcius)

def proses_celcius_kelvin():
    celcius = input_suhu_celcius()
    if celcius is None:
        return
    output_celcius_kelvin(celcius)

#DIVIDER PROCESS REAMUR

"""REAMUR PROCESS"""

def proses_reamur_celcius():
    reamur = input_suhu_reamur()
    if reamur is None:
        return
    output_reamur_celcius(reamur)

def proses_reamur_fahrenheit():
    reamur = input_suhu_reamur()
    if reamur is None:
        return
    output_reamur_fahrenheit(reamur)

def proses_reamur_kelvin():
    reamur = input_suhu_reamur()
    if reamur is None:
        return
    output_reamur_kelvin(reamur)

#DIVIDER PROCESS FAHRENHEIT
"""FAHRENHEIT PROCESS"""

def proses_fahrenheit_celcius():
    fahrenheit = input_suhu_fahrenheit()
    if fahrenheit is None:
        return
    output_fahrenheit_celcius(fahrenheit)

def proses_fahrenheit_reamur():
    fahrenheit = input_suhu_fahrenheit()
    if fahrenheit is None:
        return
    output_fahrenheit_reamur(fahrenheit)

def proses_fahrenheit_kelvin():
    fahrenheit = input_suhu_fahrenheit()
    if fahrenheit is None:
        return
    output_fahrenheit_kelvin(fahrenheit)

#DIVIDER PROCESS KELVIN
"""KELVIN PROCESS"""

def proses_kelvin_celcius():
    kelvin = input_suhu_kelvin()
    if kelvin is None:
        return
    output_kelvin_celcius(kelvin)

def proses_kelvin_reamur():
    kelvin = input_suhu_kelvin()
    if kelvin is None:
        return
    output_kelvin_reamur(kelvin)

def proses_kelvin_fahrenheit():
    kelvin = input_suhu_kelvin()
    if kelvin is None:
        return
    output_kelvin_fahrenheit(kelvin)




"""TEMPAT SISTEM DIJALANKAN"""
menu()