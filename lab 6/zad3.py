
def laborki(punktacja, studenci):
    suma_studencka = []
    suma_studencka_proc = []
    suma_global = 0
    liczba_studentow = 0
    for student in studenci:
        if not isinstance(student[1], list):
            suma_studencka.append(None)
            continue
        if False in [isinstance(element, (int, float)) for element in student[1]]:
            print(student[1])
            suma_studencka.append(None)
            continue
        liczba_studentow += 1
        suma_global += sum(student[1])
        suma_studencka.append(sum(student[1]))
    if liczba_studentow == 0:
        liczba_studentow = 1
    for element in suma_studencka:
        if element != None:
            suma_studencka_proc.append(round(100*element/sum(punktacja), 1))
        else:
            suma_studencka_proc.append(None)
    return list(zip([student[0] for student in studenci], suma_studencka, suma_studencka_proc)), round(suma_global/liczba_studentow * 100 / sum(punktacja), 1)