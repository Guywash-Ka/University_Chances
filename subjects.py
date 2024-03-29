subjects = {'Таможенное дело': ['Русский язык', 'Обществознание', 'Иностранный язык'],
            'Экономическая безопасность': ['Математика', 'Русский язык', 'Обществознание'],
            'Судебная экспертиза': ['Обществознание', 'Русский язык', 'История'],
            'Экономика': ['Математика', 'Русский язык', 'Обществознание'],
            'Менеджмент': ['Математика', 'Русский язык', 'Обществознание'],
            'Торговое дело': ['Математика', 'Русский язык', 'Обществознание'],
            'Товароведение': ['Математика', 'Русский язык', 'Обществознание'],
            'Государственное и муниципальное управление': ['Математика', 'Русский язык', 'Обществознание'],
            'Бизнес-информатика': ['Математика', 'Русский язык', 'Обществознание'],
            'Жилищное хозяйство и коммунальная структура': ['Математика', 'Русский язык', 'Обществознание'],
            'Сервис': ['Математика', 'Русский язык', 'Обществознание'],
            'Управление персоналом': ['Математика', 'Русский язык', 'Обществознание'],
            'Статистика': ['Математика', 'Русский язык', 'Обществознание'],
            'Управление качеством': ['Математика', 'Русский язык', 'Физика'],
            'Информационная безопасность': ['Математика', 'Русский язык', 'Физика'],
            'Прикладная математика и информатика': ['Математика', 'Русский язык', 'Информатика и ИКТ'],
            'Фундаментальная информатика и информационные технологии': ['Математика', 'Русский язык',
                                                                        'Информатика и ИКТ'],
            'Прикладная информатика': ['Математика', 'Русский язык', 'Информатика и ИКТ'],
            'Информационные системы и технологии': ['Математика', 'Русский язык', 'Информатика и ИКТ'],
            'Программная инженерия': ['Математика', 'Русский язык', 'Информатика и ИКТ'],
            'Юриспруденция': ['Обществознание', 'Русский язык', 'История'],
            'Реклама связи с общественностью': ['Обществознание', 'Русский язык', 'История'],
            'Туризм': ['Русский язык', 'История', 'Обществознание'],
            'Журналистика': ['Литература', 'Русский язык', 'Творческий экзамен', 'Собеседование'],
            'Зарубежное регионоведение': ['История', 'Русский язык', 'Иностранный язык'],
            'Международные отношения': ['История', 'Русский язык', 'Иностранный язык'],
            'Лингвистика': ['Иностранный язык', 'Русский язык', 'История'],
            'Организация работы с молодежью': ['Русский язык', 'История', 'Обществознание'],
            }

number_of_questions = {
    'Русский язык': 38, 'Математика': 12, 'Информатика и ИКТ': 23,
    'Обществознание': 20, 'История': 20, 'Иностранный язык': 20, 'Физика': 20
}

questions_for_math = [
    'Павел Иванович купил американский автомобиль, на спидометре которого скорость измеряется в милях в час. '
    'Американская миля равна 1609 м. Какова скорость автомобиля в километрах в час, если спидометр показывает 50 миль '
    'в час? Ответ округлите до целого числа.',
    'На рисунке точками показана месячная аудитория поискового сайта Ya.ru во все месяцы с декабря 2008 года по '
    'октябрь 2009 года. По горизонтали указываются месяцы, по вертикали — количество человек, посетивших сайт хотя бы '
    'раз за данный месяц. Для наглядности точки на рисунке соединены линией. Определите по рисунку наименьшую '
    'месячную аудиторию сайта Ya.ru в период с декабря 2008 года по апрель 2009 года.',
    'Найдите площадь четырехугольника, вершины которого имеют координаты (4; 2), (8; 4), (6; 8), (2; 6).',
    'Вероятность того, что новый электрический чайник прослужит больше года, равна 0,97. Вероятность того, '
    'что он прослужит больше двух лет, равна 0,89. Найдите вероятность того, что он прослужит меньше двух лет, '
    'но больше года.',
    'Решите уравнение: root^3(x+2) = -2',
    'Боковые стороны равнобедренного треугольника равны 5, основание равно 6. Найдите радиус вписанной окружности.',
    'На рисунке изображён график функции y = f(x). Функция  — одна из первообразных функции y = f(x). Найдите площадь '
    'закрашенной фигуры.',
    'Во сколько раз объем конуса, описанного около правильной четырехугольной пирамиды, больше объема конуса, '
    'вписанного в эту пирамиду?',
    'Найдите (a+9b+16)/(a+3b+8), если a/b=3.',
    'В розетку электросети подключены приборы, общее сопротивление которых составляет R1 = 90 Ом. Параллельно с ними '
    'в розетку предполагается подключить электрообогреватель. Определите наименьшее возможное сопротивление R2 этого '
    'электрообогревателя, если известно, что при параллельном соединении двух проводников с сопротивлениями R1 Ом и '
    'R2 Ом их общее сопротивление даeтся формулой R(общ.) = R1*R2/(R1+R2) (Ом), а для нормального функционирования '
    'электросети общее сопротивление в ней должно быть не меньше 9 Ом. Ответ выразите в омах.',
    'Два пешехода отправляются одновременно в одном направлении из одного и того же места на прогулку по аллее парка. '
    'Скорость первого на 1,5 км/ч больше скорости второго. Через сколько минут расстояние между пешеходами станет '
    'равным 300 метрам?',
    'Найдите точку минимума функции y = (x + 16)*e^(x-16).'
    ]

correct_answers_dict = {'Математика': ['80', '3150000', '20', '0,08', '-10', '1,5', '6', '2', '2', '10', '12', '-17'],
                        'Русский язык': [str(i) for i in range(38)], 'Информатика и ИКТ': [str(i) for i in range(23)],
                        'Обществознание': [str(i) for i in range(20)], 'История': [str(i) for i in range(20)],
                        'Иностранный язык': [str(i) for i in range(20)], 'Физика': [str(i) for i in range(20)]}
