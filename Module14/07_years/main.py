
one_year = int(input('Введите первый год: '))
two_year = int(input('Введите второй год: '))
for i in range (one_year,two_year):
    if (i % 10 == (i // 10) % 10 and i % 10 == (i // 100) %10) or (i % 10 ==(i // 10) % 10 and i % 10 == i // 1000) or (i % 10 == (i // 100) % 10 and i % 10 == i // 1000) or ((i // 10) % 10 == (i // 100) % 10 and ((i // 10) % 10 == i // 1000)):
        print(i)
