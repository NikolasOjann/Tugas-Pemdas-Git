data_panen = {
    'lokasi1': {
        'nama_lokasi' : 'Kebun A',
        'hasil_panen' : {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2':{
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai' : 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4':{
        'nama_lokasi': 'Kebun D',
        'hasil_panen':{
            'padi':1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi':1400,
            'jagung': 950,
            'kedelai': 480
        }
    }
}


# 1
print(f"Seluruh data panen")
print(data_panen)

# 2
hasil_panen_lokasi2 = data_panen["lokasi2"]["hasil_panen"]["jagung"] 
print(f"Hasil panen jagung Lokasi2: {hasil_panen_lokasi2}")

# 3
Nama_lokasi = data_panen["lokasi3"]["nama_lokasi"]
print(f"Nama Lokasi3 adalah:{Nama_lokasi}")

# 4
hasil_panen_padi = []
hasil_panen_kedelai = []

for lokasi in data_panen:
    padi = data_panen[lokasi]['hasil_panen']['padi']
    kedelai = data_panen[lokasi]['hasil_panen']['kedelai']

    hasil_panen_padi.append(padi)
    hasil_panen_kedelai.append(kedelai)
    
print("Hasil panen padi semua lokasi",hasil_panen_padi)
print("Hasil panen kedelai semua lokasi",hasil_panen_kedelai)

# 5
padi_di_lokasi1 = data_panen['lokasi1']['hasil_panen']['padi']
kedelai_di_lokasi1 = data_panen['lokasi1']['hasil_panen']['kedelai']

padi_di_lokasi2 = data_panen['lokasi2']['hasil_panen']['padi']
kedelai_di_lokasi2 = data_panen['lokasi2']['hasil_panen']['kedelai']

padi_di_lokasi3 = data_panen['lokasi3']['hasil_panen']['padi']
kedelai_di_lokasi3 = data_panen['lokasi3']['hasil_panen']['kedelai']

padi_di_lokasi4 = data_panen['lokasi4']['hasil_panen']['padi']
kedelai_di_lokasi4 = data_panen['lokasi4']['hasil_panen']['kedelai']

padi_di_lokasi5 = data_panen['lokasi5']['hasil_panen']['padi']
kedelai_di_lokasi5 = data_panen['lokasi5']['hasil_panen']['kedelai']


print("Hasil Panen Padi:")
print("Kebun A:", padi_di_lokasi1, "kg")
print("Kebun B:", padi_di_lokasi2, "kg")
print("Kebun C:", padi_di_lokasi3, "kg")
print("Kebun D:", padi_di_lokasi4, "kg")
print("Kebun E:", padi_di_lokasi5, "kg")

print("\nHasil Panen Kedelai:")
print("Kebun A:", kedelai_di_lokasi1, "kg")
print("Kebun B:", kedelai_di_lokasi2, "kg")
print("Kebun C:", kedelai_di_lokasi3, "kg")
print("Kebun D:", kedelai_di_lokasi4, "kg")
print("Kebun E:", kedelai_di_lokasi5, "kg")



# 6
for A in data_panen:
    nama_lokasi = data_panen[A]['nama_lokasi']
    padi = data_panen[A]['hasil_panen']['padi']
    jagung = data_panen[A]['hasil_panen']['jagung']

    if padi >1300 or jagung >800:
        tampilkan = "memerlukan perhatian khusus"
    else:
        tampilkan = "dalam kondisi baik"

    
print(f"lokasi {nama_lokasi}: hasil panen padi= {padi} kg, \nhasil panen jagung = {jagung} kg \ntampilan:{tampilkan}")
