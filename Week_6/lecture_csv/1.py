import csv

with open('test.csv', 'w', newline='') as f:
   writer = csv.writer(f, delimiter='\t')
   for i in range(7):
      writer.writerow([f'name: {i+1}', f'age: {i+1}', f'id: {i+1}'])
