# parse - take a string and convert it to python dictionary
import json

with open('sample-data.json') as f:
    data = json.load(f)

# decoration
print('Interface Status')
print('='*80)
print('DN',' '*40,'Description',' '*10,'Speed',' '*3,'MTU')
print('-'*43,'-'*22,'-'*6,' ','-'*6)

for seq in data['imdata']:
    print(seq['l1PhysIf']['attributes']['dn'], ' '*23 , seq['l1PhysIf']['attributes']['speed'], ' ' , seq['l1PhysIf']['attributes']['mtu']) 
