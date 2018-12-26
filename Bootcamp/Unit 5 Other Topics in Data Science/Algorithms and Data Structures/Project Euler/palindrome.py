palindromes = []
for n in range(10000, 998001):
    temp = n
    rev = 0
    while(n>0):
        dig = n%10
        rev = rev*10+dig
        n = n//10
    if (temp==rev):
        palindromes.append(temp)

quotients = []
for i in palindromes:
    for x in range(900, 999):
        if i%x==0:
            quotients.append(x)
products = []
for i in quotients:
    for x in range(900, 999):
        products.append(i*x)

largest_palindromes = []
for i in products:
    for x in palindromes:
        if i==x:
            largest_palindromes.append(i)

print(max(largest_palindromes))


# Short Solution
solutions = set()
for a in range(999,100,-1):
    for b in range(999,100,-1):
        product = a*b
        product_string = str(product)
        if product_string == product_string[::-1]:
            solutions.add((product))
print('Calculation complete:', max(solutions))
