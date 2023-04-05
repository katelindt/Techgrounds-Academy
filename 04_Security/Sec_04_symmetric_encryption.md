# Symmetric encryption
Encryption is the method by which information is converted into secret code that hides the information's true meaning.

There are two types of encryption in widespread use today: symmetric and asymmetric encryption. 

## Key terminology

- Encryption

- The Caesar cipher, also called a Caesar shift, gets its name from Julius Caesar, who occasionally used this encoding method in his own private messages. As one of the most basic encryption techniques, the Caesar cipher works by replacing each letter in the original plaintext message with a different letter based off a fixed shift of the alphabet.

- Algorithm - a cipher, algorithms are the rules or instructions for the encryption process. The key length, functionality, and features of the encryption system in use determine the effectiveness of the encryption.

- Decryption - the process of converting unreadable ciphertext to readable information.

- Key - a randomized string of bits used to encrypt and decrypt data. Each key is unique, and longer keys are harder to break. Typical key lengths are 128 and 256 bits for private keys and 2048 for public keys.

- Symmetric Key Systems. In a symmetric key system, everyone accessing the data has the same key. Keys that encrypt and decrypt messages must also remain secret to ensure privacy. While it's possible for this to work, securely distributing the keys to ensure proper controls are in place makes symmetric encryption impractical for widespread commercial use.

- Asymmetric Key Systems - also known as a public/private key system, uses two keys. One key remains secret—the private key—while the other key is made widely available to anyone who needs it. This key is called the public key. The private and public keys are mathematically tied together, so the corresponding private key can only decrypt that information encrypted using the public key.

- The Advanced Encryption Standard (AES) is the algorithm trusted as the standard by the U.S. Government and numerous organizations. Although it is highly efficient in 128-bit form, AES also uses keys of 192 and 256 bits for heavy-duty encryption purposes.

    AES is largely considered impervious to all attacks, except for brute force, which attempts to decipher messages using all possible combinations in the 128, 192, or 256-bit cipher.

- RSA is a public-key encryption algorithm and the standard for encrypting data sent over the internet. It also happens to be one of the methods used in PGP and GPG programs. Unlike Triple DES, RSA is considered an asymmetric algorithm due to its use of a pair of keys. You've got your public key to encrypt the message and a private key to decrypt it. The result of RSA encryption is a huge batch of mumbo jumbo that takes attackers a lot of time and processing power to break.




## Exercise

- Find two more historic ciphers besides the Caesar cipher.
- Find two digital ciphers that are being used today.
- Send a symmetrically encrypted message to one of your peers via the public Slack channel. They should be able to decrypt the message using a key you share with them. Try to think of a way to share this encryption key without revealing it to everyone. 
You are not allowed to use any private messages or other communication channels besides Slack. Analyse the shortcomings of this method.



### Sources
[https://en.wikipedia.org/wiki/History_of_cryptography](https://en.wikipedia.org/wiki/History_of_cryptography)

[https://www.britannica.com/topic/Enigma-German-code-device](https://www.britannica.com/topic/Enigma-German-code-device)

[https://www.comparitech.com/blog/information-security/famous-codes-and-ciphers-through-history-and-their-role-in-modern-encryption/](https://www.comparitech.com/blog/information-security/famous-codes-and-ciphers-through-history-and-their-role-in-modern-encryption/)

[https://www.arcserve.com/blog/5-common-encryption-algorithms-and-unbreakables-future](https://www.arcserve.com/blog/5-common-encryption-algorithms-and-unbreakables-future)

[https://www.devglan.com/online-tools/aes-encryption-decryption](https://www.devglan.com/online-tools/aes-encryption-decryption)

[https://www.devglan.com/online-tools/rsa-encryption-decryption](https://www.devglan.com/online-tools/rsa-encryption-decryption)


****

### Overcome challenges


### Results

- Examples of historic ciphers besides the Caesar cipher:
    - Vigenère Cipher.
    A Vigenère cipher uses a table consisting of different Caesar shifts in sequence and a key to encode a message across several rows of the table. By using different Caesar shifts for different characters in the message, the Vigenère cipher makes decoding the ciphertext using frequency analysis much more difficult.
    - The Playfair cipher or Playfair square or Wheatstone–Playfair cipher is a manual symmetric encryption technique and was the first literal digram substitution cipher. The Playfair cipher uses a 5 by 5 table containing a key word or phrase. Memorization of the keyword and 4 simple rules was all that was required to create the 5 by 5 table and use the cipher.
    - The Enigma machine is a cipher device developed and used in the early- to mid-20th century to protect commercial, diplomatic, and military communication.The Enigma machine produced encoded messages. Electrical signals from a typewriter-like keyboard were routed through a series of rotating wheels as well as a plugboard that scrambled the output but did so in a way that was decipherable with the right settings. 

- Ciphers that are being used today:

To date, RSA (Rivest, Shamir, Adleman) and AES (Advanced Encryption Standard) are considered safe, but as computing power increases, those will also fall one day and new ciphers will have to be developed to continue the use of cryptography on the web.

- Sending a symmetrically encrypted messages to peer.

First I generated a RCA key pair and sent the public key to the public chat. My peer sent a symmetrically encrypted message (AES) and an encrypted secret key to the public chat so that I could decrypt it.

![image](/00_includes/sec_04_1_screenshot.png)

![image](/00_includes/sec_04_2_screenshot.png)

I decrypted the secret key.

![image](/00_includes/sec_04_3_screenshot.png)

Using this key I decrypted the message.
![image](/00_includes/sec_04_4_screenshot.png)

Then we repeated our steps but it was my turn to encrypt the key and the message for my peer.

![image](/00_includes/sec_04_5_screenshot.png)

![image](/00_includes/sec_04_6_screenshot.png)