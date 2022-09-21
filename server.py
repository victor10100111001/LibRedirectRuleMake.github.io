import json
from locale import normalize
from operator import truediv
from flask import send_file

with open('./instances/data.json', 'r') as file:
    obj = json.loads(file.read())

def regler(type, block, block1, block2):
    JavaScriptDisable = False
    RemoteFontsDisable = False
    CosmeticFilteringDisable = False
    if block == "javascript": 
        JavaScriptDisable = True
    if block2 == 'remotefonts':
        RemoteFontsDisable = True
    if block1 == 'cosmeticfiltering':
        CosmeticFilteringDisable = True
    
    def instances(type):
        alle = []
        for i in obj.keys():
            if type in obj[i]: 
                alle += obj[i][type]
            elif type == "normal":
                alle += obj[i]
        return alle
    samlet = instances(type)
    with open('./instances/rules.txt', 'w') as file:
        if JavaScriptDisable == True:
            for i in samlet:
                file.write(f"no-scripting: {str(i).split(r'//')[1]} true \n") 
        if RemoteFontsDisable == True:
            for i in samlet:
                file.write(f"no-remote-fonts: {str(i).split(r'//')[1]} true \n") 
        if CosmeticFilteringDisable == True:
            for i in samlet:
                file.write(f"no-cosmetic-filtering: {str(i).split(r'//')[1]} true \n") 
    return send_file("./instances/rules.txt", as_attachment=True)



from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
        # getting input with name = fname in HTML form
        protocol = request.form.get("protocol")
        
        # getting input with name = lname in HTML form
        block = request.form.get("block")
        block1 = request.form.get("block1")
        block2 = request.form.get("block2")
        return regler(protocol,block,block1,block2)
    return render_template("form.html")

if __name__ == '__main__':
   app.run(debug=False)