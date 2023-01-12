import csv

data = [
   (
   ['Zhanserik','2004'],'user_name','birth_year'), # заголовок
   ['Kobylandy','1987'],
   ['Magzhan  ','2006'],
   ['Zhanibek ','2003']
]

with open('test3.csv','w', newline='',encoding='cp1251') as f:
   writer = csv.writer(f,delimiter='\t')
   writer.writerows(data) # if you have array of array you can use 'writerows' parameter