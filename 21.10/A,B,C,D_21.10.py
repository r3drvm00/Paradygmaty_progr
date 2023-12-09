print('---A---')

liczby = [20, 40, 50, 30, 10]

# Użyj funkcji max() i min() do znalezienia największego i najmniejszego elementu
max_value = max(liczby)
min_value = min(liczby)

# Oblicz różnicę między największym i najmniejszym elementem
roznica_a = max_value - min_value

print(f"Największy element: {max_value}")
print(f"Najmniejszy element: {min_value}")
print(f"Różnica: {roznica_a}")

print('---B---')

# Posortuj listę
liczby.sort()

# Oblicz różnicę między drugim największym i drugim najmniejszym elementem
roznica_b = liczby[-2] - liczby[1]

print(f"Drugi największy element: {liczby[-2]}")
print(f"Drugi najmniejszy element: {liczby[1]}")
print(f"Różnica: {roznica_b}")

print('---C---')

for liczba in liczby:
    pierwiastek = liczba**0.5
    kwadrat = liczba**2
    potega_trzecia = liczba**3

    print(f"Liczba: {liczba}, Pierwiastek: {pierwiastek}, Kwadrat: {kwadrat}, Potęga trzecia: {potega_trzecia}")

print('---D---')

punkty = [8, 9, 7, 5, 10]

# Odrzuć największy i najmniejszy element
punkty.sort()
punkty = punkty[1:-1]

# Oblicz średnią z pozostałych elementów
srednia = sum(punkty) / len(punkty)

print(f"Punkty po odrzuceniu największego i najmniejszego: {punkty}")
print(f"Średnia: {srednia}")
