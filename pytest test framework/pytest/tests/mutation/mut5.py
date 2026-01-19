def triangle_type(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return 'Not a triangle'
    elif a == b == c:
        return 'Equilateral'
        # trocando or para and na verificação de isósceles
    elif a == b and b == c or a == c:
        return 'Isosceles'
    else:
        return 'Scalene'