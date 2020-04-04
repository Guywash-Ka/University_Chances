import csv

school, grade = input().split()

with open('rez.csv', encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
    students = list(filter(lambda x: x['user_name'].split()[1] == school and
         x['user_name'].split()[2] == grade, sorted(sorted(reader, key=lambda x:
              x['user_name'].split()[-2], reverse=True), key=lambda x: int(x['Score']), reverse=True)))

for record in students:
    print(record['user_name'].split()[-2], record['Score'])