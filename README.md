---

# Hangman Game 🕴️

Acesta este un joc clasic de **spânzurătoare** (Hangman) implementat în Python. Jucătorul trebuie să ghicească un cuvânt ales aleatoriu litera cu litera, având un număr limitat de încercări.

## 📝 Caracteristici
- **Afișare progresivă a spânzurătorii**: De fiecare dată când o literă este greșită, o parte a spânzurătorii este desenată.
- **Cuvinte aleatorii**: Jocul selectează cuvinte dintr-un fișier text (words.txt) pentru a crea experiențe noi la fiecare sesiune.
- **Interfață text**: Oferă o interacțiune simplă și intuitivă prin consolă.

---

## 📂 Structura fișierelor

- **`hangman.py`**: Scriptul principal care rulează jocul.
- **`words.txt`**: Un fișier text care conține lista cuvintelor din care se alege aleatoriu un cuvânt pentru joc.
- **`README.md`**: Documentația proiectului.

---

## 🚀 Cum să rulezi jocul?

1. **Clonează repository-ul**:
   ```bash
   git clone https://github.com/numele-tau/hangman.git
   cd hangman
   ```

2. **Asigură-te că ai Python instalat** (versiunea 3.6+ este recomandată):
   ```bash
   python --version
   ```

3. **Rulează scriptul**:
   ```bash
   python hangman.py
   ```

---

## 📋 Instrucțiuni pentru joc
1. Jocul începe prin afișarea unui cuvânt ascuns, reprezentat prin caractere `_`.
2. Introdu câte o literă pentru a ghici cuvântul.
   - Dacă litera este corectă, ea va fi afișată în pozițiile potrivite.
   - Dacă litera este greșită, vei pierde o încercare, iar o parte din spânzurătoare va fi desenată.
3. Jocul se termină când:
   - Ghicești toate literele din cuvânt (🎉 Victorie!).
   - Epuizezi toate încercările, iar spânzurătoarea este complet desenată (💀 Pierdere).

---

## ⚠️ Notă
Asigură-te că fișierul `words.txt` conține o listă de cuvinte, fiecare pe o linie separată. De exemplu:
```
python
developer
hangman
code
programming
```

---

## 📌 Exemple de funcționare

### Jocul începe:
```plaintext
========================================
          !!! BUN VENIT LA HANGMAN !!!
========================================
Ai 6 încercări pentru a ghici cuvântul format din 8 litere.
_ _ _ _ _ _ _ _
```

### Jucătorul introduce litere:
```plaintext
Introdu litera -> p
p _ _ _ _ _ _ _
Introdu litera -> z
Nu ai ghicit :(, Încercări rămase: 5
```

---

## 📜 Licență
Acest proiect este public și poate fi folosit și modificat liber de către oricine.

---

