def multiplo(a, b):
    if a % b == 0 or b % a == 0:
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")
    
a, b = map(int, input().split())

multiplo(a, b)