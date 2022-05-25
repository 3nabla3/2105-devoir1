from primes import primes

def rev(n: int) -> list:
    res = []
    count = 0
    i = 0
    while n != 1:
        if n % primes[i] == 0:
            n = n // primes[i]
            count += 1
        else:
            res.append(count)
            count = 0
            i += 1
    res.append(count)
    return res

def gnum(l: list) -> int:
    prod = 1
    for i, val in enumerate(l):
        prod *= primes[i] ** val
    return prod

def liste_vide() -> int:
    return 1

def vide(n: int) -> bool:
    return n == 1

def dans(n: int, find: int) -> bool:
    for i in range(1000):
        if n % (primes[i] ** find) == 0:
            m = n // (primes[i] ** find)
            # make sure it wasnt a false friend
            if m % (primes[i] ** find):
                return True
    return False

def card(n: int) -> int:
    size = 0
    for i in range(1000):
        if n % primes[i] == 0:
            size = i + 1
            
    return size


def ajouter(num: int, n: int) -> int:
    s = card(n)
    return n * primes[s] ** num


def indexDe(num: int, n: int) -> int:
    ind = -1
    found = False
    for i in range(1000):
        if not found:
            m = n
            # could we take off num instances of primes[i]?
            flag = True
            for j in range(num):
                if m % primes[i] == 0:
                    m = m // primes[i]
                else:
                    flag = False

            # if we could take off num instances of primes[i] and there are no more instances of primes[i] lefts
            if flag and m % primes[i] != 0:
                found = True
                ind = i
    return ind

def index(ind: int, n: int) -> int:
    count = 0
    for _ in range(1000):
        if n % primes[ind] == 0:
            n = n // primes[ind]
            count += 1
    return count

def retirer(num: int, n: int) -> int:
    ind = indexDe(num, n)
    # on met la valeur a l'indice a 0
    n = n // primes[ind] ** num
    # on decale toutes les valeurs suivantes un indice a gauche
    for i in range(ind, 999):
        val = index(i + 1, n)
        n = n // primes[i + 1] ** val
        n = n * primes[i] ** val

    return n


def inter(s: int, t: int) -> int:
    r = 1
    writingInd = 0
    for i in range(1000):
        val = index(i, s)
        indT = indexDe(val, t)
        indR = indexDe(val, r)
        if indT >= 0 and indR == -1:
            r *= primes[writingInd] ** val
            writingInd += 1
    return r


l = [5, 4, 5, 6, 3, 2, 5, 2, 7, 5, 1, 0, 3]
# o = [3, 4, 5, 7, 9]
n = gnum(l)
print(n)
print(l)
print("length")
print(len(l), card(n))
# n = ajouter(53, n)
# print(n)
# print(rev(n))

n = retirer(4, n)
print(n)
print(rev(n))
l.remove(4)
print(l)

lst1 = [4, 9, 1, 17, 11, 26, 28, 54, 69]
lst2 = [9, 9, 74, 21, 45, 11, 63, 28, 26]
l1 = gnum(lst1)
l2 = gnum(lst2)

# print(indexDe(9, l2))

n = inter(l1, l2)
print(lst1)
print(lst2)
print(n)
print(rev(n))

n = inter(l2, l1)
print(lst1)
print(lst2)
print(n)
print(rev(n))