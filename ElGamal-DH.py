def checkPrime(n):
    if n < 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
    return True

def ExtendedEuclideanAlgorithm(a, b):
    if b == 0: # if rest is 0, return the quotient
        return a,1,0
    x2 = 1
    x1 = 0
    y2 = 0
    y1 = 1

    while b != 0: # while rest is not 0
        q = a//b # quotient
        r = a - q * b # rest
        x = x2 - q * x1 # x = x2 - q * x1
        y = y2 - q * y1 # y = y2 - q * y1
        # update values
        a = b # a = quotient
        b = r # b = rest
        x2 = x1 # x2 = x1
        x1 = x # x1 = x
        y2 = y1 # y2 = y1
        y1 = y # y1 = y

    if a < 0: # if a is negative, return the absolute value of a
        return abs(x2)
    return x2 # return x2
    
def printResults(p, a, k, x, m, yA, yB, K, C, M, invK):
    print(" ")
    print("Entries: p = " + str(p) + ", a = " + str(a) + ", k= " + str(k) + ", x = " + str(x) + ", m = " + str(m))
    print("Output: yA = " + str(yA) + ", yB = " + str(yB) + ", K = " + str(K) + ", C = " + str(C) + ", K^-1 = " + str(invK) + ", M = " + str(M))
    
def main():
    print("                                                                                                          ")
    print(" /$$$$$$$$/$$       /$$$$$$  /$$$$$$ /$$      /$$ /$$$$$$ /$$                           /$$$$$$$ /$$   /$$")
    print("| $$_____| $$      /$$__  $$/$$__  $| $$$    /$$$/$$__  $| $$                          | $$__  $| $$  | $$")
    print("| $$     | $$     | $$  \__| $$  \ $| $$$$  /$$$| $$  \ $| $$                          | $$  \ $| $$  | $$")
    print("| $$$$$  | $$     | $$ /$$$| $$$$$$$| $$ $$/$$ $| $$$$$$$| $$             /$$$$$$      | $$  | $| $$$$$$$$")
    print("| $$__/  | $$     | $$|_  $| $$__  $| $$  $$$| $| $$__  $| $$            |______/      | $$  | $| $$__  $$")
    print("| $$     | $$     | $$  \ $| $$  | $| $$\  $ | $| $$  | $| $$                          | $$  | $| $$  | $$")
    print("| $$$$$$$| $$$$$$$|  $$$$$$| $$  | $| $$ \/  | $| $$  | $| $$$$$$$$                    | $$$$$$$| $$  | $$")
    print("|________|________/\______/|__/  |__|__/     |__|__/  |__|________/                    |_______/|__/  |__/")
    print("                                                                                                          ")
    print("----------------------------------------------------------------------------------------------------------")
    print("                                                                                                          ")
    prime = False
    while(prime == False):
        print("Enter the integer prime number: ", end="")
        p = input()  # contains the prime number
        if(checkPrime(int(p)) == False):
            print("The number is not prime. Please enter a prime number.")
        else:
            prime = True
    print("Enter the integer a number: ", end="")
    a = input()  # contains the number a
    print("Enter Alice secret key: ", end="")
    k = input()  # contains Alice secret key
    print("Enter Bob secret key: ", end="")
    x = input()  # contains Bob secret key
    print("Enter the message: ", end="")
    m = input() # contains the message
    yA = pow(int(a), int(k), int(p))  # calculates the shared key. yA = a^k mod p
    yB = pow(int(a), int(x), int(p))  # calculates the shared key. yB = a^x mod p
    K = pow(yA, int(x), int(p))  # calculates the shared key. K = yA^x mod p
    C = (K * int(m)) % int(p) # calculates the cipher text. C = K * m
    x = ExtendedEuclideanAlgorithm(K, int(p)) # calculates the inverse of K
    invK = x % int(p) # calculates the inverse of K. invK = K^-1 mod p
    M = invK * int(C) % int(p) # calculates the message. M = invK * C mod p
    printResults(p, a, k, x, m, yA, yB, K, C, M, invK)
    
if __name__ == '__main__':
    main()
