fst, scnd = input(), input()
if (fst == 'бумага' and scnd == 'ножницы') \
        or (fst == 'ножницы' and scnd == 'камень') or (fst == 'камень' and scnd == 'бумага') \
        or (fst == 'пират' and scnd == 'бумага') or (fst == 'пират' and scnd == 'ром') \
        or (fst == 'ром' and scnd == 'камень') or (fst == 'ром' and scnd == 'ножницы') \
        or (fst == 'ножницы' and scnd == 'пират')or (fst == 'камень' and scnd == 'пират') \
        or (fst == 'бумага' and scnd == 'ром'):
    res = 'второй'
elif (fst == 'бумага' and scnd == 'камень') or (fst == 'камень' and scnd == 'ножницы') \
        or (fst == 'ножницы' and scnd == 'бумага') or (fst == 'бумага' and scnd == 'пират') \
        or (fst == 'ром' and scnd == 'пират') or (fst == 'ножницы' and scnd == 'ром') \
        or (fst == 'камень' and scnd == 'ром') or (fst == 'ром' and scnd == 'бумага') \
        or (fst == 'пират' and scnd == 'ножницы') or (fst == 'пират' and scnd == 'камень'):
    res = 'первый'
else:
    res = 'ничья'
print(res)