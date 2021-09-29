def getinput():
    first_prime=eval(input('Enter first prime a: '))
    second_prime=eval(input('Enter second prime b: '))
    print("you have chosen two primes a=" + str(first_prime) + ", b=" + str(second_prime))
    n=first_prime*second_prime
    print("RSA Modulus(n) = first_prime * second_prime = " + str(n))
    phi=(first_prime-1)*(second_prime-1)
    print(f"phi = ({first_prime} - 1) *({second_prime} - 1) = " + str(phi) + "\n")
    return n,phi

def modular_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def get_comprime_numbers(phi, n):
    sample = []
    for i in range(2, phi + 1):
        if gcd(i, phi) == 1 and gcd(i, n) == 1:
            sample.append(i)
    return sample

def gcd(first_number, second_number):
    while True:
        if second_number==0:
            break
        else:
            c = first_number % second_number
            first_number = second_number
            second_number = c
    return first_number


def get_encryptor_decryptor_value(n, phi):
    print("Select an encryptor value from the following list of numbers: ")
    print(str(get_comprime_numbers(phi, n)))
    encryptor=int(input())
    decryptor=modular_inverse(encryptor, phi)
    print("Public key =  (" + str(encryptor) + ", " + str(n) + ")")
    print("Private key = (" + str(decryptor) + ", " + str(n) + ")")
    return encryptor,decryptor

def encrypt(text, encryptor,n):
    encrypted_message = ''
    for i in text:
        encrypted_character=modular_inverse(ord(i)**encryptor,n)
        if encrypted_character==None:
            print('Modular multiplicative inverse can not be found for block '+str(ord(i)))
        encrypted_message += chr(encrypted_character)
    return encrypted_message

def decrypt(text, decryptor,n):
    decrypted_message = ''
    for i in text:
        decrypted_character=modular_inverse(ord(i)**decryptor,n)
        if decrypted_character==None:
            print('Modular multiplicative inverse can not be found for block '+str(ord(i)))
        decrypted_message += chr(decrypted_character)
    return decrypted_message


def start():
    n,phi=getinput()
    encryptor, decryptor = get_encryptor_decryptor_value(n, phi)
    text = input("Enter a message to encrypt: ")
    print("Original Message: " + text)
    encrypted_message = encrypt(text,encryptor,n)
    print("Encrypted message: " + encrypted_message)
    decrypted_message = decrypt(encrypted_message,decryptor,n)
    print("Decrypted message: " + decrypted_message)

start()