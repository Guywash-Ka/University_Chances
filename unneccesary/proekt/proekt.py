import sqlite3
import csv

con = sqlite3.connect('/home/vlad/projects/RodionPy/proekt/Яндекс_проект.db')
cur = con.cursor()
with open('/home/vlad/projects/RodionPy/proekt/Результаты - копия.csv', encoding = 'Windows-1251') as file:
    table = csv.reader(file, delimiter = ';', quotechar = '"')
    for i in table:
        print(i)
        # Заполнение персональных данных
        cur.execute("INSERT INTO personal_data(№, Name, gender, date_of_birthday, weight, "
                    f"length) VALUES ({int(i[0])}, '{i[1]}', (SELECT id FROM genders "
                    f"WHERE title = '{i[2]}'), '{i[3]}', {int(i[5])}, {int(i[6])});")
        # Заполнение резульнатов УМО
        print(i)
        cur.execute("INSERT INTO results(№, Date_of_UMO, EKG_relaxed, EKG_stress, Plant, "
                    "TANI_fat_mass, TANI_muscle_mass, Stability_opened, "
                    "Stability_closed, Stability_target, PWC150_170_kg_mm, "
                    "PWC150_170_CHS, PWC150_170_stress_up, PWC150_170_stress_down, MPK, "
                    "Test_functionCNS, Test_levelCNS, GRV, Cardiograph_golden_ratio,"
                    "Cardiograph_index_of_stress, Cardiograph_spectral_analysis, "
                    "Cardiograph_integral_indicator, Cardiograph_adaptation_ability, "
                    "Cardiograph_function_reserves, System_analysis_energy_capacity, "
                    "Card_psycho_emotional_state) "
                    f"VALUES ({i[0]}, '{i[4]}', '{i[17]}', '{i[18]}', '{i[19]}', '{i[20]}', "
                    f"'{i[21]}', {i[22]}, {i[23]}, {i[24]}, '{i[25]}', {i[26]}, {i[27]}, {i[28]}, "
                    f"'{i[29]}', '{i[30]}', '{i[31]}', '{i[32]}', '{i[33]}', {i[34]}, '{i[35]}', "
                    f"{i[36]}, '{i[37]}', '{i[38]}', '{i[39]}', '{i[40]}');")
    con.commit()