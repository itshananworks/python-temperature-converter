import time



#DIVIDER TAMPILAN MENU CONVERTER
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
                    proses_celcius()
                elif pilihan in [
                    "2", "reamur", "2.reamur"
                ]:
                    proses_reamur()
                elif pilihan in [
                    "3", "fahrenheit", "3.fahrenheit"
                ]:
                    proses_fahrenheit()
                elif pilihan in [
                    "4", "kelvin", "4.kelvin"
                ]:
                    proses_kelvin()




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
def output_hasil_celcius(suhu_celcius):
    hasil_celcius_to_reamur = celcius_reamur(suhu_celcius)
    hasil_celcius_to_fahrenheit = celcius_fahrenheit(suhu_celcius)
    hasil_celcius_to_kelvin = celcius_kelvin(suhu_celcius)
    print(f"Hasil Celcius Ke Reamur Adalah: {hasil_celcius_to_reamur:,.2f}")
    print(f"Hasil Celcius Ke Fahrenheit Adalah: {hasil_celcius_to_fahrenheit:,.2f}")
    print(f"Hasil Celcius Ke Kelvin Adalah: {hasil_celcius_to_kelvin:,.2f}")


#DIVIDER OUTPUT REAMUR

"""OUTPUT HASIL REAMUR"""
def output_hasil_reamur(suhu_reamur):
    hasil_reamur_to_celcius = reamur_celcius(suhu_reamur)
    hasil_reamur_to_fahrenheit = reamur_fahrenheit(suhu_reamur)
    hasil_reamur_to_kelvin = reamur_kelvin(suhu_reamur)
    print(f"Hasil Reamur Ke Celcius Adalah: {hasil_reamur_to_celcius:,.2f}")
    print(f"Hasil Reamur Ke Fahrenheit Adalah: {hasil_reamur_to_fahrenheit:,.2f}")
    print(f"Hasil Reamur Ke Kelvin Adalah: {hasil_reamur_to_kelvin:,.2f}")


#DIVIDER OUTPUT FAHRENHEIT
"""OUTPUT HASIL FAHRENHEIT"""
def output_hasil_fahrenheit(suhu_fahrenheit) :
    hasil_fahrenheit_to_celcius = fahrenheit_celcius(suhu_fahrenheit)
    hasil_fahrenheit_to_reamur = fahrenheit_reamur(suhu_fahrenheit)
    hasil_fahrenheit_to_kelvin = fahrenheit_kelvin(suhu_fahrenheit)
    print(f"Hasil Fahrenheit Ke Celcius Adalah: {hasil_fahrenheit_to_celcius:,.2f}")
    print(f"Hasil Fahrenheit Ke Reamur Adalah: {hasil_fahrenheit_to_reamur:,.2f}")
    print(f"Hasil Fahrenheit Ke Kelvin Adalah: {hasil_fahrenheit_to_kelvin:,.2f}")


#DIVIDER OUTPUT KELVIN
"""OUTPUT HASIL KELVIN"""
def output_hasil_kelvin(suhu_kelvin) :
    hasil_kelvin_to_celcius = kelvin_celcius(suhu_kelvin)
    hasil_kelvin_to_reamur = kelvin_reamur(suhu_kelvin)
    hasil_kelvin_to_fahrenheit = kelvin_fahrenheit(suhu_kelvin)
    print(f"Hasil Kelvin Ke Celcius Adalah: {hasil_kelvin_to_celcius:,.2f}")
    print(f"Hasil Kelvin Ke Reamur Adalah: {hasil_kelvin_to_reamur:,.2f}")
    print(f"Hasil Kelvin Ke Fahrenheit Adalah: {hasil_kelvin_to_fahrenheit:,.2f}")


#DIVIDER PROCESS CELCIUS

"""CELCIUS PROCESS"""
def proses_celcius():
    celcius = input_suhu_celcius()
    if celcius is None:
        return
    output_hasil_celcius(celcius)

#DIVIDER PROCESS REAMUR

"""REAMUR PROCESS"""
def proses_reamur():
    reamur = input_suhu_reamur()
    if reamur is None:
        return
    output_hasil_reamur(reamur)

#DIVIDER PROCESS FAHRENHEIT
"""FAHRENHEIT PROCESS"""
def proses_fahrenheit():
    fahrenheit = input_suhu_fahrenheit()
    if fahrenheit is None:
        return
    output_hasil_fahrenheit(fahrenheit)

#DIVIDER PROCESS KELVIN
"""KELVIN PROCESS"""
def proses_kelvin() :
    kelvin = input_suhu_kelvin()
    if kelvin is None :
        return
    output_hasil_kelvin(kelvin)




menu()