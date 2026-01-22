import pytest
import src.grade as grade

def test_nota_invalida():
    with pytest.raises(ValueError):
        grade.grade(-1)

def test_zero_eh_f():
    assert grade.grade(0) == "F"

def test_nota_100_eh_a():
    assert grade.grade(100) == "A"

def test_limite_a_b():
    assert grade.grade(90) == "A"
    assert grade.grade(89) == "B"

def test_limite_b_c():
    assert grade.grade(80) == "B"
    assert grade.grade(79) == "C"

def test_limite_c_d():
    assert grade.grade(70) == "C"
    assert grade.grade(69) == "D"

def test_limite_d_f():
    assert grade.grade(60) == "D"
    assert grade.grade(1) == "F"

def test_nota_maior_que_100_eh_invalida():
    with pytest.raises(ValueError):
        grade.grade(101)

def test_valores_internos_a():
    assert grade.grade(95) == "A"

def test_valores_internos_b():
    assert grade.grade(85) == "B"

def test_valores_internos_c():
    assert grade.grade(75) == "C"

def test_valores_internos_d():
    assert grade.grade(65) == "D"

def test_59_eh_f():
    assert grade.grade(59) == "F"

def test_valores_internos_d():
    assert grade.grade(58) == "F"

def test_nota_muito_alta():
    with pytest.raises(ValueError):
        grade.grade(150)



    # To run mutation tests with Cosmic Ray, use the following commands:
    # cosmic-ray --verbosity INFO init grade.toml grade.sqlite --force
    # cosmic-ray --verbosity=INFO baseline grade.toml
    # cr-report grade.sqlite --show-pending
    # cosmic-ray --verbosity INFO exec grade.toml grade.sqlite
    # cr-html grade.sqlite > report.html
