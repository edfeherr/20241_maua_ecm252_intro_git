import calculadora

def main():
    a = 2
    b = 3
    soma = calculadora.soma(a, b)
    print(f"{a} + {b} = {soma}")
    eleva = calculadora.eleva(a, b)
    print(f"{a} ^ {b} = {eleva}")
    main()