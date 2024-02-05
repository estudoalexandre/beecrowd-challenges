def calc(a):
    n = float(3.14159)
    n = n * ( a ** 2)
    
    return n


area = float(input())
resultado = calc(area)
print("A={:.4f}".format(resultado))