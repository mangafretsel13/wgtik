def get_last_digit(plat):
    # Ambil karakter terakhir dari nomor plat
    last_char = plat[-1]
    # Pastikan karakter terakhir adalah digit numerik
    if last_char.isdigit():
        return int(last_char)
    else:
        # Jika karakter terakhir bukan digit numerik, kembalikan 0
        return 0

def kenaRazia(date, data):
    # Lokasi Ganjil Genap
    ganjil_genap_rute = ["Gajah Mada", "Hayam Wuruk", "Sisingamangaraja", "Panglima Polim", "Fatmawati", "Tomang Raya"]

    tilang_info = {}
    for vehicle in data:
        # Hanya periksa untuk kendaraan tipe "Mobil"
        if vehicle["type"] == "Mobil":
            # Periksa apakah tanggal berada dalam rentang yang valid
            if 1 <= date <= 31:
                last_digit = get_last_digit(vehicle["plat"])
                # Inisialisasi total tilang untuk setiap pengemudi
                if vehicle["name"] not in tilang_info:
                    tilang_info[vehicle["name"]] = 0
                # Periksa apakah kendaraan harus ditilang berdasarkan rute dan nomor plat
                for route in vehicle["rute"]:
                    # Jika rute termasuk dalam daftar Ganjil Genap dan nomor plat genap (atau ganjil), kendaraan harus ditilang
                    if route in ganjil_genap_rute and (last_digit % 2 != date % 2):
                        tilang_info[vehicle["name"]] += 1

    # Ubah format tilang_info menjadi list of dict untuk konsistensi output
    tilang_info_list = [{"name": name, "tilang": total_tilang} for name, total_tilang in tilang_info.items()]
    return tilang_info_list

#main
vehicles = [
    {"name": "Denver", "plat": "B 2791 KDS", "type": "Mobil", "rute": ["TB Simatupang", "Panglima Polim", "Depok", "Senen Raya"]},
    {"name": "Toni", "plat": "B 1212 JBB", "type": "Mobil", "rute": ["Pintu Besar Selatan", "Panglima Polim", "Depok", "Senen Raya", "Kemang"]},
    {"name": "Stark", "plat": "B 444 XSX", "type": "Motor", "rute": ["Pondok Indah", "Depok", "Senen Raya", "Kemang"]},
    {"name": "Anna", "plat": "B 678 DD", "type": "Mobil", "rute": ["Fatmawati", "Panglima Polim", "Depok", "Senen Raya", "Kemang", "Gajah Mada"]}
]

date = 27
tilang_info = kenaRazia(date, vehicles)

print("Detail kendaraan yang harus ditilang:")
for info in tilang_info:
    print(f"Nama: {info['name']}, Total Tilang: {info['tilang']}")
