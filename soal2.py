print('----------------------------------------')
print('Nama     : Petrus Fendiyanto')
print('Program  : Logika')
print('----------------------------------------')

def truth_table():
    print(" p | q | p AND q | p OR q | NOT p | NOT q | p => q | p <=> q ")
    print("-" * 58)

    for p in [False, True]:
        for q in [False, True]:
            # Menghitung hasil logika
            and_result = p and q
            or_result = p or q
            not_p = not p
            not_q = not q
            implies_result = (not p) or q  # Implikasi (p => q) sama dengan (NOT p OR q)
            iff_result = p == q  # Biimplikasi (p <=> q) sama dengan p == q

            # Memunculkan hasil
            print(f"{p:>2} | {q:>2} | {and_result:>7} | {or_result:>6} | {not_p:>5} | {not_q:>5} | {implies_result:>6} | {iff_result:>6}")

# Menjalankan fungsi
if __name__ == "__main__":
    truth_table()
