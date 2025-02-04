import random
from hangman_art import spanzuratoare

def afisare_cuvant(cuvant):
    print(" ".join(cuvant))


try:
    with open('words.txt', 'r') as out:
        words = [line.strip() for line in out if line.strip()]
        if not words:
            raise ValueError("Fișierul este gol.")
except FileNotFoundError:
    print("Eroare: Fișierul 'words.txt' nu a fost găsit.")
    exit()
except ValueError as e:
    print(f"Eroare: {e}")
    exit()


random_word = random.choice(words)
cuvant = ["_"] * len(random_word)
incercari_ramase = 6
litere_ghicite = 0


print(random_word)
# Mesaj Salut
print("\n" + "=" * 70)
print("\t\t\t  !!! BUN VENIT LA HANGMAN !!!\n")
print(f"\tAi {incercari_ramase} încercări pentru a ghici cuvântul format din {len(cuvant)} litere.")
print("=" * 70)
print(spanzuratoare[6 - incercari_ramase])

# Runda de joc
while incercari_ramase != 0:
    L = input("\nIntrodu litera -> ").lower()

    # Dacă litera este corectă
    if L in random_word:
        litere_ghicite += random_word.count(L)
        for index, x in enumerate(random_word):
            if x == L:
                cuvant[index] = L
        print(f"\n\tBravo! Litera [ {L} ] exista!")
        print(spanzuratoare[6 - incercari_ramase])
        afisare_cuvant(cuvant)
    else:
        incercari_ramase -= 1
        print(f"\n\tNu ai ghicit! Încercări rămase: {incercari_ramase}")
        print(spanzuratoare[6 - incercari_ramase])
        afisare_cuvant(cuvant)

    # WIN
    if "".join(cuvant) == random_word:
        print("\n\n\t!!! FELICITĂRI, AI GHICIT CUVÂNTUL !!!")
        break
# LOSE
if incercari_ramase == 0:
    print(f"\nDin păcate, jocul s-a terminat! Cuvântul era: [ {random_word} ]")
