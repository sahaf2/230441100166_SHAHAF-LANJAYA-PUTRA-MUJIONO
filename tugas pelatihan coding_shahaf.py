# Volume Balok
print("Volume Balok")
panjang_balok = float(input("Masukan Panjang Balok = "))
lebar_balok = float(input("Masukan Lebar Balok = "))
tinggi_balok = float(input("Masukan Tinggi Balok = "))

volume_balok = panjang_balok * lebar_balok * tinggi_balok

print("Volume Balok Adalah = " , round(volume_balok))
# End Volume Balok

# Volume Tabung
print("Volume Tabung")
jari_jari_tabung = float(input("Masukan Jari-Jari Tabung = "))
tinggi_tabung = float(input("Masukan Tinggi Tabung = "))

volume_tabung = 3.14 * jari_jari_tabung * 2 * tinggi_tabung

print("Volume Tabung adalah = " , round(volume_tabung))
# End Volume Tabung

# Volume Bola
print("Volume Bola")
jari_jari_bola = float(input("Masuka Jari-Jari Bola = "))

volume_bola = 4 / 3  * 3.14 * jari_jari_bola**3

print("Volume Bola adalah = " , round(volume_bola))
# End Volume Bola                   