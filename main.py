"""
Aplikasi deteksi gempa terkini
MODULARISASI DENGAN FUNCTION

Ini adalah aplikasi utamamu yang harus memiliki file
"""


def ekstraksi_data():
    """
    Tanggal: 17 November 2021,
    Waktu: 10:30:34 WIB
    Magnitudo: 5.0
    Kedalaman: 22 km
    Lokasi: lat=3.46 LS  long=101.61 BT
    Keterangan: Pusat gempa berada di laut 65 km barat daya Bengkulu Utara
    Dirasakan: Dirasakan (Skala MMI): III Bengkulu Utara, I-II Kepahiang, III Ketahun
    :return:
    """

    hasil = dict()
    hasil['tanggal'] = '24 Agustus 2021'
    hasil['waktu'] = '10:30:34 WIB'
    hasil['magnitudo'] = 5.0
    hasil['kedalaman'] = '22 km'
    hasil['lokasi'] = {'lat': '3.46 LS', 'long': '101.61 BT'}
    hasil['pusat'] = 'Pusat gempa berada di laut 65 km barat daya Bengkulu Utara'
    hasil['dirasakan'] = 'Dirasakan (Skala MMI): III Bengkulu Utara, I-II Kapahiang, III Ketahun'

    return hasil


def tampilkan_data(result):
    print('Gempa Terakhir berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Lokasi: Latitude {result['lokasi']['lat']}")
    print(f"Lokasi: Longitude {result['lokasi']['long']}")
    print(f"Pusat {result['pusat']}")
    print(f"Dirasakan {result['dirasakan']}")

if __name__ == '__main__':
    print('Aplikasi utama')
    result = ekstraksi_data()
    tampilkan_data(result)

"""
Yang atas yang diproses. 
Perbedaannya dengan
print('Aplikasi utama')

tanpa 

if __name__ == '__main__'

itu apalagi di import dari modul lain, maka yang if name main akan dijalankan.
"""
