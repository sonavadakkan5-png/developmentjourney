def prime_no(n):

    is_prime = True

    for i in range(2,n):

        if n%i==0:

            is_prime = False

            break

    return is_prime

print(prime_no(7))

