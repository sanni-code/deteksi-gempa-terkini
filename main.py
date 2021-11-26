"""
Aplikasi deteksi gempa terkini
MODULARISASI DENGAN FUNCTION

Ini adalah aplikasi utamamu yang harus memiliki file
"""

import gempaterkini

if __name__ == '__main__':
    print('Aplikasi utama')
    result = gempaterkini.ekstraksi_data()
    gempaterkini.tampilkan_data(result)

"""
Yang atas yang diproses. 
Perbedaannya dengan
print('Aplikasi utama')

tanpa 

if __name__ == '__main__'

itu apalagi di import dari modul lain, maka yang if name main akan dijalankan.
"""

