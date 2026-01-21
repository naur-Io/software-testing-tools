def grade(score):
    if score < 0 or score > 100:
        raise ValueError("Nota invalida")
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


# cr-report grade.sqlite --show-pending
# cosmic-ray --verbosity INFO exec grade.toml grade.sqlite
# cr-html grade.sqlite > report.html