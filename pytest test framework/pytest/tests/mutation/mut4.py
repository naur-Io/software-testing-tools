def triangle_type(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return 'Not a triangle'
    elif a == b == c:
        return 'Equilateral'
        # Modificada mutação: troca 'b' para 'c' na verificação de isósceles
    elif a == c or b == c or a == c:
        return 'Isosceles'
    else:
        return 'Scalene'