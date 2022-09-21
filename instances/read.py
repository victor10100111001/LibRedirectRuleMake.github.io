import json
from locale import normalize
from operator import truediv
JavaScriptDisable = False
RemoteFontsDisable = False
CosmeticFilteringDisable = False
with open('./data.json', 'r') as file:
    obj = json.loads(file.read())
tegn = ' '
while not tegn in 'ntil':
    tegn = input("Which type of instances would you like to make rules for (normal, tor, i2p or loki?): \n")[0].lower()
blocking = input("What should be blocked in those instances (JavaScript, Remote Fonts or Cosmetic Filtering?): \n")
blocking = blocking.lower()
if 'java' in blocking:
    JavaScriptDisable = True
if 'font' in blocking:
    RemoteFontsDisable = True
if 'remote' in blocking:
    RemoteFontsDisable = True
if 'cosmetic' in blocking:
    CosmeticFilteringDisable = True
if 'filter' in blocking:
    CosmeticFilteringDisable = True
def instances(type):
    alle = []
    for i in obj.keys():
        #print(i)
        if type in obj[i]: 
            alle += obj[i][type]
        elif type == "normal":
            alle += obj[i]
    return alle
muligheder = {'n' : 'normal' , 't' : 'tor' , 'i' : 'i2p' , 'l' : 'loki'}
valg = muligheder[tegn]
samlet = instances(valg)
with open('./rules.txt', 'w') as file:
    if JavaScriptDisable == True:
        for i in samlet:
            file.write(f"no-scripting: {str(i).split(r'//')[1]} true \n") 
    if RemoteFontsDisable == True:
        for i in samlet:
            file.write(f"no-remote-fonts: {str(i).split(r'//')[1]} true \n") 
    if CosmeticFilteringDisable == True:
        for i in samlet:
            file.write(f"no-cosmetic-filtering: {str(i).split(r'//')[1]} true \n") 
