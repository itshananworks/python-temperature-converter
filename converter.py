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

