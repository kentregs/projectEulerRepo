num = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"

lrgProd = 0
digits = [int(i) for i in str(num)]
a = 0
b = 1
c = 2
d = 3
e = 4
f = 5
g = 6
h = 7
i = 8
j = 9
k = 10
l = 11
m = 12

while m < 1000:
    temp = digits[a] * digits[b] * digits[c] * digits[d] * digits[e] * digits[f] * digits[g] * digits[h] * digits[i] * digits[j] * digits[k] * digits[l] * digits[m]
    a += 1
    b += 1
    c += 1
    d += 1
    e += 1
    f += 1
    g += 1
    h += 1
    i += 1
    j += 1
    k += 1
    l += 1
    m += 1

    if lrgProd < temp:
        lrgProd = temp
        fa = a-1
        fb = b-1
        fc = c-1
        fd = d-1
        fe = e-1
        ff = f-1
        fg = g-1
        fh = h-1
        fi = i-1
        fj = j-1
        fk = k-1
        fl = l-1
        fm = m-1

print('%d %d %d %d %d %d %d %d %d %d %d %d %d' %(digits[fa], digits[fb], digits[fc], digits[fd], digits[fe], digits[ff], digits[fg], digits[fh], digits[fi], digits[fj], digits[fk], digits[fl], digits[fm]))
print(lrgProd)