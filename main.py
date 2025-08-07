import numpy as np

#===================ENCRYPT I DECRYPT ZE SPACJAMI (27x27)===================
def vigenere():
    #Rozmiar kwadratu
    count = 27
    #Mapowanie liter na liczby, A=1, B=2, ... SPACJA=27
    alpha = np.arange(1, count + 1)
    #Tworzenie macierzy z 27 przesuniętymi alfabetami
    vig = [np.roll(alpha, -n) for n in range(count)]
    vig = np.vstack(vig)
    return vig

def encrypt(plaintext, key):
    vig = vigenere()

    #Usuwanie znaków innych niż litery i spacja
    plaintext = ''.join([char for char in plaintext if char.isalpha() or char == ' '])

    #Zamiana klucza i tekstu na małe litery i przeliczenie na wartości numeryczne
    key = np.array([ord(char.lower()) - ord('a') + 1 for char in key])
    key[key < 0] = 27
    plaintext = np.array([ord(char.lower()) - ord('a') + 1 for char in plaintext])
    plaintext[plaintext < 0] = 27

    #Powielenie klucza tak, aby był taki sam jak długość tekstu
    keyIndex = np.arange(len(plaintext)) % len(key)
    key_numeric = key[keyIndex]

    #Szyfrowanie: C(m,n) = V(k(j), plaintext(j))
    ciphertext = np.array([vig[key_numeric[j]-1, plaintext[j]-1] for j in range(len(plaintext))]) - 1
    ciphertext[ciphertext == 26] = ord(' ') - ord('a')
    ciphertext = ''.join([chr(char + ord('a')).upper() for char in ciphertext])
    return ciphertext

def decrypt(ciphertext, key):
    vig = vigenere()

    #Zamiana klucza i tekstu na wartości numeryczne; A=1, B=2, itd., SPACJA=27
    key = np.array([ord(char.lower()) - ord('a') + 1 for char in key])
    key[key < 0] = 27
    key = key - 1
    ciphertext = np.array([ord(char.lower()) - ord('a') + 1 for char in ciphertext])
    ciphertext[ciphertext < 0] = 27

    # Powielenie klucza tak, aby był taki sam jak długość tekstu
    keyIndex = np.arange(len(ciphertext)) % len(key)
    key_numeric = key[keyIndex]

    # Deszyfrowanie. Każda litera klucza określa wiersz w tablicy Vigenere.
    # W tym wierszu znajdź indeks kolumny odpowiadający literze szyfrogramu.
    # Przelicz indeks z powrotem na literę, aby ustalić odszyfrowany znak (1=A, 2=B, itd.).
    plaintext = np.array([np.where(vig[m] == n)[0][0] + 1 for m, n in zip(key_numeric, ciphertext)]) - 1
    plaintext[plaintext == 26] = ord(' ') - ord('a')

    plaintext = np.where(plaintext == 27, 0, plaintext)
    plaintext = ''.join([chr(char + ord('a')).upper() for char in plaintext])
    return plaintext

# Funkcja wyboru opcji
def main():
    choice = input("Wybierz opcję: 1 = Szyfrowanie, 2 = Deszyfrowanie: ")

    if choice == '1':
        plaintext = input("Podaj tekst do zaszyfrowania: ")
        key = input("Podaj klucz: ")
        encrypted_text = encrypt(plaintext, key)
        print("Zaszyfrowany tekst:", encrypted_text)
    elif choice == '2':
        ciphertext = input("Podaj tekst do odszyfrowania: ")
        key = input("Podaj klucz: ")
        decrypted_text = decrypt(ciphertext, key)
        print("Odszyfrowany tekst:", decrypted_text)
    else:
        print("Nieprawidłowy wybór. Spróbuj ponownie.")

# Uruchomienie programu
if __name__ == "__main__":
    main()
