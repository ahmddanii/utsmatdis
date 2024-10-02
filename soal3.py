print('----------------------------------------')
print('Nama     : Petrus Fendiyanto')
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

# Definisikan domain dan kodomain
domain = {1, 2, 3}
codomain = {2, 4, 6}

# Definisikan fungsi f(x) = 2x
def function(x):
    return 2 * x

print("Domain:", domain)
print("Codomain:", codomain)
print("f(x) = 2x")
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
