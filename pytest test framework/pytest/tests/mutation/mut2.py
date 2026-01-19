def triangle_type(a, b, c):
    # MUTANTE: troca dos retornos 'Not a triangle' e 'Equilateral'
    if a + b <= c or a + c <= b or b + c <= a:
        return 'Equilateral'
    elif a == b == c:
        return 'Not a triangle'
    elif a == b or b == c or a == c:
        return 'Isosceles'
    else:
        return 'Scalene'