#Caesar Cipher
#The Caesar cipher moves each letter forward in the alphabet by
#the key.  The resulting message has all the letters advanced by 'key'
#letters.
#To run the code, run the main() function

def encode(message, key):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = message.upper()
    secret = ""

    for letter in message:
        if (alpha.find(letter) >= 0): #check to see if the letter is actually a letter
            spot = (alpha.find(letter) + key) % 26
            secret = secret + alpha[spot]
        else: # letter must have been a number, symbol, or punctuation.
            secret = secret + letter

    return secret

def decode(message, key):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = message.upper()
    plaintext = ""

    for letter in message:
         if letter in alpha:
            spot = (alpha.find(letter) - key) % 26
            plaintext += alpha[spot]
         else:
            plaintext += letter
    return plaintext
def main():
    message = input("Enter a message: ")
    key = int(input("Enter a key: "))
    
    encrypted = encode(message, key)
    print("Encrypted:", encrypted)

    decrypted = decode(encrypted, key)
    print("Decrypted:", decrypted)

if __name__ == '__main__':
  main()
