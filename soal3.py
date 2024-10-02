print('----------------------------------------')
print('Nama     : Ahmad Dani')
print('Program  : Fungsi')
print('----------------------------------------')

def is_injective(domain, codomain, function):
    # Memeriksa apakah fungsi injektif (satu-ke-satu)
    images = set()
    for x in domain:
        image = function(x)
        if image in images:
            return False  # Jika ada dua elemen domain yang dipetakan ke elemen codomain yang sama
        images.add(image)
    return True

def is_surjective(domain, codomain, function):
    # Memeriksa apakah fungsi surjektif (onto)
    images = {function(x) for x in domain}
    return images == codomain  # Semua elemen di codomain harus tercakup oleh set images

def is_bijective(domain, codomain, function):
    # Fungsi bijektif jika dan hanya jika injektif dan surjektif
    return is_injective(domain, codomain, function) and is_surjective(domain, codomain, function)

# Meminta input dari pengguna untuk domain dan codomain
domain = set(map(int, input("Masukkan elemen-elemen domain (pisahkan dengan spasi): ").split()))
codomain = set(map(int, input("Masukkan elemen-elemen codomain (pisahkan dengan spasi): ").split()))

# Meminta input untuk mendefinisikan fungsi. Misalnya f(x) = 2x, maka pengguna harus mengetik '2*x'.
function_input = input("Masukkan fungsi f(x) (contoh: 2*x untuk f(x) = 2x): ")

# Fungsi dinamis berdasarkan input pengguna
def function(x):
    return eval(function_input)

# Menampilkan domain, codomain, dan fungsi yang diinput
print('----------------------------------------')
print("Domain:", domain)
print("Codomain:", codomain)
print(f"f(x) = {function_input}")
print('----------------------------------------')

# Cek injektifitas
if is_injective(domain, codomain, function):
    print("Fungsi adalah injektif.")
else:
    print("Fungsi bukan injektif.")

# Cek surjektifitas
if is_surjective(domain, codomain, function):
    print("Fungsi adalah surjektif.")
else:
    print("Fungsi bukan surjektif.")

# Cek bijektifitas
if is_bijective(domain, codomain, function):
    print("Fungsi adalah bijektif.")
else:
    print("Fungsi bukan bijektif.")
