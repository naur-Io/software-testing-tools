def triangle_type(a, b, c):
    # Modificada mutação: troca 'a' para 'b' na verificação do triângulo
    if b + b <= a or a + c <= b or b + c <= a:
        return 'Not a triangle'
    elif a == b == c:
        return 'Equilateral'
    elif a == b or b == c or a == c:
        return 'Isosceles'
    else:
        return 'Scalene'