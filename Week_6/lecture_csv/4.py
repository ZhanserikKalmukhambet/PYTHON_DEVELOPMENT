import csv

# 1st row is considered as a key of the dictionary
with open('test2.csv', 'r') as f:
   csv_reader = csv.DictReader(f, delimiter=',')
   for line in csv_reader:
      print(line['name'], '======>>>>', line['address'])