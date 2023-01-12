import re

# RegEx - regular expression
#  it is used to find first appearance of a pattern {search}

# simple text - в точности 'simple text'
# \d{5} - последовательность из 5 цифр
#  DD/MM/YYYY - \d\d/\d\d/\d\{4}


match = re.search(r'\d\d\D\d\d', 'Phone code is 12-4555-77')
print(match[0]) if match else print('Not found')

# w - means ==> all uppercase and lowercase letters, digits, under_scores, etc.
# W - means ==> opposite of w
print(re.split(r'\W+' ,'Hello,  World!  My name is   ===>  Zhanserik Kalmukhambet'))

l = list(re.findall(r'\d\d.\d\d.\d{4}|', 'My father\'s bithday 01.01.1980 and my mother\s is 07.11.1980'))
print(l)

txt = '''
Kazakhstan, also spelled Kazakstan, officially Republic of Kazakhstan, Kazakh Qazaqstan Respublikasï, country of Central Asia. 
It is bounded on the northwest and north by Russia, on the east by China, and on the south by Kyrgyzstan, Uzbekistan, the Aral Sea, and Turkmenistan; the Caspian Sea bounds Kazakhstan to the southwest. 
Kazakhstan is the largest country in Central Asia and the ninth largest in the world. Between its most distant points, Kazakhstan measures about 1,820 miles (2,930 kilometres) east to west and 960 miles north to south. 
While Kazakhstan was not considered by authorities in the former Soviet Union to be a part of Central Asia, it does have physical and cultural geographic characteristics similar to those of the other Central Asian countries. 
The capital is Nur-Sultan (formerly Astana, Aqmola, and Tselinograd), in the north-central part of the country. 
Kazakhstan, formerly a constituent (union) republic of the U.S.S.R., declared independence on December 16, 1991.
'''
s = set(re.findall(r'\w+stan',txt))
print(s)

# check if the character I is present at the beginning of txt
find = re.findall(r"\AI", 'I am going to do the project.But I am afraid. Cause I am introvert')
find = re.findall(r"\bI", 'I am going to do the project.But I am afraid. Cause I am introvert')
if find:
   print('You mentioned yourself in your speech')
else:
   print('You didn\'t mention youself')

# check jsut presence of the word
find2 = re.findall(r'\Bkht', 'I am from Kazakhtan. Kazakhstan is wonderful counrty')
print('Yes') if find else print('No')

txt3 = 'Summarizing, we can say that working in a team is not without troubles'
print(re.split(r'\s', txt3))

txt4 = "The rain in Spain"
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())

txt5 = 'This is not such a fatal minus 77, 88 but it is 11 present. Thank you 4 your attention!'
new = re.sub(r'\s','_',txt5,5)
print(new)
new2 = re.sub(r'\d','d',txt5)
print(new2)


import re

txt = 'The rain    in   Spain'
print(re.split(r'\s+',txt))

match = re.sub(r'\s+',' ',txt)
print(match)

x = re.search(r'\bS\w+', txt)
print(x.span())

# '?P<name>'

# strip() ==> without white spaces 


