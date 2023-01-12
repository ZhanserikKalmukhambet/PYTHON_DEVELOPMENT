import csv

with open('test.csv', 'r') as f:
   reader = csv.reader(f, delimiter='\t')
   for row in reader:
      print(row[0], row[1], row[2])
      next(reader)
