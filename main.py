# import file vData.py
import vData

# tampilan menu navigasi program
print("Tugas Akhir Pelatihan")
print("======================\n")
print("Menu:")
print("1. Visualisasi data GDP per kapita")
print("2. Visualisasi data HDI (Human Development Index)")
answer = int(input('Option: '))

if answer == 1:
    print('\n')
    vData.visualisasi('GDPCAP')

elif answer == 2:
    print('\n')
    vData.visualisasi('HDI')

else:
    print('Pilih opsi yang benar!')