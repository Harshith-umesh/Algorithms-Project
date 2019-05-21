# DAA-Project
Cryptographic Library
## Abstract 

The library implemented here consists of 5 different encryption algorithms, some of which were and still are used as a standard in the industry. The algorithms are:-

* **DES(Data Encryption Standard)**: This was a standard symmetric-key block cipher used in the 1970s
* **AES(Advanced Encryption Standard)**: A symmetric-key block cipher established in the early 21st century
* **Base64**: A binary-to-text encoding scheme that represents binary data in an ASCII string format by translating it into a radix-64 representation
* **Vigenere Cipher**: A method of encrypting alphabetic text by using a series of interwoven Caesar ciphers, based on the letters of a keyword
* **Playfair**: A symmetric encryption technique that encrypts pairs of letters instead of single letters as in a simple substitution cipher

## Test Results ##

* **DES**: <br>
*Input*:- <br> ziyan zafar <br>
*Output*:- <br>
Ciphered: '\x1bj¿\x8cÅ]é\x87¹ÇÑ\ní[\x89ô' <br>
Deciphered:  ziyan zafar <br>
* **AES**:<br>
*Input*:- <br> Enter the length of key (128,192 or 256 only ): 128<br>
Enter the key in hexadecimal:
23 AA 43 C5 6D 79 B6 6F EC B4 58 F7 93 55 CC A4<br>
Enter the plaintext in hexadecimal:
56 43 DC 33 AB 27 2C C5 4D 2A 8F E1 EE 77 62 FEziyan zafar <br>
*Output*:- <br>The ciphertext after encryption:
DD FC 4B 7E 6A BC D5 5D 43 2F F9 23 E3 45 AA A2
* **Base64**:<br>
*Input*:- <br> ziyan zafar <br>
*Output*:- <br>eml5YW4gemFmYXI=
* **Base64 Decode**:<br>
*Input*:- <br> eml5YW4gemFmYXI= <br>
*Output*:- <br>ziyan zafar
* **Vignere Cipher** :<br>
*Input*:- <br> Enter the plaintext: ATTACKATDAWN <br>
Enter the key: LEMON<br>
*Output*:- ciphertext: LXFOPVEFRNHR<br>
* **Playfair Cipher** :<br>
*Input*:- <br> (E)ncode or (D)ecode: E <br>
Enter a(n) en/decryption key: Monarchy<br>
I<->J(Y/N):Y<br>
Enter the text: JAZZ<br>
*Output*:- <br>The generated cipher text: SB UZ UZ
