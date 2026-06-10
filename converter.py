"""INPUT SUHU/TEMPERATURE CELCIUS"""
def input_suhu_celcius() :
    try:
        suhu_celcius = float(input("Masukkan Suhu Celcius: "))
        return suhu_celcius
    except ValueError:
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


#DIVIDER

"""INPUT SUHU REAMUR"""
def input_suhu_reamur() :
    try:
        suhu_reamur = float(input("Masukkan Suhu Reamur: "))
        return suhu_reamur
    except ValueError:
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


#DIVIDER

"""INPUT SUHU FAHRENHEIT"""
def input_suhu_fahrenheit() :
    try:
        suhu_fahrenheit = float(input("Masukkan Suhu Fahrenheit: "))
        return suhu_fahrenheit
    except ValueError:
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


#DIVIDER






"""TEMPAT UNTUK MEMPROSES SEMUANYA"""
celcius = input_suhu_celcius()
if celcius is None:
    print("Harus masukkan angka!!")
else:
    hasil_celcius_to_reamur = celcius_reamur(celcius)
    hasil_celcius_to_fahrenheit = celcius_fahrenheit(celcius)
    hasil_celcius_to_kelvin = celcius_kelvin(celcius)
    print(f"Reamur: {hasil_celcius_to_reamur:.2f}")
    print(f"Fahrenheit: {hasil_celcius_to_fahrenheit:.2f}")
    print(f"Kelvin: {hasil_celcius_to_kelvin:.2f}")

reamur = input_suhu_reamur()
if reamur is None :
    print("Harus Masukkan Angka!!")
else:
    hasil_reamur_to_celcius = reamur_celcius(reamur)
    hasil_reamur_to_fahrenheit = reamur_fahrenheit(reamur)
    hasil_reamur_to_kelvin = reamur_kelvin(reamur)
    print(f"Hasil Reamur ke Celcius Adalah: {hasil_reamur_to_celcius:,.2f}")
    print(f"Hasil Reamur Ke Fahrenheit Adalah: {hasil_reamur_to_fahrenheit:,.2f}")
    print(f"Hasil Reamur Ke Kelvin Adalah: {hasil_reamur_to_kelvin:,.2f}")