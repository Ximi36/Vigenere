# Vigenere

This code implements the Vigenère cipher, which is a substitution encryption technique that uses multiple alphabets, changing them depending on the subsequent letters of the key. Encryption is performed by shifting the plaintext letters up or down by the value corresponding to the key letter, with spaces being treated as the 27th character. Decryption is done in the opposite way. The encrypt() and decrypt() functions take plaintext or ciphertext and a key, and then return the encrypted or decrypted text, respectively. It is worth noting that the code operates on the basis of lowercase letters of the Latin alphabet.

The code is unusual, the table used for encoding and decoding is attached. The "_" character represents the space symbol.
