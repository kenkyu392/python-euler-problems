# Problem 3: Largest prime factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

if __name__ == '__main__':
    got, want = 600851475143, 6857
    i = 3
    while i * i <= got:
        while got % i == 0:
            got = int(got / i)
        i += 2
    print('got:{} == want:{} = {}'.format(got, want, got == want))
