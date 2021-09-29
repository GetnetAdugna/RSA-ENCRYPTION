# RSA-ENCRYPTION
"""
This program is designed to compute an encryption and decryption of a message sent by a user.to write it we use an RSA technique for decryption and encryption
"""
def getinput():
    first_prime=eval(input('Enter first prime a: '))
    second_prime=eval(input('Enter second prime b: '))
    print("you have chosen two primes a=" + str(first_prime) + ", b=" + str(second_prime))
    n=first_prime*second_prime
    print("RSA Modulus(n) = first_prime * second_prime = " + str(n))
    phi=(first_prime-1)*(second_prime-1)
    print(f"phi = ({first_prime} - 1) *({second_prime} - 1) = " + str(phi) + "\n")
    return n,phi
