import json
# it is almost like python dictionary
# there is some converts from json to python like {none:None},{true:True}
# dumps - convert dict to the string
# loads - by reverse ==>
# when we create json(string) it is mandatory to use double quatation mark

# d = {
#       'name': 'Jones',
#       'age': 17,
#       'id': '21B30819'
# }

# data = json.dumps(d)
# print(type(data))

# d2 = json.loads(data)
# print(type(d2), d2['name'], d2['age'], d2['id'])
# print(d==d2)

######################################################################################

# f = open('input.txt','r')
# info = f.read()
# d = json.loads(info)
# print(d['name'], d['surname'])

######################################################################################

game_state = {
      'position':{
            'x': 100,
            'y': 200
      },
      'full_name':'Hello_World',
      'enemy':{
            'x': 300,
            'y': 300
      }
}
with open('output.','w') as f:
      f.write(json.dumps(game_state))

d = {
      'Almat': 3.9, 
      'Dima': 3.1, 
      'So on': 45
}

with open ('exam.json', 'w') as f:
      f.write(json.dumps(d))





