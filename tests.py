def duplicate_count(text):
    text = [t.capitalize() for t in text]
    letras = list(set(text))
    letras_repetidas = []

    for l in letras:
        numero_repeticoes = text.count(l)
        letras_repetidas.append({"letra": l, "rep": numero_repeticoes})

    letras_repetidas = list(filter(lambda x: x["rep"] > 1, letras_repetidas))
    return letras_repetidas.__len__()


text1 = "abBcdefff"
print(duplicate_count(text1))


def high(x):
    palavras = x.split(" ")
    points = []

    for palavra in palavras:
        pts = calcula_pontos(palavra)
        if not [pt for pt in points if pt["pts"] == pts]:
            points.append({"palavra": palavra, "pts": pts})

    points = list(sorted(points, key=lambda x: x["pts"]))
    points.reverse()
    return points[0]["palavra"]


def calcula_pontos(palavra):
    pts = 0
    for letra in palavra:
        pts += ord(letra) - 96
    return pts


text = 'aa b'
print(high(text))
