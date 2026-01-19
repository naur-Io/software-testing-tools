def triangle_type(a, b, c):
    # MUTANTE: operador lógico <= modificado para >=
    if a + b <= c or a + c >= b or b + c <= a:
        return 'Not a triangle'
    elif a == b == c:
        return 'Equilateral'
    elif a == b or b == c or a == c:
        return 'Isosceles'
    else:
        return 'Scalene'