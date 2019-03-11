def fib(end):
    n1 = 1
    n2 = 2
    nth = 0
    list = [1, 2]
    while nth <= end:
        nth = n1 + n2
        list.append(nth)
        n1, n2 = n2, nth
    return list

print(sum([x for x in fib(4000000) if x%2==0]))
