import csv

with open('test2.csv', mode='w') as f:
   csv_write = csv.writer(f,delimiter=',')
   csv_write.writerow(['line1','Jones','17'])
   csv_write.writerow(['line2','Ernar','19'])
   csv_write.writerow(['line3','Max','18'])
   csv_write.writerow(['line4','Nurik','16'])
   csv_write.writerow(['line5','Almat','17'])
   