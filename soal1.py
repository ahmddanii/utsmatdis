print('----------------------------------------')
print('Nama     : Ahmad Dani')
print('Program  : Himpunan')
print('----------------------------------------')

import matplotlib.pyplot as plt
from matplotlib_venn import venn2

# Input himpunan A dan B dari pengguna
A = set(map(int, input("Masukkan elemen-elemen Himpunan A (pisahkan dengan spasi): ").split()))
B = set(map(int, input("Masukkan elemen-elemen Himpunan B (pisahkan dengan spasi): ").split()))

# Operasi dasar pada himpunan
gabungan = A | B
irisan = A & B
komplemen_A = A - B
komplemen_B = B - A
beda_setangkup = A ^ B

# Munculkan output
print("\nGabungan A ∪ B:", gabungan)
print("Irisan A ∩ B:", irisan)
print("Komplemen A terhadap B:", komplemen_A)
print("Komplemen B terhadap A:", komplemen_B)
print("Beda setangkup A △ B:", beda_setangkup)

# Membuat diagram Venn untuk dua himpunan
plt.figure(figsize=(8, 8))
venn = venn2([A, B], set_labels=('Himpunan A', 'Himpunan B'))

# Memberi keterangan pada masing-masing area diagram Venn
venn.get_label_by_id('10').set_text(f'A - B\n{komplemen_A}')
venn.get_label_by_id('01').set_text(f'B - A\n{komplemen_B}')
venn.get_label_by_id('11').set_text(f'A ∩ B\n{irisan}')

# Judul pada diagram Venn
plt.title('Diagram Venn dengan Keterangan Operasi Himpunan')

# Menampilkan diagram
plt.show()
