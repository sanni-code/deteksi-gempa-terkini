import requests
from bs4 import BeautifulSoup


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
    try:
        content = requests.get('https://bmkg.go.id')
    except Exception:
        return None
    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')

        result = soup.find('span', {'class': 'waktu'})
        result = result.text.split(', ')
        waktu = result[1]
        tanggal = result[0]

        result = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li')
        i = 0
        magnitudo = None
        kedalaman = None
        lat = None
        long = None
        lokasi = None
        dirasakan = None



        for res in result:
            print(i, res)
            if i == 1:
                magnitudo = res.text
            elif i == 2:
                kedalaman = res.text
            elif i == 3:
                koordinat = res.text.split(' - ')
                lat = koordinat[0]
                long = koordinat[1]
            elif i == 4:
                lokasi = res.text
            elif i == 5:
                dirasakan = res.text

            i = i + 1



        hasil = dict()
        hasil['tanggal'] = tanggal #'24 Agustus 2021'
        hasil['waktu'] = waktu#'10:30:34 WIB'
        hasil['magnitudo'] = magnitudo #5.0
        hasil['kedalaman'] = kedalaman
        hasil['koordinat'] = {'lat': lat, 'long': long}
        hasil['lokasi'] = lokasi
        hasil['dirasakan'] = dirasakan #'Dirasakan (Skala MMI): III Bengkulu Utara, I-II Kapahiang, III Ketahun'
        return hasil

    else:
        return None


def tampilkan_data(result):
    if result is None:
        print('Tidak bisa menemukan data gempa terkini')
        return

    print('Gempa Terakhir berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Koordinat: Latitude {result['koordinat']['lat']}")
    print(f"Koordinat: Longitude {result['koordinat']['long']}")
    print(f"Lokasi {result['lokasi']}")
    print(f"  {result['dirasakan']}")


# if __name__ == '__main__':
#    print('Ini adalah package gempa terkini')


"""
Package yang diimport kode yang dieksekusi adalah kode yang nempel di paling kiri, yang tanpa indentasi
"""