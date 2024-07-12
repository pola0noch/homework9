# Домашнее задание по теме "Цикл "for".Элементы списка.Полезные функции в цикле.
# Cпособ через "True"
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
for i in numbers:
    for j in range(2, i):
        if i % j == 0:
            is_prime = True
            if is_prime:
                not_primes.append(i)
            break
    else:
        primes.append(i)
primes.remove(1)
print(primes, not_primes)

# Способ без "True"
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    for j in range(2, i):
        if i % j == 0:
            not_primes.append(i)
            break
    else:
        primes.append(i)
        continue
primes.remove(1)
print(primes, not_primes)






