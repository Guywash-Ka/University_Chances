import xlrd
import csv


file = xlrd.open_workbook('data.xlsx')
lst = file.sheet_by_index(0)
inp = open('output.csv', 'w')

wr = csv.writer(inp, delimiter=';')

for i in range(lst.nrows):
    wr.writerow(lst.row_values(i))

inp.close()
